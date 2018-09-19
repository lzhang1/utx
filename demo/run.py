#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from utx import *
import logging
import sys
from optparse import OptionParser
if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog [options]",version="%prog 1.0")
    options,args = parser.parse_args()
    settting.run_case = {eval(args[0])}
    #if len(args) != 4:
    #    parser.error("wrong number of arguments")
    #if args[0] == 'FULL':
    #    setting.run_case = {Tag.FULL}
    #elif args[0] == 'SMOKE':
    #    setting.run_case = {Tag.SMOKE}
    #else:
    #    setting.run_case = {Tag.SP}
    setting.check_case_doc = False  # 关闭检测是否编写了测试用例描述
    setting.full_case_name = True
    setting.max_case_name_len = 80  # 测试报告内，显示用例名字的最大程度
    setting.show_error_traceback = True  # 执行用例的时候，显示报错信息
    setting.sort_case = True  # 是否按照编写顺序，对用例进行排序
    setting.create_bstest_style_report = args[1]
    setting.create_ztest_style_report = args[2]
    log.set_level(args[3])
    #if args[3] == 'DEBUG':
    #    log.set_level(logging.DEBUG)
    #elif args[3] == 'INFO':
    #    log.set_level(logging.INFO)
    #elif args[3] == 'ERROR':
    #    log.set_level(logging.ERROR)
    #else:
    #    log.set_level(logging.WARNING)

    runner = TestRunner()
    runner.add_case_dir(r"testcase")
    runner.run_test(report_title='接口自动化测试报告')
