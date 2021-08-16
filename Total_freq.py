def myfunc(file,chromo,tot):
    data=file.read()
    
    length=len(data)
    final="AAAG"
    l1=len(final)
    count=0
    word=""
    length=0
    string1=""
    
    
    string2=data.split('\n')
    for i in range(0,len(string2)):
        string1=string1+string2[i]
   
    flag = 0  
    for j in range(0,len(string1)):
            
        word=string1[j:j+l1]
        
        if(word==final):
            # last_index=j+l1
            flag=0
            for k in range(j+l1,len(string1)):
                next_word=string1[k:k+l1]
                if(next_word=="ACGT"):
                    count = count + 1
                    flag=1
                if(flag==1):
                    break

            j=k+l1        
    tot=tot+count
    
    file2= open(r"F:\SEm2\SOP[BIO F266]\Output_Files\AAAGACGT\freq.txt", "a")
    file2.write("Chromosome: %d 'AAAG' FREQUENCY: %d\n" %(chromo,count))
    file2.close()
    return tot
        

file2= open(r"F:\SEm2\SOP[BIO F266]\Output_Files\AAAGACGT\freq.txt", "a")
file2.write("\nGenome data:\n")
file2.close()
  

total=0
chro=1
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome1.txt", "r")
total=myfunc(file1,chro,total)
chro=chro + 1

file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome2.txt", "r")

total=myfunc(file1,chro,total)
chro=chro + 1
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome3.txt", "r")

total=myfunc(file1,chro,total)
chro=chro + 1
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome4.txt", "r")

total=myfunc(file1,chro,total)
chro=chro + 1
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome5.txt", "r")
 
total=myfunc(file1,chro,total)

file2= open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Output_Files\Total freq.txt", "a")
file2.write("\n\nTOTAL FREQUENCY: %d" %(total))
file2.close()

