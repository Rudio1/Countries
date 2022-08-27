

from tkinter import CENTER
import requests
import json
import xlsxwriter 
import pandas as pd


#Criando o Excel e formatando.
workbook = xlsxwriter.Workbook('Countries.xlsx') 
center_format = workbook.add_format()
center_format.set_align("COUNTRIES")
workbook.formats[1].set_font_size(30)
worksheet = workbook.add_worksheet() 
worksheet.merge_range('A1:D2', "")
worksheet.write('A1', "Countries", center_format)

# worksheet.write('A2', 'COUNTRIES LIST')
worksheet.write('A3', 'Name') 
worksheet.write('B3', 'Capital') 
worksheet.write('C3', 'Area') 
worksheet.write('D3', 'Currencies') 

listCountries = []
listCapital = []
listCurrencies = []
listArea = []  

url = requests.get("https://restcountries.com/v2/all")
request = json.loads(url.content)
formatJson = json.dumps(request, sort_keys=True, indent=4)
count = 4
for pais in request:
    try:
        listCountries.append(pais["name"])
        listCapital.append(pais["capital"])
        listCurrencies.append(pais["currencies"])
        listArea.append(pais["area"])
    except(Exception):
        continue
    worksheet.write('A'+str(count), pais["name"])
    worksheet.write('B'+str(count), pais["capital"])
    worksheet.write('C'+str(count), pais["area"])
    for info in listCurrencies:
        worksheet.write('D'+ str(count), info[0]["code"])
    count = count + 1
workbook.close() 


    


