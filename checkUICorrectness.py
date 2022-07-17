from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as Conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


url = "https://auth.interviewready.io/signin/"
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
wait = WebDriverWait(driver, timeout=60)


def checkLoginPageUI():
    driver. get(url)

    # Getting the email field
    wait.until(Conditions.element_to_be_clickable(
        (By.XPATH, '//*[@id="email"]')))
    email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')

    # Getting the Password field
    wait.until(Conditions.element_to_be_clickable(
        (By.XPATH, '//*[@id="password"]')))
    password = driver.find_element(by=By.XPATH, value="//*[@id='password']")

    submit = driver.find_element(
        by=By.XPATH, value="//*[@id='__layout']/div/div[1]/div[2]/div[2]/div/form/div[4]/div[1]/button")

    # Validating the attributes and values
    if(email.tag_name == "input" and
        email.get_attribute("type") == "email" and
            email.get_attribute("placeholder") != None):
        print("Email field is correctly coded as per requirement")
    else:
        print("Email field is not as per requirement")

    if(password.tag_name == "input" and
        password.get_attribute("type") == "password" and
            password.get_attribute("placeholder") != None):
        print("Password field is correctly coded as per requirement")
    else:
        print("Password field is not as per requirement")

    if((submit.tag_name == "input" and submit.get_attribute("type") == "button") or
            (submit.tag_name == "button" and
             (submit.get_attribute("innerText").lower() == "submit" or submit.get_attribute("value").lower() == "submit"))):
        print("Submit Button is coded as per requirement")
    else:
        print("Submit Button is not coded as per requirement")


checkLoginPageUI()
