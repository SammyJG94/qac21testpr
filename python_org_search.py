from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get("http://www.schoology.com")
assert "Google" in driver.title
elem = driver.find_element_by_id("login-header")
elem.click()
elem.send_keys("Disneyland")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source


