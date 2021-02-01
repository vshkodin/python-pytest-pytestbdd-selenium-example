from pytest_bdd import scenarios, given, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure
import time
import os
import random
import string


class SharedDriver:
    def __init__(self,driver):
        self.driver=driver

    def _driver_wait_locate_element(self, LOCATOR, BY):
        if BY == "ID":
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, LOCATOR)))
            elem = self.driver.find_element_by_id(LOCATOR)

        elif BY == "XPATH":
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, LOCATOR)))
            elem = self.driver.find_element_by_xpath(LOCATOR)

        elif BY == "CSS_SELECTOR":
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOCATOR)))
            elem = self.driver.find_element_by_css_selector(LOCATOR)

        elif BY == "CLASS_NAME":
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, LOCATOR)))
            elem = self.driver.find_element_by_class_name(LOCATOR)

        elif BY == "LINK_TEXT":
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, LOCATOR)))
            elem = self.driver.find_element_by_link_text(LOCATOR)

        return elem

    def _driver_wait_locate_elements(self, LOCATOR, BY):
        if BY == "ID":
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.ID, LOCATOR)))
            elems = self.driver.find_elements_by_id(LOCATOR)

        elif BY == "CSS_SELECTOR":
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, LOCATOR)))
            elems = self.driver.find_elements_by_css_selector(LOCATOR)

        elif BY == "XPATH":
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, LOCATOR)))
            elems = self.driver.find_elements_by_xpath(LOCATOR)

        elif BY == "CLASS_NAME":
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, LOCATOR)))
            elems = self.driver.find_elements_by_class_name(LOCATOR)

        elif BY == "LINK_TEXT":
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.LINK_TEXT, LOCATOR)))
            elem = self.driver.find_elements_by_link_text(LOCATOR)

        return elems

    def _take_screenshots(self):
        if self.driver.step_with_screenshot == "True":
            time.sleep(int(self.driver.extra_timing))
            self.driver.save_screenshot("screenshot.png")
            allure.attach.file("screenshot.png", attachment_type=allure.attachment_type.PNG)
            os.system('rm -f ' + "screenshot.png")
        else: time.sleep(2)

    def _get(self,URL):
        self.driver.get(URL)
        self._take_screenshots()

    def _validate_page_source(self, PATTERN):
        time.sleep(int(self.driver.extra_timing))
        source = self.driver.page_source
        if PATTERN in source: self._take_screenshots()
        else: raise AssertionError(f'{PATTERN} pattern not match source code {source}')

    def _validate_is_displayed(self, LOCATOR, BY):
        time.sleep(int(self.driver.extra_timing))
        try:
            assert self._driver_wait_locate_element(LOCATOR, BY).is_displayed()
            self._take_screenshots()
        except AssertionError:
            assert self._driver_wait_locate_element(LOCATOR, BY).is_displayed()
            self._take_screenshots()

    def _click(self, LOCATOR, BY):
        time.sleep(int(self.driver.extra_timing))
        try:
            self._driver_wait_locate_element(LOCATOR, BY).click()
            self._take_screenshots()
        except:
             self._driver_wait_locate_element(LOCATOR, BY).click()
             self._take_screenshots()

    def _send_keys(self, LOCATOR, BY, STRING):
        time.sleep(int(self.driver.extra_timing))
        try:
            self._driver_wait_locate_element(LOCATOR, BY).send_keys(STRING)
            self._take_screenshots()
        except:
            self._driver_wait_locate_element(LOCATOR, BY).send_keys(STRING)
            self._take_screenshots()


    def _hit_enter(self, LOCATOR, BY):
        time.sleep(int(self.driver.extra_timing))
        self._driver_wait_locate_element(LOCATOR, BY).send_keys(Keys.ENTER)
        self._take_screenshots()

    def _click_on_random_element_from_the_list(self, LOCATOR, BY):
        time.sleep(int(self.driver.extra_timing))
        list_of_elemnts = self._driver_wait_locate_elements(LOCATOR, BY)
        click_on = random.choice(list_of_elemnts)
        click_on.click()
        self._take_screenshots()

    def _click_on_specific_element_from_the_list(self, LOCATOR, BY, NUM):
        time.sleep(int(self.driver.extra_timing))
        list_of_elemnts = self._driver_wait_locate_elements(LOCATOR, BY)
        list_of_elemnts[int(NUM)].click()
        self._take_screenshots()

    def _validate_text(self, LOCATOR, BY, STRING):
        time.sleep(int(self.driver.extra_timing))
        try:
            validate = (self._driver_wait_locate_element(LOCATOR, BY).text)
            assert validate == STRING
            self._take_screenshots()
        except AssertionError:
            #time.sleep(3)
            validate = (self._driver_wait_locate_element(LOCATOR, BY).text)
            assert validate == STRING
            self._take_screenshots()

    def _refresh_page(self):
        time.sleep(int(self.driver.extra_timing))
        self.driver.refresh()
        self._take_screenshots()

    def _execute_script(self, SCRIPT):
        time.sleep(int(self.driver.extra_timing))
        self.driver.execute_script(SCRIPT)
        #time.sleep(2)
        self._take_screenshots()

    def _validate_url(self, PATTERN):
        time.sleep(int(self.driver.extra_timing))
        URL=self.driver.current_url
        if PATTERN in URL:
            self._take_screenshots()
        else: raise AssertionError(f'{PATTERN} pattern not in {URL}')

    def _switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self._take_screenshots()

    def _validate_title(self, PATTERN):
        time.sleep(int(self.driver.extra_timing))
        title=self.driver.title
        if PATTERN in title:
            self._take_screenshots()
        else: raise AssertionError(f'{PATTERN} pattern not in {title}')

    def _get_cookie_and_assert(self, COOKIE, PATTERN):
        time.sleep(int(self.driver.extra_timing))
        get_cookie = self.driver.get_cookie(COOKIE)
        if PATTERN in str(get_cookie):
            self._take_screenshots()
        else: raise AssertionError(f'{PATTERN} not in {get_cookie}')

    def _clean_cookies(self): self.driver.delete_all_cookies()


    def _send_keys_random_email(self, LOCATOR, BY):
        time.sleep(int(self.driver.extra_timing))
        fakegmail=(''.join(random.choice(string.ascii_letters) for x in range(20)) + '@gmail.com')
        self._driver_wait_locate_element(LOCATOR, BY).send_keys(fakegmail)
        self._take_screenshots()

    def _time_wait(self, num): time.sleep(int(num))

    def _check_javascript_errors(self):
        output = []
        for entry in self.driver.get_log('browser'):
            if entry['source'] == 'javascript': output.append(entry)
        if output != []: raise AssertionError(f"{output}")

    def _page_down(self):
        time.sleep(int(self.driver.extra_timing))
        self._driver_wait_locate_element("body", "CSS_SELECTOR").send_keys(Keys.PAGE_DOWN)
        self._take_screenshots()

    def _get_attribute_and_compare(self, LOCATOR, BY, PATTERN, ATTRIBUTE):
        elem = self._driver_wait_locate_element(LOCATOR,BY)
        _attribute= elem.get_attribute(ATTRIBUTE)
        if PATTERN in _attribute: self._take_screenshots()
        else: raise AssertionError(f'{PATTERN} not in {_attribute}')
