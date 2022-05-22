import selenium
import time
from selenium import webdriver
import csv
from csv import reader
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

print( os.getcwd() )

def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        options = webdriver.ChromeOptions()
        #browser = webdriver.Chrome(options=options)
        browser = uc.Chrome(use_subprocess=True)
        def exists_by_xpath(driver, thex, howlong):
            try:
                WebDriverWait(driver, howlong).until(EC.visibility_of_element_located((By.XPATH, thex)))
            except:
                return False        
        try:
            browser.get('https://www.gmail.com/')

            email_field = browser.find_element_by_id("identifierId")
            email_field.clear()

            email_field.send_keys(id_str)

            email_next_button = browser.find_element_by_id("identifierNext")
            email_next_button.click()

            time.sleep(2)

            password_field = browser.find_element_by_name("password")
            password_field.clear()

            password_field.send_keys(pass_str)

            password_next_button = browser.find_element_by_id("passwordNext")
            password_next_button.click()
            time.sleep(3)

            #pulih = browser.find_element_by_xpath('//span[contains(.,"Verify that it’s you")]').is_displayed()
            try :

                WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div/div[2]')))
                print("minta pemulihan")
                email_pulih = browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div/div[2]')
                email_pulih.click()
                time.sleep(2)

                isi_pemulihan = browser.find_element_by_id("knowledge-preregistered-email-response")
                isi_pemulihan.send_keys('wahyuotong77@gmail.com')
                time.sleep(3)
                browser.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            except TimeoutException:
                print("ga minta pemulihan")
                pass

            #browser.get('https://colab.research.google.com/drive/12dcreVyGOaxX1gcmMibbTJ3I0gQOMfQt?usp=sharing')
            time.sleep(300)

            
            #subscribe_next_button = browser.find_element_by_class_name("style-scope ytd-subscribe-button-renderer")
            #subscribe_next_button.click()

            #time.sleep(5)
            #browser.quit()
        except:
            print("Ei")
            #browser.quit()
    else:
        print("Either ID or PASSWORD is null")

    


with open('id_pass.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

print("Total Ids and Passwords: ", len(list_of_rows))
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows

Connecting_To_Browser("Birtoirwin@gmail.com", "Percayadiri2018")
# for i in range(len(ids_pass_list)):
#     id_str = ids_pass_list[i][0]
#     id_pass = ids_pass_list[i][1]
#     print(i)
#     print("Login Id: ", id_str)
#     print("Login Password: ", id_pass)

#     Connecting_To_Browser(id_str, id_pass)
