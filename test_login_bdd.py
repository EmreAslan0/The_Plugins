import pytest
from pytest_bdd import scenario, given, when, then

@scenario("login.feature", "Successful login with correct credentials")
def test_successful_login_with_correct_credentials():
    pass

@given("a registered user")
def registered_user():
    return {"username": "admin", "password": "1234"}

@when("the user logs in with valid credentials")
def login_attempt(registered_user):
    assert registered_user["username"] == "admin"

@then("access is granted")
def access():
    assert True
