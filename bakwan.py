from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Bakwan:

    def __init__(self):
        self.driver     = webdriver.Chrome('/home/burger-man/Downloads/chromedriver')
        self.wait       = WebDriverWait(self.driver, 600)

    def sendMessageWithAPI(self, nomor, message):
        self.driver.get("https://web.whatsapp.com/send?phone=" + nomor)

        self.waitLogin()

        message_target = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message_target.send_keys(message)

        time.sleep(1)

        sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()

    def waitLogin(self):

        target = '"_3RWII"'
        x_arg = '//div[contains(@class, ' + target + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        print(group_title)

