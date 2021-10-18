from selenium import webdriver # importing required package of webdriver
import sys

# Just Run this to execute the below script
if __name__ == '__main__':
   # Instantiate the webdriver with the executable location of MS Edge web driver
    browser = webdriver.Edge(r"./msedgedriver.exe")

    url = 'https://www.lambdatest.com'
    browser.get(url)