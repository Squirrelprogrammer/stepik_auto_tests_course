import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '100')
)

book_button = WebDriverWait(browser, 12).until(
    EC.element_to_be_clickable((By.ID, "book"))
)

book_button.click()

x = browser.find_element(By.ID, 'input_value').text
y = str(calc(int(x)))

answer_input = browser.find_element(By.ID, 'answer')
answer_input.send_keys(y)
submit_button = browser.find_element(By.ID, "solve")
submit_button.click()

# Немного ждем для просмотра результата
time.sleep(10)

# Закрываем браузер
browser.quit()
