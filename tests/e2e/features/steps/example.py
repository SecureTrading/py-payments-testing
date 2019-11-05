from behave import given, then


@given('I open google.com')
def open_google(context):
    context.driver.get("http://www.google.com")


@then('the title should contain "{title}"')
def title_should_contain(context, title):
    browser_title = context.driver.title
    assert title in browser_title, f'Found "{browser_title}" instead'