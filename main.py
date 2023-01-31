import os.path
import time

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'}

page = 1
while True:
    res = requests.get(f'https://unsplash.com/napi/topics/architecture/photos?page={page}&per_page=10', headers=headers)
    res = res.json()

    for i in res:
        link = i['urls']['full']
        name = i['id']

        folder = os.path.join(os.getcwd(), 'photos')
        if not(os.path.isdir(folder)):
            os.makedirs(folder)

        with open(f'{folder}/{name}.jpg' , 'wb') as f:
            res = requests.get(link, headers=headers, stream=True)
            for byte in res:
                f.write(byte)

        time.sleep(1)

    time.sleep(2)