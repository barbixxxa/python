from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')

emailElem = browser.find_element_by_id('email')
emailElem.send_keys('not_my_real_email')

passwordElem = browser.find_element_by_name('pass')
passwordElem.send_keys('12345')
passwordElem.submit()
