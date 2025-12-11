import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element(By.ID, "num1").text)
y = int(browser.find_element(By.ID, "num2").text)
res_sum = x + y

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(res_sum))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ждем загрузки страницы
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()
