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

        name=input("Enter Category you want to search:")

        cat=self.driver.find_element_by_xpath('//*[@id="ember42"]/input')  
        cat.click()
        cat.send_keys(name+" in people")
        sleep(2)

        send=self.driver.find_element_by_xpath('//*[@id="ember40"]/div[2]')
        send.click()
        sleep(4)

       
            
        # for i in range(2):
        #     self.driver.execute_script("window.scrollBy(0,200)","")
        #     sleep(3)

        for i in range(2):
            send1=self.driver.find_element_by_link_text('Connect')
            sleep(4)

            send1.click()
        
       
       
        # while(True):
        #      connect=self.driver.find_element_by_link_text("Connect")
        #      counter=0
        #      cb_length=3

        #      while(counter<cb_length):
        #          connect[counter].click()
                
        #          counter+=1
       

        

bot=Bot()
bot.main()