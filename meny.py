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
    return (user_input)




def printallserver (f):
    data = json.load(f)
    for line in data : 
        print (f"-- Name:{line["name"]:<11}, Address:{line["address"]:<11}, Environment:{line["environment"]:>11}, Role:{line["role"]:<11}, status: {line["status"]:<11} , Last checked :{line["last_checked"]:<11} ")
        print ()
        
        

def ShowserverinEnv(f, env):
        data = json.load(f)
        for line in data:
            if line["environment"] == env:
                print (f"Name:{line["name"]:<11}, Address:{line["address"]:<11}, Environment:{line["environment"]:<11}, Role:{line["role"]:<11}, status: {line["status"]:<11} , Last checked :{line["last_checked"]:<11} ")
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
    
    searching_adress = None
    
    for line in data :
        if line ["address"] == input_address:
            searching_adress = input_address 
        else :
            continue
            
    
    
    if searching_adress != None:
        
     user_confirmation = "y"
     for line in data:
        if line ["environment"] == "prod" and line ["name"] == name:
            user_confirmation = input ("Are you Sure you want to remove it? y/n?")
            if user_confirmation != "y":
                print("Removal cancelled")
                return None 
        
        else :
                
            if  line["address"] != input_address and line["name"] == name: 
                print ("No Host match with this name!")
                return None 
            elif line["address"]== input_address and line["name"] != name: 
                print ("No host with thats name Exist! ")
                return None
            elif line["address"] != input_address and user_confirmation == "y":             
                newdata.append({"name": line["name"], "address": line["address"], "environment": line["environment"], "role": line["role"], "status" : line["status"],  "last_checked": line["last_checked"]})
            
     print (f"Server {name} has been Removed")
     newdata = json.dumps(newdata, indent=2)
     with open (path, "w") as f :
        f.write(newdata)
    
    
    else :
         print ("No such Host exist ")
         return None 
     
 
        



        

## A additonal funtion i made to match Command line (arg] ->env)
def ShowAlllenv(path):
    with open (path, "r")as f: 
        data = json.load(f)
        
        envoirments = []
        for env in data:
            envoirments.append (env["environment"])
            
    return envoirments