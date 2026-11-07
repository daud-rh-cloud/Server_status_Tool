import os 
import json
import subprocess 
import sys 
from datetime import datetime


def controll_All(path):
    with open(path, "r") as f : 
        data  = json.load(f)
        
        now = datetime.now().strftime("%d/%m/%Y, %H:%M")
        new_file = []
        
        for line in data:
            hostname = line["address"]
            x = subprocess.run(["ping", "-c" ,"1" ,hostname ] )
            returncode = x.returncode
            
            try  : 
                if returncode == 0: 
                    print (line["name"], "service is UP!.. ")
                    new_file.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : "UP",  "last_checked": now})
                else:
                    print (line["name"], "service is DOWN!.. ")
                    new_file.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : "DOWN",  "last_checked": now})
            except Exception as e  :
                print (e)
    
    new_file = json.dumps(new_file, indent=2 )
    with open (path , "w") as f:
        f.write (new_file)
        
        
        
        
        
        
        
def controllByName (path, keyword ):
    with open (path, "r") as f : 
        data  = json.load(f) 
        
        now =  datetime.now().strftime("%d-%m-%Y, %H:%M")
        new_file = []
        
        for line in data:
            if line["name"] == keyword :
                hostname = line["address"]
                x = subprocess.run(["ping", "-c" ,"1" ,hostname ] )
                returncode = x.returncode
            
                try : 
                    if returncode == 0:
                        print (line["name"], "service is UP!.. ")
                        new_file.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : "UP",  "last_checked": now})
                    else :
                        print (line["name"], "service is Down!.. ")
                        new_file.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : "DOwn",  "last_checked": now})
                       
                except Exception as e: 
                    print (e)
            
            else :
                #if this is not the desired server, then write it back as it was 
                new_file.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : line ["status"],  "last_checked": line["last_checked"]})
        
        
        new_file = json.dumps(new_file, indent=2 )
        with open (path, 'w')as f: 
            f.write (new_file)
