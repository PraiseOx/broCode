import csv

from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

quotes = soup.findAll('span', attrs={'class':'text'})

authors = soup.findAll('small', attrs={'class':'author'})

"""for quote in quotes:
    print(quote.text)

for author in authors:
    print(author.text)"""

"""with open('scraped_quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["S/N", "QUOTES", "AUTHORS"])
    for i, (quote, author) in enumerate(zip(quotes, authors), start=1):
        print(f"{quote.text} - {author.text}")
        writer.writerow([i, quote.text, author.text])

print("Quotes saved to scraped_quotes.csv.")"""

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])
for quote, author in zip(quotes, authors):
     print(quote.text + "_" + author.text)
     writer.writerow([quote.text, author.text])
file.close

#Youtube tutorial Github link - https://github.com/gigafide/basic_python_scraping/