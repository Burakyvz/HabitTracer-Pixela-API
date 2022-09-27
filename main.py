import requests
import datetime as dt
import os

## --- POST REQUEST --- #

USER_NAME = os.environ.get("USER_NAME")
TOKEN = os.environ.get("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Minute",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

## --- POSTING PIXELS --- #

post_pixel_endpoint = f"{graph_endpoint}/graph1"

today = dt.datetime.now()

quantity = input("How many minutes did you read? ")

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity,
}


response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)

## --- UPDATING PIXELS --- #


update_endpoint = f"{post_pixel_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "47"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)


## --- DELETING PIXELS --- #

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)