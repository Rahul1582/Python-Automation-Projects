from selenium import webdriver
from confidential import username,password  
from time import sleep


sleep(4)
class Bot():
    def __init__(self):
        self.driver=webdriver.Chrome("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")

    def main(self):
        self.driver.get('https://www.linkedin.com/home')

        login=self.driver.find_element_by_xpath('/html/body/nav/a[3]')    

        login.click()
        sleep(4)

        user=self.driver.find_element_by_xpath('//*[@id="username"]')
        user.click()
        user.send_keys(username)
        sleep(4)

        pwd=self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.click()
        pwd.send_keys(password)
        sleep(4)

        cat= self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[4]')

        cat.click()


        #Searching for the people whom you want to send conections

        name=input("Enter Category:")

        cat=self.driver.find_element_by_xpath('//*[@id="ember42"]/input')  
        cat.click()
        cat.send_keys(name)


        send=self.driver.find_element_by_xpath('//*[@id="ember40"]/div[2]')
        send.click()


        people=self.driver.find_elements_by_css_selector('#ember6675 > ul > li:nth-child(1)')
        people.click()
       
        





bot=Bot()
bot.main()