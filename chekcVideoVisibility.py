import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as Conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


url = "https://get.interviewready.io/"
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
wait = WebDriverWait(driver, timeout=60)


def login():
    driver.get(url)
    # Sign Up Button
    driver.find_element(
        by=By.XPATH, value="//*[@id='__layout']/div/header/div/div/div[2]/span[2]").click()

    # Email Input
    wait.until(Conditions.element_to_be_clickable(
        (By.XPATH, '//*[@id="email"]')))
    email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')

    # Password Input
    wait.until(Conditions.element_to_be_clickable(
        (By.XPATH, '//*[@id="password"]')))
    password = driver.find_element(by=By.XPATH, value="//*[@id='password']")

    # Submit Button
    submit = driver.find_element(
        by=By.XPATH, value="//*[@id='__layout']/div/div[1]/div[2]/div[2]/div/form/div[4]/div[1]/button")

    # Sending the credentials, keeping it static for the sake of simplicity
    email.send_keys("dave.harsiddh.44@gmail.com")
    password.send_keys("harsiddhdave44")
    submit.click()
    time.sleep(10)


def CheckVideoVisibility():
    # Waiting for the 'Course Preview' link to be visible, and clicking on it
    wait.until(Conditions.element_to_be_clickable(
        (By.XPATH, "//*[@id='__layout']/div/header/div/div/div[2]/a[2]")))
    driver.find_element(
        by=By.XPATH, value="//*[@id='__layout']/div/header/div/div/div[2]/a[2]").click()

    # Scrolling to the next page and fetching the vimeo player iframe
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    wait.until(Conditions.element_to_be_clickable(
        (By.XPATH, "//*[@id='vimeo-player-2']/iframe")))
    vimeo_player = driver.find_element(
        by=By.XPATH, value="//*[@id='vimeo-player-2']/iframe")

    # Getting the video player dimensions to check if they're right
    player_width = vimeo_player.get_attribute("width")
    player_height = vimeo_player.get_attribute("height")

    # The dimensions are kept static as they don't change at window resize
    if(vimeo_player != None and player_width == '640' and player_height == '320'):
        print("Element visible and has right dimensions")
    else:
        print("Element does not have right dimensions or is not visible")


# Function calls
login()
CheckVideoVisibility()
