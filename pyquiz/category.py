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

    

    def display_categories(self):
        """
        Prints all category names with an accompanying label
            '
            1)  General Knowledge
            2)  ...
            '
        """
        for i in range(len(self.names)):
            label = i + 1
            name = self.names[i]
            formatted = "{})  {}".format(label, name)
            print(formatted)

    
    def get_user_choice(self):
        """
        Allows user input of the desired category.
        Checks for valid selection.
        Returns the id of the chosen category.
        """
        print("Enter desired category number:")
        category_number = input(">> ")
        if category_number.isdigit():
            category_number = int(category_number)
            if category_number > 0 and category_number < len(self.names):
                # Calculate the id by offsetting the number entered
                category_id = category_number + 8
                return category_id
            
            else:
                print("Number must be between 1 and 24.")
                exit()
        else:
            print("Invalid input.")
            exit()


if __name__ == "__main__":
    print("Running category test.")
    test_category = Category()
    test_category.display_categories()
    print(test_category.get_user_choice())
