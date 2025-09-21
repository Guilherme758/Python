from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import utils
import time

class drive:
    def __init__(self):
        self.settings = utils.get_settings()
        self.driver = utils.start_driver()
        self.actions = ActionChains(self.driver)
        
        self.login()

    def login(self):
        self.driver.get(self.settings['Settings']['GDriveBaseURL'])

        # User
        email_locator = (By.CSS_SELECTOR, "#identifierId")
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(email_locator))

        email_element = self.driver.find_element(*email_locator)
        email_element.clear()

        self.actions.send_keys_to_element(email_element, self.settings['Settings']['GDriveUser']).perform()
        
        self.driver.find_element(By.CSS_SELECTOR, "#identifierNext").click()

        # Password
        password_locator = (By.CSS_SELECTOR, "#password input")

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(password_locator))

        password_element = self.driver.find_element(*password_locator)
        password_element.clear()

        self.actions.send_keys_to_element(password_element, self.settings['Settings']['GDrivePassword']).perform()

        self.driver.find_element(By.CSS_SELECTOR, "#passwordNext").click()
        
    def download_files(self):
        pass

drive()