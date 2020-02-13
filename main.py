import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.mayflowerbrewing.com/")
time.sleep(4)

element = driver.find_element_by_xpath("//*[@id=\"menu-item-1005\"]/a")
hover = ActionChains(driver).move_to_element(element)
hover.perform()
time.sleep(5)

element2 = driver.find_element_by_xpath("//*[@id=\"menu-item-4598\"]/a")
element2.click()
time.sleep(3)


