from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://hidemy.name/ru/proxy-list/?start=128#list')

proxies = []

a = driver.find_element(By.TAG_NAME, 'table')
b = a.find_elements(By.TAG_NAME, 'tr')
for i in b:
    c = i.find_elements(By.TAG_NAME, 'td')
    proxies.append([c[0].text + ':' + c[1].text, c[4].text])
with open('text.txt', 'w') as file:
    for i in proxies:
        file.write(', '.join(i) + '\n')
