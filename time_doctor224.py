# -*- coding: utf-8 -*-
"""
Created on Fri May 14 10:43:39 2021

@author: youssef ouahman
"""
import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PyQt5 import QtWidgets,QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from win32process import CREATE_NO_WINDOW
# import requests
# from win32process import CREATE_NO_WINDOW

# def start(self):
#     """
#     Starts the Service.

#     :Exceptions:
#      - WebDriverException : Raised either when it can't start the service
#        or when it can't connect to the service
#     """
#     try:
#         cmd = [self.path]
#         cmd.extend(self.command_line_args())
#         self.process = subprocess.Popen(cmd, env=self.env,
#                                         close_fds=platform.system() != 'Windows',
#                                         stdout=self.log_file, stderr=self.log_file, creationflags=CREATE_NO_WINDOW)
#     except TypeError:
#         raise

 	

def login(driver):
    l=[['//*[@id="user_login"]',"chef"],['//*[@id="user_pass"]',"jqkt&#UVnzm820s4Oxx6aYmW"]]
    #entrer login 
    driver.get("https://hassanhirech.net//wp-admin")

    #entrer text element.send_keys("some text")
    for i in range(2):
        login_form = driver.find_element_by_xpath(l[i][0])
        login_form.send_keys(l[i][1])
        time.sleep(2)

    driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
    
# def login(driver):
#     l=[['//*[@id="user_login"]',"admin"],['//*[@id="user_pass"]',"admin@sudalphag.com"]]
#     #entrer login 
#     driver.get("https://sudalphag.com//booked//wp-admin")

#     #entrer text element.send_keys("some text")
#     for i in range(2):
#         login_form = driver.find_element_by_xpath(l[i][0])
#         login_form.send_keys(l[i][1])
#         time.sleep(2)

#     driver.find_element_by_xpath('//*[@id="wp-submit"]').click()




def iniale(driver):
    try:
        #annule //*[@id="customTimeslotsContainer"]/div/a
        annuler_entr = driver.find_elements_by_xpath( '//*[@id="customTimeslotsContainer"]/div/div/span')
        time.sleep(5)
        if(len(annuler_entr) >= 2):
            driver.find_element_by_xpath('//*[@id="customTimeslotsContainer"]/div/a').click()
            time.sleep(2)
            driver.switch_to_alert().accept()
            time.sleep(5) 
            return True
        elif(len(annuler_entr) == 1):
            return False
        else:
            return True
    except:
        #add first general 
        iniale(driver)
        
def work(driver,word,date,startime,endtime,number,pos): 
    if(pos == False): 
    #add singel button addSingleTimeslot  //*[@id="customTimeslotsContainer"]/div/button[1]
        login_form66 = driver.find_element_by_xpath('//*[@id="customTimeslotsContainer"]/div/button[1]')
        login_form66.click()
        time.sleep(8)
                                                
        login_form8 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/input")
        login_form8.send_keys(word)
        time.sleep(5)

        select = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/select[1]"))
        select.select_by_visible_text(str(startime))
        time.sleep(5)
    
        select1 = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/select[2]"))
        select1.select_by_visible_text(str(endtime))
        time.sleep(5)
    
        select2 = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/select[3]"))
        select2.select_by_visible_text(str(number)+" spaces available")
        time.sleep(5)

        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/button[1]").click()
        time.sleep(5)
        driver.switch_to_alert().accept()
        time.sleep(60)
        driver.close()
        
    else:      
        #check button addd //*[@id="customTimeslots"]/div[2]/button
        driver.find_element_by_xpath('//*[@id="customTimeslots"]/div[2]/button').click()
        time.sleep(3)

        #first booked_custom_start_date   "booked_custom_end_date"
        login_form55 =  driver.find_element_by_name('booked_custom_start_date')
        login_form55.send_keys(date)
        time.sleep(3)

        login_form666 = driver.find_element_by_name("booked_custom_end_date")
        login_form666.send_keys(date)
        time.sleep(3)

    #add singel button addSingleTimeslot  //*[@id="customTimeslotsContainer"]/div/button[1]
        login_form6666 = driver.find_element_by_xpath('//*[@id="customTimeslotsContainer"]/div/button[1]')
        login_form6666.click()
        time.sleep(11)
    
    

        login_form88 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/input")
        login_form88.send_keys(word)
        time.sleep(4)
        
        select0 = Select(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/select[1]'))
        select0.select_by_visible_text(str(startime))
        time.sleep(4)
 
        select11 = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/select[2]"))
        select11.select_by_visible_text(str(endtime))
        time.sleep(4)
    
        select22 = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/form/select[3]"))
        select22.select_by_visible_text(str(number)+" spaces available")
        time.sleep(4)

        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div[1]/button[1]").click()
        time.sleep(4)
        driver.switch_to_alert().accept()
        time.sleep(60)
        driver.close()
    
# def finich(driver):
#     # create class="button-primary addSingleTimeslot_button"
#     driver.find_element_by_class_name("button-primary addSingleTimeslot_button").click()



def appilquer(word,startime,endtime,number,i):
    #install driver chrome 
    options = webdriver.ChromeOptions()
    
    options.add_argument('--log-level=3')
    # options.add_argument('headless')
    # # options = webdriver.ChromeOptions()
    # options.headless = True
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument("--disable-extensions")
    # options.add_argument("--proxy-server='direct://'")
    # options.add_argument("--proxy-bypass-list=*")
    # options.add_argument("--start-maximized")
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    #driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome("C:/chromedriver.exe")
    driver.maximize_window()
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    time.sleep(5)
    try:
        login(driver) # function for enter the site
    
        #arrive for page time
        driver.get("https://hassanhirech.net/wp-admin/admin.php?page=booked-settings#custom-timeslots")
    
        pos = iniale(driver)
        #determiner la date 
        date = str(datetime.datetime(3556,12,23).now().date()) 
        time.sleep(5)
        work(driver,word,date,str(startime),str(endtime),str(number),pos) #function the applique
        
        
    except:
        driver.close()
        # print("fail")
        time.sleep(5)
        if(i <15):
            i = i + 1
            appilquer(word,startime,endtime,number,i)
        else:
            pass
    # finich(driver)#out for site




def final(time_working ,number):
    timee = str(datetime.datetime(3556,12,23).now().time())   
    timeee = timee.split(":")[:2]
    word=["الفترة الصباحية","الفترة المسائية"]
    mytime =str(time.ctime())[:3]
    
    if(mytime != "Sun" and mytime != "Sat"):
        #حدد الساعة 0 والدقيقة 1 في الصباح      
        if(timeee[0] == '06' and timeee[1] == '58'):
            i=0
            appilquer(word[0],time_working[0],time_working[1],number[0],i)
             #حدد الساعة 0 والدقيقة 1 في المساء      
        elif(timeee[0] == '12' and timeee[1] == '58'):
            i=0
            appilquer(word[1],time_working[2],time_working[3],number[1],i) 
            
    if(mytime == "Sat") :  
        if(timeee[0] == '06' and timeee[1] == '58'):
            i=0
            appilquer(word[0],time_working[0],time_working[1],number[0],i)
            
             #حدد الساعة 0 والدقيقة 1 في المساء      
        elif(timeee[0] == '12' and timeee[1] == '58'):
#            if(number[0] != "25"):
#                i=0
#                appilquer(word[1],time_working[2],time_working[3],number[1],i)
#            else:
#                i=0
#                appilquer(word[1],time_working[2],time_working[3],"25",i) 
            options = webdriver.ChromeOptions()
            options.add_argument('--log-level=3')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.maximize_window()
            time.sleep(5)
            login(driver)
            time.sleep(5)
            driver.get("https://hassanhirech.net/wp-admin/admin.php?page=booked-settings#custom-timeslots")
            time.sleep(5) 
            driver.find_element_by_xpath('//*[@id="customTimeslotsContainer"]/div/a').click()
            time.sleep(3)
            driver.switch_to_alert().accept()
            time.sleep(60)
            driver.close()                





class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setEnabled(True)
        dialog.resize(600, 520)
        font = QtGui.QFont()
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        dialog.setFont(font)
        dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        dialog.setAcceptDrops(False)
        dialog.setWindowTitle("Automate rendez-vous")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/mo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/mo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        dialog.setWindowIcon(icon)
        dialog.setWindowOpacity(16.0)
        dialog.setToolTip("")
        dialog.setStatusTip("")
        dialog.setWhatsThis("")
        dialog.setAccessibleName("")
        dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        dialog.setWindowFilePath("")
        dialog.setInputMethodHints(QtCore.Qt.ImhNone)

        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 460, 181, 51))
        self.pushButton.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";\n"
"font: 8pt \"MS Sans Serif\";\n"
"font: 75 27pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 460, 181, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";\n"
"font: 8pt \"MS Sans Serif\";\n"
"font: 75 27pt \"MS Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(dialog)
        self.textBrowser.setGeometry(QtCore.QRect(-10, 110, 611, 41))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 270, 601, 41))
        self.textBrowser_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(450, 170, 61, 31))
        self.textBrowser_4.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(240, 170, 51, 31))
        self.textBrowser_5.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_8 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_8.setGeometry(QtCore.QRect(40, 420, 521, 31))
        self.textBrowser_8.setStyleSheet("alternate-background-color: rgb(166, 166, 166);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(370, 170, 61, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 170, 61, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser_9 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_9.setGeometry(QtCore.QRect(660, 460, 51, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_10.setGeometry(QtCore.QRect(960, 460, 51, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(770, 460, 181, 31))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textBrowser_6 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(250, 330, 51, 31))
        self.textBrowser_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(460, 330, 51, 31))
        self.textBrowser_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 330, 61, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 330, 61, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 341, 91))
        self.label.setMaximumSize(QtCore.QSize(16765, 1677))
        self.label.setStyleSheet("\n"
"\n"
"background-image: url(.img/mo.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".img/mo.png"))
        self.label.setScaledContents(True)
        
        self.label.setObjectName("label")
        self.textBrowser_11 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_11.setGeometry(QtCore.QRect(360, 230, 171, 31))
        self.textBrowser_11.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(250, 230, 101, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 380, 101, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.textBrowser_12 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_12.setGeometry(QtCore.QRect(360, 380, 171, 31))
        self.textBrowser_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.textBrowser_12.setObjectName("textBrowser_12")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("dialog", "START"))
        self.pushButton_2.setText(_translate("dialog", "STOP"))
        self.textBrowser.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">الفترة الصباحية</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">الفترة المسائية</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">من</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">الى</span></p></body></html>"))
        self.lineEdit.setInputMask(_translate("dialog", "00:00"))
        self.lineEdit.setText(_translate("dialog", "00:00"))
        self.lineEdit_2.setInputMask(_translate("dialog", "00:00"))
        self.lineEdit_2.setText(_translate("dialog", "00:00"))
        self.textBrowser_9.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa5500;\">الى</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa5500;\">من</span></p></body></html>"))
        self.lineEdit_3.setInputMask(_translate("dialog", "00:00"))
        self.lineEdit_3.setText(_translate("dialog", "00:00"))
        self.textBrowser_6.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffffff;\">الى</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffffff;\">من</span></p></body></html>"))
        self.lineEdit_4.setInputMask(_translate("dialog", "00:00"))
        self.lineEdit_4.setText(_translate("dialog", "00:00"))
        self.lineEdit_5.setInputMask(_translate("dialog", "00:00"))
        self.lineEdit_5.setText(_translate("dialog", "00:00"))
        self.textBrowser_11.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">العداد</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">العداد</span></p></body></html>"))
 

       
class main(QtWidgets.QMainWindow,Ui_dialog):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)
        self.pushButton.pressed.connect(self.start)
        self.pushButton_2.pressed.connect(self.stop)
       
    def start(self):
        # try:
        #     cmd = [self.path]
        #     cmd.extend(self.command_line_args())
        #     self.process = subprocess.Popen(cmd, env=self.env,close_fds=platform.system() != 'Windows',stdout=self.log_file,stderr=self.log_file,stdin=PIPE,creationflags=CREATE_NO_WINDOW)
        # except TypeError:
        #     raise
        
        self.thear = addItemThread(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text())
        self.thear.start()
        # self.thear.add_item0.connect(self.lineEdit.text())
        # self.thear.add_item2.connect(self.lineEdit_2.text)
        # self.thear.add_item4.connect(self.lineEdit_4.text)
        # self.thear.add_item5.connect(self.lineEdit_5.text)
        # self.thear.add_item6.connect(self.lineEdit_6.text)
        # self.thear.add_item7.connect(self.lineEdit_7.text) #مقاعد الفترة المساىية
        self.thear.add_item8.connect(self.textBrowser_8.setText)
      
     
    def stop(self):
        self.thear.stop()

     
class addItemThread(QThread) :
    # add_item0 = pyqtSignal(int)
    # add_item2 = pyqtSignal(str)
    # add_item4 = pyqtSignal(str)
    # add_item5 = pyqtSignal(str)
    # add_item6 = pyqtSignal(str)
    # add_item7 = pyqtSignal(str)
    add_item8 = pyqtSignal(str)
    
    def __init__(self,add_item0,add_item2,add_item4,add_item5,add_item6,add_item7,parent = None):
        QThread.__init__(self,parent)
        self.isRunning = True
        
        #defnition des variable
        self.add_item0=add_item0
        self.add_item2=add_item2
        self.add_item4=add_item4
        self.add_item5=add_item5
        self.add_item6=add_item6
        self.add_item7=add_item7
        
        
        self.l = ["09:00","13:30","17:00","21:00"]
        self.number =['14','14']
        
        if(self.add_item0 !="00:00" ):
            self.l[0] = str(self.add_item0)
                
        if(self.add_item2 !="00:00" ):
            self.l[1] = str(self.add_item2) 
                
        if(self.add_item4 !="00:00" ):
            self.l[2] = str(self.add_item4)
                
        if(self.add_item5 !="00:00" ):
            self.l[3] = str(self.add_item5)    
                
        if(self.add_item6 !=''):    
            self.number[0]  = str(self.add_item6)
                
        if(self.add_item7 !=''):    
            self.number[1]  = str(self.add_item7)
    def run(self):
        while(self.isRunning): 
            self.add_item8.emit (str("ثم بدا فتح المواعيد المرجوا عدم غلق البرنامج لتجنب حدوث مشاكل "))
            final(self.l,self.number)
            self.add_item8.emit (str("يمكنك الان غلق البرنامج او توقيفه للتعديل او الايقاف النهاىي")) 
            time.sleep(1)
    def stop(self): 
        self.isRunning = False
        self.add_item8.emit (str("ثم اغلاق البرنامج بنجاح "))
        self.quit()
        
            
        
    
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)   
    window = main()
    window.show()
    app.exec_()
   

        
