import requests
import json
import random

from pprint import pprint

class Quiz:
    # initialises the class
    def __init__(self, questions_url):
        print("Starting the quiz. With url:")
        print(questions_url)
        response = requests.get(questions_url)
        if response.status_code != 200:
            exit("Question download failed.", response.status_code)
        
        self.data = json.loads(response.text)
        # pprint(self.data)

        self.questions = self.data["results"]


    def ask_question(self):
        question = self.questions.pop(0)
        self.answers = question["incorrect_answers"]
        self.correct_answer = question["correct_answer"]
        self.answers.insert(random.randrange(0, len(self.answers)), question["correct_answer"])
        print(question["question"])
        for i in range(len(self.answers)):
            answer = self.answers[i]
            label = i + 1
            print("{}) {}".format(label, answer))
    

    def get_user_answer(self):
        print("Enter answer:")
        answer = input("> ")
        if answer.isdigit():
            answer = int(answer)
            if answer > 0 and answer <= len(self.answers):
                
                # actually check the answer
                user_answer = self.answers[answer - 1]
                if user_answer == self.correct_answer:
                    print("Well done. Correct answer.")
                else:
                    print("Sorry, that was wrong. The correct answer was:")
                    print(self.correct_answer)
            else:
                print("Invalid answer.")
        else:
            print("Must choose a number.")
