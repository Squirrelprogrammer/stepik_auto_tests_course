import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, 'button')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, 'input_value').text
y = str(calc(int(x)))

input = browser.find_element(By.ID, 'answer')
input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ждем загрузки страницы
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()
