from selenium import webdriver
import time
import captcha_decoder
import scraping

web = webdriver.Chrome()
URL='https://satvika-eda.github.io/captchaweb/index.html'
web.get(URL)

time.sleep(2)

name=scraping.filename(URL)
result=captcha_decoder.decoder(name)
last = web.find_element_by_xpath('//*[@id="captcha"]')
last.send_keys(result)

time.sleep(2)

Submit = web.find_element_by_xpath('/html/body/form/button')
Submit.click()
