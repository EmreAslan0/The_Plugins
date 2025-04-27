import pytest
import allure

@allure.feature("Login Feature")
@allure.story("User can log in with valid credentials")
def test_login_success():
    with allure.step("Open login page"):
        pass

    with allure.step("Enter username"):
        pass

    with allure.step("Enter password"):
        pass

    with allure.step("Click login button"):
        assert 1 == 1
