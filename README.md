
# web_pilot

A simple selenium extension which contains Browser class with methods defining different actions can be performed on the web elements.

## Development purpose

- The goal of web pilot is to reduce the code complexities for developing a testing script that should test if your web applications is working fine.
- When ever a developer or designer make a changes to your web application. Testing needs to be performed for all the elements of your web.
- After every change you may need to add or modify a lengthy selenium code.
- Number of Exceptions are needed to be handled for each action.
- web_pilot handles all those and continous with checking all the elements.

## Actions Available

- open_url
- fetch_element
- click_element
- hover_over_element
- switch_frame
- enter_input
- handle_alert
- fetch_all_elements

## Installation

python setup.py install

## Drivers

For headless mode which can be used for automate the testing I prefer using [headless_ie_selenium](https://github.com/kybu/headless-selenium-for-win/releases) driver.

>This is for windows only.

## Example

``` python
# Example for IE
from web_pilot.browser import Browser

driver_location = "/path/to/IEdriver.exe" #or "/path/to/selenium_headless_ie.exe"

browser = Browser(driver_location,"IE")

browser.open_url('https://selenium-python.readthedocs.io/')
action = browser.click_element('//*[@id="selenium-with-python"]/div[2]/ul/li[1]/a',"Unable to click on element")
if action == "ActionPerformed":
    print ("Opened Docs for python selenium")

# browser.psuedo_browser.quit()
```