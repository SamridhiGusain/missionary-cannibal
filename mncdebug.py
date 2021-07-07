#%%
import copy
import sys

visited=[]
q = []
j=int(0)

def is_valid(a):
    if a[0]>=0 and a[1]>=0 and a[3]>=0 and a[4]>=0:
        if (a[0]==0 or a[0]>=a[1]) and (a[3]==0 or a[3]>=a[4]):
            
            return 1
        else:
            return 0
    else:
        return 0

def is_goal(a,g):
    if a==g:
        return(1)
    else:
        return(0)
def one_m(a):
    temp = copy.deepcopy(a)
    if temp[2]=='L':
        temp[0]=temp[0]-1 
        temp[3]=temp[3]+1
        temp[2]='R'
    elif temp[2]=='R':
        temp[0]=temp[0]+1 
        temp[3]=temp[3]-1
        temp[2]='L'
    
    if is_valid(temp):
        if temp not in q and temp not in visited:
            q.append(temp)
            print("one_m applied on ", a ," to give state ", temp)
        else:
            print("one_m: already visited state",temp)
    else:
        print("one_m not applicable on ", a)
        

def one_c(a):
    temp = copy.deepcopy(a)
    if temp[2]=='L':
        temp[1]=temp[1]-1 
        temp[4]=temp[4]+1
        temp[2]='R'
    elif temp[2]=='R':
        temp[1]=temp[1]+1 
        temp[4]=temp[4]-1
        temp[2]='L'
    
    if is_valid(temp):
        if temp not in q and temp not in visited:
            q.append(temp)
            print("one_c applied on ", a ," to give state ", temp)
        else:
            print("one_c: already visited state",temp)
    else:
        print("one_c not applicable on ", a)
            
        
def two_m(a):
    temp = copy.deepcopy(a)
    if temp[2]=='L':
        temp[0]=temp[0]-2 
        temp[3]=temp[3]+2
        temp[2]='R'
    elif temp[2]=='R':
        temp[0]=temp[0]+2 
        temp[3]=temp[3]-2
        temp[2]='L'
    
    if is_valid(temp):
        if temp not in q and temp not in visited:
            q.append(temp)
            print("two_m applied on ", a ," to give state ", temp)
        else:
            print("two_m: already visited state",temp)
    else:
        print("two_m not applicable on ", a)
           

def two_c(a):
    temp = copy.deepcopy(a)
    if temp[2]=='L':
        temp[1]=temp[1]-2 
        temp[4]=temp[4]+2
        temp[2]='R'
    elif temp[2]=='R':
        temp[1]=temp[1]+2 
        temp[4]=temp[4]-2
        temp[2]='L'
    
    if is_valid(temp):
        if temp not in q and temp not in visited:
            q.append(temp)
            print("two_c applied on ", a ," to give state ", temp)
        else:
            print("two_c: already visited state",temp)
    else:
        print("two_c not applicable on ", a)
           
def one_m_one_c(a):
    temp = copy.deepcopy(a)
    if temp[2]=='L':
        temp[0]=temp[0]-1 
        temp[1]=temp[1]-1 
        temp[3]=temp[3]+1
        temp[4]=temp[4]+1
        temp[2]='R'
    elif temp[2]=='R':
        temp[0]=temp[0]+1 
        temp[1]=temp[1]+1 
        temp[3]=temp[3]-1
        temp[4]=temp[4]-1
        temp[2]='L'
    
    if is_valid(temp):
        if temp not in q and temp not in visited:
            q.append(temp)
            print("one_m_one_c applied on ", a ," to give state ", temp)
        else:
            print("one_m_one_c: already visited state",temp)
    else:
        print("one_m_one_c not applicable on ", a)
           

def bfs_search(a,g):
    global q
    global visited
    global j
    q.append(a)

    while(1):
        if len(q)>0:
            current=q.pop(0)
            print("*********LEVEL ",j,"***********" )
            visited.append(current)
            print("current: ",current)
            print("open queue: ",q)
            print("visited: ",visited)

            


            if is_goal(current,g):
                for xs in visited:
                    print(" ".join(map(str, xs)))
                print("Number of states explored is ",len(visited))
                break
            else:
                one_m_one_c(current)
                one_c(current)
                one_m(current)
                two_c(current)
                two_m(current)
            j=j+1
       
        
        else:
            print("NO SOLUTION FOUND")
            break

        

def main():
    a = [3,3,'L',0,0]
    g = [0,0,'R',3,3]

    bfs_search(a,g)
main()


# %%
