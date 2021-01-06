import re
import requests
from pytest_bdd import scenario, given, when, then, parsers
from environment import context, client, driver

@scenario(
    'test_browser_example.feature',
    'Browser can get correct page',
)
def test_publish():
    pass


@given(
    parsers.parse("I get the {page_name} page"),
    target_fixture="page_name"
)
def get(context, driver, page_name):
    context.page_name = page_name.lower()
    context.current_url = '{host}{uri}'.format(
        host=context.host,
        uri=context.page_name
    )
    context.driver.get(context.current_url)

@then(parsers.parse('I should be on {expected_page}'))
def assert_page(context, driver, expected_page):
    assert context.host is context.driver.current_url, \
    'expected {expected_host} to be in {current_host}'.format(
        expected_host=context.host,
        current_host=context.driver.current_url
    )
