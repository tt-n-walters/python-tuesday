import requests
import json


class Category:
    def __init__(self):
        response = requests.get("https://opentdb.com/api_category.php")
        if not response.status_code == 200:
            print("Category download failed.")
            exit()
        else:
            data = json.loads(response.text)
            categories = data["trivia_categories"]
            
            for i in range(len(categories)):
                category = categories[i]
                category_name = category["name"]
                print(category_name)


Category()
