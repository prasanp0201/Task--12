from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, 'username')
        self.password_input = (By.NAME, 'password')
        self.login_button = (By.XPATH, '//button[@type="submit"]')

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

    def is_login_successful(self):
        # Wait for an element that appears only when login is successful
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'menu_dashboard_index')))
            return True
        except:
            return False
