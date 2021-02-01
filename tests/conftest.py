from pytest_bdd import given, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from lib.core.sharedDriver import SharedDriver
import allure
import pytest
import time
import os
import pprint

driver_desktop, driver_mobile, _request = None, None, None


def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', dest='base_url')
    parser.addoption('--selenium_server', action='store', dest='selenium_server')
    parser.addoption('--step_with_screenshot', action='store', dest='step_with_screenshot')
    parser.addoption('--extra_timing', action='store', dest='extra_timing')


@pytest.fixture(scope='function')
def init_driver_desktop(request):
    global driver_desktop
    desiredCapabilities = {"browserName": "chrome"}
    driver_desktop = webdriver.Remote(command_executor=request.config.getoption('selenium_server'),
                                        desired_capabilities=desiredCapabilities)
    driver_desktop.step_with_screenshot = request.config.getoption('step_with_screenshot')
    driver_desktop.extra_timing = request.config.getoption('extra_timing')
    driver_desktop.implicitly_wait(25)
    driver_desktop.maximize_window()
    driver_desktop.get(request.config.getoption('base_url'))
    yield driver_desktop
    driver_desktop.quit()


@pytest.fixture(scope='function')
def init_driver_mobile(request):
    global driver_mobile
    mobile_emulation = {

        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},

        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver_mobile = webdriver.Remote(command_executor=request.config.getoption('selenium_server'),options=chrome_options)
    driver_mobile.step_with_screenshot = request.config.getoption('step_with_screenshot')
    driver_mobile.extra_timing = request.config.getoption('extra_timing')
    yield driver_mobile
    driver_mobile.quit()

@pytest.fixture(scope='function')
def init_driver_desktop_proxy(init_driver_desktop,request):
    global _request
    driver=init_driver_desktop
    _request=request
    yield driver


@pytest.fixture(scope='function')
def init_driver_mobile_proxy(init_driver_mobile,request):
    global _request
    driver=init_driver_mobile
    _request=request
    yield driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if 'init_driver_desktop_proxy' in str(_request):
            _driver=driver_desktop
        elif'init_driver_mobile_proxy' in str(_request):
            _driver=driver_mobile

        _driver.save_screenshot("ERROR.png")
        allure.attach.file("ERROR.png", attachment_type=allure.attachment_type.PNG, name='ERROR')
        allure.attach(f'<head></head><body> COOKIES : {_driver.get_cookies()} </body>',
                          'COOKIES', allure.attachment_type.HTML)
        os.system('rm -f ' + "ERROR.png ")
