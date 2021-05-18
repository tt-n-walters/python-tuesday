from url import URL

url_generator = URL()
url_generator.choose_category()
url_generator.choose_type()
url_generator.choose_difficulty()
url_generator.choose_number_of_questions()

api_url = url_generator.generate()
print(api_url)
