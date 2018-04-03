Site Blocker

Customized Python3 script to block specific websites during working hours. 
It could be a handy tool if someone wants to be productive during work hours by avoiding time wasting website. 

Main functionality:
* Blocks listed sites during specific hours. 


Usages:

* Python3 must be installed in the machine.
> python3 site-blocker.py

In linux
> sudo python3 site-blocker.py
* Schedule by using  > sudo crontab -e 
add:
@reboot python3 /home/......path to the python file
Save the file.

In Windows
* In order to run the script in the background site-blocker.py > site-blocker.pyw in windows
* Script can be run using Task Scheduler. Tick mark "Run with highest privileges" while setting up scheduler
http://desktop.arcgis.com/en/arcmap/10.3/analyze/executing-tools/scheduling-a-python-script-to-run-at-prescribed-times.htm







