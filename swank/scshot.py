from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def scshotfunc(swankurl):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(swankurl)
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    savedir = 'media/'
    driver.save_screenshot(savedir + 'noname.png')
    returnname = 'noname.png'
