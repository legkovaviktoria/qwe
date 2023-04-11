from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element(By.CSS_SELECTOR,"#answer")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    element.send_keys(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.form-check.form-check-custom > label")
    input1.click()
    input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.form-check.form-radio-custom > label")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    input3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла