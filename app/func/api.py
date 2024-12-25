import json
import logging
import os
import sys

from collections import defaultdict
from datetime import datetime
from requests import get, patch, post, put, RequestException

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from middleware.exception import exception_message

uvicorn_logger = logging.getLogger('uvicorn.error')
system_logger = logging.getLogger('custom.error')

### 801 ###
class Hos801Data:

    def __init__(self, base_url="http://0.0.0.0:726/api/v1"):

        self.base_url = base_url

    def post_ordercodemaster_data(self, ordercodemaster_data):

        url = f"{self.base_url}/ordercodemaster"

        for data in ordercodemaster_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("ORDERCODEMASTER data post successfully")

                else:
                    print(f"Failed to post ORDERCODEMASTER data: {response.text}")
                    system_logger.error(f"Failed to post ORDERCODEMASTER data: {response.text}")
            
            except RequestException as e:
                system_logger.error(exception_message(e))

    def get_ordercodemaster_data(self):

        url = f"{self.base_url}/ordercodemaster"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve ORDERCODEMASTER data: {response.text}")
                system_logger.error(f"Failed to retrieve ORDERCODEMASTER data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_cure_rec_data(self, cure_rec_data):

        url = f"{self.base_url}/cure_rec"

        for data in cure_rec_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("CURE_REC data post successfully")

                else:
                    print(f"Failed to post CURE_REC data: {response.text}")
                    system_logger.error(f"Failed to post CURE_REC data: {response.text}")
            
            except RequestException as e:
                system_logger.error(exception_message(e))

    def get_cure_rec_data(self):

        url = f"{self.base_url}/cure_rec"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve CURE_REC data: {response.text}")
                system_logger.error(f"Failed to retrieve CURE_REC data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_dtlfa_data(self, dtlfa_data):
        
        url = f"{self.base_url}/dtlfa"

        for data in dtlfa_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("DTLFA data sent successfully")
                
                else:
                    print(f"Failed to post DTLFA data: {response.text}")
                    system_logger.error(f"Failed to post DTLFA data: {response.text}")

            except RequestException as e:
                system_logger.error(exception_message(e))
    
    def get_dtlfa_data(self):

        url = f"{self.base_url}/dtlfa"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve DTLFA data: {response.text}")
                system_logger.error(f"Failed to retrieve DTLFA data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))
    
    def post_ordfa_data(self, ordfa_data):

        url = f"{self.base_url}/ordfa"

        for data in ordfa_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("ORDFA data sent successfully")
                
                else:
                    print(f"Failed to post ORDFA data: {response.text}")
                    system_logger.error(f"Failed to post ORDFA data: {response.text}")

            except RequestException as e:
                system_logger.error(exception_message(e))
    
    def get_ordfa_data(self):

        url = f"{self.base_url}/ordfa"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve ORDFA data: {response.text}")
                system_logger.error(f"Failed to retrieve ORDFA data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_hismedd_data(self, hismedd_data):
        
        url = f"{self.base_url}/hismedd"

        for data in hismedd_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("HISMEDD data sent successfully")
                
                else:
                    print(f"Failed to post HISMEDD data: {response.text}")
                    system_logger.error(f"Failed to post HISMEDD data: {response.text}")

            except RequestException as e:
                system_logger.error(exception_message(e))
    
    def get_hismedd_data(self):

        url = f"{self.base_url}/hismedd"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve HISMEDD data: {response.text}")
                system_logger.error(f"Failed to retrieve HISMEDD data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))
    
    def post_nhidtlb_data(self, nhidtlb_data):

        url = f"{self.base_url}/nhidtlb"

        for data in nhidtlb_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("NHIDTLB data sent successfully")
                
                else:
                    print(f"Failed to post NHIDTLB data: {response.text}")
                    system_logger.error(f"Failed to post NHIDTLB data: {response.text}")

            except RequestException as e:
                system_logger.error(exception_message(e))
    
    def get_nhidtlb_data(self):

        url = f"{self.base_url}/nhidtlb"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve NHIDTLB data: {response.text}")
                system_logger.error(f"Failed to retrieve NHIDTLB data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_nhiordb_data(self, nhiordb_data):

        url = f"{self.base_url}/nhiordb"

        for data in nhiordb_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("NHIORDB data sent successfully")
                
                else:
                    print(f"Failed to post NHIORDB data: {response.text}")
                    system_logger.error(f"Failed to post NHIORDB data: {response.text}")

            except RequestException as e:
                system_logger.error(exception_message(e))
    
    def get_nhiordb_data(self):

        url = f"{self.base_url}/nhiordb"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve NHIORDB data: {response.text}")
                system_logger.error(f"Failed to retrieve NHIORDB data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_fexreport_data(self, fexreport_data):

        url = f"{self.base_url}/fexreport"

        for data in fexreport_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("FEXREPORT data sent successfully")
                
                else:
                    print(f"Failed to post FEXREPORT data: {response.text}")
                    system_logger.error(f"Failed to post FEXREPORT data: {response.text}")

            except RequestException as e:
                system_logger.error(exception_message(e))
    
    def get_fexreport_data(self):

        url = f"{self.base_url}/fexreport"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve FEXREPORT data: {response.text}")
                system_logger.error(f"Failed to retrieve FEXREPORT data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))

    def get_lisdetail_data(self, report_date: str):

        url = f"{self.base_url}/aiot_research"

        try:
            params = {"report_date": report_date}

            response = get(url, params=params)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve LISDETAIL data: {response.text}")
                system_logger.error(f"Failed to retrieve LISDETAIL data: {response.text}")
                return None
        
        except RequestException as e:
            system_logger.error(exception_message(e))
            return None

    def get_query_data_range(self, start_date: str, end_date: str, template_name: str, performed_item: str = None):

        url = f"{self.base_url}/aiot_research/range"

        try:
            # 構建請求參數
            params = {
                "start_date": start_date,
                "end_date": end_date,
                "template_name": template_name
            }

            if performed_item:
                params["performed_item"] = performed_item

            # 發送 GET 請求
            response = get(url, params=params)

            # 檢查回應狀態
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=True))
                return response.json()
            else:
                print(f"Failed to retrieve AIOT research data: {response.text}")
                system_logger.error(f"Failed to retrieve AIOT research data: {response.text}")
                return None

        except RequestException as e:
            system_logger.error(f"Request exception: {e}")
            return None

    def post_fxyreport_data(self, fxyreport_data):

        url = f"{self.base_url}/fxyreport"

        for data in fxyreport_data:

            try:
                response = post(url, json=data)

                if response.status_code == 200:
                    print("FXYREPORT data sent successfully")
                
                else:
                    print(f"Failed to post FXYREPORT data: {response.text}")
                    system_logger.error(f"Failed to post FXYREPORT data: {response.text}")

            except RequestException as e:
                system_logger.error(exception_message(e))
    
    def get_fxyreport_data(self):

        url = f"{self.base_url}/fxyreport"

        try:
            response = get(url)

            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, ensure_ascii=False))
                return response.json()

            else:
                print(f"Failed to retrieve FXYREPORT data: {response.text}")
                system_logger.error(f"Failed to retrieve FXYREPORT data: {response.text}")
        
        except RequestException as e:
            system_logger.error(exception_message(e))


class HealthBankData:

    def __init__(self, base_url="http://0.0.0.0:726/api/v1"):

        self.base_url = base_url

    def post_r1_data(self):

        url = f"{self.base_url}/r1"

        try:
            response = post(url)

            if response.status_code == 200:
                print("R1 post successfully")
            
            else:
                print(f"Failed to post R1: {response.text}")
                system_logger.error(f"Failed to post R1: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))
    
    def get_r1_data_by_cno(self, cno: str): 

        url = f"{self.base_url}/r1"

        try:
            response = get(url, params={"cno": cno})
            if response.status_code == 200:
                data = response.json()

                r1_output = []
                r1_dict = defaultdict(list)

                for entry in data:
                    r1_1_item = {
                        "r1_1.1": entry['order_code'] if entry['order_code'] != 'nan' else '',
                        "r1_1.3": str(entry['total_number']) if entry['total_number'] is not None else '',
                        "r1_1.4": entry['dose_day'] if entry['dose_day'] != 'nan' else ''
                    }
                    r1_dict[entry['dtlid']].append(r1_1_item)
                
                for dtlid, r1_1_items in r1_dict.items():
                    first_entry = next(entry for entry in data if entry['dtlid'] == dtlid)
                    r1_item = {
                        "r1.5": first_entry['treatment_date'].replace('-', ''),
                        "r1.8": first_entry['cm_code'] if first_entry['cm_code'] != 'nan' else '',
                        "r1.10": first_entry['pcs_code'] if first_entry['pcs_code'] != 'nan' else '',
                        "r1_1": r1_1_items
                    }
                    r1_output.append(r1_item)

                print(json.dumps(r1_output, indent=4, ensure_ascii=False))
                return r1_output
            
            else:
                print(f"Failed to retrieve R1 data by CNO: {response.text}")
                system_logger.error(f"Failed to retrieve R1 data by CNO: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_r2_data(self):

        url = f"{self.base_url}/r2"

        try:
            response = post(url)

            if response.status_code == 200:
                print("R2 post successfully")
            
            else:
                print(f"Failed to post R2: {response.text}")
                system_logger.error(f"Failed to post R2: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))
    
    def get_r2_data_by_cno(self, cno: str): 

        url = f"{self.base_url}/r2"

        try:
            response = get(url, params={"cno": cno})
            if response.status_code == 200:
                data = response.json()

                r2_output = []
                r2_dict = defaultdict(list)

                for entry in data:
                    r2_1_item = {
                        "r2_1.2": entry['execution_date'].replace('-', ''),
                        "r2_1.3": entry['expiration_date'].replace('-', ''),
                        "r2_1.4": entry['order_code'],
                        "r2_1.6": str(entry['total_number'])
                    }
                    r2_dict[entry['accession_number']].append(r2_1_item)

                for accession_number, r2_1_items in r2_dict.items():
                    first_entry = next(e for e in data if e['accession_number'] == accession_number)
                    r2_item = {
                        "r2.5": first_entry['admission_date'].replace('-', ''),
                        "r2.6": first_entry['discharge_date'].replace('-', ''),
                        "r2.10": first_entry['cm_code'] if first_entry['cm_code'] != 'nan' else '',
                        "r2.12": first_entry['pcs_code'] if first_entry['pcs_code'] != 'nan' else '',
                        "r2_1": r2_1_items
                    }
                    r2_output.append(r2_item)

                print(json.dumps(r2_output, indent=4, ensure_ascii=False))
                return r2_output
            
            else:
                print(f"Failed to retrieve R2 data by CNO: {response.text}")
                system_logger.error(f"Failed to retrieve R2 data by CNO: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_r7_data(self):

        url = f"{self.base_url}/r7"

        try:
            response = post(url)

            if response.status_code == 200:
                print("R7 post successfully")
            
            else:
                print(f"Failed to post R7: {response.text}")
                system_logger.error(f"Failed to post R7: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))

    def get_r7_data_by_cno(self, cno: str): 

        url = f"{self.base_url}/r7"

        try:
            response = get(url, params={"cno": cno})
            if response.status_code == 200:
                data = response.json()

                r7_output = []

                if isinstance(data, list):
                    for entry in data:
                        r7_item = {
                            "r7.6": str(entry['report_date']).replace('-', ''), 
                            "r7.8": entry['order_code'],
                            "r7.10": entry['ordclnm_name'],
                            "r7.11": entry['data']
                        }
                        r7_output.append(r7_item)
                else:
                    r7_item = {
                        "r7.6": str(data['report_date']).replace('-', ''), 
                        "r7.8": data['order_code'],
                        "r7.10": data['ordclnm_name'],
                        "r7.11": data['data']
                    }
                    r7_output.append(r7_item)

                print(json.dumps(r7_output, indent=4, ensure_ascii=False))
                return r7_output
            
            else:
                print(f"Failed to retrieve R7 data by CNO: {response.text}")
                system_logger.error(f"Failed to retrieve R7 data by CNO: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))

    def post_r8_data(self):

        url = f"{self.base_url}/r8"

        try:
            response = post(url)

            if response.status_code == 200:
                print("R8 post successfully")
            
            else:
                print(f"Failed to post R8: {response.text}")
                system_logger.error(f"Failed to post R8: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))

    def get_r8_data_by_cno(self, cno: str): 

        url = f"{self.base_url}/r8"

        try:
            response = get(url, params={"cno": cno})
            if response.status_code == 200:
                data = response.json()

                r8_output = []

                if isinstance(data, list):
                    for entry in data:
                        r8_item = {
                            "r8.6": str(entry['performed_start_date']).replace('-', ''), 
                            "r8.8": entry['order_code'],
                            "r8.10": entry['report_text']
                        }
                        r8_output.append(r8_item)
                else:
                    r8_item = {
                        "r8.6": str(data['performed_start_date']).replace('-', ''), 
                        "r8.8": data['order_code'],
                        "r8.10": data['report_text']
                    }
                    r8_output.append(r8_item)

                print(json.dumps(r8_output, indent=4, ensure_ascii=False))
                return r8_output
            
            else:
                print(f"Failed to retrieve R8 data by CNO: {response.text}")
                system_logger.error(f"Failed to retrieve R8 data by CNO: {response.text}")

        except RequestException as e:
            system_logger.error(exception_message(e))

### Data processing ###
class Process801Data:

    def __init__(self, hos='801'):
        self.hos = hos

    def convert_time_type(self, date):
        return f"{int(str(date)[:3]) + 1911}{str(date)[3:]}"

    def format_date(self, date, format='%Y%m%d'):
        return datetime.strptime(str(date), format).strftime('%Y-%m-%d')

    def process_dtlfa_data(self, json_data):
        required_fields = ['DTLID', 'CHARTNO', 'DTLFA_D9', 'DTLFA_D19', 'DTLFA_D24']

        for entry in json_data:
            filtered_entry = {key: entry[key] for key in required_fields if key in entry}  # 過濾出需要的欄位
            filtered_entry['hos'] = self.hos
            filtered_entry['dtlid'] = filtered_entry.pop('DTLID')  # 將欄位重命名
            filtered_entry['cno'] = filtered_entry.pop('CHARTNO')
            filtered_entry['treatment_date'] = filtered_entry.pop('DTLFA_D9')
            filtered_entry['cm_code'] = filtered_entry.pop('DTLFA_D19')
            filtered_entry['pcs_code'] = filtered_entry.pop('DTLFA_D24')

            try:
                filtered_entry['treatment_date'] = datetime.strptime(filtered_entry['treatment_date'][:10], '%Y-%m-%d').strftime('%Y-%m-%d') # 處理日期格式
            except (ValueError, TypeError):
                filtered_entry['treatment_date'] = None

            for key, value in filtered_entry.items():  # 清理無效值
                if value in [None, 'NaN', float('inf'), float('-inf')]:
                    filtered_entry[key] = None

            for key in filtered_entry.keys():
                if key != 'treatment_date':
                    filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()  # 更新原始項目為過濾後的項目
            entry.update(filtered_entry)

        return json_data

    def process_ordfa_data(self, json_data):
        required_fields = ['DTLID', 'ORDFA_P1', 'ORDFA_P4', 'ORDFA_P10']

        for entry in json_data:
            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['fk_dtlid'] = filtered_entry.pop('DTLID')
            filtered_entry['dose_day'] = filtered_entry.pop('ORDFA_P1')
            filtered_entry['order_code'] = filtered_entry.pop('ORDFA_P4')
            filtered_entry['total_number'] = filtered_entry.pop('ORDFA_P10')
            
            try:
                filtered_entry['dose_day'] = str(float(filtered_entry['dose_day']))
            except (ValueError, TypeError):
                filtered_entry['dose_day'] = 'None'

            for key, value in filtered_entry.items():
                if value in [None, 'NaN', float('inf'), float('-inf')]:
                    filtered_entry[key] = None
            
            for key in filtered_entry.keys():
                filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data

    def process_ordercodemaster_data(self, json_data):
        required_fields = ['ORDERCODE', 'INSRCODE']
    
        for entry in json_data:

            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['hos_ordercode'] = filtered_entry.pop('ORDERCODE')
            filtered_entry['order_code'] = filtered_entry.pop('INSRCODE')

            for key in filtered_entry.keys():
                filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data

    def process_cure_rec_data(self, json_data):
        required_fields = ['CUREID', 'ACCESSNO']
        
        for entry in json_data:

            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['fk_hos_ordercode'] = filtered_entry.pop('CUREID')
            filtered_entry['accession_number'] = filtered_entry.pop('ACCESSNO')

            for key in filtered_entry.keys():
                filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data
    
    def process_hismedd_data(self, json_data):
        required_fields = ['MEDNO', 'CHARTNO']

        for entry in json_data:

            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['medno'] = filtered_entry.pop('MEDNO')
            filtered_entry['cno'] = filtered_entry.pop('CHARTNO')
            
            for key in filtered_entry.keys():
                filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data

    def process_nhidtlb_data(self, json_data):
        required_fields = ['MEDNO', 'DTLB_06', 'DTLB_15', 'DTLB_16', 'DTLB_28', 'DTLB_33']

        for entry in json_data:
            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['fk_medno'] = filtered_entry.pop('MEDNO')
            filtered_entry['accession_number'] = filtered_entry.pop('DTLB_06')
            filtered_entry['admission_date'] = filtered_entry.pop('DTLB_15')
            filtered_entry['discharge_date'] = filtered_entry.pop('DTLB_16')
            filtered_entry['cm_code'] = filtered_entry.pop('DTLB_28')
            filtered_entry['pcs_code'] = filtered_entry.pop('DTLB_33')
            
            filtered_entry['admission_date'] = self.convert_time_type(filtered_entry.get('admission_date', ''))
            filtered_entry['discharge_date'] = self.convert_time_type(filtered_entry.get('discharge_date', ''))

            filtered_entry['admission_date'] = self.format_date(filtered_entry['admission_date'])
            filtered_entry['discharge_date'] = self.format_date(filtered_entry['discharge_date'])

            for key in filtered_entry.keys():
                if key not in ['admission_date', 'discharge_date']:
                    filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data

    def process_nhiordb_data(self, json_data):
        required_fields = ['MEDNO', 'ORDB_06', 'ORDB_10', 'ORDB_13', 'ORDB_14', 'ORDB_15']

        for entry in json_data:
            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['fk_medno'] = filtered_entry.pop('MEDNO')
            filtered_entry['accession_number'] = filtered_entry.pop('ORDB_06')
            filtered_entry['order_code'] = filtered_entry.pop('ORDB_10')
            filtered_entry['execution_date'] = filtered_entry.pop('ORDB_13')
            filtered_entry['expiration_date'] = filtered_entry.pop('ORDB_14')
            filtered_entry['total_number'] = filtered_entry.pop('ORDB_15')
            
            filtered_entry['execution_date'] = str(filtered_entry['execution_date'])[:7]
            filtered_entry['expiration_date'] = str(filtered_entry['expiration_date'])[:7]

            filtered_entry['execution_date'] = self.convert_time_type(filtered_entry.get('execution_date', ''))
            filtered_entry['expiration_date'] = self.convert_time_type(filtered_entry.get('expiration_date', ''))

            filtered_entry['execution_date'] = self.format_date(filtered_entry['execution_date'])
            filtered_entry['expiration_date'] = self.format_date(filtered_entry['expiration_date'])

            for key in filtered_entry.keys():
                if key not in ['execution_date', 'expiration_date']:
                    filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data

    def process_fexreport_data(self, json_data):
        required_fields = ['CNO', 'REPORT_DATE', 'LISACCES', 'ORDCLNM_NAME', 'DATA', 'HIS_NHICODE']

        for entry in json_data:
            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['cno'] = filtered_entry.pop('CNO')
            filtered_entry['report_date'] = filtered_entry.pop('REPORT_DATE')
            filtered_entry['fk_accession_number'] = filtered_entry.pop('LISACCES')
            filtered_entry['ordclnm_name'] = filtered_entry.pop('ORDCLNM_NAME')
            filtered_entry['data'] = filtered_entry.pop('DATA')
            filtered_entry['order_code'] = filtered_entry.pop('HIS_NHICODE')
            
            filtered_entry['order_code'] = None if filtered_entry['order_code'] in [None, '', 'NaN'] else filtered_entry['order_code']
            filtered_entry['report_date'] = self.format_date(filtered_entry['report_date'], format='%Y%m%d')

            for key in filtered_entry.keys():
                if key != 'report_date':
                    filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data

    def process_fxyreport_data(self, json_data):
        required_fields = ['PATIENT_ID', 'PERFRMD_START_DATE', 'CODE', 'report_text']

        for entry in json_data:
            filtered_entry = {key: entry[key] for key in required_fields if key in entry}
            filtered_entry['hos'] = self.hos
            filtered_entry['cno'] = filtered_entry.pop('PATIENT_ID')
            filtered_entry['performed_start_date'] = filtered_entry.pop('PERFRMD_START_DATE')
            filtered_entry['fk_hos_ordercode'] = filtered_entry.pop('CODE')
            filtered_entry['report_text'] = filtered_entry.pop('report_text')
            
            filtered_entry['performed_start_date'] = self.format_date(filtered_entry['performed_start_date'], format='%Y%m%d')

            for key in filtered_entry.keys():
                if key != 'performed_start_date':
                    filtered_entry[key] = str(filtered_entry[key]) if filtered_entry[key] is not None else None

            entry.clear()
            entry.update(filtered_entry)

        return json_data

if __name__ == "__main__":

    import pandas as pd

    processor = Process801Data()
    processor_api = Hos801Data()
    processor_all = HealthBankData()
    
    # DTLFA
    # dtlfa_data = pd.read_csv('./example/DTLFA.csv')
    # dtlfa_dict_list = dtlfa_data.to_dict(orient='records')
    # dtlfa_dict_list = processor.process_dtlfa_data(dtlfa_dict_list)

    # # ORDFA
    # ordfa_data = pd.read_csv('./example/ORDFA.csv')
    # ordfa_dict_list = ordfa_data.to_dict(orient='records')
    # ordfa_dict_list = processor.process_ordfa_data(ordfa_dict_list)
    
    # # ORDERCODEMASTER
    # ordercodemaster_data = pd.read_csv('./example/ORDERCODEMASTER.csv')
    # ordercodemaster_data_dict_list = ordercodemaster_data.to_dict(orient='records')
    # ordercodemaster_data_dict_list = processor.process_ordercodemaster_data(ordercodemaster_data_dict_list)

    # # CURE_REC
    # cure_rec_data = pd.read_csv('./example/CURE_REC.csv')
    # cure_rec_data_dict_list = cure_rec_data.to_dict(orient='records')
    # cure_rec_data_dict_list = processor.process_cure_rec_data(cure_rec_data_dict_list)

    # # HISMEDD
    # hismedd_data = pd.read_csv('./example/HISMEDD.csv')
    # hismedd_data_dict_list = hismedd_data.to_dict(orient='records')
    # hismedd_data_dict_list = processor.process_hismedd_data(hismedd_data_dict_list)

    # # NHIDTLB
    # nhidtlb_data = pd.read_csv('./example/NHIDTLB.csv')
    # nhidtlb_data_dict_list = nhidtlb_data.to_dict(orient='records')
    # nhidtlb_data_dict_list = processor.process_nhidtlb_data(nhidtlb_data_dict_list)
    
    # # NHIORDB
    # nhiordb_data = pd.read_csv('./example/NHIORDB.csv')
    # nhiordb_data_dict_list = nhiordb_data.to_dict(orient='records')
    # nhiordb_data_dict_list = processor.process_nhiordb_data(nhiordb_data_dict_list)
    
    # # FEXREPORT
    # fexreport_data = pd.read_csv('./example/FEXREPORT.csv')
    # fexreport_data_dict_list = fexreport_data.to_dict(orient='records')
    # fexreport_data_dict_list = processor.process_fexreport_data(fexreport_data_dict_list)

    # # FXYREPORT
    # fxyreport_data = pd.read_csv('./example/FXYREPORT.csv')
    # fxyreport_data_dict_list = fxyreport_data.to_dict(orient='records')
    # fxyreport_data_dict_list = processor.process_fxyreport_data(fxyreport_data_dict_list)

    # processor_api.post_ordercodemaster_data(ordercodemaster_data_dict_list)
    # processor_api.get_ordercodemaster_data()

    # processor_api.post_cure_rec_data(cure_rec_data_dict_list)
    # processor_api.get_cure_rec_data()

    # processor_api.post_dtlfa_data(dtlfa_dict_list)
    # processor_api.get_dtlfa_data()

    # processor_api.post_ordfa_data(ordfa_dict_list)
    # processor_api.get_ordfa_data()

    # processor_api.post_hismedd_data(hismedd_data_dict_list)
    # processor_api.get_hismedd_data()

    # processor_api.post_nhidtlb_data(nhidtlb_data_dict_list)
    # processor_api.get_nhidtlb_data()

    # processor_api.post_nhiordb_data(nhiordb_data_dict_list)
    # processor_api.get_nhiordb_data()

    # processor_api.post_fexreport_data(fexreport_data_dict_list)
    # processor_api.get_fexreport_data()
    # processor_api.get_lisdetail_data(report_date='20240910')

    # processor_api.get_query_data_range('20230101', '20230102', '超音波檢查報告', 'Echo')

    # processor_api.post_fxyreport_data(fxyreport_data_dict_list)
    # processor_api.get_fxyreport_data()

    # processor_all.post_r1_data()
    # processor_all.get_r1_data_by_cno('3363739')

    # processor_all.post_r2_data()
    # processor_all.get_r2_data_by_cno('3363739')

    # processor_all.post_r7_data()
    processor_all.get_r7_data_by_cno('3363739')

    # processor_all.post_r8_data()
    # processor_all.get_r8_data_by_cno('3363739')
    
    quit()

    # python -m func.api