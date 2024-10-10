-- 門診
WITH Combined_DTLFA AS (
  SELECT "DTLID", "CHARTNO", "DTLFA_D19", "DTLFA_D24", "DTLFA_D9"
  FROM "HIS2USER2"."DTLFA"
  UNION ALL
  SELECT "DTLID", "CHARTNO", "DTLFA_D19", "DTLFA_D24", "DTLFA_D9"
  FROM "HIS2USER2"."DTLFA_OLD"
),
Combined_ORDFA AS (
  SELECT "DTLID", "ORDFA_P1", "ORDFA_P10", "ORDFA_P4"
  FROM "HIS2USER2"."ORDFA"
  UNION ALL
  SELECT "DTLID", "ORDFA_P1", "ORDFA_P10", "ORDFA_P4"
  FROM "HIS2USER2"."ORDFA_OLD"
)
SELECT D."DTLID",
D."CHARTNO",
D."DTLFA_D19",
D."DTLFA_D24",
D."DTLFA_D9",
O."ORDFA_P1",
O."ORDFA_P10",
O."ORDFA_P4"
FROM Combined_DTLFA D
JOIN Combined_ORDFA O
ON D."DTLID" = O."DTLID"
WHERE D."CHARTNO" = '3363739'

-- 住院
SELECT H.[CHARTNO], 
H.[MEDNO], 
D.AdmissionDate, 
D.DischargeDate, 
D.ICDCode, 
D.ICDProcedureCode, 
O.OrderStartDate, 
O.OrderEndDate, 
O.OrderCode, 
O.TotalOrderAmount
FROM (
  SELECT [MEDNO], [CHARTNO]
  FROM [dbo].[HISMEDD]
  WHERE [CHARTNO] = '3363739'
) H
LEFT JOIN (
  SELECT H.[MEDNO], 
  D.[DTLB_15] AS AdmissionDate, 
  D.[DTLB_16] AS DischargeDate, 
  D.[DTLB_28] AS ICDCode, 
  D.[DTLB_33] AS ICDProcedureCode
  FROM [dbo].[NHIDTLB] D
  JOIN [dbo].[HISMEDD] H ON H.[MEDNO] = D.[MEDNO]
  WHERE H.[CHARTNO] = '3363739'
) D ON H.[MEDNO] = D.[MEDNO]
LEFT JOIN (
  SELECT H.[MEDNO], 
  O.[ORDB_13] AS OrderStartDate, 
  O.[ORDB_14] AS OrderEndDate, 
  O.[ORDB_10] AS OrderCode, 
  O.[ORDB_15] AS TotalOrderAmount
  FROM [dbo].[NHIORDB] O
  JOIN [dbo].[HISMEDD] H ON H.[MEDNO] = O.[MEDNO]
  WHERE H.[CHARTNO] = '3363739'
) O ON H.[MEDNO] = O.[MEDNO];

-- 檢查
SELECT [CNO], [REPORT_DATE], [ORDCLNM_NAME], [DATA], [HIS_NHICODE], [LISACCES]
FROM [dbo].[FEXREPORT]
WHERE [CNO] = '3363739'


SELECT DISTINCT "O"."ORDERCODE", "O"."INSRCODE"
FROM "HIS2USER2"."ORDERCODEMASTER" O
WHERE "O"."ORDERCODE" IN (
  SELECT "C"."CUREID"
  FROM "HIS2USER2"."CURE_REC" C
  WHERE "C"."ACCESSNO" = '3084098959'
)

SELECT LISTAGG("INSRCODE", ',') WITHIN GROUP (ORDER BY "INSRCODE") AS insr_codes
FROM (
  SELECT DISTINCT "O"."INSRCODE"
  FROM "HIS2USER2"."ORDERCODEMASTER" O
  WHERE "O"."ORDERCODE" IN (
    SELECT "C"."CUREID"
    FROM "HIS2USER2"."CURE_REC" C
    WHERE "C"."ACCESSNO" = '3084098959'
  )
)

-- 影像
SELECT TOP 500 [PATIENT_ID]
	,[PERFRMD_START_DATE]
	,[report_text]
	,[CODE]
FROM [dbo].[FXYREPORT]
WHERE [PATIENT_ID] = '3363739'

-- CURE_REC
SELECT "CUREID", "ACCESSNO"
FROM "HIS2USER2"."CURE_REC"
WHERE "ACCESSNO" IN ('3084098957',
                     '3084098958',
                     '3084098959',
                     '4067631304',
                     '4067631305',
                     '4067631306',
                     '4067631307',
                     '4067631308',
                     '4067631309',
                     '4077737915',
                     '4077737916',
                     '4077737917',
                     '4077737918',
                     '4077737919',
                     '4077737920',
                     '4087924876',
                     '4087924877',
                     '4087924878',
                     '4087924879',
                     '4087924880',
                     '4087924881',
                     '4090589036',
                     '4090589037',
                     '4090589038');


-- ORDERCODEMASTER
SELECT "ORDERCODE", "INSRCODE"
FROM "HIS2USER2"."ORDERCODEMASTER"
WHERE "ORDERCODE" IN ('09002C',
                      '09021C',
                      '09022C',
                      '09025C',
                      '09015C',
                      'LAB058',
                      'LAB063',
                      'LAB062',
                      'LAB143',
                      '11003C',
                      'LAB061',
                      '11001C',
                      'LAB060',
                      'LAB127',
                      'LAB060',
                      '09001C',
                      '09002C',
                      '09004C',
                      '09015C',
                      '09021C',
                      '09022C',
                      '09023C',
                      '09025C',
                      '09026C',
                      '09031C',
                      '09032C',
                      '09038C',
                      '09040C',
                      '12015C',
                      '09043C',
                      '09044C',
                      '09046B',
                      'LAB045',
                      'LAB128',
                      '06009C',
                      '06013C',
                      '27004C',
                      '27027B',
                      'LAB127',
                      'LAB060',
                      '09040C',
                      '09026C',
                      '09032C',
                      '09038C',
                      '09043C',
                      '09044C',
                      '09001C',
                      '09002C',
                      '09004C',
                      '09015C',
                      '09021C',
                      '09022C',
                      '09023C',
                      '09025C',
                      'LAB045',
                      '09046B',
                      '12015C',
                      '09031C',
                      'LAB128',
                      '06009C',
                      '06013C',
                      '27004C',
                      '27027B',
                      'LAB060',
                      'LAB127',
                      '09032C',
                      '09038C',
                      '09040C',
                      '09043C',
                      '09044C',
                      '09046B',
                      '12015C',
                      'LAB045',
                      '09001C',
                      '09002C',
                      '09004C',
                      '09015C',
                      '09021C',
                      '09022C',
                      '09023C',
                      '09025C',
                      '09026C',
                      '09031C',
                      '06009C',
                      '06013C',
                      'LAB128',
                      '27004C',
                      '27027B',
                      'R05031',
                      'R10011');

