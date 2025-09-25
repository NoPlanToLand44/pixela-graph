from create_user import user_params , USERNAME , TOKEN
import requests


pixela_endpoint = "https://pixe.la/v1/users"

try:
    response = requests.post(url = pixela_endpoint, json= user_params)
    response_dict = response.json()
    response.raise_for_status()
    
except requests.exceptions.HTTPError as e:
    if response.status_code == 409 :
        print("user already exists")
    else: 
        print(f"other http error : {e}")
        
profile_endpoint = f"https://pixe.la/@{USERNAME}"
profile_params = {
    "displayName": 'Emil slacker tracker' ,
    "timezone": "Europe/Sofia",
    "aboutURL" : "https://github.com/NoPlanToLand44/pixela-graph"
}
headers = {'X-USER-TOKEN': TOKEN}

put_response = requests.put(url=profile_endpoint, headers = headers, json = profile_params)
print(put_response.text)
