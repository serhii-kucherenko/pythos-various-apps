import requests
from bs4 import BeautifulSoup


def scraping_stackoverflow_question():
    response = requests.get('https://stackoverflow.com/questions')
    soup = BeautifulSoup(response.text, 'html.parser')

    questions = soup.select('.s-post-summary')

    for i, question in enumerate(questions):
        print(f'{i + 1}.', question.select_one('.s-post-summary--content-title').getText().strip())
        print("Votes:", question.select_one('.s-post-summary--stats-item-number').getText().strip())
        print('\n')


scraping_stackoverflow_question()
