#Cobra(Code of Ballistic missile launcher to a Region and Area)
#it is a missile launching software

C_Name="Asia", "Africa", "North America", "South America", "Antarctica", "Europe"," Australia"  #Continent Details
C_lat="11.0168deg N"   # Latitude of Coimbatore
C_lng="76.9558deg E"   # Longitude of Coimbatore
V_lat="46.2123deg N"   # Latitude of Vernier
V_lng="6.1053deg E"    # Longitude of Vernier
def Missile():
    while True:
        
                    print("___________________WELCOME TO MISSILE LAUNCH SOFTWARE______[COBRA]____ \n")
                    # So the we have a list of ballistic missiles here the user may Enter the missile name to start the program Eg. "prithvi seires" which i have witten using .lower() so it can take both cap and small words
                    print("\n Missile List: \n Seq_1.)Prithvi Series \t Seq_2.)Agni Series \t Seq_3.)Prahaar \t Seq_4.)Pralay \n")
                    Name=input("PLEASE ENTER THE MISSILE NAME (Eg. prithvi series/PRITHVI SERIES) :_______ ").lower()
                    
                    #PRITHVI SERIES
                    if Name=="prithvi series":
                        print("[PRITHVI SERIES]")
                        print(" Seq_1.)PRITHVI - I \n  Seq_2.)PRITHVI -II \n  Seq_3.)PRITHVI-III \n  Seq_4.)PRITHVI-IV")
                        #The user operating the program could select the sequence of his/her choice by entering the sequence numbers present in the list 
                        Seq=int(input("\n ENTER THE SEQUENCE FROM THE LIST (Eg. Type '1') - " ))
                        if Seq==1:
                            #Then the program displays the spefications of the missile selected by the user
                            print("\n MISSILE NAME - PRITHVI-I \n")
                            print("TYPE   - (SRBM)'Short Range Ballistic Missile'")
                            print("RANGE  - 150 KM")
                            print("WEIGHT - 1000KG")
                            print("ACCURACY - (10-50m)")
                            #The continent list is displayed along with the specifications enabling user to select the continent he wants the missie to launch
                            print("SELECT CONTINENT")
                            print("CONTINENT LIST - ",C_Name)
                            continent=input("\n Enter Continent Name (Eg.'Asia' as mentioned in the list) : ")
                            if continent=="Asia":
                                #Then the user gets an access to the list of the countries present in that specific contient the user had choosen and later the programs asks the user the specific state in the country
                                print("\n Countries located in Asia : 48 (FORTY EIGHT)")
                                print("Country List : 1.)India \t 2.)China \t 3.)Japan \t 4.) Indonesia")
                                country=input("\n Select country (Eg.'India' as mentioned in the list) - ")
                                if country=="India":
                                    location=input("Enter the location (Eg.'Tamil Nadu'):  ")
                                    if location=="Tamil Nadu":
                                        #The user is asked to enter the latitude and longitudes of the place in exact and displays the location of the place between the entered latitudes and longitudes
                                        latitude=input("Enter The Latitude (Eg.11.0168deg N)- ")
                                        lattitude=C_lat
                                        if lattitude==C_lat:
                                            longitude=input("Enter The Longitude (Eg.76.9558deg E) -")
                                            longitude=C_lng
                                            if longitude==C_lng:
                                                input("PLACE - COIMBATORE \n 'PRESS ENTER TO LOCK THE TARGET'\n")
                                                input("--THE TARGET IS LOCKED AT THE CO-ORDINATES--(PRESS ENTER TO CONTINUE)")
                                                input("DO YOU WANT TO LAUNCH___'PRESS ENTER'")
                                                input("DO YOU WANT TO LAUNCH___'PRESS ENTER'")
                                                input("DO YOU WANT TO LAUNCH___'PRESS ENTER'")
                                                choose=input("Final Call - Choose 'YES' or 'NO' ______")
                                                if choose=="YES":
                                                    print("----------------BOOM----------------")
                                                    print(" The Missile Launched Successfully")
                                                elif choose=="NO":
                                                        print("The Missile launch Action is Terminated")
                                                else:
                                                    print("[INVALID OPTION ]")

                                            else:
                                                print("INVALID INFORMATION THE LONGITUDE DOESN'T MATCH")
                                        else:
                                            print("INVALID INFORMATION THE LATITUDE DOESN'T MATCH")
                                    else:
                                        print("THE LOCATION YOU HAVE ENTER IS INCORRECT")
                                else:
                                    print("THE NAME OF THE COUNTRY DOESN'T EXIST IN THIS CONTINENT")
                            else:
                                print("NO CONTINENT WITH THIS NAME")

                        else:
                            print("THE ENTERED SEQUENCE IS INVALID")
                    
                    else:
                        print("The Operation has been Terminated")
                
                    
            
           

                                                                                               
                    #AGNI SERIES
                        
                    if Name=="agni series":
                        print("[AGNI SERIES]")
                        print("Seq_1.)AGNI - I \n  Seq_2.)AGNI -II \n  Seq_3.)AGNI-III \n  Seq_4.)AGNI-IV \n Seq_5.)AGNI-V \n")
                        Seq=int(input("ENTER SEQUENCE (Eg.Type-5)- "))
                        if Seq==5:
                            print("\n MISSILE NAME - [AGNI-V] \n ")
                            print("TYPE   - (ICBM)'Inter-continental Ballistic Missile'")
                            print("RANGE  - 5000 KM")
                            print("WEIGHT - 5TONS")
                            print("ACCURACY - (10m CEP)")
                            print("SELECT CONTINENT")
                            print("CONTINENT LIST - ",C_Name)
                            continent=input("\n Enter Continent Name (Eg. Europe): ")
                            if continent=="Europe":
                                print("\n Countries located in Europe : 44 (FORTY FOUR)")
                                print("Country List : 1.)Russia \t 2.)Germany \t 3.)Italy \t 4.)Switzer Land")
                                country=input("\n Select country (Eg.Switzer Land)- ")
                                if country=="Switzer Land":
                                    location=input("Enter the location (Eg.Geneva):  ")
                                    if location=="Geneva":
                                        latitude=input("Enter The Latitude (Eg.46.2123deg N) - ")
                                        lattitude=V_lat
                                        if lattitude==V_lat:
                                            longitude=input("Enter The Longitude (Eg.6.1053deg E) -")
                                            longitude=V_lng
                                            if longitude==V_lng:
                                                input("PLACE - VERNIER \n'PRESS ENTER TO LOCK THE TARGET'\n ")
                                                input("--THE TARGET IS LOCKED AT THE CO-ORDINATES--")
                                                input("DO YOU WANT TO LAUNCH___'PRESS ENTER'")
                                                input("DO YOU WANT TO LAUNCH___'PRESS ENTER'")
                                                input("DO YOU WANT TO LAUNCH___'PRESS ENTER'")
                                                choose=input("Final Call - Choose 'YES' or 'NO' ______")
                                                if choose=="YES":
                                                    print("----------------BOOM----------------")
                                                    print(" The Missile Launched Successfully")
                                                elif choose=="NO":
                                                            print("The Missile launch Action is Terminated")
                                                else:
                                                    print("[INVALID OPTION]")
                                            else:
                                                print("INVALID INFORMATION THE LONGITUDE DOESN'T MATCH")
                                        else:
                                            print("INVALID INFORMATION THE LATITUDE DOESN'T MATCH")
                                    else:
                                        print("THE LOCATION YOU HAVE ENTERED IS INCORRECT")
                                else:
                                    print("THE NAME OF THE COUNTRY DOESN'T EXIST IN THIS CONTINENT")
                                                                
                            else:
                                print("ENTERED WRONG INFORMATION")

                        else:
                            print("THE ENTERED SEQUENCE IS INVALID")
                    else:
                        print("The Operation has Been Terminated")


                            

                                        





Missile()





