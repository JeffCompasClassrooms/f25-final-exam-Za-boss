from brute import Brute
import pytest
from unittest.mock import patch
from random import seed

@pytest.fixture
def one_try_to_success(mocker):
    mock_random_guess_one_try = mocker.patch.object(Brute, "randomGuess", return_value="abc")

    return mock_random_guess_one_try

@pytest.fixture
def three_tries_to_success(mocker):
    mock_random_guess_three_tries = mocker.patch.object(Brute, "randomGuess", side_effect=["a", "b", "abc"])

    return mock_random_guess_three_tries
@pytest.fixture
def one_thousand_tries_to_success(mocker):
    mock_random_guess_one_thousand_tries = mocker.patch.object(Brute, "randomGuess", side_effect=["x"] * 1000)
    mock_hash = mocker.patch.object(Brute, "hash", side_effect=["y"] + ["x"] * 998 + ["y"])
    return (mock_random_guess_one_thousand_tries, mock_hash)

@pytest.fixture
def ten_million_tries_to_success(mocker):
    mock_random_guess_ten_million_tries = mocker.patch.object(Brute, "randomGuess", side_effect=["x"] * 10000000 + ["y"])
    return mock_random_guess_ten_million_tries
@pytest.fixture
def ten_million_and_one_hash_values(mocker):
    mock_hash = mocker.patch.object(Brute, "hash", side_effect=["y"] + ["x"] * 9999999 + ["y"])
    return mock_hash

def describe_brute_functionality():
    def describe_init_functionality():
        def it_sets_the_correct_hash_target():
            brute = Brute("123")

            assert brute.target == "3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2"
    def describe_brute_once_functionality():
        def it_fails_if_it_cannot_get_it_first_time():
            brute = Brute("abc")
            assert brute.bruteOnce("a") == False
        def it_succeeds_if_it_gets_it_first_time():
            brute = Brute("abc")
            assert brute.bruteOnce("abc") == True
    def describe_brute_many_functionality():
        def it_succeeds_if_it_gets_it_within_attempt_limit(one_thousand_tries_to_success):
            brute = Brute("abc")
            result = brute.bruteMany(limit=1000)

            assert result != -1
        def it_will_fail_if_it_cannot_get_it_in_attempt_limit(ten_million_and_one_hash_values, ten_million_tries_to_success):
            brute = Brute("abc")
            result = brute.bruteMany(limit=1000)

            assert result == -1
        def it_succeeds_without_a_hash_mock(three_tries_to_success):
            brute = Brute("abc")
            result = brute.bruteMany(limit=10)

            assert result != -1
        def it_succeeds_in_a_real_environment_using_a_seeded_environment():
            seed(1)
            brute = Brute("abc")
            result = brute.bruteMany(limit=10000000)

            assert result != -1
        def it_returns_the_time_taken_for_cracking(one_thousand_tries_to_success):
            brute = Brute("abc")
            result = brute.bruteMany(limit=1000)

            assert result >= 0
        def it_instantly_fails_if_limit_is_zero():
            brute = Brute("abc")
            result = brute.bruteMany(limit=0)

            assert result == -1
        def it_instantly_fails_if_limit_is_negative():          
            brute = Brute("abc")
            result = brute.bruteMany(limit=-10)

            assert result == -1
        def it_can_succeed_in_one_try(one_try_to_success):
            brute = Brute("abc")
            result = brute.bruteMany(limit=1)

            assert result != -1