from asyncio.windows_events import NULL
from itertools import count
import requests
import json
import xlsxwriter 

#Criando o Excel e formatando.
workbook = xlsxwriter.Workbook('Countries.xlsx') 
worksheet = workbook.add_worksheet() 
worksheet.write('A1', 'COUNTRIES LIST')
worksheet.write('A2', 'Name') 
worksheet.write('B2', 'Capital') 
worksheet.write('C2', 'Area') 
worksheet.write('D2', 'Currencies') 

listCountries = []
listCapital = []
listCurrencies = []
listArea = []  

url = requests.get("https://restcountries.com/v2/all")
request = json.loads(url.content)
formatJson = json.dumps(request, sort_keys=True, indent=4)
count = 3
for pais in request:
    try:
        listCountries.append(pais["name"])
        listCapital.append(pais["capital"])
        listCurrencies.append(pais["currencies"])
        listArea.append(pais["area"])
    except(Exception):
        print(listCapital)
        continue
    worksheet.write('A'+str(count), pais["name"])
    worksheet.write('B'+str(count), pais["capital"])
    worksheet.write('C'+str(count), pais["area"])
    for info in listCurrencies:
        worksheet.write('D'+ str(count), info[0]["code"])
    count = count + 1
workbook.close() 

    


