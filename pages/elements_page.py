from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        self.center_text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        super().__init__(driver, self.base_url)

