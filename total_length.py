def myfunc(file,chromo):
    data=file.read()
    
    length=len(data)
    final="ACGT"
    l1=len(final)
    count=0
    word=""
    length=0
    string1=""
    
    
    string2=data.split('\n')
    for i in range(0,len(string2)):
        string1=string1+string2[i]
    
    
    file2= open(r"F:\SEm2\SOP[BIO F266]\Output_Files\ACGT\freq.txt", "a")
    file2.write("Total length of chr %d= %d\n" %(chromo,len(string1)))
    file2.close()
    
        

file2= open(r"F:\SEm2\SOP[BIO F266]\Output_Files\ACGT\freq.txt", "a")
file2.write("\nSequence: CGTCA\n")
file2.close()
  


chro=1
file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome1.txt", "r")
myfunc(file1,chro)
chro=chro + 1

file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome2.txt", "r")
myfunc(file1,chro)
chro=chro + 1

file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome3.txt", "r")
myfunc(file1,chro)
chro=chro + 1

file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome4.txt", "r")
myfunc(file1,chro)
chro=chro + 1

file1=open(r"F:\SEm2\SEM 2-2\SOP[BIO F266]\Data\AT Genomw\promoter_chromosome5.txt", "r")
myfunc(file1,chro)





            
        
         
        
             
    
                
                
                
            

            
        
               

        
        
            
                
            