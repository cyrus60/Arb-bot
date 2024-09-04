# attempt at basic selenium scrape 
# mainly just basic testing at this point

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# configuring headless options
options = Options()
options.headless = True
options.add_argument('--window-size=1900,1200')

# path to chrome driver
DRIVER_PATH = 'C:/Users/Cyrus Straley/Downloads/chromedriver-win64/chromedriver.exe'

# intializing chrome driver
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# test
driver.get('www.draftkings.com')
print(driver.page_source)

