from config.config import logger
import os

def case_log(data):
    url=data['url']
    test_name=data['test_name']
    input_args=data["input_args"]
    expire_result=data['expire_result']
    logger.info("%s 测试开始"%test_name)
    logger.info("url:%s"%url)
    logger.info("入参:%s"%input_args)
    logger.info("期望结果:%s"%expire_result)