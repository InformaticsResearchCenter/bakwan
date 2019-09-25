from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class SendWithoutAPI:

    driver = ''
    wait   = ''

    def __init__(self):
        self.driver = webdriver.Chrome('/home/burger-man/Downloads/chromedriver')
        self.wait = WebDriverWait(self.driver, 600)
        self.driver.get("https://web.whatsapp.com")
        target = '"_3RWII"'
        x_arg = '//div[contains(@class, ' + target + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        print (group_title)
        print("Tunggu bentaran!")

    def sendMessageWithoutAPI(self, contact, message):

        chat = self.driver.find_elements_by_tag_name("span")[12]
        chitchat = chat.get_attribute("data-icon")
        if chitchat == "chat":
            chat.click()


        search = self.driver.find_element_by_tag_name("input")
        sirchsearch =  search.get_attribute("title")
        if sirchsearch == "Search contacts":
            search.click()
            search.send_keys(contact)

        time.sleep(1)

        npm_target = '"'+contact+'"'

        target_npm = '//span[contains(@title,' + npm_target + ')]'
        target_npm_click = self.wait.until(EC.presence_of_element_located((By.XPATH, target_npm)))
        target_npm_click.click()

        time.sleep(1)

        message_target = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message_target.send_keys(message)

        time.sleep(1)

        sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()

class SendWithAPI:

    driver  = ''
    wait    = ''
    nomor   = '6282217401448'

    def __init__(self):
        self.driver     = webdriver.Chrome('/home/burger-man/Downloads/chromedriver')
        self.wait       = WebDriverWait(self.driver, 600)

        self.driver.get("https://web.whatsapp.com/send?phone=" + self.nomor)

        target = '"_3RWII"'
        x_arg = '//div[contains(@class, ' + target + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        print(group_title)

    def sendMessageWithAPI(self, message):

        message_target = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message_target.send_keys(message)

        time.sleep(1)

        sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()

sending = SendWithAPI()
sending.sendMessageWithAPI("Hey, kamu bimbingan dulu")