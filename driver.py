from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller

# define environment
chromedriver_autoinstaller.install()
def getDriver():
    driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
    return driver
