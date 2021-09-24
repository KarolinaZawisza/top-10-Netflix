import datetime
import smtplib
from selenium import webdriver

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

date = datetime.datetime.now().strftime('%Y-%m-%d')

driver.get(f'https://flixpatrol.com/top10/netflix/world/{date}/')

movies = driver.find_element_by_xpath('//*[@id="netflix-1"]/div[2]/div/div/table/tbody').text.split('\n')
shows = driver.find_element_by_xpath('//*[@id="netflix-2"]/div[2]/div/div/table/tbody').text.split('\n')
top_movies = []
top_shows = []

def get_title(inputs, outputs):
    for movie in inputs:
        if inputs.index(movie) % 3 == 1:
            outputs.append(movie)


get_title(movies, top_movies)
get_title(shows, top_shows)

sorted_movies = "\n".join([f'{top_movies.index(movie)+1}. {movie}' for movie in top_movies])
sorted_shows = "\n".join([f'{top_shows.index(movie)+1}. {movie}' for movie in top_shows])

message = f'SUBJECT: TOP 10 Netflix ({date})\n\n' \
          f'Top 10 filmów:\n' \
          f'{sorted_movies}\n\n' \
          f'Top 10 seriali:\n' \
          f'{sorted_shows}'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user='mail', password='password')
    connection.sendmail(from_addr='mail',
                        to_addrs='mail_to',
                        msg=message.encode('utf-8')
                        )

driver.quit()
