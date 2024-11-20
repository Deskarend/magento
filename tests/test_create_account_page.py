def test_create_account(create_account, first_name, last_name, email, password):
    create_account.open_page()
    create_account.create_account(first_name, last_name, email, password, password)

    create_account.check_creating_new_account()


def test_fill_incorrect_email(create_account):
    create_account.open_page()
    incorrect_email = "Incorrect_email"

    create_account.fill_email(incorrect_email)
    create_account.click_create_account()

    create_account.check_is_there_email_error()


def test_fill_different_passwords(create_account, password):
    create_account.open_page()
    a_different_password = 'Another' + password

    create_account.fill_password(password)
    create_account.fill_confirm_password(a_different_password)
    create_account.click_create_account()

    create_account.check_is_there_confirm_error()
