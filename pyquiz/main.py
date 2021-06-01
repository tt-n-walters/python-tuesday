from url import URL
from quiz import Quiz

url_generator = URL()
url_generator.choose_category()
url_generator.choose_type()
url_generator.choose_difficulty()
url_generator.choose_number_of_questions()
# url_generator.number_of = 5
# url_generator.category = "any"
# url_generator.difficulty = "any"
# url_generator.type = "any"

api_url = url_generator.generate()


quiz = Quiz(api_url)
quiz.ask_question()
quiz.get_user_answer()