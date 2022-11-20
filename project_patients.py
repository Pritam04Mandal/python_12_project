# MAIN PROGRAM 
import fun
c="Y"
while(c=="y" or c=="Y"):
       print("1. ARE YOU A DIABETIC PATIENT")
       print("2. ARE YOU CANCER PATIENT")
       print("3. ARE YOU CORONAVIRUS PATIENT")
       f=int(input("Enter Your Choice"))
       if(f==1):
              print("1. ADD PATIENT'S DETAILS ")
              print("2. SEARCH PATIENT'S DETAILS")
              print("3. DISPLAY ALL  PATIENT'S DETAIL ","!!ONLY FOR OFFICIALS!!")
              print("4. MODIFY PATIENT'S DETAILS")
              C=int(input("Enter your choice"))
              if(C==1):
                     fun.add_diabetes()
              elif(C==2):
                     fun.search_diabetes()
              elif(C==3):
                      k=int(input("Enter SECURITY PIN"))
                      z=5016
                      if(k==z):
                             fun.display_diabetes()
                      else:
                             
                             print("NEED AUTHORISED PIN")
                             break
              elif(C==4):
                     fun.modify_diabetes()
              else:
                     print("!!!!wrong choice!!!!")
       elif(f==2):
              print("1. ADD PATIENT'S DETAILS ")
              print("2. SEARCH PATIENT'S DETAILS")
              print("3. DISPLAY ALL  PATIENT'S DETAIL ","!!ONLY FOR OFFICIALS!!")
              print("4. DO YOU WANT TO MODIFY YOUR DATA")
              C=int(input("Enter your choice"))
              if(C==1):
                     fun.add_cancer()
              elif(C==2):
                     fun.search_cancer()
              elif(C==3):
                      k=int(input("Enter SECURITY PIN"))
                      z=5016
                      if(k==z):
                             fun.display_cancer()
                      else:
                             print("NEED AUTHORISED PIN")
                             break
              elif(C==4):
                     fun.modify_cancer()
              else:
                     print("!!!!wrong choice!!!!")

       elif(f==3):
              print("1. ADD PATIENT'S DETAILS ")
              print("2. SEARCH PATIENT'S DETAILS")
              print("3. DISPLAY ALL  PATIENT'S DETAIL ","!!ONLY FOR OFFICIALS!!")
              print("4. DO YOU WANT TO MODIFY YOUR  DATA")
              C=int(input("Enter your choice"))
              if(C==1):
                      fun.add_covid()
              elif(C==2):
                      fun.search_covid()
              elif(C==3):
                     k=int(input("Enter SECURITY PIN"))
                     z=5016
                     if(k==z):
                            fun.display_covid()
                     else:
                            print("NEED AUTHORISED PIN")
                            break
              elif(C==4):
                     fun.modify_covid()
              else:
                     print("!!!!wrong choice!!!!")

       else:
              print("!!!!WRONG ENTRY ABOUT PATIENTS!!!")
       c=input("DO YOU WANT MORE DETAILS")


k=input("PRESS  'ENTER'  TO END")








   
