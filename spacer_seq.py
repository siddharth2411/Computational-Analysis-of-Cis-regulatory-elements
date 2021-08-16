def myfunc(file):  
    data=file.read()

    length=len(data)
    final="AAAG"
    l1=len(final)
    word=""
    length=0
    string1=""
    spacer_sq=""
    count=0)
    string1=""
    string2=data.split('\n')
    for i in range(0,len(string2)):
        string1=string1+string2[i]
    last_index=0
    start_index=0

    flag=0      
    for j in range(0,len(string1)):
            
        word=string1[j:j+l1]
        
        if(word==final):
            last_index=j+l1
            flag=0
            for k in range(j+l1,len(string1)):
                next_word=string1[k:k+l1]
                if(next_word=="ACGT"):
                    start_index=k
                    flag=1
                if(flag==1):
                    break
            space=start_index-last_index
            
            if(space==10):
                spacer_sq = string1[last_index: start_index] 
                file2= open(r"F:\SEm2\SOP[BIO F266]\Output_Files\AAAGACGT\spacer_Seq.txt", "a")
                file2.write(spacer_sq)
                file2.write("\n")
                file2.close()               
            spacer_sq=""
            j=k
    

file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome1.txt", "r")
myfunc(file1)
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome2.txt", "r")
myfunc(file1)
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome3.txt", "r")
myfunc(file1)
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome4.txt", "r")
myfunc(file1)
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome5.txt", "r")
myfunc(file1)