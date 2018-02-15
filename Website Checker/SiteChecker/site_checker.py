"""
!/usr/bin/env python3
__author__ = Habibul Islam
__license__ = "Public Domain"
__version__ = 3.0

"""

import json

json_file = './config.json'
file_name = './log_report.txt'

with open(json_file) as config_file:
    config = json.load(config_file)
print(json.dumps(config, indent=4))

log_file = open(file_name, "w")
log_file.write("Name" + "\t" + "   Date" + "\t" + "\t" + " Time" + "\t" + "Status"
               + "\t" + "  Ping Time(ms)" + "  " + "Report" + "\n")  # Logs header

for i in range(0, int(config['frequency']['total_itarations'])):  # number of times it should check
    time.sleep(int(config['frequency']["check_interval"]))  # In seconds

    for site in config['sites']:
        try:
            site_name = (site["name"])
            req = requests.get(site["url"])
            start = time.time()
            soup = BeautifulSoup(req.text, 'html.parser')
            content = soup.findAll(text=site['content'])
            print(site_name)
            print(req)
            print(content)
        except HTTPError as e:
            status = 'Not OK'
        else:
            print(OK)
        # Need to be implemented soon... 
        log_file.close()
        # Need to be implemented soon... 
