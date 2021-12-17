# -*- coding: cp1252 -*-
import requests
import pprint
import json
import csv

url = "https://api.meraki.com/api/v1/organizations"

payload = None
i = 0
k = 0
j = 0
organizaciones=[]
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

lista = requests.request('GET', url, headers=headers, data = payload)
lista.raise_for_status()
lista = lista.json()
pprint.pprint(lista)

while i < len(lista):
    organizaciones.append(lista[i]['name'])
    print(organizaciones[i])
    i=i+1


url2 = "https://api.meraki.com/api/v1/organizations/681155/devices?productTypes%5B%5D=wireless"
url3 = "https://api.meraki.com/api/v1/organizations/681155/devices?productTypes%5B%5D=appliance"
disp_wireless=requests.get(url2, headers=headers, data = payload)
disp_appliance=requests.get(url3, headers=headers, data = payload)
dev_wir=disp_wireless.json()
dev_appli=disp_appliance.json()
pprint.pprint(dev_wir)
pprint.pprint(dev_appli)


lista_dispositivos = open('devices.csv', 'w')
with lista_dispositivos:
    writer = csv.writer(lista_dispositivos)
    while k < len(dev_wir):
        if (dev_wir[k]['productType'] == "wireless"):
            writer.writerows(dev_wir[k])
        k = k+1
    while j < len(dev_appli):
         if (dev_appli[j]['productType'] == "apppliance"):
            writer.writerows(dev_appli[j])
         j = j+1










    
