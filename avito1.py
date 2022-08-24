# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 21:36:44 2021

@author: youssef ouahman
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
from openpyxl import Workbook


#driver = webdriver.Chrome("C:/chromedriver.exe")

def avito():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    workbook = Workbook()
    driver.maximize_window()
    start = input("entry number the first  page:")
    end = input("entry number the finish page:")
    total = [["name","telphone"]]
    for j in range(int(start),int(end)):
        try:
            driver.get("https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?o="+str(j))
            driver.implicitly_wait(10)
            for i in range(1,4):
                try:
                    peice =[]
                    time.sleep(5)
                    ser = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[7]/div[1]/div/div[2]/div['+str(i)+']')
                    ser.click()
                    time.sleep(5)
                    ser = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]')
                    ser.click() 
                    time.sleep(15)
                #name
                    name = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div/div/div/div/h4')
                    print(name.text)
                    peice.append(name.text)
                    time.sleep(5)               
                #tel
                    tel = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div/div/div/div/a')
                    print(tel.text) 
                    peice.append(tel.text)
                    total.append(peice)
                
                    time.sleep(5)
                    ser = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[1]/div/div/span/button')
                    ser.click()
                
                    time.sleep(5)
                    ser = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button')
                    ser.click()
        
                    time.sleep(5)                
                except:  
                    print("probleme")
                    driver.get("https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?o="+str(j))
                    driver.implicitly_wait(10)
                    pass
        except:
            pass
        
    driver.close()
    sheet = workbook.active    
    for row in total:
        sheet.append(row)
    workbook.save(filename="data_avito_{}_{}.xlsx".format(start,end))
        
avito()    
#try:
#    ser = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/button")
#    ser.click()
#
#    ser = driver.find_element_by_class_name("iMkwaC")
#
#    l = ser.text
#    ll = l.split('.')
#    lll = l.split()
#    lis.append(lll[len(lll)-1])
#    print(lll[len(lll)-1])
#
#    ser = driver.find_element_by_class_name("cMTeXP")
#    ser.click()
#    time.sleep(5)
#    ser = driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[3]/a")
#    ser.click()
#except:
#    ser = driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[3]/a")
#    ser.click()
#while(i < 3):
#        try:
#            ser = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/button")
#            ser.click()
#            ser = driver.find_element_by_class_name("iMkwaC")
#            l = ser.text
#            ll = l.split('.')
#            lll = l.split()
#            lis.append(lll[len(lll)-1])
#            print(lll[len(lll)-1])

#            ser = driver.find_element_by_class_name("cMTeXP")
#            ser.click()
#            time.sleep(5)
#            ser = driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[3]/a")
#            ser.click()    
#            i = i + 1
#        except:
#            i = i + 1
#            ser = driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div[3]/a")
#            ser.click() 
#            pass
