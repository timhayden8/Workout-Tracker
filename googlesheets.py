import requests
import os

def sheetwriter(sheet_inputs):
    endpoint = os.environ.get('sheetyendpoint')
    token = os.environ.get('sheetytoken')
    header ={
        'Authorization':f'Bearer {token}'
    }

    json1 =sheet_inputs
    requests.post(url=endpoint,headers=header,json=json1)