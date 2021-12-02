from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("{profile.default_content_setting_values.notifications : 1}")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://google.co.in')
signinbutton = driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a')
signinbutton.click()
email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys('rahulsharma4329')
email.send_keys(Keys.RETURN)
driver.implicitly_wait(15)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys('Rahul4329$')
password.send_keys(Keys.RETURN)
driver.get('https://google.com')
driver.implicitly_wait(100)
driver.get('https://meet.google.com/aky-nifj-zqz')
driver.refresh()
dismissbtn = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
dismissbtn.click()
for i in range(100000000):
    pass
joinbtn = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
joinbtn.click()