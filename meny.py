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
        print (f"-- Name:{line["name"]:<8}, Address:{line["address"]:<15}, Environment:{line["environment"]:<8}, Role:{line["role"]:<8}, status: {line["status"]:<8} , Last checked :{line["last_checked"]:<8} ")
        print ()
        
        

def ShowserverinEnv(f, env):
        data = json.load(f)
        for line in data:
            if line["environment"] == env:
                print (f"Name:{line["name"]}, Address:{line["address"]}, Environment:{line["environment"]}, Role:{line["role"]}, status: {line["status"]} , Last checked :{line["last_checked"]} ")
            else :
                continue 
        
        
        
        
        
        
def add_server(path, f, name,address,environment,role):
    data = json.load(f)
    environment_list= ["prod", "test", "dev"]
    environment = environment.lower()
    
    while not environment in environment_list:
        print (f"Invalid Env Name! Please choose from {environment_list}")
        environment = input("provide a new name: ")
    else : 
        pass 
    
    
    if name :
        for server in data:
            if server.get("name") == name: 
                print ("ServerName Already taken")
                return None 
     
    
        
    
    data.append({"name": name, "address": address, "environment": environment, "role": role, "status": "unknown", "last_checked": ""})
    data= json.dumps (data, indent=2 )
    with open (path, "w") as f:
        f.write(data)





def remove_server(f,path,name,input_address):
    newdata = []
    data = json.load(f)
    for line in data:
        if line["address"] != input_address and line["name"] != name: 
         newdata.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : line["status"],  "last_checked": line["last_checked"]})
        elif line["address"] != input_address and line["name"] == name: 
         print ("No Host match with this name!")
        elif line["address"]== input_address and line["name"] != name: 
            print ("No host with thats name Exist! ")
            
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