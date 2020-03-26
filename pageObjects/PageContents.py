import random
import string
import re
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def generateString(self, stringLength=500):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

    image = (By.ID, 'inputImage')
    create = (By.XPATH, '//button[contains(text(),"Create Item")]')
    edit = (By.XPATH, '//button[contains(text(),"Edit")]')
    text = (By.CSS_SELECTOR, 'textarea.form-control')
    confirm = (By.XPATH, '//button[contains(text(),"Update Item")]')
    body = (By.CLASS_NAME, 'media-left')
    delete = (By.XPATH, '//button[contains(text(),"Delete")]')
    modal = (By.CSS_SELECTOR, 'modal-content')
    errase = (By.XPATH, '//*[@id="top"]/div[5]/div/div/div[3]/button[1]')
    disabled = (By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div[3]/button')
    area = (By.CSS_SELECTOR, 'textarea.ng-maxlength')

    # /code/example.jpg"
    def creation(self):
        self.driver.find_element(*HomePage.image).send_keys("C:\Files\example.jpg")
        self.driver.find_element(*HomePage.text).send_keys("This is an example")
        self.driver.find_element(*HomePage.create).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.implicitly_wait(30)

    def edition(self):
        self.driver.execute_script("window.scroll(0, 0);")
        self.driver.find_element(*HomePage.edit).click()
        self.driver.find_element(*HomePage.text).send_keys("Edition")
        self.driver.find_element(*HomePage.confirm).click()
        self.driver.implicitly_wait(30)

    def count(self):
        self.driver.find_element(*HomePage.image).send_keys("C:\Files\example.jpg")
        letters = self.generateString()
        self.driver.find_element(*HomePage.text).send_keys(letters)
        checkbutton = self.driver.find_element(*HomePage.disabled)
        if checkbutton.is_enabled():
            assert False
        else:
            assert len(letters)
        self.driver.implicitly_wait(30)

    def deleting(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.implicitly_wait(30)
        self.driver.find_element(*HomePage.delete).click()




        # media = self.driver.find_element(*HomePage.body)
        #deleted = self.driver.find_element(*HomePage.modal)

         #   self.driver.find_element(*HomePage.errase).click()


        # self.driver.find_element(*HomePage.delete).click()
        # self.driver.implicitly_wait(30)
        # self.driver.find_element(*HomePage.modal).click()

    def presentitem(self):
        src = self.driver.page_source
        text_found = re.search(r'assets/images/hawkins.jpg', src)
        if text_found:
            assert True
        else:
            assert False
