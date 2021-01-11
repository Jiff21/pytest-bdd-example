'''An Example test using Selenium browser.'''
from functools import partial
from pytest_bdd import scenarios, given, when, then, parsers
from qa.steps.environment import context, driver
from qa.config.conftest import PAGES_DICT


# Set steps for multiple scenarios, also relative to path set in pytest.ini
scenarios(
    'browser_example.feature',
    'about.feature'
)

@given(parsers.parse("I get the {page_name} page"))
@when(parsers.parse("I get the {page_name} page"))
def get(context, driver, page_name):
    context.current_url = context.human_readable_pages(page_name, context.host)
    context.driver.get(context.current_url)

@then(parsers.parse('I should be on {expected_page}'))
def assert_page(context, driver, expected_page):
    assert context.host in context.driver.current_url, \
    'expected {expected_host} to be in {current_host}'.format(
        expected_host=context.host,
        current_host=context.driver.current_url
    )
