from selenium import webdriver
import time


def fetch(url, pages):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--disable-extensions')
    # desired_capabilities = dict()
    # desired_capabilities['chromeOptions'] = {
    #     "args": ["--disable-extensions"],
    #     "extensions": []
    # }

    # driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    delay = 3

    driver.get(url)
    for i in range(pages):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

    html_source = driver.page_source
    data = html_source.encode('utf-8')

    return html_source
