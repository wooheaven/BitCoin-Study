import requests
import json
import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import psycopg2


class UpBit:
    url_str = None
    response = None
    driver = None

    def __init__(self, url):
        self.url_str = url

    def set_url(self, url):
        self.url_str = url

    def request_data(self):
        for index in range(1, 10):
            wait = random.randrange(9) + 1
            time.sleep(wait)
            # print(str(index) + " step = " + str(wait) + " sec is waiting")
            self.response = requests.get(self.url_str)
            if self.response.ok:
                self.response = self.response.json()
                break

    def create_driver(self):
        # capabilities = webdriver.DesiredCapabilities().FIREFOX
        # capabilities["marionette"] = False
        # binary = FirefoxBinary(r'/usr/bin/firefox')
        # binary = FirefoxBinary(r'/Applications/Firefox.app/Contents/MacOS/firefox-bin')
        # self.driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)
        self.driver = webdriver.Firefox('/usr/local/bin/')
        self.driver.implicitly_wait(10)
        # self.driver.set_window_position(2000, 10)
        self.driver.set_window_size(1000, 1000)
        self.driver.get("https://upbit.com/exchange?code=CRIX.UPBIT.KRW-ETH")
        # time.sleep(8)

    def crawl_data(self):
        if self.driver is None:
            self.create_driver()
        elm = self.driver.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL + 't')
        self.driver.get(self.url_str)
        bs = BeautifulSoup(self.driver.page_source, "html.parser")
        # self.response = json.loads(str(bs.find(name="pre").contents[0]))
        self.response = json.loads(bs.find_all("div")[1].text)
        elm = self.driver.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL + 'w')

    def insert_data(self, conn):
        query = None
        try:
            cur = conn.cursor()
            query = ""
            query += "INSERT INTO crawl (url, response) " + "\n"
            query += "VALUES (%s, %s) "
            cur.execute(query, (self.url_str, json.dumps(self.response)))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(query)
            print(error)

    def quit_driver(self):
        self.driver.quit()

    def print(self):
        # print(self.url_str)
        print(json.dumps(self.response, indent=4))
        # print(json.dumps(self.response))


if __name__ == "__main__":
    url_str = "https://crix-api-endpoint.upbit.com/v1/crix/candles/" \
              "minutes/10?code=CRIX.UPBIT.KRW-ETH&count=3&to=2018-06-06%2010:00:00"
    upBit = UpBit(url_str)
    # upBit.requestData()
    conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='55432' password='123qwe'")

    upBit.crawl_data()
    upBit.insert_data(conn)
    upBit.quit_driver()
    upBit.print()

    conn.close()