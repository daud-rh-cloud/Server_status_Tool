import meny
import os 
import sys 
from argparse import ArgumentParser
import subprocess 
import kontroller 
import argparse 
import CSVwritter


if "INVENTORY_DATAFILE" in os.environ:
    path = os.environ.get("INVENTORY_DATAFIL")
else:
    path = "server.json"
    


### COMMAND LINE 

parser = argparse.ArgumentParser()

parser.add_argument("--list", "--lista",action= "store_true" )
parser.add_argument("--env", "--miljo", choices=meny.ShowAlllenv(path), help="--list + --env [name] ")
parser.add_argument("--controll-all", "--kontrollera-alla", action = "store_true")
parser.add_argument("--controll","--kontrollera", metavar="name")
parser.add_argument("--export", action="store_true")

#reading and parsing the user arguments from Sys.argv[]
user_argument = parser.parse_args()

with open (path, "r") as f : 
    
    if user_argument.list and user_argument.env :
        with open (path, "r") as f:
            meny.ShowserverinEnv(f,user_argument.env)

    elif  user_argument.list: 
            meny.printallserver(f)

    elif user_argument.controll_all:
        kontroller.controll_All(path)
        
    elif user_argument.controll: 
        kontroller.controllByName(path, keyword=user_argument.controll)

    elif user_argument.export:
        print ("CSV Report Has been Exported")
        CSVwritter.wrtieCsvFile(path) 



    else :
        while True :
            user_input = meny.visa_meny()
            
            if user_input == 1: 
                    meny.printallserver(f)
            
            
            elif user_input == 2 :
                environment_list= ["prod", "test", "dev"]

                env = input ("Which environment ?:  ")
                if not env in environment_list:
                    print ("invalid Env!!")
                else :
                    meny.ShowserverinEnv(f, env=env)
            
            
            elif user_input == 3: 
                
                name = input("Enter name: ")
                address = input("Enter address: ")
                environment = input ("Environment tag: ")
                role = input ("Enter role: ")

                 
                meny.add_server(path,f=f, name=name, address=address, environment=environment, role=role)
                    
                    
                    
            elif user_input == 4:
                input_adress = input("Enter the Hsot name: ")
                meny.remove_server(f,path,input_address=input_adress)
                    
                    
            elif user_input == 5: 
                keyword  = input ("Enter server name: ")
                kontroller.controllByName(path, keyword=keyword)
                
                
        
            elif user_input==6 :
                kontroller.controll_All(path)
        
            elif user_input== 7:
                print ("CSV Report Has been Exported")
                CSVwritter.wrtieCsvFile(path)  
            
            elif user_input == 8:
                print ("Bye ")
                break




