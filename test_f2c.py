import pytest
import ftoc


def test_32():
    assert 0.0 == ftoc.f2c(32.0)


def test_minus_32():
    assert -35.56 == ftoc.f2c(-32.0)


def test_100():
    assert 37.78 == ftoc.f2c(100.0)


def test_minus_100():
    assert -73.33 == ftoc.f2c(-100.0)


def test_1():
    assert -17.22 == ftoc.f2c(1.0)


def test_minus_1():#
    assert -18.33 == ftoc.f2c(-1.0) #


def test_0():
    assert -17.78 == ftoc.f2c(0.0)


def test_minus_0():
    assert -17.78 == ftoc.f2c(-0.0)


def test_300():
    assert 148.89 == ftoc.f2c(300.0)


def test_minus_300():
    assert -184.44 == ftoc.f2c(-300)
