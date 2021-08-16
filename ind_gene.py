with  open(r"C:\Users\Admin\Desktop\TAIR10_upstream_1000_20101104.txt", "r") as file:
    data=file.readlines()
      
    final="CGTCA"
    count=0
    lines=[]
    gene=0
    for i in range(0,len(data)):
        line=data[i]
        if(line[0]!='>' and i<len(data)-1):
            
            lines.append(data[i])

        elif(i==(len(data)-1)):
           
            lines.append(data[i])
                
            for single in lines:
                for k in range(0,len(single)):
                    word=single[k:k+5]
                    if(word==final):
                        count=count + 1
                        k=k+5
            file2= open(r"C:\Users\Admin\Desktop\Final_data.txt", "a")
            file2.write("Gene no: %d frequency: %d\n" %(gene, count))
            file2.close()


        else:
            
           
            gene=gene+1
            if(gene>1):
                
                for single in lines:
                    for k in range(0,len(single)):
                        word=single[k:k+5]
                        if(word==final):
                            count=count + 1
                            k=k+5
                file2= open(r"C:\Users\Admin\Desktop\Final_data.txt", "a")
                file2.write("Gene no: %d frequency: %d\n" %(gene-1, count))
                file2.close()
                count=0
                lines.clear()
            

            
        
               

        
        
            
                
            