import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # Path to chromedriver executable
        chromedriver_path = "C:/Users/Usuario/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
        
        # Set up the service object
        service_obj = Service(chromedriver_path)
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(service=service_obj)
        
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif browser_name == "firefox":

        geckodriver_path = "C:/Users/Usuario/Downloads/geckodriver-v0.35.0-win32/geckodriver.exe"
        binary_path = "C:/Program Files/Mozilla Firefox/firefox.exe"

        firefox_options = FirefoxOptions()
        firefox_options.binary_location = binary_path      

        # Initialize Firefox WebDriver
        firefox_service = FirefoxService(executable_path=geckodriver_path)
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

       
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    
    request.cls.driver = driver
        
        # Yield to the test
    yield
        
        # Close the driver
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
    
