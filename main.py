import requests
import selectorlib
import smtplib, ssl
import os
import time

"""
INSERT INTO events VALUES ('Tigers', 'Tigers City', '2028.12.14')
SELECT * FROM events WHERE date='2028.10.25'
"""

URL = "https://programmer100.pythonanywhere.com/tours"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    with open("data.txt", "a") as file:
        return file.write(extracted + "\n")


def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()



def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "soleariaeve@gmail.com"
    password = "xlmdfbjxgusnzvek"

    receiver = "soleariaeve@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="Hey, new event was found!")
        time.sleep(2)