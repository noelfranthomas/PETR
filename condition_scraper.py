from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from os import makedirs
from os.path import join, isdir

def condition_scraper(url):
    driver = webdriver.Chrome()
    driver.get(url)

    if not isdir("data"):
            makedirs("data")

    condition_url_param = driver.current_url.split("/")[-2]
    condition_type_url_param = driver.current_url.split("/")[-3]

    ccc = driver.find_element(By.ID, "ccc-notify-dismiss")
    ccc.click()

    try:
        guide_navigation_container = driver.find_element(By.ID, "guide-navigation")

        links = guide_navigation_container.find_elements(By.TAG_NAME, "a")

        elems = []
        p_index = 0

        for link in links:
            link.click()

            active_container = driver.find_element(By.CSS_SELECTOR, "div.active")
            editors = active_container.find_elements(By.CLASS_NAME, "editor")

            for editor in editors:
                all_elems = editor.find_elements(By.CSS_SELECTOR, "*")

                for elem in all_elems:
                    if elem.tag_name == "h2":
                        elems.append(elem.text)
                        p_index = len(elems)
                    elif elem.tag_name == "p":
                        try:
                            elems[p_index] += (" " + elem.text)
                        except IndexError:
                            elems.append(elem.text)
                    elif elem.tag_name == "a":
                        try:
                            elems[p_index] += (" [" + elem.text + "]")
                        except IndexError:
                            elems.append(elem.text)

    except NoSuchElementException:
        try:
            active_container = driver.find_element(By.CSS_SELECTOR, "div.tab")
            editors = active_container.find_elements(By.CLASS_NAME, "editor")

            elems = []
            p_index = 0

            for editor in editors:
                all_elems = editor.find_elements(By.CSS_SELECTOR, "*")

                for elem in all_elems:
                    if elem.tag_name == "h2":
                        elems.append(elem.text)
                        p_index = len(elems)
                    elif elem.tag_name == "p":
                        try:
                            elems[p_index] += (" " + elem.text)
                        except IndexError:
                            elems.append(elem.text)
                    elif elem.tag_name == "a":
                        try:
                            elems[p_index] += (" [" + elem.text + "]")
                        except IndexError:
                            elems.append(elem.text)
        except:
            # active_container = driver.find_element(By.CSS_SELECTOR, "div.tab")
            editors = driver.find_elements(By.CLASS_NAME, "editor")

            elems = []
            p_index = 0

            for editor in editors:
                all_elems = editor.find_elements(By.CSS_SELECTOR, "*")

                for elem in all_elems:
                    if elem.tag_name == "h2":
                        elems.append(elem.text)
                        p_index = len(elems)
                    elif elem.tag_name == "p":
                        try:
                            elems[p_index] += (" " + elem.text)
                        except IndexError:
                            elems.append(elem.text)
                    elif elem.tag_name == "a":
                        try:
                            elems[p_index] += (" [" + elem.text + "]")
                        except IndexError:
                            elems.append(elem.text)
    
    f_name = join("data", condition_type_url_param, condition_url_param + ".md")

    if not isdir(join("data", condition_type_url_param)):
        makedirs(join("data", condition_type_url_param))

    with open(f_name, 'a') as f:
        for e in elems:
            f.write(e)
            f.write("\n")
    driver.close()

if __name__ == "__main__":
    URL = "https://www.nhsinform.scot/illnesses-and-conditions/stomach-liver-and-gastrointestinal-tract/acute-cholecystitis/"
    URL = "https://www.nhsinform.scot/illnesses-and-conditions/mental-health/anxiety/"
    URL = "https://www.nhsinform.scot/illnesses-and-conditions/sexual-and-reproductive/bacterial-vaginosis/"
    condition_scraper(URL)