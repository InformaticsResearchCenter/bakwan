from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Bakwan:

    def openBrowser(self):
        self.saveProfile()
        self.wait       = WebDriverWait(self.driver, 600)

    def sendContact(self, contact, message):
        self.openBrowser()
        self.driver.get("https://web.whatsapp.com")
        self.waitLogin()
        self.searchAndClick(contact)
        self.typeAndSend(message)
        time.sleep(2)
        self.closeBrowser()


    def sendNumber(self, nomor, message):
        self.openBrowser()
        self.driver.get("https://web.whatsapp.com/send?phone=" + nomor)
        time.sleep(5)
        self.waitLogin()
        self.typeAndSend(message)
        time.sleep(2)
        self.closeBrowser()

    def waitLogin(self):
        target = '"_3RWII"'
        x_arg = '//div[contains(@class, ' + target + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        print(group_title)

    def saveProfile(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./user_data')
        self.driver = webdriver.Chrome(chrome_options=options)

    def typeAndSend(self, message):
        time.sleep(1)

        message_target = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message_target.send_keys(message)

        time.sleep(1)

        sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()

    def searchAndClick(self, contact):
        chat = self.driver.find_elements_by_tag_name("span")[12]
        chitchat = chat.get_attribute("data-icon")
        if chitchat == "chat":
            chat.click()

        search = self.driver.find_element_by_tag_name("input")
        sirchsearch = search.get_attribute("title")
        if sirchsearch == "Search contacts":
            search.click()
            search.send_keys(contact)

        time.sleep(1)

        npm_target = '"' + contact + '"'

        target_npm = '//span[contains(@title,' + npm_target + ')]'
        target_npm_click = self.wait.until(EC.presence_of_element_located((By.XPATH, target_npm)))
        target_npm_click.click()

    def closeBrowser(self):
        self.driver.close()