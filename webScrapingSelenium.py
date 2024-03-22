from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
URL = "https://onepa.gov.sg/cc"
# Load the HTML content
driver.get(URL)
time.sleep(5)
# Parse the HTML with BeautifulSoup
outF = open("output.txt", 'w')



# Iterate through each div element
for i in range(12):
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    div_elements = driver.find_elements(By.XPATH, '//div[@class="CCLocatorItem"]')
    for div_element in div_elements:
        # Use XPath to extract the title attribute from the anchor tag within the div
        title = div_element.find_element(By.XPATH, './/a').get_attribute('title')
        address = div_element.find_element(By.XPATH, './/p[@class="CCLocatorItem__inner__details--label"]').text
        
        # outF.write(address.split(",")[-1] + ",")
        outF.write(title + ",")
        outF.write(address.split(",")[-1] + "\n") # to obtain only the postal code
        # outF.write("\n")
        print("Title:", title)
        #print("Address:", address)
        print("Postal Code:", address.split(",")[-1])
        print()
    button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="btnNext"]')))

    # Scroll into view
    actions = ActionChains(driver)
    actions.move_to_element(button_element).perform()

    # Click the button using JavaScript
    driver.execute_script("arguments[0].click();", button_element)
    time.sleep(2)


# Close the WebDriver instance
input("Press enter to close the program: ")
outF.close()
driver.quit()
