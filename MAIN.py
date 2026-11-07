import meny
import os 
import sys 
from argparse import ArgumentParser
import subprocess 
import kontroller 
import argparse 
import CSVwritter

def main ():
    
    if "INVENTORY_DATAFILE" in os.environ:
        path = os.environ.get("INVENTORY_DATAFILE")
    else:
        path = "server.json"
        
    if not os.path.exists(path):
        print ("Source File Doesn't Exist!" )
    else: 
        pass 


    ### COMMAND LINE 
    parser = argparse.ArgumentParser()

    parser.add_argument("--list", "--lista",action= "store_true", help= "Lists All Server" )
    parser.add_argument("--env", "--miljo", choices=meny.ShowAlllenv(path), help="--list --env [name]/ (List server in Env XYZ ")
    parser.add_argument("--controll-all", "--kontrollera-alla", action = "store_true", help=("Cheaks All server status" ))
    parser.add_argument("--controll","--kontrollera", metavar="name", help=("Cheaks server Specefic servers Status"))
    parser.add_argument("--export", action="store_true",help="Exports CSV Report")

    #reading and parsing the user arguments from Sys.argv[]
    user_argument = parser.parse_args()

    
        
    if user_argument.list and user_argument.env :
            with open (path, "r") as f:
                meny.ShowserverinEnv(f,user_argument.env)

    elif  user_argument.list: 
        with open (path, "r") as f :
                meny.printallserver(f)

    elif user_argument.controll_all:
        with open (path, "r") as f :
            kontroller.controll_All(path)
            
    elif user_argument.controll: 
        with open (path, "r") as f :
            kontroller.controllByName(path, keyword=user_argument.controll)

    elif user_argument.export:
        
            print ("CSV Report Has been Exported")
            CSVwritter.wrtieCsvFile(path) 



    else :
        while True :
            user_input = meny.visa_meny()
            
            if user_input == 1: 
                with open (path, "r") as f :
                    meny.printallserver(f)
            
            
            elif user_input == 2 :
             environment_list= ["prod", "test", "dev"]
             env = input ("Which environment ?:  ")
             if not env in environment_list:
                    print ("invalid Env!!")
             else :
                 with open (path, "r") as f :
                    meny.ShowserverinEnv(f, env=env) 
            
            
            elif user_input == 3: 
                
                name = input("Enter name: ")
                address = input("Enter address: ")
                environment = input ("Environment tag: ")
                role = input ("Enter role: ")

                with open (path, "r") as f :
                    meny.add_server(path,f=f, name=name, address=address, environment=environment, role=role)
                        
                    
                    
            elif user_input == 4:
                input_adress = input("Enter the Hsot name: ")
                with open (path, "r") as f :
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




if __name__ == "__main__":
    main()