from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
web = 'https://www.thesun.co.uk/sport/football/'

driver.get(web)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()
