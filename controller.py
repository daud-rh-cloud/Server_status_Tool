import os 
import json
import subprocess 
import sys 
from datetime import datetime


def controll_all(path):
    with open(path, "r") as f : 
        data  = json.load(f)
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_file = []
        exit_code = 0
        for line in data:
            hostname = line["adress"]
            try:
                x = subprocess.run(["ping", "-c" ,"1" ,hostname ], capture_output=True, timeout=5)
                returncode = x.returncode
            except subprocess.TimeoutExpired:
                # no answer within 5 seconds counts as down
                returncode = 1
            
            try  : 
                if returncode == 0: 
                    print (line["namn"], "service is UP!.. ")
                    new_file.append({"namn": line["namn"], "adress": line["adress"], "miljo": line["miljo"], "roll": line["roll"], "status" : "up",  "senast_kontrollerad": now})
                else:
                    print (line["namn"], "service is DOWN!.. ")
                    new_file.append({"namn": line["namn"], "adress": line["adress"], "miljo": line["miljo"], "roll": line["roll"], "status" : "down",  "senast_kontrollerad": now})
                    exit_code = 1
            except Exception as e  :
                print (e)
                
    new_file = json.dumps(new_file, indent=2 )
    with open (path , "w") as f:
        f.write (new_file)
        return  exit_code

        
        
        
        
        
        
def controll_by_name (path, keyword ):
    with open (path, "r") as f : 
        data  = json.load(f) 
        
        now =  datetime.now().strftime("%Y-%m-%d %H:%M")
        new_file = []
        selected_name = None
        exit_code=0
        
        for line in data:
            if line.get("namn") == keyword:
                selected_name = keyword
        
        if selected_name == None: 
             print("The Server Does't exist!")   
             exit_code = 1
             return exit_code
             
           
        for line in data:
                    if line["namn"] == keyword :
                        hostname = line["adress"]
                        x = subprocess.run(["ping", "-c" ,"1" ,hostname ], capture_output=True, timeout=5)
                        returncode = x.returncode
                    
                        try : 
                            if returncode == 0:
                                print (line["namn"], "service is UP!.. ")
                                new_file.append({"namn": line["namn"], "adress": line["adress"], "miljo": line["miljo"], "roll": line["roll"], "status" : "up",  "senast_kontrollerad": now})
                            else :
                                print (line["namn"], "service is Down!.. ")
                                new_file.append({"namn": line["namn"], "adress": line["adress"], "miljo": line["miljo"], "roll": line["roll"], "status" : "down",  "senast_kontrollerad": now})
                                exit_code = 1
                        except Exception as e: 
                            print (e)
                    
                    else :
                            #if this is not the desired server, then write it back as it was 
                            new_file.append({"namn": line["namn"], "adress": line["adress"], "miljo": line["miljo"], "roll": line["roll"], "status" : line ["status"],  "senast_kontrollerad": line["senast_kontrollerad"]})
         
       
        new_file = json.dumps(new_file, indent=2 )
        with open (path, 'w')as f: 
            f.write (new_file)
            return (exit_code)
