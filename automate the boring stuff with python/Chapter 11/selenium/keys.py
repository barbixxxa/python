from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com/')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
htmlElem = browser.find_element_by_link_text('Amazon')
htmlElem.send_keys(Keys.HOME)    # scrolls to top

browser.get('https://facebook.com')

browser.back()

browser.forward()

htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom

browser.refresh()

browser.quit()
