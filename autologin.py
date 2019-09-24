from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

nomor = "6282144361462"

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(chrome_options=options)
#driver.get('https://web.whatsapp.com/')

#driver = webdriver.Chrome(r'E:\IRC\chromedriver')

driver.get("https://web.whatsapp.com/send?phone=" + nomor)

wait = WebDriverWait(driver, 600)

string = 'hello, crot!'

target = '"_3RWII"'

x_arg = '//div[contains(@class, ' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
print (group_title)
print("Tunggu bentaran!")

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
message.send_keys(string)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()