import requests
import json
import xlsxwriter 


workbook = xlsxwriter.Workbook('Countries.xlsx') 
worksheet = workbook.add_worksheet() 

workbook.close() 


istCountries = []
listCapital = []
listCurrencies = []
listArea = []  



url = requests.get("https://restcountries.com/v2/all")
request = json.loads(url.content)
formatJson = json.dumps(request, sort_keys=True, indent=4)
for pais in request:
    try:
        listCountries.append(pais["name"])
        listCapital.append(pais["capital"])
        listCurrencies.append(pais["currencies"])
        listArea.append(pais["area"])
        worksheet.write('A1', 'Hello..') 
        worksheet.write('B1', 'Geeks') 
        worksheet.write('C1', 'For') 
        worksheet.write('D1', 'Geeks') 
    except(Exception):
        continue
for info in listCurrencies:
   code = info[0]["code"]


    


