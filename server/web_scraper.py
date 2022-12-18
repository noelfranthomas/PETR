from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 20)

URL = "https://www.nhsinform.scot/illnesses-and-conditions/heart-and-blood-vessels/conditions/abdominal-aortic-aneurysm/"

driver.get(URL)

guide_navigation_container = driver.find_element(By.ID, "guide-navigation")