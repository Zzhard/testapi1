import unittest
import requests
from config.config import datapath, logger
from lib import readexceldata
import os
import json
from lib import case_log


class Check(unittest.TestCase):
    def setUp(self):
        file = os.path.join(datapath, "接口自动化测试用例.xlsx")
        self.data_list = readexceldata.excel_to_list(file, 'check')


    def test_city_ok(self):
        data = readexceldata.get_test_data("test_city_ok", self.data_list)
        case_log.case_log(data)
        url = data["url"]
        input_args = eval(data["input_args"])
        print(type(input_args),input_args)
        expire_result = data["expire_result"]
        # response=requests.post(url,data=input_args)
        response = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % response)
        print(response.text)
        self.assertIn("成功", response.text)


    def test_city_not_exist(self):
        data = readexceldata.get_test_data("test_city_not_exist", self.data_list)
        print(data)
        case_log.case_log(data)
        url = data["url"]
       # input_args=data["input_args"]
        input_args = eval(data["input_args"])
        # print(type(input_args),input_args)
        expire_result = data["expire_result"]
        # response=requests.post(url,data=input_args)
        response = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % response)
        print(response.text)
        self.assertIn("城市错误或不支持", response.text)


    def test_city_null(self):
        data = readexceldata.get_test_data("test_city_null", self.data_list)
        case_log.case_log(data)
        url = data["url"]
        input_args = eval(data["input_args"])
        expire_result = data["expire_result"]
        # response=requests.post(url,data=input_args)
        response = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % response)
        print(response.text)
        self.assertIn("城市名不能为空", response.text)


    def test_wrong_key(self):
        data = readexceldata.get_test_data("test_wrong_key", self.data_list)
        case_log.case_log(data)
        url = data["url"]
        input_args = eval(data["input_args"])
        expire_result = data["expire_result"]
        # response=requests.post(url,data=input_args)
        response = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % response)
        print(response.text)
        self.assertIn("错误的请求KEY", response.text)


    def test_no_key(self):
        data = readexceldata.get_test_data("test_no_key", self.data_list)
        case_log.case_log(data)
        url = data["url"]
        input_args = eval(data["input_args"])
        expire_result = data["expire_result"]
        # response=requests.post(url,data=input_args)
        response = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % response)
        print(response.text)
        self.assertIn("错误的请求KEY", response.text)

    def test_no_page(self):
        data = readexceldata.get_test_data("test_no_page", self.data_list)
        case_log.case_log(data)
        url = data["url"]
        input_args = eval(data["input_args"])
        expire_result = data["expire_result"]
        # response=requests.post(url,data=input_args)
        response = requests.post(url, data=input_args)
        logger.info("响应内容:%s" % response)
        print(response.text)
        self.assertIn("成功", response.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
