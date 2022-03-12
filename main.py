from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
name = soup.findAll(name="a", class_="titlelink")


article_texts = []
article_links = []
for all_articles in name:
    article_text = all_articles.get_text()
    article_texts.append(article_text)
    article_link = all_articles.get("href")
    article_links.append(article_link)

article_point = [int(score.get_text().split()[0])for score in soup.findAll(name="span", class_="score")]

max_point = max(article_point)
max_index = article_point.index(max_point)

print(article_texts[max_index])
print(article_links[max_index])

