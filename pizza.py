import numpy
file=open("d_big.in","r")
l=file.readline()
r,c,min_i,max_c=[int(n) for n in l.split()]
l=list(file)
#l=l[1::]
print(l)
i=0;j=0;res=[]
while(i<r):
    j=0;
    while(j<c):
        z=j;t=0;m=0;
        while(z-j<max_c and z<=c):
            if(l[i][z]=='T'):
                t+=1;
            elif(l[i][z]=='M'):
                m+=1;
            if(m>=min_i and t>=min_i):
                res.append([i,j,i,z]);
                j=z+1;t=0;m=0;
            z+=1;
        j=j+1
    i+=1;


                
x=[len(res)];a=[]
y=['\0' for n in range(len(res[0])-1)]
x.extend(y)
a.append(x)
a.extend(res)
#print(a)
numpy.savetxt('big.in',a,fmt="%s")
