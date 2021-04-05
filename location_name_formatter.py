#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# In[2]:


class LocationNameFormatter:
    
    '''
        Can be used to format a location name and return the actual name of a location from Google Map
    '''
    
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(options=chrome_options )
    browser.implicitly_wait(5)

    browser.get(r'''https://www.google.com/maps/@23.8698828,90.3842619,15z?hl=en''')
   
    def __init__(self):
        
        time.sleep(5)
    def formatter(self,name,
                  input_xpath="//input[@id='searchboxinput']",
                  output_xpath="section-hero-header-title-title.gm2-headline-5"
                 ):      
        '''
            Args:
                name: Takes a string of location name which is expected to be formatted
                
                input_xpath: Takes a string of xpath of google map search input box. 
                              Search box input element xpath can be changed from time to time. 
                              So xpath can be passed through this parameter.
                              
                output_xpath: Takes a string of xpath of the formatted title element of the given name. 
                              Title element xpath can be changed from time to time. 
                              So xpath can be passed through this parameter. 
            Return:
                formatted_str : Returns formatted name string
                
        '''
        formatted_str = name
        #em = self.browser.find_element_by_xpath("//input[@name='q']")
        em = self.browser.find_element_by_xpath(input_xpath)
        
        em.clear()
        em.send_keys(name)
        from selenium.webdriver.common.keys import Keys
        em.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            div = self.browser.find_elements_by_class_name(output_xpath)

            for it in div:
                #print(it)
                try:
                    #print(it.text)
                    formatted_str = it.text
                    return formatted_str 
                except:
                    print("not found")
        except: 
            print("error")
        return formatted_str
    
    
    

