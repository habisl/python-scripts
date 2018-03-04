"""
!/usr/bin/env python3
-*- coding: utf-8 -*-
"""

from urllib.error import URLError, HTTPError
import numpy as np
import time
import json
import requests
from bs4 import BeautifulSoup

json_file = './config.json'
file_name = './log_report.txt'

with open(json_file) as config_file:
    config = json.load(config_file)

# Setting up headers for creating logs
log_file = open(file_name, "w")
log_file.write("Website" + "\t" + "   Date" + "\t" + "\t" + " Time" + "\t" + "Status"
               + "\t" + "  ResponseTime(ms)" + "  " + "ContentCheck" + "  " + "\t"+"Report" + "\n")  # For Logs header
log_file.close()


for i in range(0, int(config['frequency']['total_itarations'])):  # number of times it should check
    time.sleep(int(config['frequency']["check_interval"]))  # In seconds

    for site in config['sites']:

        try:
            log_file = open(file_name, "a")  # Takes log entry for each url hits
            current_date = time.strftime("%x")
            current_time = time.strftime("%X")
            site_name = (site["name"])
            req = requests.get(site["url"])
            start = time.time()
            soup = BeautifulSoup(req.text, 'html.parser')
            content = soup.findAll(text=site['content'])  # search for all matches and hold it in an array
            end = time.time()
            del_time = end - start
            del_time = (np.round(del_time * 10000)) / 10000  # Response time round-up in milliseconds
            del_time = str(del_time)
            print([site_name, 'checked on ', str(current_date), ' at time ', str(current_time)])
            if len(content) > 0:
                note = "Content Found:" + str(len(content))
            else:
                note = 'Content Not Found.'
        except HTTPError as e:
            status = 'Not OK'
            remarks = 'The server couldn\'t fulfill the request with Error code: ' + str(e.code)
            print(remarks)
            status = 'Not OK'
            del_time = 'NA'
            log_file.write("%s,%s,%s,%s,%s,%s\n" % (site_name, current_date, current_time, status, del_time, remarks))
            log_file.close()
        except URLError as e:
            status = 'Not OK'
            remarks = 'Website faced connection problem with Reason: ' + str(e.reason)
            print(remarks)
            status = 'Not OK'
            del_time = 'NA'
            log_file.write("%s,%s,%s,%s,%s,%s\n" % (site_name, current_date, current_time, status, del_time, remarks))
            log_file.close()
        else:
            print('Website is working fine')
            remarks = 'Website is working fine'
            status = 'OK'
            log_file.write("%s, %s, %s, %s, %s, %s, %s\n" % (site_name, current_date, current_time, status, del_time, note, remarks,))
            log_file.close()


