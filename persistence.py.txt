# persistence.py  
import json, datetime  
state = {  
    "day": 1,  
    "last_concept": "Oscilador de Van der Pol",  
    "hardware": ["ESP32", "termopares"]  
}  
with open('state/state.json', 'w') as f:  
    json.dump(state, f)  