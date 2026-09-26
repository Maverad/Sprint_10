from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import config


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, config.Timeouts.base_timeout).until(EC.visibility_of_element_located((locator)))

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
    
    def check_visibility(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def move_to_element(self, locator):
        element = self.driver.find_element(*locator)
        AC(self.driver).move_to_element(element).perform()

    def disable_animations(self):
        self.driver.execute_script("""
        const s = document.createElement('style');
        s.setAttribute('data-selenium', 'no-anim');
        s.innerHTML = `
            *, *::before, *::after {
                transition: none !important;
                transition-duration: 0s !important;
                transition-delay: 0s !important;
                animation: none !important;
                animation-duration: 0s !important;
                animation-delay: 0s !important;
            }`;document.head.appendChild(s);""")

    def wait_for_text_to_appear(self, locator, expected_text):
        WebDriverWait(self.driver, config.Timeouts.base_timeout).until(lambda d: d.find_element(*locator).text == expected_text)
        return self.driver.find_element(*locator).text