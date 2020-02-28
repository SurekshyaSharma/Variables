import pytest
import revstr


#  Importing the main file


def test_string_apple():
    assert "elppa" == revstr.reverse("apple")
    # assert (the value it has to be) == Testfile.functionName


def test_string_apple():
    assert "madam" == revstr.reverse("madam")


def test_string_apple():
    assert "olleh" == revstr.reverse("hello")


def test_string_apple():
    assert "redder" == revstr.reverse("redder")


def test_string_apple():
    assert "yppah" == revstr.reverse("happy")


def test_string_apple():
    assert "rts" == revstr.reverse("str")


def test_string_apple():
    assert "00000" == revstr.reverse("00000")


def test_string_apple():
    assert "--++**" == revstr.reverse("**++--")


def test_string_apple():
    assert "yam" == revstr.reverse("may")


def test_string_apple():
    assert "DDA###" == revstr.reverse("###ADD")
