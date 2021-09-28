#!/usr/bin/env python3

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    
    browser.find_element_by_xpath("//button").click()
    browser.switch_to.alert.accept()
    
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    y = calc(x)
    
    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
