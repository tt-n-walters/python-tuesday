import requests


# url = "https://httpbin.org/post"
# post_data = {
#     "username": "tt-n-walters",
#     "password": "password123"
# }
# response = requests.post(url, data=post_data)

# print(response)
# print(response.text)


url = "https://www.google.co.uk/search"
get_arguments = {
    "q": "this is my test search"
}
response = requests.get(url, params=get_arguments)
print(response)
print(response.request.url)