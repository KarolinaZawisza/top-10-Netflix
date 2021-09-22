import requests as requests
from bs4 import BeautifulSoup
import datetime as dt
from email_manager import EmailManager

# date = dt.datetime.now().strftime('%Y-%m-%d')
time = dt.datetime.now().strftime('%H:%M:%S')
date = '2021-09-22'
response = requests.get(f'https://flixpatrol.com/top10/netflix/poland/{str(date)}/').text
soup = BeautifulSoup(response, 'html.parser')

titles = [item.getText() for item in soup.find_all(name='a', class_='hover:underline')]

position = 0
top_movies = []
top_shows = []

for title in titles:
    position += 1
    if 11 <= position < 21:
        top_movies.append(f'{position-10}. {title}')
    elif 21 <= position < 31:
        top_shows.append(f'{position-20}. {title}')

movies_formatted = " \n".join(top_movies)
shows_formatted = " \n".join(top_shows)

message = f'SUBJECT: Top 10 Netflix ({date})\n\n' \
          f'Top 10 filmów:\n' \
          f'{movies_formatted}\n\n' \
          f'Top 10 seriali: \n' \
          f'{shows_formatted}'

EmailManager.send_email(message, time)