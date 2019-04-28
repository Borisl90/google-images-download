import sys

version = (3, 0)
cur_version = sys.version_info

import time  # Importing the time library to check the time of code execution
import os
import ssl
import datetime
import json
import re
import codecs
import socket
from .user_input import *


def get_size(self, size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return size


def get_source(element, browser):
    for i in range(30):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    try:
        browser.find_element_by_id("smb").click()
        for i in range(50):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)  # bot id protection
    except:
        for i in range(10):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)  # bot id protection

    print("Reached end of Page.")
    time.sleep(0.5)

    source = browser.page_source  # page source
    # close the browser
    browser.close()

    return source


def get_cur_version(self, s):
    start_line = s.find('class="rg_meta notranslate">')
    start_object = s.find('{', start_line + 1)
    end_object = s.find('</div>', start_object + 1)
    object_raw = str(s[start_object:end_object])
    # remove escape characters based on python version
    version = (3, 0)
    cur_version = sys.version_info
    if cur_version >= version:  # python3
        final_object = correct_version(object_raw)
    else:  # python2
        final_object = Incorrect_version(self, object_raw)
    return final_object, end_object


def correct_version(object_raw):
    try:
        object_decode = bytes(object_raw, "utf-8").decode("unicode_escape")
        final_object = json.loads(object_decode)
    except:
        final_object = ""
    return final_object


def Incorrect_version(self, object_raw):
    try:
        final_object = (json.loads(self.repair(object_raw)))
    except:
        final_object = ""
        return final_object


def read_file(search_keyword, f):
    for line in f:
        if line in ['\n', '\r\n']:
            pass
        else:
            search_keyword.append(line.replace('\n', '').replace('\r', ''))
