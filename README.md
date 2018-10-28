
# web_tester

A simple selenium extension which contains Browser class with methods defining different actions can be performed on the web elements.

## Development purpose

---

- The goal of web tester is to reduce the code complexities for developing a testing script that should test if your web applications is working fine.
- When ever a developer or designer make a changes to your web application. Testing needs to be performed for all the elements of your web.
- After every change you may need to add or modify a lengthy selenium code.
- Number of Exceptions are needed to be handled for each action.
- web_tester handles all those and continous with checking all the elements.

## Actions Available

---

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

## Example

---

``` python
# Example for IE
from web_tester.browser import Browser

driver_location = "/path/to/IEdriver.exe" #or "/path/to/selenium_headless_ie.exe"

browser = Browser(driver_location,"IE")

browser.open_url('https://github.com/vishnu-chegondi/')
action = browser.click_element('//*[@id="js-pjax-container"]/div/div[2]/div[3]/div[1]/div/ol/li[3]/span/span/a',"Unable to navigate to project")

```