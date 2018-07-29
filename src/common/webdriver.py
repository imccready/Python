from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Webdriver(object):
    def __init__(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        print("Opening page: {}.".format(url))
        #self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(2120, 550)
        self.driver.get(url)

    def get_page(self):
        content = self.driver.page_source
        return content

    def next_page(self, clickElement):
        #self.driver.find_element(By="class name", value=clickElement).click()
        self.driver.find_element_by_class_name(clickElement).click()
        print("URL: {}".format(self.driver.current_url))

    def finish(self):
        self.driver.quit()

