

class URL:
    def __init__(self):
        print("Initialising new URL.")
    
    def choose_number_of_questions(self):
        print("Enter number of questions:")
        self.number_of = input(">> ")

    def choose_category(self):
        print("Enter category:")
        self.category = input(">> ")

    def choose_difficulty(self):
        print("Enter difficulty:  (any/easy/medium/hard)")
        self.difficulty = input(">> ")
        if self.difficulty in ["any", "easy", "medium", "hard"]:
            print
        else:
            print("Invalid difficulty.")

    def choose_type(self):
        print("Enter type of questions:  (any/multiple/boolean)")
        self.type = input(">> ")
    
    def generate(self):
        pass


new_url = URL()
new_url.choose_difficulty()

print("You chose a difficulty of:", new_url.difficulty)