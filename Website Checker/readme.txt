Site Checker

A Python3 script that monitors list of websites and reports their availability. This tool is intended as a monitoring
tool for web site administrators for detecting problems on their sites.

Main functionality:

1.	Reads a list of web pages (HTTP URLs) and corresponding page content requirements from a JSON configuration file.
2.	Periodically makes an HTTP request to each page according to the configuration.
3.	Verifies that the page content received from the server matches the content requirements.
4.	Measures the time it took for the web server to complete the whole request.
5.	Writes a log file that shows the progress of the periodic checks.
    The log file contains the checked URLs, their status and the response times etc.
6. The program also distinguish between connection level problems


Usages:

* Python3 must be installed in the machine.
* Check and install the dependencies from requirements.txt
* Configure the config.json for your own entries
* Go to the program directory from command prompt:
For Windows, e.g: > cd C:/Users/......Desktop/SiteChecker
> python3 site_checker.py
* Check the log_report.txt for logs

Log File:

The log file consists following items:
* Website: Name of the Website that has been checked according to config.json file.
* Date: Current of checking
* Time: Time of the checking occurred.
* Status: Confirms if the website working or not. OK indicates working.
* ResponseTime(ms): Successful ping time for measured in mili seconds
* ContentCheck: Confirms the availability of the content. Also shows how many matches it founds.
* Report: Gives addition information for each occurrence.



