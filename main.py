from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./user_data')
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

string = 'Anda belum bimbingan'

target = '"_3RWII"'

x_arg = '//div[contains(@class, ' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
print (group_title)
print("Tunggu bentaran!")

new_chat = driver.find_elements_by_tag_name("span")[12].get_attribute("data-icon")

chat = driver.find_elements_by_tag_name("span")[12]
chitchat = chat.get_attribute("data-icon")
if chitchat == "chat":
    chat.click()


#search target
search_chat = driver.find_element_by_tag_name("input").get_attribute("title")

search = driver.find_element_by_tag_name("input")
sirchsearch =  search.get_attribute("title")
if sirchsearch == "Search contacts":
    search.click()
    search.send_keys("Dezha Polpos")

time.sleep(1)

npm_target = '"Dezha Polpos"'

#click target
target_npm = '//span[contains(@title,' + npm_target + ')]'
target_npm_click = wait.until(EC.presence_of_element_located((By.XPATH, target_npm)))
target_npm_click.click()

time.sleep(1)

#write message
message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
message.send_keys(string)

time.sleep(1)

#send message
sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()