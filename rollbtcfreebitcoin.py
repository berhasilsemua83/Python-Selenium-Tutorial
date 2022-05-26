#! /home/masher2/.venvs/freebitbot/bin/python
import logging
import selenium
import time
from selenium import webdriver
import logging.config
import re
from time import sleep
from unittest import result
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotInteractableException, ElementClickInterceptedException,
    NoSuchElementException
)
from SolveHcaptcha import solveHcaptcha

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'console': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
            'datefmt': '%H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
})
logger = logging.getLogger(__name__)


class FreebitBot:

    def __init__(self):
        logger.info('Initializing FreebitBot.')
        #options = webdriver.ChromeOptions()
        self.driver = uc.Chrome(use_subprocess=True)
        #self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.get('https://freebitco.in/')

        self.deny_notifications()

        # Login
        logger.info('Navigating to the loging screen.')
        self.driver\
            .find_element(By.CLASS_NAME,'login_menu_button')\
            .click()
        self.driver\
            .find_element(By.ID, 'login_form_btc_address')\
            .send_keys('josenabdel@gmail.com')
        self.driver\
            .find_element(By.ID,'login_form_password')\
            .send_keys('Bijaksana2020')
        self.driver\
            .find_element(By.ID,'login_button')\
            .click()       
        logger.info('Wating for the user to log in.')
        self.wait_for_login()

    def wait_for_login(self):
        try:
            self.driver.find_element(By.ID,'login_form_btc_address')
            sleep(5)
            self.wait_for_login()
        except NoSuchElementException:
            logger.info('Successfully logged')

    def deny_notifications(self):
        logger.info('Removing the notification popup')
        try:
            self.driver\
                .find_element(By.CSS_SELECTOR,'div.pushpad_deny_button')\
                .click()
            logger.info('Removed the pop up')
        except ElementNotInteractableException:
            logger.error('Could not remove the notification popup')
        except Exception as e:
            logger.error(f"Unexpected error, retrying.\nThe exception was: {e}")
    
    def tutup_popup(self):
        logger.info('Tutup popup setelah claim')
        try:
            self.driver\
                .find_element(By.XPATH, '//*[@id="myModal22"]/a')\
                .click()
            logger.info('Tutup pop up')
        except ElementNotInteractableException:
            logger.error('ga bisa nutup popup')
        except Exception as e:
            logger.error(f"Unexpected error, retrying.\nThe exception was: {e}")
    
    def claim_btc(self):
        try:
            logger.info('Trying to claim the btc.')
            self.driver.find_element(By.ID,'free_play_form_button').click()
            sleep(5)
            logger.info('BTC Claimed!')
        except Exception:
            sleep(5)
    def urus_hcaptcha(self):
        try:
            result = solveHcaptcha(
                '6ba78ccd-f275-4c2d-be45-5e4b46a4a4d8',
                'https://freebitco.in',
            )

            code = result['code']
            print(code)
            print('hcapctha solve')
            self.driver.execute_script(
                "document.querySelector(" + "'" + '[name="h-captcha-response"]' + "'" + ").innerHTML = " + "'" + code + "'"
            )

            # self.driver.execute_script(
            #     "document.querySelector(" + "'" + '[name="g-recaptcha-response"]' + "'" + ").innerHTML = " + "'" + code + "'"
            # )            
        except:
            return False

    def check(self):
        """ Checks if can claim the BTC
        Returns False if not ready to claim, True otherwise
        """
        try:
            # No internet
            if self.driver.title == 'Server Not Found':
                self.driver.refresh()
                return False

            # Stopped clock
            if re.search('^0m\:0s', self.driver.title):
                self.driver.refresh()
                return False

            # Waiting
            if re.search('^\d{1,2}m\:\d{1,2}s', self.driver.title):
                return False

            # Notification popup
            if self.driver.find_element(By.CSS_SELECTOR,'div.pushpad_deny_button').is_displayed():
                self.deny_notifications()
                return False

            # Are we ready?
            ready = self.driver.find_element(By.ID,'free_play_form_button').is_displayed()
            if ready:
                # Scrolling to bottom
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                print('scroll ke bawah')
                time.sleep(100)
                # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                #     (By.CSS_SELECTOR, '#free_play_recaptcha > form > div > iframe')))
                #self.driver.switch_to.frame(1)
                #self.driver.find_element(By.ID,'checkbox').click()
                #self.driver.find_element(By.CSS_SELECTOR, ".label-container").click()
                #print('klik box')
                #self.driver.switch_to.default_content()
                #self.urus_hcaptcha()
            return ready

        except Exception:
            return False

    def main(self):
        while True:
            if self.check():
                self.claim_btc()
                sleep(3)
                self.tutup_popup()
            else:
                sleep(10)


if __name__ == '__main__':
    bot = FreebitBot()
    bot.main()
