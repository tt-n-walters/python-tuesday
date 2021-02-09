import requests

# host_url = "https://jan21python.herokuapp.com/"
host_url = "http://127.0.0.1:5000/"


def download_messages():
    response = requests.get(host_url + "messages")
    print(response.text)


def send_message():
    final_url = host_url + "send"
    arguments = {
        "user": "nico",
        "message": input("Enter message: ")
    }
    response = requests.get(final_url, params=arguments)


while True:
    download_messages()
    send_message()
