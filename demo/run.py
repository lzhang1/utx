#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from utx import *
import logging
import sys
from optparse import OptionParser
if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog [options]",version="%prog 1.0")
    options,args = parser.parse_args()
    if len(args) != 4:
        parser.error("wrong number of arguments")
    #setting.run_case = {args[0]}
    setting.run_case = {Tag.args[0]}
    setting.check_case_doc = False  # 关闭检测是否编写了测试用例描述
    setting.full_case_name = True
    setting.max_case_name_len = 80  # 测试报告内，显示用例名字的最大程度
    setting.show_error_traceback = True  # 执行用例的时候，显示报错信息
    setting.sort_case = True  # 是否按照编写顺序，对用例进行排序
    setting.create_bstest_style_report = args[1]
    setting.create_ztest_style_report = args[2]
    #log.set_level(args[3])
    log.set_level(logging.DEBUG)

    runner = TestRunner()
    runner.add_case_dir(r"testcase")
    runner.run_test(report_title='接口自动化测试报告')
