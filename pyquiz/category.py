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
            self.names = []
            self.ids = []

            for i in range(len(categories)):
                category = categories[i]
                category_name = category["name"]
                category_id = category["id"]
                self.names.append(category_name)
                self.ids.append(category_id)

            print(self.names)
            print(self.ids)
    

    def display_categories(self):
        """
        Prints all category names with an accompanying label
            '
            1)  General Knowledge
            2)  ...
            '
        """
        pass

Category()
