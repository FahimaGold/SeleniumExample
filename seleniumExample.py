#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pc
#
# Created:     04/04/2020
# Copyright:   (c) pc 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
import sys
import getpass

#Launching Firefox
browser = webdriver.Firefox()
type(browser)

#Getting the email from the commandline
try:
    email = sys.argv[1]
except:
    print("You need to provide an email address please")


#Redirecting the browser to gmail signin page
browser.get('https://mail.google.com/mail/ca/u/0/')

#Getting the input in which the user indicates their email address
emailInput = browser.find_elements_by_id('identifierId')

#Filling up the email input with email address entered  via cmd
emailInput[0].send_keys(email)

#Finding the "Next" button
nextButton = browser.find_element_by_class_name('CwaK9')
nextButton.click()

#Prompting for password
password = getpass.getpass("Type your password:  ")

#Finding the password input
pwdInput = browser.find_element_by_name("password")

#Copy the password into the password input
pwdInput.send_keys(password)

#Simulating click; if password is correct, you'll be signed in to gmail.
nextButton = browser.find_element_by_class_name('CwaK9')
nextButton.click()


