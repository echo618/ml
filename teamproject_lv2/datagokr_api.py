import requests
from bs4 import BeautifulSoup
import csv
import Input_YM
import test

ym1=input("조회시작년월6자리수를 입력하세요: ")
ym2=input("조회끝년월6자리수를 입력하세요: ")

if len(ym1)!=6 or len(ym2)!=6:
  pass
else:

    file=open("C:\\Users\\Owner\\Documents\\금융데이타분석과정\\deal_trade.csv","w",newline="",encoding="utf-8")
    csv_writer=csv.writer(file)

    url="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
    LAWD_CDS=test.land_code()
    LAWD_CDS_keys=test.land_code().keys()

    DEAL_YMDS=Input_YM.input_YM(ym1,ym2)

    csv_writer.writerow(["년","월","일","시군구코드","시군구","법정동","아파트명","거래가격","전용면적"])
    for DEAL_YMD in DEAL_YMDS:
        for LAWD_CD in LAWD_CDS_keys:

            payload = {
            "serviceKey": "7pKXTHaVhHyx+1mjp1fTYnVIxrc7rh8SFeeM0e7IqS16ZtSiwjIKiDVs8TXUDS45spBIw9O5+5/VnJS86wqn3A==",
            "LAWD_CD": LAWD_CD,
            "DEAL_YMD": DEAL_YMD
            }

            data = requests.get(url, params=payload)
            soup=BeautifulSoup(data.content, 'lxml-xml')
            items=soup.items
            list=[]
            for item in items:
                price = item.거래금액.text
                name = item.아파트.text
                location1 = item.지역코드.text
                location2 = item.법정동.text
                year = item.년.text
                month = item.월.text
                day = item.일.text
                size = item.전용면적.text
                #loc_name = LAWD_CDS[LAWD_CD]
                list = [year, month, day, location1, location2, name, price, size]
                csv_writer.writerow(list)

    file.close()