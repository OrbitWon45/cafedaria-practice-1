from behave import given, when, then


@given('Open the main page')
def open_the_main_page(context):
    context.app.main_page.open_the_main_page()


@when('Scroll down to the footer')
def scroll_down_to_footer(context):
    context.app.main_page.scroll_down_to_footer()


@when('Verify the title Cafedaria in the footer exists')
def verify_the_title_cafedaria_in_footer_exists(context):
    context.app.main_page.verify_the_title_cafedaria_in_footer_exists()


@then('Verify the footer contains a map')
def verify_the_footer_contains_a_map(context):
    context.app.main_page.verify_the_footer_contains_a_map()



