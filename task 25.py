from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

# Setup WebDriver path and options
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDb Advanced Name Search page
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 10)
driver.execute_script("window.scrollTo(500, 500);")
time.sleep(20)
# Open the filmography section
credits = driver.find_element(By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label').click()
time.sleep(2)

# Find the credit input element
credit = driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

# Use ActionChains to input text and select the first suggestion
actions = ActionChains(driver)
actions.send_keys_to_element(credit, "Holiday")
actions.pause(2)  # Wait for suggestions to appear
actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
actions.pause(1)  # Pause briefly to ensure the selection
actions.send_keys(Keys.ENTER)  # Press the Enter key to select
actions.perform()

# Confirmation
print("Search performed successfully.")
