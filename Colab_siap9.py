import selenium
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from twocaptcha import TwoCaptcha
from solveRecaptcha import solveRecaptcha
import csv
from csv import reader
import os
import pyautogui

print( os.getcwd() )

#PROXY = "45.140.13.119:9132"
# PROXY = "45.142.28.83:8094"
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=%s' % PROXY)
# options.add_experimental_option('excludeSwitches' , ['enable-logging'])
# options.add_argument('--lang=en-US') #need for recaptcha be in english
#options.add_extension('C:\Packages\mpbjkejclgfgadiemmefgebjfooflfhl.crx')
#options.add_extension('C:\Packages\ceipnlhmjohemhfpbjdgeigkababhmjc.crx')
# driver = webdriver.Chrome(chrome_options=options)
# action = ActionChains(driver)




def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        options = webdriver.ChromeOptions()
        driver = uc.Chrome(use_subprocess=True, chrome_options=options)
        #driver = webdriver.Chrome(chrome_options=options)
        options.add_experimental_option('excludeSwitches' , ['enable-logging'])
        options.add_argument('--lang=en-US') #need for recaptcha be in english
        driver.implicitly_wait(8)
        driver.maximize_window()
        def urus_capca():
            try:
                result = solveRecaptcha(
                    '6LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip',
                    'https://colab.research.google.com/drive/12dcreVyGOaxX1gcmMibbTJ3I0gQOMfQt?usp=sharing',
                )

                code = result['code']
                print(code)

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'g-recaptcha-response-100000'))
                )
                driver.execute_script(
                    "document.getElementById('g-recaptcha-response-100000').innerHTML = " + "'" + code + "'")
                driver.execute_script(
                    f"___grecaptcha_cfg.clients['0']['L']['L']['callback']('{code}');")
                driver.execute_script(
                    f"___grecaptcha_cfg.clients['100000']['L']['L']['promise-callback']('{code}');")
                print("ngurus capca")
            except:
                return False
        def exists_by_id(driver, thex, howlong):
            try:
                WebDriverWait(driver, howlong).until(EC.visibility_of_element_located((By.ID, thex)))
            except:
                return False
        def exists_by_xpath(driver, thex, howlong):
            try:
                WebDriverWait(driver, howlong).until(EC.visibility_of_element_located((By.XPATH, thex)))
            except TimeoutException:
                return True
        def cari_gpu():
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#cell-kYTd5eO8AKHM colab-static-output-renderer:nth-child(1) > div:nth-child(1)')))
                gpucpu = driver.find_element(By.CSS_SELECTOR, '#cell-kYTd5eO8AKHM colab-static-output-renderer:nth-child(1) > div:nth-child(1)').text
            except:
                return False

        def Cek_typegpu():
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#cell-ExPwqHtxdosc colab-static-output-renderer:nth-child(1) > div:nth-child(1)')))
                gpuType = driver.find_element(By.CSS_SELECTOR, '#cell-ExPwqHtxdosc colab-static-output-renderer:nth-child(1) > div:nth-child(1)').text
            except:
                return False                
        def exists_by_text2(driver, text):
            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), '"+str(text)+"')]")))
            except Exception:
                    return False
            return True
        
        def exists_by_text(driver, text):
            #driver.implicitly_wait(2)
            try:
                driver.find_element(By.XPATH, "//*[contains(text(), '"+str(text)+"')]" )
                #jajal = driver.find_element_by_xpath("//*[contains(text(), '"+str(text)+"')]")
            except NoSuchElementException:
                driver.implicitly_wait(5)
                return False
            driver.implicitly_wait(5)
            return True
        

        try:
            driver.get('https://colab.research.google.com/drive/12dcreVyGOaxX1gcmMibbTJ3I0gQOMfQt?usp=sharing')
            tombol_login = driver.find_element(By.LINK_TEXT, "Sign in")
            tombol_login.click()

            email = driver.find_element(By.ID , "identifierId")
            email.send_keys(id_str)
            time.sleep(2)

            klikmail = driver.find_element(By.CSS_SELECTOR , "#identifierNext > div > button > span")
            klikmail.click()

            paswod = driver.find_element(By.NAME , "password")
            paswod.clear()

            paswod.send_keys(id_pass)
            time.sleep(2)

            paswod.send_keys(u'\ue007') #unicode for enter key
            time.sleep(4)
            try :

                WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div/div[2]')))
                print("minta pemulihan")
                email_pulih = driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div/div[2]')
                email_pulih.click()
                time.sleep(2)

                isi_pemulihan = driver.find_element_by_id("knowledge-preregistered-email-response")
                isi_pemulihan.send_keys('wahyuotong77@gmail.com')
                time.sleep(3)
                driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            except TimeoutException:
                print("ga minta pemulihan")
                pass
            #============= klik tombol 1 ==================================================
            tombol1 = driver.find_element(By.CSS_SELECTOR , "#cell-kYTd5eO8AKHM colab-run-button")
            tombol1.click()
            print("klik Cari GPU")
            time.sleep(4)

            driver.find_element(By.ID, "ok").click()
            print("klik accept")
            time.sleep(10)
            try :
                WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//colab-recaptcha-dialog")))
                print("ada captcha coy")
                urus_capca()
            except TimeoutException:
                print("ga ada captcha")

            # if exists_by_xpath(driver, "//colab-recaptcha-dialog", 5):
            # #if exists_by_text2(driver, "Are you still there?"):
            #     print("ada captcha")
            #     urus_capca()

            if exists_by_text2(driver,"Failed to assign a backend"):
                print("nobackend")
                time.sleep(4)
                driver.quit()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#cell-kYTd5eO8AKHM colab-static-output-renderer:nth-child(1) > div:nth-child(1)")))
            # elemen = driver.find_element(By.CSS_SELECTOR, '#cell-kYTd5eO8AKHM colab-static-output-renderer:nth-child(1) > div:nth-child(1)').text
            # print(elemen)
            cari_gpu()
            time.sleep(3)            
            #========= kliik tombol 2 ====================================================================

            tombol2 = driver.find_element(By.CSS_SELECTOR, "#cell-ExPwqHtxdosc colab-run-button")
            tombol2.click()
            print("klik cek Type GPU")
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#cell-ExPwqHtxdosc colab-static-output-renderer:nth-child(1) > div:nth-child(1)")))
            gpuType = driver.find_element(By.CSS_SELECTOR, '#cell-ExPwqHtxdosc colab-static-output-renderer:nth-child(1) > div:nth-child(1)').text
            print(gpuType)            

            #===============================================================================================
            if gpuType == "Tesla K80" :
                print("cari selain :", gpuType)
                menu = driver.find_element_by_id("runtime-menu-button")
                menu.click()
                driver.find_element(By.XPATH, "//*[contains(text(), 'Manage sessions')]").click()
                print("klik manage sesi")
                time.sleep(4)

                #== layar gede  GPU ONLY =====================================================

                #======= Terminate atas ===
                pyautogui.click(x=1748, y=629)
                #========= konfirmasi =====
                pyautogui.click(x=1817, y=908)
                #== Terminate bawah/cpu  =====
                #pyautogui.click(x=1505, y=492)

                #======== Close ========
                pyautogui.click(x=1539, y=947)
                #==============================================================================


                #=== kecil GPU ONLY =============================================================
                #===atas======
                # pyautogui.click(x=1444, y=382)
                # time.sleep(5)
                # #=== konfirmasi =====
                # pyautogui.click(x=1518, y=667)
                # time.sleep(5)
                # #=== Close ======
                # pyautogui.click(x=1477, y=912)
                # time.sleep(200)
                #==================================================================================

                    
            time.sleep(3000)
            #driver.quit()
            #driver.quit()
        except:
            print("olala")
            #driver.quit()
    else:
        print("Either ID or PASSWORD is null")

    


with open('id_pass2.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

print("Total Ids and Passwords: ", len(list_of_rows))
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows
#=======================================
id_str = "anaksolehah557@gmail.com"
id_pass = "Percayadiri2018"

Connecting_To_Browser(id_str, id_pass)
#==================================================
# for i in range(len(ids_pass_list)):
#     try:
#         id_str = ids_pass_list[i][0]
#         id_pass = ids_pass_list[i][1]
#         print(i)
#         print("Login Id: ", id_str)
#         print("Login Password: ", id_pass)
#         Connecting_To_Browser(id_str, id_pass)
#     except:
#         print("gagal")

    
