import requests as requests
from bs4 import BeautifulSoup
import datetime as dt
from email_manager import EmailManager

date = dt.datetime.now().strftime('%Y-%m-%d')
time = dt.datetime.now().strftime('%H:%M:%S')

response = requests.get(f'https://flixpatrol.com/top10/netflix/poland/{str(date)}/').text
soup = BeautifulSoup(response, 'html.parser')

description_labels = [item.getText() for item in soup.find_all(name='h3', class_='table-th text-gray-400 text-center')]
movie_index = int(description_labels.index('TOP 10 Overall'))

titles = [item.getText() for item in soup.find_all(name='a', class_='hover:underline')]

position = 0
top_movies = []
print(titles)

for title in titles:
    position += 1
    if (movie_index*10)+1 <= position <= (movie_index*10)+10:
        top_movies.append(f'{position}. {title}')


movies_formatted = " \n".join(top_movies)

message = f'SUBJECT: Top 10 Netflix ({date})\n\n' \
          f'Top 10 filmów:\n' \
          f'{movies_formatted}\n\n' \

print(movies_formatted)

EmailManager.send_email(message, time)
