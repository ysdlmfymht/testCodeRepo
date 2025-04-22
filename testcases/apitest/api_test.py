# coding=utf-8
import allure
import requests
# import json


@allure.epic("testDemoProject")
@allure.testcase("")
@allure.issue("")
@allure.feature("测试功能1")
class TestProject:
    @allure.story("搜索测试")
    def test_demo1(self):
        url = "https://search.douban.com/movie/subject_search"
        headers = {
            "accept":
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                "application/signed-exchange;v=b3;q=0.7",
            "accept-encoding":
                "gzip, deflate, br, zstd",
            "accept-language":
                "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "user-agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 "
                "Safari/537.36 Edg/134.0.0.0"
        }
        params = dict(search_text=u'刘德华')
        response = requests.get(url, params=params, headers=headers)
        # print("status_code:", response.status_code)
        assert response.status_code == 200
