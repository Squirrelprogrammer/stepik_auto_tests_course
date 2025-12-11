import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(str(y))
input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-check-input[type="checkBox"]')
input2.click()
input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-check-input[value="robots"]')
input3.click()

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()
