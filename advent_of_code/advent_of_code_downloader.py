import requests


def download_inputs(day_number):
    url = "https://adventofcode.com/2020/day/1/input"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Error downloading.", response.status_code, response.text)
        exit()


download_inputs(1)
