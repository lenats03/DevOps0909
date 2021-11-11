from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chrome_op
from selenium.webdriver.edge.options import Options as edge_op
from selenium.webdriver.firefox.options import Options as ff_op
from time import sleep


edge_driver = webdriver.Edge(executable_path='C:/Users/Lenats/Downloads/edgedriver_win64/msedgedriver.exe')

# 1
chrome_driver = webdriver.Chrome(executable_path='C:/Users/Lenats/Downloads/chromedriver_win32/chromedriver.exe')
chrome_driver.get("http://walla.co.il")
ff_driver = webdriver.Firefox(executable_path='C:/Users/Lenats/Downloads/geckodriver-v0.30.0-win64/geckodriver.exe')
ff_driver.get('http://ynet.co.il')

# 2
orig_page_title = chrome_driver.find_element_by_xpath('/html/head/title')
print(orig_page_title)
chrome_driver.refresh()
assert chrome_driver.find_element_by_xpath('/html/head/title') == orig_page_title

# 3
# kind of.
# /html/body/div[4]/div/main/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div
# /html/body/div[4]/div/main/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div
# /html/body/div[4]/div/main/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/a


# 4
ff_driver.get("https://translate.google.com/?sl=iw&tl=en&op=translate")

ff_driver.find_element_by_xpath(
   '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').send_keys(
  'שלום')

# 5

chrome_driver.get("https://www.youtube.com/")
chrome_driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys('abracadabra') #//*[@id="search"]
chrome_driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()


# 6

chrome_driver.get("https://translate.google.com/?sl=iw&tl=en&op=translate")

chrome_driver.find_element_by_xpath(
   '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').send_keys(
   'שלום\n')
chrome_driver.find_element_by_xpath(
   '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').send_keys(
   'אחד שתיים ארבע \n')
chrome_driver.find_element_by_css_selector(
   '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb '
   '> div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > '
   'textarea').send_keys('אחד שתיים שלוש')

#
sleep(4)
element = chrome_driver.find_element_by_css_selector(
   '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb > div.dePhmb > div > div.J0lOec > span.VIiyi').text
print(element)


# 7
chrome_driver.get("https://facebook.com")
chrome_driver.find_element_by_id('email').send_keys('lenats@gmail.com')
chrome_driver.find_element_by_id('pass').send_keys('123456')
chrome_driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

# 8
chrome_driver.get("https://facebook.com")
chrome_driver.delete_all_cookies()
print(chrome_driver.get_cookies())

# 9
#אביאל , לא הצלחתי לתפוס את השורה של ה search . איך עושים זאת? ניסיתי לפי path , full path שם, שם הקלאס.....

#chrome_driver.get("https://github.com/search")
# <input aria-label="Search GitHub" autocapitalize="off" autocomplete="off" autofocus=""
# class="form-control input-block" data-hotkey="s" name="q" placeholder="Search GitHub" spellcheck="false" type="text">
# chrome_driver.find_element_by_xpath('//placeholder[contains( text( ), "Search or jump to…")]')  #  //*[placeholder='Search or jump to…']")
#chrome_driver.find_element(By.NAME, 'q').click()
#chrome_driver.find_element(By.TAG_NAME, 'input').send_keys = ('selenium')


# chrome_driver.find_element(By.XPATH,'/html/body/div[4]/main/div/div/form/div/div/input[1]').submit()
# chrome_driver.find_element(By.XPATH,'//*[@id="search_form"]/div/button').click()


# 10



def test_browser(browser, ops, ex_path):
    browser_ops = ops()
    browser_ops.add_argument('--disable-extensions')
    driver = browser(options=browser_ops, executable_path=ex_path)
    driver.get('https://google.com')
    driver.close()
    return 0


test_browser(webdriver.Chrome, chrome_op, 'C:/Users/Lenats/Downloads/chromedriver_win32/chromedriver.exe')
test_browser(webdriver.Edge, edge_op, 'C:/Users/Lenats/Downloads/edgedriver_win64/msedgedriver.exe')
test_browser(webdriver.Firefox, ff_op, 'C:/Users/Lenats/Downloads/geckodriver-v0.30.0-win64/geckodriver.exe')

edge_driver.close()
ff_driver.close()
chrome_driver.close()