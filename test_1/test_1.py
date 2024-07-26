import requests
import json


def send_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("result.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    send_request('https://jsonplaceholder.typicode.com/posts')
