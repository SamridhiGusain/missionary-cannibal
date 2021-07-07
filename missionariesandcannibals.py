#%%
import copy
import sys

visited=[]
q = []

def is_valid(a):
    #checks the condition that number of missionaries and the number of cannibals should be positive
    if a[0]>=0 and a[1]>=0 and a[3]>=0 and a[4]>=0:
        #checks the condition that number of missionaries should be greater than the number of cannibals and if it is less , it should be 0
        if (a[0]==0 or a[0]>=a[1]) and (a[3]==0 or a[3]>=a[4]):
            
            return 1
        else:
            return 0
    else:
        return 0
#function to check if current state is equal to goal state
def is_goal(a,g):
    if a==g:
        return(1)
    else:
        return(0)
#movement of one missionary wrt left or right bank
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
        
#movement of one cannibal wrt left or right bank
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
            
#movement of two missionaries wrt left or right bank       
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
           
#movement of two cannibals wrt left or right bank
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
#movement of one missionary and one cannibal wrt left or right bank          
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
           
#performs search function to find the path for solution
def search(a,g):
    global q
    global visited
    q.append(a)

    while(1):
        if len(q)>0:
            current=q.pop(0)

            visited.append(current)
            

            
            if is_goal(current,g):
                for i in range (len(visited)):
                    print(visited[i])
                print("Number of states explored is ",len(visited))
                break
            else:
                one_m_one_c(current)
                one_c(current)
                one_m(current)
                two_c(current)
                two_m(current)
       
        
        else:
            print("NO SOLUTION FOUND")
            break

        

def main():
    a = [3,3,'L',0,0]
    g = [0,0,'R',3,3]

    search(a,g)
main()


# %%
