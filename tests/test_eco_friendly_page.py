def test_click_on_sale_link(eco_friendly_page):
    eco_friendly_page.open_page()

    eco_friendly_page.click_on_sale_link()

    eco_friendly_page.check_is_this_sale_page()


def test_click_on_random_product(eco_friendly_page):
    eco_friendly_page.open_page()

    eco_friendly_page.click_random_product()

    eco_friendly_page.check_is_this_random_product_page()


def test_click_on_sing_in_link(eco_friendly_page):
    eco_friendly_page.open_page()

    eco_friendly_page.click_on_sign_in_link()

    eco_friendly_page.check_is_this_sign_in_page()
