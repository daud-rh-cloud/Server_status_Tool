import csv 
import json 
import datetime 
import os



date = datetime.datetime.now().strftime("%d-%m-%Y,%H:%M")
report_file = f"Reports/inventering_{date}.csv"
reportfolder = "Reports"

if os.path.exists(reportfolder):
    pass
else: 
    os.mkdir(reportfolder)


def wrtieCsvFile(path):
    with open (path, "r") as f:
        data = json.load(f)
    
    if os.path.exists(report_file):
        os.remove(report_file)
    else:
        pass 
    
    
    with open (report_file, "w")as z:
        writter = csv.writer(z)
        
        header = data[0].keys()
        writter.writerow(header)
        
        for server in data:
            values = []
            for key,value in server.items():
                values.append(value)
            writter.writerow(values)

        
 
        
