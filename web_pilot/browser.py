''' browser.py: Description of what browser contains

This creates a class of Browser which contains browser
actions performed on the elements of Web as methods
'''

__author__ = "Vishnu Chegondi"
__status__ = "Development"
__created__ = "30/01/2018"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Browser():
    '''
    This class holds all the actions that can be performed on the
    web browser
    Inputs:
        driver_path: Specifies the location of the executable driver
                     location
        Browser Type: Defines the browser, supports
                    - Chrome
                    - FireFox
                    - IE
    '''

    def __init__(self,driver_path,browser_type):
        if browser_type=='IE':
            self.psuedo_browser = webdriver.Ie(driver_path)
        elif browser_type=='Chrome':
            self.psuedo_browser = webdriver.Chrome(driver_path)
        elif browser_type=='Firefox':
            self.psuedo_browser = webdriver.Firefox(driver_path)
        else:
            raise IOError("Invalid browser_type")

    def open_url(self,url):
        '''
        Loads the web page of url provided
        '''
        self.psuedo_browser.get(url)
    
    def fetch_element(self, xpath, error="Element not found"):
        '''
        Fetches the element waiting for maximum of 10 secs
        xpath: xpath of the element which is to be fetched
        error: Error to return if element is not found
        Success: returns element
        '''
        try:
            element = WebDriverWait(self.psuedo_browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        except Exception as _:
            return error
    
    def click_element(self, xpath, error="Unable to click on element"):
        '''
        xpath: xpath of the element which is to be clicked
        error: Error to return if unable to click
        success: returns ActionPerformed
        '''
        element = self.fetch_element(xpath)
        if isinstance(element, str):
           return element
        else:
            try:
                element.click()
                return "ActionPerformed"
            except Exception as _:
                return error

    def hover_over_element(self, xpath, error = "Unable to hover over element"):
        '''
        xpath: xpath of the element on which cursor is to be moved on
        error: Error to return if unable to click
        success: returns ActionPerformed
        '''
        element = self.fetch_element(xpath)
        if isinstance(element, str):
            return element
        else:
            try:
                cursor = ActionChains(self.psuedo_browser)
                cursor.move_to_element(element).perform()
                return "ActionPerformed"
            except Exception as _:
                return error
    
    def switch_frame(self, xpath, error):
        '''
        xpath: iframe xpath must be provided if default given
                switches to default frame
        error: Error to return if unable to switch frame
        success: returns ActionPerformed
        '''
        if xpath == "default":
            self.psuedo_browser.switch_to_default_content()
        else:
            element = self.fetch_element(xpath)
            if isinstance(element, str):
                return "Unable to find the frame"
            else:
                try:
                    self.psuedo_browser.switch_to.frame(element)
                    return "ActionPerformed"
                except Exception as _:
                    return error
    
    def enter_input(self, xpath, value):
        '''
        xpath: Input tag xpath must be provided
        value: Value to be entered
        error: Exception is catched and retuned
        success: returns ActionPerformed
        '''
        element = self.fetch_element(xpath)
        if isinstance(element, str):
            return element
        else:
            try:
                self.psuedo_browser.execute_script("arguments[0].setAttribute('value',arguments[1])",element, value)
            except Exception as e:
                return "Error is {}".format(e)
    
    def  handle_alert(self, alertdata, accept=True):
        '''
        alertdata: This is the data populated on the alert box
        accept: default accepts the alerts
        success: returns ActionPerformed
        '''
        try:
            WebDriverWait(self.psuedo_browser, 5).until(EC.alert_is_present(),alertdata)
            if accept:
                self.psuedo_browser.switch_to_alert.accept()
            else:
                self.psuedo_browser.switch_to_alert.dismiss()
            return "ActionPerformed"
        except Exception as e:
            return "Error is {}".format(e)

    def fetch_all_elements(self, xpath, error="Element not found"):
        '''
        Fetches all the elements matches for the given xpath
        xpath: xpath of the elements which are to be fetched
        error: Error to return if element is not found
        Success: returns elements
        '''
        try:
            elements = WebDriverWait(self.psuedo_browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            return elements
        except Exception as _:
            return error
    
    def close_browser(self):
        '''
        Closes the browser
        '''
        try:
            self.psuedo_browser.quit()
            return "ActionPerformed"
        except Exception as e:
            return "Error in closing browser : {}".format(e)
