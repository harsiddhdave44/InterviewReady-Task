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


def CheckVideoVisibility():
    driver.get("https://get.interviewready.io/course-preview/")

    # Waiting for the 'Course Preview' link to be visible, and clicking on it
    wait.until(Conditions.element_to_be_clickable(
        (By.XPATH, "//*[@id='__layout']/div/header/div/div/div[2]/a[2]")))
    driver.find_element(
        by=By.XPATH, value="//*[@id='__layout']/div/header/div/div/div[2]/a[2]").click()

    # Scrolling to the next page and fetching the vimeo player iframe
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(5)
    vimeo_player = driver.find_element(
        by=By.XPATH, value="//*[@id='vimeo-player-1']/iframe")

    # Getting the video player dimensions to check if they're right
    player_width = vimeo_player.get_attribute("width")
    player_height = vimeo_player.get_attribute("height")

    # The dimensions are kept static as they don't change at window resize
    if(vimeo_player != None and player_width == '640' and player_height == '320'):
        print("Element visible and has right dimensions")
    else:
        print("Element does not have right dimensions or is not visible")


CheckVideoVisibility()
