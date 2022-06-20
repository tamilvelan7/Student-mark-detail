tam=int(input("Enter the student Tamil mark= "))
eng=int(input("Enter the student English mark= "))
mat=int(input("Enter the student Maths mark= "))
sci=int(input("Enter the student science mark= "))
ss=int(input("Enter the student social science mark= "))
list_mark=[]
list_sub=["Tamil","English","Mathematics","Science","Social Science"]
for i in tam,eng,mat,sci,ss:
    list_mark.append(i)
Total=(tam+eng+mat+sci+ss)
avg=(tam+eng+mat+sci+ss)/5
print("\n")
for i,j in zip(list_sub,list_mark):
    if j>=50:
        print(i,"=Pass")
    else:
        print(i,"=Fail")

print("\nStudent marks= ",list_mark,'\nTotal= ',Total)
print("\nStudent avarage= ",avg,"\n")
