# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:23:25 2020

@author: Rahul1582
"""
from selenium import webdriver
from confidential import username,password

###########################################################


website_link="https://www.hackerearth.com/"




###########################################################


element_for_login='//*[@id="__next"]/div/div/div[1]/div/div[2]/div[1]'

element_for_username='//*[@id="__next"]/div[1]/div/div[2]/div[3]/form/input[1]'

element_for_password='//*[@id="__next"]/div[1]/div/div[2]/div[3]/form/input[2]'

element_for_button='//*[@id="__next"]/div[1]/div/div[2]/div[3]/form/div[2]/button'

###########################################################


driver = webdriver.Chrome("D:/chromedriver_win32/chromedriver.exe")
	
driver.get((website_link))

login_but=driver.find_element_by_xpath(element_for_login)

login_but.click()

for i,j in zip(username,password):
    
    try:
        username_key= driver.find_element_by_xpath(element_for_username) 
        username_key.click()
        username_key.send_keys(i)
        
        password_key=driver.find_element_by_xpath(element_for_password)
        password_key.click()                                          
        password_key.send_keys(j)        
        
        
        submit = driver.find_element_by_xpath(element_for_button)

        submit.click()    
        
        username_key.clear()
        password_key.clear()                         
	
	
    except:
        print("Some error occured :(")
        
	#### This exception occurs if the element are not found in the webpage.
	   

    

