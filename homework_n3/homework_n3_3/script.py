import requests
from bs4 import BeautifulSoup

# URL веб-сайта
url = "https://example.com"

# Получение данных с веб-сайта
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML-кода с использованием BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Пример: вывод заголовков всех статей на странице
    articles = soup.find_all('h2')
    for article in articles:
        print(article.text)
else:
    print(f"Ошибка при запросе: {response.status_code}")