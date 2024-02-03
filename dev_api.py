import requests

zelf_url = 'https://hackapi.hellozelf.com/backend/api/v1/contents?page='


for i in range(1, 5):
    response = requests.post(f'{zelf_url}{i}')
    res_data_2 = response.json()
    data_to_post = res_data_2['data'][0]['author'])




