    #write a python program to accept a word and charecter . and find the distance of two charecters else
#return -1also handle appropriate ecceptions .
try:
    str1=input("Enter the string")
    ch=input("Enter the character")
    count=0
    ans=0
    for i in range(len(str1)):
        if str1[i]==ch:
            count=count+1
            if count==1:
                index1=i
            elif count==2:
                index2=i
                ans=index2-index1
                break
    if count==1:
        ans=-1
    print(ans)
except IndexError:
    print("Enter valid character")
