import json


json_file = './config.json'
file_name = './log_report.txt'


with open(json_file) as config_file:
    config = json.load(config_file)
print(json.dumps(config, indent=4))


log_file = open(file_name, "w")
log_file.write("Name" + "\t" + "   Date" + "\t" + "\t" + " Time" + "\t" + "Status"
                        + "\t" + "  Ping Time(ms)" + "  " + "Report" + "\n")  # Logs header
                      
# Will be implemented soon...                      
                      
log_file.close()
