import json


def visa_meny():
    user_input = input ("""
        --- Server Inventory Tool ---
        1. Show all servers
        2. Show servers in an environment
        3. Add a server
        4. Remove a server
        5. control a server
        6. control all servers
        7. Export report as CSV
        8. Exit
        """)
    return int(user_input)




def printallserver (f):
    data = json.load(f)
    for line in data : 
        print (f"-- Name:{line["name"]}, Address:{line["address"]}, Environment:{line["environment"]}, Role:{line["role"]}, status: {line["status"]} , Last checked :{line["last_checked"]} ")
        print ()
        
        

def ShowserverinEnv(f, env):
        data = json.load(f)
        for line in data:
            if line["environment"] == env:
                print (f"Name:{line["name"]}, Address:{line["address"]}, Environment:{line["environment"]}, Role:{line["role"]}, status: {line["status"]} , Last checked :{line["last_checked"]} ")
            else :
                continue 
        
        
        
        
        
        
def add_server(path, f, name,address,environment,role):
    environment_list= ["prod", "test", "dev"]
    environment = environment.lower()
    if not environment in environment_list:
        print (f"Invalid Env Name! Please choose from {environment_list}")
        return None  
    else :  
        pass 
        
    data = json.load(f)
    
    data.append({"name": name, "address": address, "environment": environment, "role": role, "status": "unknown", "last_checked": ""})
    data= json.dumps (data, indent=2 )
    with open (path, "w") as f:
        f.write(data)





def remove_server(f,path,input_address):
    newdata = []
    data = json.load(f)
    for line in data:
        if line["address"] != input_address:
         newdata.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : line["status"],  "last_checked": line["last_checked"]})
    
    newdata = json.dumps(newdata, indent=2)
    with open (path, "w") as f :
        f.write(newdata)





        

## A additonal funtion i made to match Command line (arg] ->env)
def ShowAlllenv(path):
    with open (path, "r")as f: 
        data = json.load(f)
        
        envoirments = []
        for env in data:
            envoirments.append (env["environment"])
            
    return envoirments