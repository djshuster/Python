# Last updated 7 July, 2020
# Created by David Shuster

'''
This program uses data from Sperling's Best Places (bestplaces.net) to create a CSV file with
"the overall cost of living for an area where 100 equals the national average." In our case,
 the data we examined is the county-level cost of living score.

However, it should be noted that, in each state, only the scores of the 100 counties with the highest COL were examined.
Thus a few states did not receive complete information, namely the following:
[Number of counties- State]
254– Texas
159– Georgia
134– Virginia
120– Kentucky
115– Missouri
105– Kansas
102– Illinois
Source: https://simple.wikipedia.org/wiki/County_(United_States)
[This program also covers data for the District of Columbia.]

The approach is a fairly brute-force approach and would need to be altered for different screen sizes, etc.
(This was done largely to experiment with pynput.)
'''

#TODO Remove unused modules
import webbrowser
import pynput
from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyboardController
import time
from bs4 import BeautifulSoup
import requests
import csv
import win32clipboard

# from pywinauto.application import Application
# app = Application().start("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

mouse = mouseController()
kb = keyboardController()

def buildAnotherList():
    mouse.position = (188, 474)
    mouse.click(Button.left, 1)
    time.sleep(2)

    mouse.position = (387, 540)
    mouse.scroll(0, -10)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    kb.press(Key.down)
    kb.release(Key.down)
    mouse.move(0, 40)
    mouse.click(Button.left, 1)

def outputRawText(f):
    time.sleep(2)
    kb.press(Key.ctrl)
    kb.press('a')
    kb.release('a')
    kb.press('c')
    kb.release('c')
    kb.release(Key.ctrl)
    time.sleep(1)
    win32clipboard.OpenClipboard()
    rawText = win32clipboard.GetClipboardData()
    f.write(rawText)
    win32clipboard.CloseClipboard()

def processRawText():
    csv_file = open("COL_by_county.csv", 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['County Name', 'COL Score'])

    f = open("raw_text.txt", "r")
    useful = False
    for line in f.readlines():
        if useful:
            if line=='States with the Best Air Quality\n':
                useful=False
            elif line != '\n':
                entry = line.strip().split('\t')
                csv_writer.writerow([entry[0],entry[1]])

        else:
            if line=='Cost of Living\tCounty\tMetro\tState\tUnited States\n':
                useful=True

    csv_file.close()
    f.close()


def main():
    f = open("raw_text.txt", "w")

    # Start with Alaska loaded
    time.sleep(2)
    outputRawText(f)

    for i in range(0,50):
        time.sleep(2)
        buildAnotherList()
        outputRawText(f)

    f.close()
    processRawText()

if __name__ == '__main__':
    main()




'''
ACKNOWLEDGEMENTS

Thanks to "Nitratine" (https://www.youtube.com/watch?v=2BXr9U6ZL8Y,
https://nitratine.net/blog/post/simulate-keypresses-in-python/) for the great tutorials.

Thanks to https://www.bestplaces.net/tools/ for the data.
'''