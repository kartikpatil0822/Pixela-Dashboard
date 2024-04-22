import requests
from datetime import datetime

PIXELA_URL = "https://pixe.la/"

# Creating new user
CREATE_USER_ENDPOINT = f"{PIXELA_URL}/v1/users"

user_params = {
    "token": "thistokenisalreadytakenbysomeone",
    "username": input("Please enter your username: "),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

resp = requests.post(url=CREATE_USER_ENDPOINT, json=user_params)
print(resp.text)

# output of above response: 
# Please enter your username: kartikpatil
# {"message":"Success. Let's visit https://pixe.la/@kartikpatil , it is your profile page!","isSuccess":true}

USERNAME = "kartikpatil"
TOKEN = "thistokenisalreadytakenbysomeone"

# Updated User Parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Adding new graph for newly added user

ADD_GRAPH_ENDPOINT = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": "activity",
    "name": "learning",
    "unit": "hours",
    "type": "int",
    "color": "ajisai",
}

resp = requests.post(url=ADD_GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(resp.text) # {"message":"Success.","isSuccess":true}

# To view newly created graph

GRAPH_ID = "activity"

VIEW_GRAPH_ENDPOINT = f"{PIXELA_URL}v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"

# Add pixel to our newly added graph

PIXEL_CREATION_ENDPOINT = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    # "date": "20240329",
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "8",
}

resp = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
print(resp.text) # {"message":"Success.","isSuccess":true}

# Updating existing pixel data

PIXEL_DAY = "20240328"

UPDATE_PIXEL_DATA_ENDPOINT = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{PIXEL_DAY}"

new_pixel_data = {
    "quantity": "11",
}

resp = requests.put(url=UPDATE_PIXEL_DATA_ENDPOINT, json=new_pixel_data, headers=headers)
print(resp.text) # {"message":"Success.","isSuccess":true}

# Deleting existing pixel data

PIXEL_DAY = "20240323"

DELETE_PIXEL_ENDPOINT = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{PIXEL_DAY}"

resp = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(resp.text) # {"message":"Success.","isSuccess":true}