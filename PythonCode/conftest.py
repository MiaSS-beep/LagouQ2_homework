import pytest


@pytest.fixture()
def set_and_teardown():
    print("开始计算")
    yield
    print("计算结束")