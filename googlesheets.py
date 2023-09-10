import requests
import os

def sheetwriter(sheet_inputs):
    endpoint = 'https://api.sheety.co/3e6d2b3fe2c1c58561fc71bfa79a52b3/myWorkouts/workouts'
    token = os.environ.get('sheetytoken')
    header ={
        'Authorization':f'Bearer {token}'
    }

    json1 =sheet_inputs
    requests.post(url=endpoint,headers=header,json=json1)