import re
t=int(input())
for _ in range(t):
    s=list(input())
    q=int(input())
    count1 = sum(1 for i in range(len(s) - 3) if s[i:i + 4] == ['1', '1', '0', '0'])
    for j in range(q):
        i,v=map(int,input().split())
        i-=1
        before= sum(1 for i in range(max(0,i-3),(min(i+3,len(s))+1)) if s[i:i + 4] == ['1', '1', '0', '0'])
        s[i]=str(v)
        after= sum(1 for i in range(max(0,i-3),(min(i+3,len(s))+1)) if s[i:i + 4] == ['1', '1', '0', '0'])
        count1= count1+(after-before)
        if count1>0:
            print("YES")
        else:
            print("NO")
            
        

'''
    foundat=[]
    if m:
        foundat.append(m.start())
    for j in range(q):
        i,v=map(int,input().split())
        i-=1
        s=s[:i]+str(v)+s[i+1:]
        if len(foundat)>0:
            if (i not in foundat) and (i+1 not in foundat) and (i+2 not in foundat) and (i+3 not in foundat) :
                print("YES")
                foundat.append(i)
                
            else:
                if i in foundat :
                    if v==1:
                        foundat.remove(i)
                        print("NO")
                    else:
                        print("YES")
                        

                elif i+1 in foundat:
                    if v==1:
                        foundat.remove(i+1)
                        print("NO")
                    else:
                        print("YES")

                          
                elif i+2 in foundat:
                    if v==0:
                        foundat.remove(i+2) 
                        print("NO") 
                    else:
                        print("YES")    
                elif i+3 in foundat:
                    if v==0:
                        foundat.remove(i+3) 
                        print("NO") 
                    else:
                        print("YES")       

            
        else:
            if i==0 or i==1:
                j=0
            else:
                j=i-1    
            if i==0 or i==1 or i==2:
                k=0
            else:
                k=i-2     
            if v==1 and '1100' ==s[j:i+3]:
                print("YES")
                foundat.append(j)
            elif v==0 and '1100' == s[k:i+2]:
                print ("YES")
                foundat.append(k)
            else:
                print ("NO")         
  '''