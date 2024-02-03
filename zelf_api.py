import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse


API_key = '4b45191bsk_e19ask_47edsk_95d7sk_5fac05cd47b61706932713'


# 1. Create the header
header = {
    "x-api-key": API_key
}

url1 = 'https://hackapi.hellozelf.com/backend/api/v1/contents?page=2'
url2 = 'https://hackapi.hellozelf.com/backend/api/v1/authors/919301'
base_url = 'https://hackapi.hellozelf.com/backend/api/v1/contents?page='
# number = 2
# new_url = f'{base_url}{number}{number}'
# print(new_url)

# 2. Make the url request
response = requests.get(url='https://hackapi.hellozelf.com/backend/api/v1/contents?page=2', headers=header)
print(response.status_code)

# 3. Get the data
# print(response.text)
data = response.json()

# 4. Get the data for different pages
for i in range(1, 10):
    response = requests.get(url=f'https://hackapi.hellozelf.com/backend/api/v1/contents?page={i}', headers=header)
    # print(response.status_code)
    res_data = response.json()
    print(res_data['data'][0]['author'])

response2 = requests.post('http://127.0.0.1:8000/ddjangos/')










# 4. Create the FastAPI app
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     response = requests.get(url=url1, headers=header)
#     return response.json()


# 5. Create another url that takes the page no and pulls the data
# @app.get("/{num}")
# async def get_users(num):
#     response = requests.get(url=f'{base_url}{num}', headers=header)
#     res_data = response.json()
#     for items in res_data["data"]:
#         author_details = items["author"]
#         return author_details

# python -m uvicorn FApi:app -–reload
# python -m uvicorn main:app -–reload


