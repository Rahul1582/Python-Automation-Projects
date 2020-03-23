from selenium import webdriver

class Music():
    def __init__(self):
        self.driver=webdriver.Chrome("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")

    def play(self):
        name=input("Enter a youtube channel link")
        self.driver.get("https://www.youtube.com/user/"+name+"/videos")

        new=self.driver.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[1]')

        new.click()

bot=Music()
bot.play()            