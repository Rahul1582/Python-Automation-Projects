from selenium import webdriver
from confidential import username,password  

class Bot():
    def __init__(self):
        self.driver=webdriver.Chrome("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")

    def main(self):
        self.driver.get('https://www.hackerearth.com/')

        login=self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div/div[2]/div/div[3]')    

        login.click()

        user=self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div[2]/div[3]/form/input[1]')
        user.click()
        user.send_keys(username)

        pwd=self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div[2]/div[3]/form/input[2]')
        pwd.click()
        pwd.send_keys(password)

        submit = self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div[2]/div[3]/form/div[2]/button')

        submit.click()

bot=Bot()           
bot.main()  