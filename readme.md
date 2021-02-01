### Example of UI Testing Framework with screenshots and Report using Python, Pytest, Pytest-BDD,  Selenium, Doker, and Allure.

##### CLone repo:
```
git clone 
cd 
```

##### Build Docker container:
```
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm  selenium/standalone-chrome:3.141.59-xenon
```
#### collect all tests
```
python -m pytest --collect-only -q
```
#### Running one test
```
python -m pytest --alluredir=report --base_url https://swapi.dev \
                           --selenium_server http://localhost:4444/wd/hub \
                           --extra_timing 2 \
                           --step_with_screenshot True \
                           tests/test_dynamic/test_dynamic.py::test_any_name_test
```
#### Running all tests
```
python -m pytest --alluredir=report \
                           --base_url https://swapi.dev \
                           --selenium_server http://localhost:4444/wd/hub \
                           --extra_timing 2 \
                           --step_with_screenshot True \
                           tests
```
##### How to add UI tests
Open "/tests/features/*.feature" file and Create new
Scenario with shared given statements "Open base url desktop view" or
"Open base url mobile view" you also can create new (.feture) file.
Please use predefined statements, see the statements below.
```
    Usage: "Given"
        Open base url desktop view
        Open base url mobile view
    Allowed statements: "Then"
        Open Page "/URL"
        Validate source with "PATTERN"
        Validate element is presented "LOCATOR", By "BY"
        Click on "LOCATOR", By "BY"
        In field "LOCATOR" type "STRING", By "BY"
        Hit Enter Button "LOCATOR", By "BY"
        Click on random element from the list "LOCATOR_LIST", By "BY"
        Validate text "LOCATOR", "STRING", By "BY"
        Refresh page
        Execute script "SCRIPT"
        Validate current url with "PATTERN"
        Validate current title with "PATTERN"
        Switch tab
        Get cookie "COOKIE" and assert "PATTERN"
        Clean Cookies
        Wait "SEC"
        Then Click on specific element from the list "LOCATOR", By "BY", Num "NUM"
        Check JS errors
        Page Down
        In field "LOCATOR" type random gmail, By "BY"
        Get attribute "ATTRIBUTE" of element "LOCATOR", by "BY" and validate attribute with "PATTERN"
    Allowed type locators : CSS_SELECTOR, ID, XPATH, CLASS_NAME, LINK_TEXT
 ```
