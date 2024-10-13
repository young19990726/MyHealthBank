if __name__ == "__main__":
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

    hismedd_data.rename(columns={
        'MEDNO': 'medno',
        'CHARTNO': 'cno'
    }, inplace=True)

    hismedd_data['hos'] = '801'

    for column in hismedd_data.columns:
        hismedd_data[column] = hismedd_data[column].astype(str)
    
    # 存起來      
    hismedd_data.to_csv(
        './example/HISMEDD_processed.csv', 
        index=False, 
        encoding='utf-8'
    )

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

    # 存起來      
    nhidtlb_data.to_csv(
        './example/NHIDTLB_processed.csv', 
        index=False, 
        encoding='utf-8'
    )

    # 將資料轉為字典列表格式以便發送

    nhiordb_data.rename(columns={
        'MEDNO': 'fk_medno',
        'ORDB_06': 'accession_number',
        'ORDB_13': 'execution_date',
        'ORDB_14': 'expiration_date',
        'ORDB_10': 'order_code',
        'ORDB_15': 'total_number'
    }, inplace=True)

    nhiordb_data['execution_date'] = nhiordb_data['execution_date'].astype(str).str[:7]
    nhiordb_data['expiration_date'] = nhiordb_data['expiration_date'].astype(str).str[:7]

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
    
    # 存起來      
    nhiordb_data.to_csv(
        './example/NHIORDB_processed.csv', 
        index=False, 
        encoding='utf-8'
    )

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

    # 存起來      
    fexreport_data.to_csv(
        './example/FEXREPORT_processed.csv', 
        index=False, 
        encoding='utf-8'
    )

    fxyreport_data.rename(columns={
        'PATIENT_ID': 'cno',
        'PERFRMD_START_DATE': 'performed_start_date',
        'CODE': 'fk_hos_ordercode',
        'report_text': 'report_text'
    }, inplace=True)

    fxyreport_data['hos'] = '801'

    fxyreport_data['performed_start_date'] = pd.to_datetime(fxyreport_data['performed_start_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d') 

    for column in fxyreport_data.columns:
        if column != 'performed_start_date':
            fxyreport_data[column] = fxyreport_data[column].astype(str)

    # 存起來      
    fxyreport_data.to_csv(
        './example/FXYREPORT_processed.csv', 
        index=False, 
        encoding='utf-8'
    )
