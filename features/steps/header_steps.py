from behave import given, when, then


@when('Verify the title Cafedaria exists on the navigation bar')
def verify_title_cafedaria_exists_on_nav_bar(context):
    context.app.header_page.verify_title_cafedaria_exists_on_nav_bar()


@when('Verify there are {expected_amount} sub-titles in the navigation bar and all of them are clickable')
def verify_6_subtitles_are_in_nav_bar_and_are_clickable(context, expected_amount):
    context.app.header_page.verify_subtitles_are_in_nav_bar_and_are_clickable(expected_amount)


@then('Verify the cart and search icons exists')
def verify_the_cart_and_search_icons_exist(context):
    context.app.header_page.verify_the_cart_and_search_icons_exist()



