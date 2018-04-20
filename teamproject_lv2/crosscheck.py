import requests
from bs4 import BeautifulSoup

url="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"

payload = {
"serviceKey": "7pKXTHaVhHyx+1mjp1fTYnVIxrc7rh8SFeeM0e7IqS16ZtSiwjIKiDVs8TXUDS45spBIw9O5+5/VnJS86wqn3A==",
"LAWD_CD": "11110",
"DEAL_YMD": "201512"
}

data = requests.get(url, params=payload)
soup=BeautifulSoup(data.content, 'lxml-xml')
items=soup.items

print(items)
#for item in items:
 #   print(item)
