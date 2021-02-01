from pytest_bdd import scenarios, given, then, parsers
import allure, time
from lib.core.sharedDriver import SharedDriver

scenarios('')


@given("Open base url desktop view")
def open_base_url_desktop(init_driver_desktop_proxy,request):
    global _driver
    init_driver_desktop_proxy.get(request.config.getoption('base_url'))
    _driver=init_driver_desktop_proxy


@given("Open base url mobile view")
def open_base_url_mobile(init_driver_mobile_proxy,request):
    global _driver
    init_driver_mobile_proxy.get(request.config.getoption('base_url'))
    _driver=init_driver_mobile_proxy


@then(parsers.parse('Open Page "{URL}"'))
def _open_page(request, URL):
    with allure.step('Open Page : mobile view '+ str(request.config.getoption('base_url'))+str(URL)):
        SharedDriver(_driver)._get(f"{request.config.getoption('base_url')}{URL}")


@then(parsers.parse('Validate source with "{PATTERN}"'))
def _validate_source(PATTERN):
    with allure.step(f'Validate source with "{PATTERN}"'):
        SharedDriver(_driver)._validate_page_source(PATTERN)


@then(parsers.parse('Validate element is presented "{LOCATOR}", By "{BY}"'))
def _validate_displayed(LOCATOR, BY):
    with allure.step(f'Validate element is presented LOCATOR : {LOCATOR}, By : {BY}'):
        SharedDriver(_driver)._validate_is_displayed(LOCATOR, BY)


@then(parsers.parse('Click on "{LOCATOR}", By "{BY}"'))
def _click(LOCATOR, BY):
    with allure.step(f"Click BY : {BY} LOCATOR: {LOCATOR}"):
        SharedDriver(_driver)._click(LOCATOR,BY)


@then(parsers.parse('In field "{LOCATOR}" type "{STRING}", By "{BY}"'))
def _send_keys(LOCATOR, BY, STRING):
    with allure.step(f"Send Keys by : {BY} LOCATOR: {LOCATOR}  TYPE : {STRING}"):
        SharedDriver(_driver)._send_keys(LOCATOR, BY, STRING)


@then(parsers.parse('Hit Enter Button "{LOCATOR}", By "{BY}"'))
def _hit_enter(LOCATOR, BY):
    with allure.step(f'Hit Enter Button LOCATOR {LOCATOR}, By : {BY}'):
        SharedDriver(_driver)._hit_enter(LOCATOR, BY)


@then(parsers.parse('Click on random element from the list "{LOCATOR}", By "{BY}"'))
def _click_on_random_element_from_the_list(LOCATOR, BY):
    with allure.step(f"Click on random element from the list LOCATOR : {LOCATOR}, By : {BY}"):
        SharedDriver(_driver)._click_on_random_element_from_the_list(LOCATOR, BY)


@then(parsers.parse('Validate text "{LOCATOR}", "{STRING}", By "{BY}"'))
def _validate_text(LOCATOR, BY, STRING):
    with allure.step(f'Validate text LOCATOR : {LOCATOR}, STRING : {STRING}, By  : {BY}'):
        SharedDriver(_driver)._validate_text(LOCATOR, BY, STRING)


@then(parsers.parse('Refresh page'))
def _refresh_page():
    with allure.step('Refresh page'):
        SharedDriver(_driver)._refresh_page()


@then(parsers.parse('Execute script "{SCRIPT}"'))
def _execute_script(SCRIPT):
    with allure.step(f'Execute script {SCRIPT}'):
        SharedDriver(_driver)._execute_script(SCRIPT)


@then(parsers.parse('Validate current url with "{PATTERN}"'))
def _validate_url(PATTERN):
    with allure.step(f'validate current url with {PATTERN}'):
        SharedDriver(_driver)._validate_url(PATTERN)


@then(parsers.parse('Validate current title with "{PATTERN}"'))
def _validate_title(PATTERN):
    with allure.step(f'Validate current title with {PATTERN}'):
        SharedDriver(_driver)._validate_title(PATTERN)


@then(parsers.parse('Switch tab'))
def _switch_tab():
    with allure.step(f'Switch tab'):
        SharedDriver(_driver)._switch_tab()

@then(parsers.parse('Get cookie "{COOKIE}" and assert "{PATTERN}"'))
def _get_cookie_and_assert(COOKIE, PATTERN):
    with allure.step(f'Get cookie "{COOKIE}" and assert "{PATTERN}"'):
        SharedDriver(_driver)._get_cookie_and_assert(COOKIE, PATTERN)

@then(parsers.parse('Clean Cookies'))
def _clean_cookies():
    with allure.step(f'Clean Cookies'):
        SharedDriver(_driver)._clean_cookies()

@then(parsers.parse('Wait "{SEC}"'))
def _time_wait(SEC):
    with allure.step(f'Wait "{SEC}"'):
        SharedDriver(_driver)._time_wait(SEC)


@then(parsers.parse('In field "{LOCATOR}" type random gmail, By "{BY}"'))
def _send_keys_random(LOCATOR, BY):
    with allure.step(f'In field "{LOCATOR}" type random gmail, By "{BY}"'):
        SharedDriver(_driver)._send_keys_random_email(LOCATOR, BY)

@then(parsers.parse('Check JS errors'))
def _check_js_errors():
    with allure.step(f'Check JS errors'):
        SharedDriver(_driver)._check_javascript_errors()

@then(parsers.parse('Page Down'))
def _page_down():
    with allure.step(f'Page Down'):
        SharedDriver(_driver)._page_down()

@then(parsers.parse('Click on specific element from the list "{LOCATOR}", By "{BY}", Num "{NUM}"'))
def _click_on_specific_element_from_the_list(LOCATOR, BY, NUM):
    with allure.step(f'Click on specific element from the list "{LOCATOR}", By "{BY}", Num "{NUM}"'):
        SharedDriver(_driver)._click_on_specific_element_from_the_list(LOCATOR, BY, NUM)\

@then(parsers.parse('Get attribute "{ATTRIBUTE}" of element "{LOCATOR}", by "{BY}" and validate attribute with "{PATTERN}"'))
def _get_attribute_and_compare(LOCATOR, BY, PATTERN,ATTRIBUTE):
    with allure.step(f'Get attribute "{ATTRIBUTE}" of element "{LOCATOR}", by "{BY}" and validate attribute with "{PATTERN}"'):
        SharedDriver(_driver)._get_attribute_and_compare(LOCATOR, BY, PATTERN, ATTRIBUTE)
