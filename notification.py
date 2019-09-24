from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Notification:

    driver = ""
    wait = ""

    def __init__(self):        
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./user_data')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://web.whatsapp.com/")
        self.wait = WebDriverWait(self.driver, 600)
        target = '"_3RWII"'
        x_arg = '//div[contains(@class, ' + target + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        print(group_title)
        print("Send Notification!")

    def sendNotification(self, npm, message):
        #search chat
        chat = self.driver.find_elements_by_tag_name("span")[12]
        search_chat = chat.get_attribute("data-icon")
        if search_chat == "chat":
            chat.click()
        #search target
        target = self.driver.find_element_by_tag_name("input")
        search_target =  target.get_attribute("title")
        if search_target == "Search contacts":
            target.click()
            target.send_keys(npm)
        time.sleep(1)
        #click target
        click = '//span[contains(@title,' + npm + ')]'
        target_click = self.wait.until(EC.presence_of_element_located((By.XPATH, click)))
        target_click.click()
        time.sleep(1)
        #write message
        write = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        write.send_keys(message)
        time.sleep(1)
        #send message
        send = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        send.click()
        

notif = Notification()
notif.sendNotification("Dezha Polpos", "Anda Belum Bimbingan")