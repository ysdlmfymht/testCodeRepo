import pytest

# allure generate ./report/testinf1/xml -o ./report/testinf1/html -c
if __name__ == '__main__':
    pytest.main(["-s", "-v", "./api/api_test.py", "--alluredir", "./report/xml"])
