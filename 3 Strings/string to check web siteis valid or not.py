#wRITE A PYTHON TO ACCEPT A WEB SITE NAME AND PRINT THE SITE IS VALID OR NOT
str=input("Enter the name of website")
chk=str.endswith(".com") or str.endswith(".gov") or str.endswith(".ido") or str.endswith(".in") or str.endswith(".orj")
if chk==True:
    print("valid website")
else :
    print("invalid Website")
