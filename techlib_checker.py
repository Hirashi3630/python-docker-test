import requests
from bs4 import BeautifulSoup
import csv
import datetime

if __name__ == '__main__':
    url = 'https://www.techlib.cz/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element containing the number of persons in the library
    population = int(soup.select('.text-center span')[0].text)

    # Write the number of persons to a CSV file
    with open('persons.csv', 'a', newline='') as csvfile:
        fieldnames = ['date', 'persons']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'date': datetime.datetime.now(), 'persons': population})

    print("Scraped and added to CSV file")

