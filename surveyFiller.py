# Last updated 18 October, 2020
# Created by David Shuster

# This program automatically fills out the Amherst College Health Status Update survey to get a GREEN result.
# Please run this program only if the program's specified answers are accurate.
# Note that this program will only work if you are logged into your Amherst account in your Chrome profile's default
# settings and have Chrome closed when the program starts running.

from selenium import webdriver
import time

def main():
    # TODO: add your own path to your downloaded Chrome driver here.
    chromePath = r"C:\Users\djssh\Documents\Programming\Python\chromedriver\chromedriver.exe"
    # TODO: add your own survey link below.
    websitePath = "https://docs.google.com/forms/d/e/1FAIpQLSesp35CGcGMT_b3HC2XAdYuzfmmnynidhFJSgZfDIOTBivm_A/viewform"

    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation']);

    # TODO: add your Chrome user data directory here.
    userDataPath = "user-data-dir=/Users/djssh/AppData/Local/Google/Chrome/User Data"

    option.add_argument(userDataPath)
    browser = webdriver.Chrome(executable_path=chromePath, options=option)
    browser.get(websitePath)

    time.sleep(0.5)

    #Are you staying in College-provided housing? *
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobuttons[0].click()
    next = browser.find_element_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next.click()

    #Travel
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobuttons[0].click()
    next = browser.find_elements_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next[1].click()

    #Safety Training
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobuttons[0].click()
    next = browser.find_elements_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next[1].click()

    #Testing Program Participation
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobuttons[0].click()
    next = browser.find_elements_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next[1].click()

    #In the last 24 hours, have you had any signs of fever or a measured temperature above 100.3 degrees?
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobuttons[1].click()
    next = browser.find_elements_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next[1].click()

    #Have you had any close contact with a person diagnosed with COVID–19 in the last 14 days?
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobuttons[1].click()
    next = browser.find_elements_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next[1].click()

    #Have you had two (2) or more of these symptoms in the past 14 days?
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobuttons[1].click()
    next = browser.find_elements_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next[1].click()

    #Your status is GREEN. Welcome!
    radiobutton = browser.find_element_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radiobutton.click()
    next = browser.find_elements_by_class_name("freebirdFormviewerViewNavigationNoSubmitButton")
    next[1].click()

    #Submit
    submitbuttons = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    submitbuttons[1].click()
    time.sleep(1)
    browser.quit()

if __name__ == "__main__":
    main()