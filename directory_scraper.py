from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from condition_scraper import condition_scraper

def directory_scraper(url="https://www.nhsinform.scot/illnesses-and-conditions/a-to-z#A"):
    driver = webdriver.Chrome()
    driver.get(url)
    ccc = driver.find_element(By.ID, "ccc-notify-dismiss")
    ccc.click()

    main = driver.find_element(By.ID, "maincontent")
    wrapper = driver.find_element(By.CLASS_NAME, "panel-content-wrap").find_element(By.CLASS_NAME, "wrapper")
    row = wrapper.find_element(By.CLASS_NAME, "row")
    items = row.find_elements(By.CSS_SELECTOR, "div.col")

    for item in items:
        if item.get_attribute("id") == "":
            ul = item.find_element(By.TAG_NAME, "ul")

            for li in ul.find_elements(By.TAG_NAME, "li"):
                a = li.find_element(By.TAG_NAME, "a")
                print(a.get_attribute("href"))
                try:
                    condition_scraper(a.get_attribute("href"))
                except NoSuchElementException:
                    with open("log.txt", 'w') as f:
                        f.write("Failed to scrape: " + a.get_attribute("href"))

if __name__ == "__main__":
    directory_scraper()