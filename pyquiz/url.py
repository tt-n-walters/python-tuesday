from category import Category


class URL:
    host = "https://opentdb.com/api.php?"

    def __init__(self):  # initialise
        print("Initialising new URL.")

    def choose_number_of_questions(self):
        """
        Gets user input of a number of questions for the URL.
        Number of questions must be a positive integer.
        """
        print("Enter number of questions:")
        self.number_of = input(">> ")
        if self.number_of.isdigit():
            self.number_of = int(self.number_of)
            if self.number_of > 0:
                print("Number of questions saved.")
            else:
                print("At least 1 question required.")
                exit()
        else:
            print("Invalid input.")
            exit()

    def choose_category(self):
        """
        Gets user input of a category.
        """
        category = Category()
        category.display_categories()
        self.category = category.get_user_choice()
        print("Category saved.")

    def choose_difficulty(self):
        """
        Gets user input for the difficulty.
        Difficulty must be "any", "easy", "medium", or "hard".
        """
        print("Enter difficulty:  (any/easy/medium/hard)")
        self.difficulty = input(">> ")
        if self.difficulty in ["any", "easy", "medium", "hard"]:
            print("Difficulty saved.")
        else:
            print("Invalid difficulty.")
            exit()

    def choose_type(self):
        """
        Gets user input for the question type.
        Type must be "any", "multiple", or "boolean".
        """
        print("Enter type of questions:  (any/multiple/boolean)")
        self.type = input(">> ")
        if self.type in ["any", "multiple", "boolean"]:
            print("Type saved.")
        else:
            print("Invalid type.")
            exit()

    def generate(self):
        """
        Uses all the user chosen URL options and generates the final API URL.
        """
        arguments = []
        arguments.append("amount={}".format(self.number_of))

        if not self.category == "any":
            category_arg = "category={}".format(self.category)
            arguments.append(category_arg)

        if not self.difficulty == "any":
            difficulty_arg = "difficulty={}".format(self.difficulty)
            arguments.append(difficulty_arg)
            
        if not self.type == "any":
            type_arg = "type={}".format(self.type)
            arguments.append(type_arg)
        
        argument_string = "&".join(arguments)
        return URL.host + argument_string


if __name__ == "__main__":
    new_url = URL()
    new_url.choose_difficulty()
    new_url.choose_category()
    new_url.choose_type()
    new_url.choose_number_of_questions()

    print(new_url.generate())
