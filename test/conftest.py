import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    driver.get("http://immense-hollows-74271.herokuapp.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield


def tearDown(self):
    self.driver.close()
