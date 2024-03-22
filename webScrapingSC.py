from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
URL = "https://www.activesgcircle.gov.sg/facilities/swimming-pools"
# Load the HTML content
driver.get(URL)
time.sleep(5)
# Parse the HTML with BeautifulSoup
outF = open("outputSC.txt", 'w')

# Iterate through each div element
for i in range(12):
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    div_elements = driver.find_elements(By.XPATH, '//div[@class="cst-list-item"]')
    for div_element in div_elements:
        # Use XPath to extract the title attribute from the anchor tag within the div
        title = div_element.find_element(By.XPATH, './/div[@class="cst-cnt"]').text
        outF.write(title + ",")
        print("Title:", title)
        print()

    try:
        button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="next-posts-link post-nav  "]')))
    # <a class="next-posts-link post-nav  " href="https://www.activesgcircle.gov.sg/facilities/swimming-pools?page_num=3"><span class="page-text">Next</span></a>
        #<a class="previous-posts-link  " href="https://www.activesgcircle.gov.sg/facilities/swimming-pools?page_num=1" title="Next">Next</a>
        # Scroll into view
        actions = ActionChains(driver)
        actions.move_to_element(button_element).perform()

        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", button_element)
        time.sleep(2)
    except:
        break


# Close the WebDriver instance
input("Press enter to close the program: ")
outF.close()
driver.quit()
