from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success():
    # Wait for the login button to be visible within 10 seconds
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'login-button'))
    )
    # Perform login actions
    # ...