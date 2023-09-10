import requests
import os
import datetime
from googlesheets import sheetwriter

def nutrionixapi(query):
    currentdate = datetime.datetime.now().strftime("%m/%d/%Y")
    currenttime=datetime.datetime.now().strftime("%H:%M %p")
    query=query
    nutrionixendpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
    header={
        'x-app-id':'430ca3e0',
        'x-app-key':os.environ.get('nutrionixkey'),
    }

    parameters={
        'query':query,
        'gender':'male',
        'weight_kg':104,
        'height_cm':182.88,
        'age':30
    }
    response = requests.post(url = nutrionixendpoint,json=parameters, headers=header)
    for exercise in response.json()["exercises"]:
        try:
            sheet_inputs = {
                'workout': {
                    "date": currentdate,
                    "time": currenttime,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }
            sheetwriter(sheet_inputs)
        except:
            continue
