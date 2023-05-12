from selenium import webdriver


class WebDriver(webdriver.Chrome):
    def __init__(self):
        super().__init__()
        self.implicitly_wait(5)
        self.set_page_load_timeout(30)
        self.maximize_window()
