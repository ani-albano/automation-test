from selenium.webdriver.common.by import By
import random
import string


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def generateString(self, stringLength=301):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

    edit = (By.XPATH, '//*[@id="content"]/div[1]/div/ul/li[1]/div/div/div[1]/button[1]')
    text = (By.CSS_SELECTOR, 'textarea.form-control')
    confirm = (By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div[3]/button[2]')
    delete = (By.XPATH, '//*[@id="content"]/div[1]/div/ul/li[13]/div/div/div[1]/button[2]')
    modal = (By.CSS_SELECTOR, 'button.btn.btn-primary')

    def creation(self):
        self.driver.find_element_by_id("inputImage").send_keys("/code/example.jpg")
        self.driver.find_element_by_css_selector('textarea.form-control').send_keys("This is an example")
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/form/div[3]/button').click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.implicitly_wait(30)

    def edition(self):
        self.driver.execute_script("window.scroll(0, 0);")
        self.driver.find_element(*HomePage.edit).click()
        self.driver.find_element(*HomePage.text).send_keys("Edition")
        self.driver.find_element(*HomePage.confirm).click()
        self.driver.implicitly_wait(30)

    def count(self):
        letters = self.generateString()
        self.driver.find_element(*HomePage.text).send_keys(letters)
        self.driver.implicitly_wait(30)

    def deleting(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.implicitly_wait(30)
        self.driver.find_element(*HomePage.delete).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*HomePage.modal).click()
