
# WEB SCRAPING PARA O BUSCAR AS PRINCIPAIS NOTÍCIAS NO SITE REVISTA APÓLICE

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# Request
r1 = requests.get('https://www.revistaapolice.com.br/revistas/')
r1.status_code
 
# We'll save in coverpage the cover page content
coverpage = r1.content

# Soup creation
soup1 = BeautifulSoup(coverpage, 'html.parser')

# News identification
coverpage_news = soup1.find_all('a', class_='p-url')

title = np.array([])
link = np.array([])
for i in range(23):
    title = np.append(title, coverpage_news[i].get_text())
    link = np.append(link, coverpage_news[i]['href'])



news_data = pd.DataFrame({'Title': title, 'Link': link})

news_data = news_data.drop([0,1,2,3,8,9,10,11,12,13,14,15,16])

news_data.index = [i for i in range(len(news_data))]





abstract = np.array([])

for i in range(len(news_data['Link'])):
    # Request
    r1 = requests.get(news_data['Link'][i])
 
    # We'll save in coverpage the cover page content
    coverpage = r1.content

    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html.parser')

    # News identification
    coverpage_news_abs = soup1.find_all('h6', class_='h4')
    
    
    abstract = np.append(abstract, coverpage_news_abs[2].get_text())

news_data['Abstract'] = abstract

news_data.to_excel('principais_noticias.xlsx')