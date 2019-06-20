from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://inventwithpython.com")

#linkElem = driver.find_element_by_link_text('More Info')

linkElem = driver.find_element_by_link_text('YouTube')
print(type(linkElem))
linkElem.click()  # follows the "YouTube" link
