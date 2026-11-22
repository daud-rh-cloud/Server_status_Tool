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


def print_header():
    print (f"{"Name":<15}{"Address":<15}{"miljo":<15}{"roll":<15}{"Status":<15}{"Last checked":<15}")
    print ("-----------------------------------------------------------------------------------------------" )


def print_all_servers (f):
    data = json.load(f)
    print_header()
    for line in data : 
        print (f"{line["namn"]:<15}{line["adress"]:<15}{line["miljo"]:<15}{line["roll"]:<15}{line["status"]:<15}{line["senast_kontrollerad"]:<15}")
         
        
        

def show_servers_in_env(f, env):
        data = json.load(f)
        print_header()
        for line in data:
            if line["miljo"] == env:
                print (f"{line["namn"]:<15}{line["adress"]:<15}{line["miljo"]:<15}{line["roll"]:<15}{line["status"]:<15}{line["senast_kontrollerad"]:<15}")        
                continue 
        
        
        
        
        
        
def add_server(path, f, name,address,environment,role):
    data = json.load(f)
    if not name.strip():
        print ("Name can not be empty!")
        return None
    environment_list= ["prod", "test", "dev"]
    environment = environment.lower()
    
    while not environment in environment_list:
        print (f"Invalid Env Name! Please choose from {environment_list}")
        environment = input("provide a new name: ")
    else : 
        pass 
    
    
    if name :
        for server in data:
            if server.get("namn") == name: 
                print ("ServerName Already taken")
                return None 
     
    
        
    
    data.append({"namn": name, "adress": address, "miljo": environment, "roll": role, "status": "unknown", "senast_kontrollerad": ""})
    data= json.dumps (data, indent=2 )
    with open (path, "w") as f:
        f.write(data)





def remove_server(f,path,name,input_address):
    newdata = []
    data = json.load(f)
    
    searching_adress = None
    
    for line in data :
        if line ["adress"] == input_address:
            searching_adress = input_address 
        else :
            continue
            
    
    
    if searching_adress != None:
        
     user_confirmation = "y"
     for line in data:
        if line ["miljo"] == "prod" and line ["namn"] == name:
            user_confirmation = input ("Are you Sure you want to remove it? y/n?")
            if user_confirmation != "y":
                print("Removal cancelled")
                return None 
        
        else :
                
            if  line["adress"] != input_address and line["namn"] == name: 
                print ("No Host match with this name!")
                return None 
            elif line["adress"]== input_address and line["namn"] != name: 
                print ("No host with thats name Exist! ")
                return None
            elif line["adress"] != input_address and user_confirmation == "y":             
                newdata.append({"namn": line["namn"], "adress": line["adress"], "miljo": line["miljo"], "roll": line["roll"], "status" : line["status"],  "senast_kontrollerad": line["senast_kontrollerad"]})
            
     print (f"Server {name} has been Removed")
     newdata = json.dumps(newdata, indent=2)
     with open (path, "w") as f :
        f.write(newdata)
    
    
    else :
         print ("No such Host exist ")
         return None 
     
 
        



        

## A additonal funtion i made to match Command line (arg] ->env)
def show_all_env(path):
    with open (path, "r")as f: 
        data = json.load(f)
        
        envoirments = []
        for env in data:
            envoirments.append (env["miljo"])
            
    return envoirments