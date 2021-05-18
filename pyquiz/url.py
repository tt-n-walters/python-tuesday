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
        if self.category == "any" and self.difficulty == "any" and self.type == "any":
            generated_url = "{}amount={}".format(URL.host, self.number_of)

        elif self.category == "any" and self.difficulty == "any" and not self.type == "any":
            generated_url = "{}amount={}&type={}".format(
                URL.host, self.number_of, self.type)

        elif self.category == "any" and not self.difficulty == "any" and self.type == "any":
            generated_url = "{}amount={}&difficulty={}".format(
                URL.host, self.number_of, self.difficulty)

        elif not self.category == "any" and self.difficulty == "any" and self.type == "any":
            generated_url = "{}amount={}&category={}".format(
                URL.host, self.number_of, self.category)

        elif self.category == "any" and not self.difficulty == "any" and not self.type == "any":
            generated_url = "{}amount={}&difficulty={}&type={}".format(
                URL.host, self.number_of, self.difficulty, self.type)

        elif not self.category == "any" and not self.difficulty == "any" and self.type == "any":
            generated_url = "{}amount={}&category={}&difficulty={}".format(
                URL.host, self.number_of, self.category, self.difficulty)

        elif not self.category == "any" and self.difficulty == "any" and not self.type == "any":
            generated_url = "{}amount={}&category={}&type={}".format(
                URL.host, self.number_of, self.category, self.type)

        elif not self.category == "any" and not self.difficulty == "any" and not self.type == "any":
            generated_url = "{}amount={}&category={}&difficulty={}&type={}".format(
                URL.host, self.number_of, self.category, self.difficulty, self.type)

        return generated_url


if __name__ == "__main__":
    new_url = URL()
    new_url.choose_difficulty()
    new_url.choose_category()
    new_url.choose_type()
    new_url.choose_number_of_questions()

    print(new_url.generate())
