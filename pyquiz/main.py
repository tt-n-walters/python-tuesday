

class URL:
    def __init__(self):
        print("Initialising new URL.")
    
    def choose_number_of_questions(self):
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
        print("Enter category:")
        self.category = input(">> ")

    def choose_difficulty(self):
        print("Enter difficulty:  (any/easy/medium/hard)")
        self.difficulty = input(">> ")
        if self.difficulty in ["any", "easy", "medium", "hard"]:
            print("Difficulty saved.")
        else:
            print("Invalid difficulty.")
            exit()

    def choose_type(self):
        print("Enter type of questions:  (any/multiple/boolean)")
        self.type = input(">> ")
        if self.type in ["any", "multiple", "boolean"]:
            print("Type saved.")
        else:
            print("Invalid type.")
            exit()
    
    def generate(self):
        generated_url = "https://opentdb.com/api.php"


new_url = URL()
new_url.choose_difficulty()

print("You chose a difficulty of:", new_url.difficulty)