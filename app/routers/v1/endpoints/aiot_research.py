from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from typing import List, Optional
from datetime import datetime
import logging

from app.database.aiot_research import get_conn_aiot  

router = APIRouter()
system_logger = logging.getLogger('custom.error')


@router.get("", response_model=List[dict], name="Get AIOT research", description="Get AIOT research")
async def get_query_data(
    report_date: str  
    ):
    base_query = """
        SELECT * FROM LISDETAIL WHERE 檢查日期 LIKE :report_date
    """

    try:
        if len(report_date) != 8:
            raise HTTPException(status_code=400, detail="Invalid report_date format. Expected format is YYYYMMDD.")

        west_year = int(report_date[:4]) 
        roc_year = west_year - 1911      
        roc_date_str = f"{roc_year}{report_date[4:]}" 
        params = {'report_date': f"{roc_date_str}%"}

        with next(get_conn_aiot()) as db:
            result = db.execute(text(base_query), params)
            columns = result.keys()
            rows = result.fetchall()

            if not rows:
                return []

            result_list = [dict(zip(columns, row)) for row in rows]
            return result_list

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {ve}")
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as e:
        system_logger.error(f"An error occurred while fetching AIOT research data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/range", response_model=List[dict], name="Get AIOT research range", description="Get AIOT research range")
async def get_query_data_range(
    start_date: str, 
    end_date: str,
    template_name: str,
    performed_item: Optional[str] = None 
):

    base_query = """
        SELECT * FROM RISREPORT2 
        WHERE Template_name = :template_name 
        AND PERFRMD_START_DATE BETWEEN :start_date AND :end_date
    """
    
    if performed_item:
        base_query += " AND PERFRMD_ITEM LIKE :performed_item"

    try:
        params = {
            'start_date': start_date, 
            'end_date': end_date,
            'template_name': template_name
        }
        
        if performed_item:
            params['performed_item'] = f"{performed_item}%"

        with next(get_conn_aiot()) as db:
            result = db.execute(text(base_query), params)
            columns = result.keys()
            rows = result.fetchall()

            print(rows,"/////")

            if not rows:
                return JSONResponse(content=[], media_type="application/json; charset=utf-8")

            result_list = [dict(zip(columns, row)) for row in rows]
            return JSONResponse(content=result_list, media_type="application/json; charset=utf-8")
        
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {ve}")
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as e:
        system_logger.error(f"An error occurred while fetching AIOT research data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
