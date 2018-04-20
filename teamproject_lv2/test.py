import csv

def land_code():
  results = {}
  with open("C:\\Users\\Owner\\Documents\\금융데이타분석과정\\법정동명코드.csv",newline="", encoding="EUC-KR") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
      results[row['코드']]=row['법정동']
  return results

print(land_code().keys())
print(land_code().values())
