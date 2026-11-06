#json.py -- >             -->> Menu.py -- >  1(-servers class with attribute takes (art: art:)] ->( EACH Line --> one server with its  attribute we caan call and change)  ),,,  controller.py (takes the json[org]], Keyword:  -->> returs a list[ Server-objects] ) -->>>READER/WRITER.py ->  Org json --> csv 
             # main ....argv                                [{0,0}] or [{},{}]
             
             
x = [
    {"namn": "web01", "adress": "example.com", "miljo": "prod", "roll": "webbserver", "status": "unknown", "senast_kontrollerad": ""},
    {"namn": "db01", "adress": "127.0.0.1", "miljo": "prod", "roll": "databas", "status": "unknown", "senast_kontrollerad": ""},
    {"namn": "test01", "adress": "192.0.2.10", "miljo": "test", "roll": "testserver", "status": "unknown", "senast_kontrollerad": ""},
    {"namn": "dev01", "adress": "localhost", "miljo": "dev", "roll": "utvecklingsserver", "status": "unknown", "senast_kontrollerad": ""}
    ]


print (len(x))

# JSON file get loaded from env varibale (INVENTORY_DATAFIL) else defult to /server.json 



# - just .py -- . menu - 
# add,
# remove , 
# list all server ,
# list servers in a given environment,  
# controll all server, 
#controll one server,
# exopirt report as csv 




# main.py -- commands (Read from file each time) 
#           -- list all server 
                #json file ->load list 
                
#           -- list servers in a given environmen
                # json file -> load list - > if element[x]["env"] = "prod"  
                #                             print ["name"] 
                
                
                
#           -- kontroll sepcefic server by (name)  
#           -- konttroll -all --> EXIT Code 
                # JSOn file -> load list[{},{}] --> ping [hosname]  ->return code -? 
                # --> newline.append(dict{name: x , host; x , status;x , last coontrolled:x  } ) 
                # json.dumps (list[dicts])


#           -- eexport as csv --> Json..py (env) to CSV with dates 
#           -- 