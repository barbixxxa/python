# check https://github.com/theeam/ubuntu-setup/blob/master/seleniumDrivers.sh for installation of drivers

from selenium import webdriver

# firefox
driver = webdriver.Firefox()
driver.get("https://www.mozilla.org")

# chrome
#chromedriver = "/usr/bin/chromedriver"
#driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome()
driver.get("http:google.com")
