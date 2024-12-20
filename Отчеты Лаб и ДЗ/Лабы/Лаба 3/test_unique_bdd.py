from unique import Unique
from pytest_bdd import given, when, then, scenario

@scenario("unique.feature", "Remove duplicates from a list of integers")
def test_unique_integers():
    pass

@scenario("unique.feature", "Remove duplicates from a case-sensitive list of strings")
def test_unique_strings_case_sensitive():
    pass

@scenario("unique.feature", "Remove duplicates from a case-insensitive list of strings")
def test_unique_strings_ignore_case():
    pass

@given("a list of integers with duplicates")
def data_integers():
    return [1, 1, 2, 2, 3, 3]

@given("a case-sensitive list of strings with duplicates")
def data_strings_case_sensitive():
    return ['a', 'A', 'b', 'B']

@given("a case-insensitive list of strings with duplicates")
def data_strings_ignore_case():
    return ['a', 'A', 'b', 'B']

@when("we create a Unique iterator for integers")
def unique_integers(data_integers):
    return list(Unique(data_integers))

@when("we create a Unique iterator for case-sensitive strings")
def unique_strings_case_sensitive(data_strings_case_sensitive):
    return list(Unique(data_strings_case_sensitive))

@when("we create a Unique iterator for case-insensitive strings")
def unique_strings_ignore_case(data_strings_ignore_case):
    return list(Unique(data_strings_ignore_case, ignore_case=True))

@then("the result should only contain unique integers")
def verify_unique_integers(unique_integers):
    assert unique_integers == [1, 2, 3]

@then("the result should only contain unique case-sensitive strings")
def verify_unique_strings_case_sensitive(unique_strings_case_sensitive):
    assert unique_strings_case_sensitive == ['a', 'A', 'b', 'B']

@then("the result should only contain unique case-insensitive strings")
def verify_unique_strings_ignore_case(unique_strings_ignore_case):
    assert unique_strings_ignore_case == ['a', 'b']
