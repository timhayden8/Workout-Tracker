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
        'x-app-id':os.environ.get('nutrionixappid'),
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
    try:
        for exercise in response.json()["exercises"]:
            try:
                duration = exercise["duration_min"]
                sheet_inputs = {
                    'workout': {
                        "date": currentdate,
                        "time": currenttime,
                        "exercise": exercise["name"].title(),
                        "duration": f"{duration} minutes",
                        "calories": exercise["nf_calories"]
                    }
                }
                sheetwriter(sheet_inputs)
            except:
                continue
    except:
        print("Please check env variables.")

