import os
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

GRID_HUB_URL = os.environ.get('GRID_HUB_URL')

def before_feature(context, feature):
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


def after_feature(context, feature):
    context.driver.quit()
