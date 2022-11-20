#ALL FUNCTIONS 
#diabetic patients
def add_diabetes():
    f1=open("diabetes.txt","a")
    f2=open("diabetes.txt","r")
    r=int(input("Enter 5 Digit Application number"))
    n=input("Enter Patient Name")
    l=int(input("Enter  Patient's Age"))
    g=input("Enter Patient's Gender M/F/O")
    f1.write(str(r)+","+"PATIENT'S_NAME:"+n+","+"PATIENT'S_AGE:"+str(l)+","+"PATIENT'S_GENDER:"+g+"\n")
    f1.close()
def search_diabetes():
       f3=open("diabetes.txt","r")
       rn=str(input("enter the application number:"))
       i=0
       for s in f3:
              st=""
              i=0
              n=len(s)
              for i in range (0,n):
                     if (s[i]!=','):
                            st+=s[i]
                     else:
                            break
              if(rn==st):
                     print(s)
       f3.close()
def display_diabetes():
    f3=open("diabetes.txt",'r')
    d=f3.read()
    print("DETAILS OF ALL DIABETIC PATIENTS \n",d)
def modify_diabetes():
    import os
    f4=open("diabetes.txt","r")
    f5=open("temp.txt","w")
    x=int(input("Enter 5 Digit Application number"))
    a=input("enter patient's correct name")
    b=int(input("enter patient's correct age"))
    c=input("enter patient's correct gender")
    
    t=f4.readlines()
    k=len(t)
    for s in t:
        st="";
        for j in range(len(s)):
            if(s[j]!=','):
                st=st+s[j]
            else:
                break
        if(x==int(st)):
          f5.write(str(x)+","+"PATIENT'S_NAME:"+a+","+"PATIENT'S_AGE:"+str(b)+","+"PATIENT'S_GENDER:"+c+"\n")
        else:
            f5.write(s)
    f4.close()
    f5.close()
    os.remove("diabetes.txt")
    os.rename("temp.txt","diabetes.txt")
# cancer patients
def add_cancer():
    f1=open("cancer.txt","a")
    f2=open("cancer.txt","r")
    r=int(input("Enter 5 Digit Application number"))
    n=input("Enter Patient Name")
    l=int(input("Enter  Patient's Age"))
    g=input("Enter Patient's Gender M/F/O")
    f1.write(str(r)+","+"PATIENT'S_NAME:"+n+","+"PATIENT'S_AGE:"+str(l)+","+"PATIENT'S_GENDER:"+g+"\n")
    f1.close()
def search_cancer():
    f3=open("cancer.txt","r")
    rn=input("Enter Patient's Application Number")
    for s in f3:
        st=""
        i=0
        for i in range (0,len(s)):
            if (s[i]!=','):
                st+=s[i]
            else:
                break
        if(rn==st):
            print(s)
    f3.close()
def display_cancer():
    f3=open("cancer.txt",'r')
    d=f3.read()
    print("DISPLAY DETAILS OF ALL CANCER  PATIENTS \n",d)
def modify_cancer():
    import os
    f4=open("cancer.txt","r")
    f5=open("temp.txt","a")
    x=input("Enter 5 Digit Application number")
    a=input("enter patient's correct name")
    b=input("enter patient's correct age")
    c=input("enter patient's correct gender")

    t=f4.readlines()
    for  s in t :
        st=""
        for i in range(len(s)):
            if(s[i]!=","):
                st+=s[i]
            else:
                break
        if(x==st):
            f5.write(str(x)+","+"PATIENT'S_NAME:"+a+","+"PATIENT'S_AGE:"+str(b)+","+"PATIENT'S_GENDER:"+c+"\n")
        else:
            f5.write(s)
    f4.close()
    f5.close()
    os.remove("cancer.txt")
    os.rename("temp.txt","cancer.txt")
#covid-19 patients
def add_covid():
    f1=open("covid-19.txt","a")
    f2=open("covid-19.txt","r")
    r=int(input("Enter 5 Digit Application number"))
    n=input("Enter Patient Name")
    l=int(input("Enter  Patient's Age"))
    g=input("Enter Patient's Gender M/F/O")
    f1.write(str(r)+","+"PATIENT'S_NAME"+n+","+"PATIENT'S_AGE"+str(l)+","+"PATIENT'S_GENDER_"+g+"\n")
    f1.close()
def search_covid():
       f3=open("covid-19.txt","r")
       rn=input("Enter Patient's Application Number")
       for s in f3:
              st=""
              i=0
              for i in range (0,len(s)):
                     if (s[i]!=','):
                            st+=s[i]
                     else:
                            break
              if(rn==st):
                     print(s)
       f3.close()
def display_covid():
    f3=open("covid-19.txt",'r')
    d=f3.read()
    print("DISPLAY DETAILS OF ALL CORONAVIRUS  PATIENTS \n",d)
def modify_covid():
    import os
    f4=open("covid-19.txt","r")
    f5=open("temp.txt","a")
    x=input("Enter 5 Digit Application number")
    a=input("enter patient's correct name")
    b=input("enter patient's correct age")
    c=input("enter patient's correct gender")
    
    t=f4.readlines()
    for  s in t :
        st=""
        for i in range(len(s)):
            if(s[i]!=","):
                st+=s[i]
            else:
                break
        if(x==st):
            f5.write(str(x)+","+"PATIENT'S_NAME:"+a+","+"PATIENT'S_AGE:"+str(b)+","+"PATIENT'S_GENDER:"+c+"\n")
        else:
            f5.write(s)
    f4.close()
    f5.close()
    os.remove("covid-19.txt")
    os.rename("temp.txt","covid-19.txt")
l=input("PRESS  'ENTER'  TO START")
