# Workout Tracker
This uses the nutrionix GPT-3 API to take string input (IE, "I ran 3 miles today"), then uses the Sheety API to write this information into a google spreadsheet to track work outs. 

It expects an API key for both APIs, via environmental variables. It will look for sheetytoken and sheetyendpoint.

It will look for nutrionixkey and nutrionixappid. It also assumes the name of your spreadsheet is "workouts".
