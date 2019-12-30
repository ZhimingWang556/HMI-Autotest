import unittest
import time
from common.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # 定义测试用例目录为当前目录
    test_dir = './test_case'
    suit = unittest.defaultTestLoader.discover(start_dir=test_dir,
                                               pattern='test*.py')

    # 获取当前日期和时间
    now_time = time.strftime("%Y-%m-%d %H-%M-%S")
    test_report = './test_report/' + now_time + 'result.html'
    with(open(test_report, 'wb')) as fp:
        runner = HTMLTestRunner(stream=fp,
                                title="HMI测试报告",
                                description="运行环境：Android 7.1.1")
        runner.run(suit)