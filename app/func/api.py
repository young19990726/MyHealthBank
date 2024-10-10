import json
import logging

from collections import defaultdict
from requests import get, patch, post, put, RequestException

from middleware.exception import exception_message

uvicorn_logger = logging.getLogger('uvicorn.error')
system_logger = logging.getLogger('custom.error')

## DTLFA
def post_dtlfa_data(dtlfa_data):

    url = "http://0.0.0.0:726/api/v1/dtlfa"

    for data in dtlfa_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("DTLFA data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post DTLFA data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))

def get_dtlfa_data():

    url = "http://0.0.0.0:726/api/v1/dtlfa"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve DTLFA data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

## ORDFA
def post_ordfa_data(ordfa_data):

    url = "http://0.0.0.0:726/api/v1/ordfa"

    for data in ordfa_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("ORDFA data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post ORDFA data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))

def get_ordfa_data():

    url = "http://0.0.0.0:726/api/v1/ordfa"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve ORDFA data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

## R1
def post_r1():

    url = "http://0.0.0.0:726/api/v1/r1"

    try:
        response = post(url)

        if response.status_code == 200:
            print("R1 post successfully")
            # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

        else:
            print("Failed to post R1 data")
            print(response.text)

    except RequestException as e:
                system_logger.error(exception_message(e))


def get_r1_data(cno: str):
    url = "http://0.0.0.0:726/api/v1/r1"

    try:
        response = get(url, params={"cno": cno})

        if response.status_code == 200:
            data = response.json()

            r1_output = []
            r1_dict = defaultdict(list)  # 使用 defaultdict 來根據 dtlid 組合 r1_1 項目

            for entry in data:
                # 構建 r1_1 項目
                r1_1_item = {
                    "r1_1.1": entry['order_code'] if entry['order_code'] != 'nan' else '',
                    "r1_1.3": str(entry['total_number']) if entry['total_number'] is not None else '',
                    "r1_1.4": entry['dose_day'] if entry['dose_day'] != 'nan' else ''
                }

                # 使用 dtlid 將 r1_1_item 加入對應的列表
                r1_dict[entry['dtlid']].append(r1_1_item)

            # 構建 r1 項目
            for dtlid, r1_1_items in r1_dict.items():
                # 找到第一個條目的基本信息（假設所有相同 dtlid 的條目有相同的 treatment_date、cm_code 和 pcs_code）
                first_entry = next(entry for entry in data if entry['dtlid'] == dtlid)

                r1_item = {
                    "r1.5": first_entry['treatment_date'].replace('-', ''),  # 格式化日期
                    "r1.8": first_entry['cm_code'] if first_entry['cm_code'] != 'nan' else '',
                    "r1.10": first_entry['pcs_code'] if first_entry['pcs_code'] != 'nan' else '',
                    "r1_1": r1_1_items  # 包含所有相同 dtlid 的 r1_1 項目
                }

                # 將組合好的 r1_item 加入輸出列表
                r1_output.append(r1_item)

            print(json.dumps(r1_output, indent=4, ensure_ascii=False))
            return r1_output

        else:
            system_logger.error(f"Failed to retrieve r1 data: {response.text}")

    except RequestException as e:
        system_logger.error(exception_message(e))

## ORDERCODEMASTER
def post_ordercodemaster_data(ordercodemaster_data):

    url = "http://0.0.0.0:726/api/v1/ordercodemaster"

    for data in ordercodemaster_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("ORDERCODEMASTER data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post ORDERCODEMASTER data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))

def get_ordercodemaster_data():

    url = "http://0.0.0.0:726/api/v1/ordercodemaster"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve ORDERCODEMASTER data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

## CURE_REC
def post_cure_rec_data(cure_rec_data):

    url = "http://0.0.0.0:726/api/v1/cure_rec"

    for data in cure_rec_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("CURE_REC data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post CURE_REC data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))

def get_cure_rec_data():

    url = "http://0.0.0.0:726/api/v1/cure_rec"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve CURE_REC data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

# HISMEDD
def post_mismedd_data(mismedd_data):

    url = "http://0.0.0.0:726/api/v1/hismedd"

    for data in mismedd_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("HISMEDD data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post HISMEDD data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))


def get_mismedd_data():

    url = "http://0.0.0.0:726/api/v1/hismedd"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve HISMEDD data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

# NHIDTLB
def post_nhidtlb_data(nhidtlb_data):

    url = "http://0.0.0.0:726/api/v1/nhidtlb"

    for data in nhidtlb_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("NHIDTLB data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post NHIDTLB data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))


def get_nhidtlb_data():

    url = "http://0.0.0.0:726/api/v1/nhidtlb"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve NHIDTLB data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

# NHIORDB
def post_nhiordb_data(nhiordb_data):

    url = "http://0.0.0.0:726/api/v1/nhiordb"

    for data in nhiordb_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("NHIORDB data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post NHIORDB data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))


def get_nhiordb_data():

    url = "http://0.0.0.0:726/api/v1/nhiordb"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve NHIORDB data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

## R2
def post_r2():

    url = "http://0.0.0.0:726/api/v1/r2"

    try:
        response = post(url)

        if response.status_code == 200:
            print("R2 post successfully")
            # print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            # return response.json()
        else:
            print("Failed to post R2 data")
            print(response.text)

    except RequestException as e:
                system_logger.error(exception_message(e))

def get_r2_data(cno: str):
    url = "http://0.0.0.0:726/api/v1/r2"

    try:
        response = get(url, params={"cno": cno})

        if response.status_code == 200:
            data = response.json()

            r2_output = []
            r2_dict = defaultdict(list)  # 使用 defaultdict 來根據 dtlid 組合 r1_1 項目

            for entry in data:
                # 構建 r2_1 項目
                r2_1_item = {
                    "r2_1.2": entry['execution_date'].replace('-', ''),
                    "r2_1.3": entry['expiration_date'].replace('-', ''),
                    "r2_1.4": entry['order_code'],
                    "r2_1.6": str(entry['total_number'])
                }

                # 使用 accession_number 將 r2_1_item 加入對應的列表
                r2_dict[entry['accession_number']].append(r2_1_item)

            # 構建 r2 項目
            for accession_number, r2_1_items in r2_dict.items():
                # 找到第一個條目的基本信息（假設所有相同 dtlid 的條目有相同的 treatment_date、cm_code 和 pcs_code）
                first_entry = next(entry for entry in data if entry['accession_number'] == accession_number)

                r2_item = {
                    "r2.5": first_entry['admission_date'].replace('-', ''),  # 格式化日期
                    "r2.6": first_entry['discharge_date'].replace('-', ''),
                    "r2.10": first_entry['cm_code'] if first_entry['cm_code'] != 'nan' else '',
                    "r2.12": first_entry['pcs_code'] if first_entry['pcs_code'] != 'nan' else '',
                    "r2_1": r2_1_items  # 包含所有相同 dtlid 的 r1_1 項目
                }

                # 將組合好的 r1_item 加入輸出列表
                r2_output.append(r2_item)

            print(json.dumps(r2_output, indent=4, ensure_ascii=False))
            return r2_output

        else:
            system_logger.error(f"Failed to retrieve r2 data: {response.text}")

    except RequestException as e:
        system_logger.error(exception_message(e))

## FEXREPORT
def post_fexreport_data(fexreport_data):

    url = "http://0.0.0.0:726/api/v1/fexreport"

    for data in fexreport_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("FEXREPORT data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post FEXREPORT data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))

def get_fexreport_data():

    url = "http://0.0.0.0:726/api/v1/fexreport"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve FEXREPORT data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

## R8
def post_r7():

    url = "http://0.0.0.0:726/api/v1/r7"

    try:
        response = post(url)

        if response.status_code == 200:
            print("R7 post successfully")
            # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

        else:
            print("Failed to post R7 data")
            print(response.text)

    except RequestException as e:
                system_logger.error(exception_message(e))

def get_r7_data(cno: str):
    url = "http://0.0.0.0:726/api/v1/r7"

    try:
        response = get(url, params={"cno": cno})

        if response.status_code == 200:
            data = response.json()

            r7_output = []

            # 如果返回的是列表，則遍歷每一個項目
            if isinstance(data, list):
                for item in data:
                    report_date = str(item['report_date']).replace('-', '')
                    r7_item = {
                        "r7.6": report_date, 
                        "r7.8": item['order_code'],
                        "r7.10": item['ordclnm_name'],
                        "r7.11": item['data']
                    }
                    r7_output.append(r7_item)
            else:
                # 如果返回的不是列表，假設是單一字典，直接處理
                report_date = str(data['report_date']).replace('-', '')
                r7_item = {
                    "r7.6": report_date, 
                    "r7.8": data['order_code'],
                    "r7.10": data['ordclnm_name'],
                    "r7.11": data['data']
                }
                r7_output.append(r7_item)

            print(json.dumps(r7_output, indent=4, ensure_ascii=False))
            return r7_output

        else:
            print(f"Failed to retrieve r7 data: {response.text}")

    except RequestException as e:
        print(f"Error occurred: {str(e)}")

## FXYREPORT
def post_fxyreport_data(fxyreport_data):

    url = "http://0.0.0.0:726/api/v1/fxyreport"

    for data in fxyreport_data:
        try:
            response = post(url, json=data)

            if response.status_code == 200:
                print("FXYREPORT data post successfully")
                # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

            else:
                print("Failed to post FXYREPORT data")
                print(response.text)
        
        except RequestException as e:
            system_logger.error(exception_message(e))

def get_fxyreport_data():

    url = "http://0.0.0.0:726/api/v1/fxyreport"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()

        else:
            system_logger.error(f"Failed to retrieve FXYREPORT data: {response.text}")
    
    except RequestException as e:
        system_logger.error(exception_message(e))

## R8
def post_r8():

    url = "http://0.0.0.0:726/api/v1/r8"

    try:
        response = post(url)

        if response.status_code == 200:
            print("R8 post successfully")
            # print(json.dumps(response.json(), indent=4, ensure_ascii=False))

        else:
            print("Failed to post R8 data")
            print(response.text)

    except RequestException as e:
                system_logger.error(exception_message(e))


def get_r8_data(cno: str):
    url = "http://0.0.0.0:726/api/v1/r8"

    try:
        response = get(url, params={"cno": cno})

        if response.status_code == 200:
            data = response.json()

            r8_output = []

            # 如果返回的是列表，則遍歷每一個項目
            if isinstance(data, list):
                for item in data:
                    performed_start_date_str = str(item['performed_start_date']).replace('-', '')
                    r8_item = {
                        "r8.6": performed_start_date_str, 
                        "r8.8": item['order_code'],
                        "r8.10": item['report_text']
                    }
                    r8_output.append(r8_item)
            else:
                # 如果返回的不是列表，假設是單一字典，直接處理
                performed_start_date_str = str(data['performed_start_date']).replace('-', '')
                r8_item = {
                    "r8.6": performed_start_date_str, 
                    "r8.8": data['order_code'],
                    "r8.10": data['report_text']
                }
                r8_output.append(r8_item)

            print(json.dumps(r8_output, indent=4, ensure_ascii=False))
            return r8_output

        else:
            print(f"Failed to retrieve r8 data: {response.text}")

    except RequestException as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":

    import numpy as np
    import pandas as pd
    
    # 門診
    dtlfa_data = pd.read_csv('./example/DTLFA.csv')

    dtlfa_data.rename(columns={
        'DTLID': 'dtlid',
        'CHARTNO': 'cno',
        'DTLFA_D19': 'cm_code',
        'DTLFA_D24': 'pcs_code',
        'DTLFA_D9': 'treatment_date'  
    }, inplace=True)

    dtlfa_data['hos'] = '801'

    dtlfa_data = dtlfa_data.replace([np.inf, -np.inf], None)
    dtlfa_data = dtlfa_data.where(pd.notnull(dtlfa_data), None)

    dtlfa_data['treatment_date'] = dtlfa_data['treatment_date'].astype(str).str[:10]
    dtlfa_data['treatment_date'] = pd.to_datetime(dtlfa_data['treatment_date'], errors='coerce')
    dtlfa_data['treatment_date'] = dtlfa_data['treatment_date'].dt.strftime('%Y-%m-%d')

    for column in dtlfa_data.columns:
        if column != 'treatment_date':
            dtlfa_data[column] = dtlfa_data[column].astype(str)

    # 存起來      
    dtlfa_data.to_csv(
        './example/DTLFA_processed.csv', 
        index=False, 
        encoding='utf-8'
    )

    dtlfa_dict_list = dtlfa_data.to_dict(orient='records')

    # 住院
    ordfa_data = pd.read_csv('./example/ORDFA.csv')

    ordfa_data.rename(columns={
        'DTLID': 'fk_dtlid',
        'ORDFA_P1': 'dose_day',
        'ORDFA_P10': 'total_number',
        'ORDFA_P4': 'order_code'
    }, inplace=True)

    ordfa_data['hos'] = '801'

    ordfa_data['dose_day'] = pd.to_numeric(ordfa_data['dose_day'], errors='coerce').fillna('None').astype(str)
    ordfa_data['total_number'] = ordfa_data['total_number'].astype(str)
    
    # 存起來      
    ordfa_data.to_csv(
        './example/ORDFA_processed.csv', 
        index=False, 
        encoding='utf-8'
    )
    ordfa_dict_list = ordfa_data.to_dict(orient='records')
    
    # post_dtlfa_data(dtlfa_dict_list)
    # post_ordfa_data(ordfa_dict_list)
    # post_r1()
    # data = get_r1_data('3363739')

    # ORDERCODEMASTER
    ordercodemaster_data = pd.read_csv('./example/ORDERCODEMASTER.csv')

    ordercodemaster_data.rename(columns={
        'ORDERCODE': 'hos_ordercode',
        'INSRCODE': 'order_code'
    }, inplace=True)

    ordercodemaster_data['hos'] = '801'
    # 存起來      
    ordercodemaster_data.to_csv(
        './example/ORDERCODEMASTER_processed.csv', 
        index=False, 
        encoding='utf-8'
    )
    ordercodemaster_data_dict_list = ordercodemaster_data.to_dict(orient='records')

    # CURE_REC
    cure_rec_data = pd.read_csv('./example/CURE_REC.csv')

    cure_rec_data.rename(columns={
        'CUREID': 'fk_hos_ordercode',
        'ACCESSNO': 'accession_number'
    }, inplace=True)

    cure_rec_data['hos'] = '801'

    for column in cure_rec_data.columns:
        cure_rec_data[column] = cure_rec_data[column].astype(str)
    # 存起來      
    cure_rec_data.to_csv(
        './example/CURE_REC_processed.csv', 
        index=False, 
        encoding='utf-8'
    )
    cure_rec_data_dict_list = cure_rec_data.to_dict(orient='records')

    # 

    # FXTREPORT
    fxyreport_data = pd.read_csv('./example/FXYREPORT.csv')

    fxyreport_data.rename(columns={
        'PATIENT_ID': 'cno',
        'PERFRMD_START_DATE': 'performed_start_date',
        'CODE': 'fk_hos_ordercode',
        'report_text': 'report_text'
    }, inplace=True)


    fxyreport_data['hos'] = '801'


    fxyreport_data['performed_start_date'] = pd.to_datetime(
        fxyreport_data['performed_start_date'], format='%Y%m%d'
    ).dt.strftime('%Y-%m-%d') 


    for column in fxyreport_data.columns:
        if column != 'performed_start_date':
            fxyreport_data[column] = fxyreport_data[column].astype(str)


    fxyreport_data_dict_list = fxyreport_data.to_dict(orient='records')


    # post_fxyreport_data(fxyreport_data_dict_list)

    # post_r8()
    # get_r8_data('3363739')

    # HISMEDD
    hismedd_data = pd.read_csv('./example/HISMEDD.csv')
    

    hismedd_data.rename(columns={
        'MEDNO': 'medno',
        'CHARTNO': 'cno'
    }, inplace=True)


    hismedd_data['hos'] = '801'

    for column in hismedd_data.columns:
        hismedd_data[column] = hismedd_data[column].astype(str)

    hismedd_data_dict_list = hismedd_data.to_dict(orient='records')

    

    # NHIDTLB
    nhidtlb_data = pd.read_csv('./example/NHIDTLB.csv')
    nhidtlb_data.rename(columns={
        'MEDNO': 'fk_medno',
        'DTLB_06': 'accession_number',
        'DTLB_15': 'admission_date',
        'DTLB_16': 'discharge_date',
        'DTLB_28': 'cm_code',
        'DTLB_33': 'pcs_code'
    }, inplace=True)

    nhidtlb_data['hos'] = '801'

    def convert_minguo_to_gregorian(date_str):
        # 提取年份、月份和日期
        date_str = str(date_str)
        year = int(date_str[:3]) + 1911  # 民國年轉公元年
        month_day = date_str[3:]         # 保持月份和日期部分
        return f"{year}{month_day}"      # 返回轉換後的 'YYYYMMDD' 格式

    # 轉換日期欄位
    nhidtlb_data['admission_date'] = nhidtlb_data['admission_date'].apply(convert_minguo_to_gregorian)
    nhidtlb_data['discharge_date'] = nhidtlb_data['discharge_date'].apply(convert_minguo_to_gregorian)

    # 轉換為 datetime 格式，並格式化為 'YYYY-MM-DD'
    nhidtlb_data['admission_date'] = pd.to_datetime(nhidtlb_data['admission_date'], format='%Y%m%d', errors='coerce')
    nhidtlb_data['discharge_date'] = pd.to_datetime(nhidtlb_data['discharge_date'], format='%Y%m%d', errors='coerce')

    # 將日期欄位轉換為字串格式，避免 Timestamp 錯誤
    nhidtlb_data['admission_date'] = nhidtlb_data['admission_date'].dt.strftime('%Y-%m-%d')
    nhidtlb_data['discharge_date'] = nhidtlb_data['discharge_date'].dt.strftime('%Y-%m-%d')

    # 轉換其他欄位為字串格式，跳過日期欄位
    for column in nhidtlb_data.columns:
        if column not in ['admission_date', 'discharge_date']:
            nhidtlb_data[column] = nhidtlb_data[column].astype(str)

    # 檢查轉換後的數據
    # print(nhidtlb_data)

    # 將資料轉為字典列表格式以便發送
    nhidtlb_data_dict_list = nhidtlb_data.to_dict(orient='records')


    # NHIORDB
    nhiordb_data = pd.read_csv('./example/NHIORDB.csv')
    nhiordb_data.rename(columns={
        'MEDNO': 'fk_medno',
        'ORDB_06': 'accession_number',
        'ORDB_13': 'execution_date',
        'ORDB_14': 'expiration_date',
        'ORDB_10': 'order_code',
        'ORDB_15': 'total_number'
    }, inplace=True)

    nhiordb_data['execution_date'] = nhiordb_data['execution_date'].astype(str).str[:7]
    # nhiordb_data['execution_date'] = pd.to_datetime(nhiordb_data['execution_date'], errors='coerce')
    # nhiordb_data['execution_date'] = nhiordb_data['execution_date'].dt.strftime('%Y-%m-%d')

    nhiordb_data['expiration_date'] = nhiordb_data['expiration_date'].astype(str).str[:7]
    # nhiordb_data['expiration_date'] = pd.to_datetime(nhiordb_data['expiration_date'], errors='coerce')
    # nhiordb_data['expiration_date'] = nhiordb_data['expiration_date'].dt.strftime('%Y-%m-%d')

    nhiordb_data['execution_date'] = nhiordb_data['execution_date'].apply(convert_minguo_to_gregorian)
    nhiordb_data['expiration_date'] = nhiordb_data['expiration_date'].apply(convert_minguo_to_gregorian)

    # 轉換為 datetime 格式，並格式化為 'YYYY-MM-DD'
    nhiordb_data['execution_date'] = pd.to_datetime(nhiordb_data['execution_date'], format='%Y%m%d', errors='coerce')
    nhiordb_data['expiration_date'] = pd.to_datetime(nhiordb_data['expiration_date'], format='%Y%m%d', errors='coerce')

    # 將日期欄位轉換為字串格式，避免 Timestamp 錯誤
    nhiordb_data['execution_date'] = nhiordb_data['execution_date'].dt.strftime('%Y-%m-%d')
    nhiordb_data['expiration_date'] = nhiordb_data['expiration_date'].dt.strftime('%Y-%m-%d')

    nhiordb_data['hos'] = '801'
    for column in nhiordb_data.columns:
        if column not in ['execution_date', 'expiration_date']:
            nhiordb_data[column] = nhiordb_data[column].astype(str)
    # print(nhiordb_data)

    nhiordb_data_dict_list = nhiordb_data.to_dict(orient='records')

    # post_mismedd_data(hismedd_data_dict_list)
    # post_nhidtlb_data(nhidtlb_data_dict_list)
    # post_nhiordb_data(nhiordb_data_dict_list)
    # post_r2()
    # get_r2_data('3363739')


    # FEXREPORT
    fexreport_data = pd.read_csv('./example/FEXREPORT.csv')
    fexreport_data.rename(columns={
        'CNO': 'cno',
        'REPORT_DATE': 'report_date',
        'LISACCES': 'fk_accession_number',
        'ORDCLNM_NAME': 'ordclnm_name',
        'DATA': 'data',
        'HIS_NHICODE': 'order_code'
    }, inplace=True)
    fexreport_data['hos'] = '801'
    fexreport_data['order_code'] = fexreport_data['order_code'].apply(lambda x: None if pd.isna(x) else x)

    fexreport_data['report_date'] = pd.to_datetime(fexreport_data['report_date'], format='%Y%m%d', errors='coerce')
    fexreport_data['report_date'] = fexreport_data['report_date'].dt.strftime('%Y-%m-%d')
    for column in fexreport_data.columns:
        if column != 'report_date':
            fexreport_data[column] = fexreport_data[column].astype(str)
    # print(fexreport_data)
    fexreport_data_dict_list = fexreport_data.to_dict(orient='records')
    # post_fexreport_data(fexreport_data_dict_list)
    # post_ordercodemaster_data(ordercodemaster_data_dict_list)
    # post_cure_rec_data(cure_rec_data_dict_list)
    # post_r7()
    get_r7_data('3363739')
    # # python -m func.api