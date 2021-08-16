def myfunc(file,l):  
    data=file.read()

    length=len(data)
    final="ACGT"
    # l1=len(final)
    # word=""
    # length=0
    string1=""
    # spacer_sq=""
    # count=0
    # file2= open(r"F:\SEm2\SOP[BIO F266]\Output_Files\AAAG\spacer_Seq.txt", "a")
    # file2.write("Chr 1 data:\n\n")
    # file2.close()
    string1=""
    string2=data.split('\n')
    for i in range(0,len(string2)):
        string1=string1+string2[i]

    for j in range(0,len(string1)):
        if(string1[j]=='A'):
            l[0]= l[0] + 1 
        elif(string1[j]=='C'):
            l[1]= l[1] + 1  
        elif(string1[j]=='G'):
            l[2]= l[2] + 1 
        else:
             l[3]= l[3] + 1

    return len(string1)

li=[0]*4
file1=open(r"F:\SEm2\SOP[BIO F266]\Output_Files\AAAGACGT\spacer_Seq.txt", "r")
length = myfunc(file1,li)

for i in range(0,4):

    file2= open(r"F:\SEm2\SOP[BIO F266]\Output_Files\AAAGACGT\ACGT%.txt", "a")
    file2.write("%f\n" %((li[i]/length)*100))
    file2.close() 