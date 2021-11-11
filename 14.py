from selenium import webdriver
from time import sleep

my_driver=webdriver.Chrome(executable_path='C:/Users/Lenats/Downloads/chromedriver_win32/chromedriver.exe')
my_driver.get("file:///C:/Users/Lenats/Downloads/tip_calc/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys('100')
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
my_driver.find_element_by_xpath('//*[@id="calculate"]').click()
expected='20.00'
actual=my_driver.find_element_by_xpath('//*[@id="tip"]').text
if expected==actual:
    print ('OK')
else:
    print("not OK")




