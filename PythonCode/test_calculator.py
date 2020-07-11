import pytest
import yaml

from PythonCode.Calculator import Calculator


class TestCal:

    @pytest.mark.parametrize('a,b,res',yaml.safe_load(open("./Calculator_data.yml"))["add"])
    def test_add(self,a,b,res,set_and_teardown):
        cal = Calculator()
        print(f"{a} {b} {res}")
        assert res == cal.add(a,b)

    @pytest.mark.parametrize('a,b,res',yaml.safe_load(open("./Calculator_data.yml"))["subtract"])
    def test_substract(self,a,b,res,set_and_teardown):
        cal = Calculator()
        assert res == cal.subtract(a,b)

    @pytest.mark.parametrize('a,b,res',yaml.safe_load(open("./Calculator_data.yml"))["mult"])
    def test_mult(self,a,b,res,set_and_teardown):
        cal = Calculator()
        assert res == cal.mult(a,b)

    @pytest.mark.parametrize('a,b,res',yaml.safe_load(open("./Calculator_data.yml"))["div"])
    def test_div(self,a,b,res,set_and_teardown):
        cal = Calculator()
        assert res == cal.div(a,b)

