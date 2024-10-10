from fastapi import APIRouter, Depends

from app.routers.v1.endpoints import (
    dtlfa,
    ordfa,
    r1,
    ordercodemaster,
    cure_rec,
    hismedd,
    nhidtlb,
    nhiordb,
    r2,
    fexreport,
    r7,
    fxyreport,
    r8
)


router_v1 = APIRouter() 


## [GET] : Test
@router_v1.get("", tags=["Test"])
async def test():
    return JSONResponse(status_code=200, content="Here goes the apis")

router_v1.include_router(dtlfa.router, prefix="/dtlfa", tags=["DTLFA"])
router_v1.include_router(ordfa.router, prefix="/ordfa", tags=["ORDFA"])
router_v1.include_router(ordercodemaster.router, prefix="/ordercodemaster", tags=["ORDER CODE MASTER"])
router_v1.include_router(cure_rec.router, prefix="/cure_rec", tags=["CURE REC"])
router_v1.include_router(hismedd.router, prefix="/hismedd", tags=["HISMEDD"])
router_v1.include_router(nhidtlb.router, prefix="/nhidtlb", tags=["NHIDTLB"])
router_v1.include_router(nhiordb.router, prefix="/nhiordb", tags=["NHIORDB"])
router_v1.include_router(fexreport.router, prefix="/fexreport", tags=["FEXREPORT"])
router_v1.include_router(fxyreport.router, prefix="/fxyreport", tags=["FXYREPORT"])

router_v1.include_router(r1.router, prefix="/r1", tags=["R1"])
router_v1.include_router(r2.router, prefix="/r2", tags=["R2"])
router_v1.include_router(r7.router, prefix="/r7", tags=["R7"])
router_v1.include_router(r8.router, prefix="/r8", tags=["R8"])