import os
from selenium.webdriver.chrome.options import Options
from sauceclient import SauceClient

from selenium import webdriver

GRID_HUB_URL = os.environ.get('GRID_HUB_URL')
SAUCE_URL = os.environ.get('SAUCE_URL')

def before_feature(context, feature):
    if SAUCE_URL is None:
        if GRID_HUB_URL is None:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')  # Last I checked this was necessary.
            options.add_argument('--no-sandbox')
            context.driver = webdriver.Chrome(options=options)
        else:
            desired_capabilities = webdriver.DesiredCapabilities.CHROME
            context.driver = webdriver.Remote(
                desired_capabilities=desired_capabilities,
                command_executor=GRID_HUB_URL
            )
    else:
        # sauce_client = SauceClient(os.getenv("SAUCE_USERNAME"), os.getenv("SAUCE_ACCESS_KEY"))
        desired_cap = {
            "browser_name": "chrome"
            # "name": name,
            # "platform": os.environ.get('platform'),
            # "browser_name": os.environ.get('browserName'),
            # "version": os.environ.get('version'),
            # "build": build,
        }
        print("before remote")
        context.driver = webdriver.Remote(
            command_executor=SAUCE_URL,
            desired_capabilities=desired_cap)


def after_feature(context, feature):
    context.driver.quit()
