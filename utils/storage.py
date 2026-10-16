# Import tools for working with JSON data and file paths
import json
import os

#Find the location of our saved project data
DATA_FILE = os.path.join(
    
    os.path.dirname(os.path.dirname(__file__)), 
    "data", 
    "projects.json"

)

# Loads saved data or creates empty collections
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return
        { 
            "users": [], 
            "projects": [], 
            "tasks": []
        }

# Saves data to the JSON file
def save_data(data):

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)                 