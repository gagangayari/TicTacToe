# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:18:28 2020

@author: Gagan
"""

board=[[0,0,0],[0,0,0],[0,0,0]]

def board_view(board):
    print("   a  b  c")
    for count,row in enumerate(board):
        print(count,row)
def check_horizontal(board):
    for row in board:
        if(row.count(row[0])==len(row) and row[0]!=0):
            print("Player : ",row[0]," won !!")
            return True


def check_vertical(board):
    board_T=[]
    for i in range(len(board)):
        temp=[]
        for j in range(len(board)):    
            col=board[j][i]
            temp.append(col)
        # print(temp)
        board_T.append(temp)
    
    # print(board_T)
    for row in board_T:
        if(row.count(row[0])==len(row) and row[0]!=0):
            print("Player : ",row[0]," won !!")
            return True

def check_diagonal(board):
    flag_1=True
    count1=0
    for i in range(len(board)-1):
        if(board[i][i]!=board[i+1][i+1]):
            flag_1=False
        
        if(flag_1==False):
            break
        count1+=1
        if(count1==2 and board[0][0]!=0):
            print("Player : ",board[0][0]," won !!")
            return True
    
    """Diagonal from other end"""
    
    flag_2=True
    list1=list(range(0,len(board)))
    list2=reversed(list1)
    
    count2=0
    
    for p,q in zip(list1,list2):
        if(board[p][q]!=board[p+1][q-1]):
            flag_2=False
        
        if(flag_2==False):
            break
        
        count2+=1
        if(count2==2 ):
            if(board[0][2]!=0):
                print("Player : ",board[0][2]," won !!")
                return True
            break
    
#%%

def game(board):    
    board_view(board)
    player=1
    while(True):

        co_ord=(input("Player "+str(player)+" enter position ( hint=like a0,b2 ,c1 etc.00 to exit) : "))
        if(co_ord=="00"):
            print("Game Over ! ")
            break
        # processing of Input
        my_dict={'a':0,'b':1,'c':2}
        index_1=my_dict[co_ord[0]]
        index_2=int(co_ord[1])

        ##Check if already co-ordinate occupied
        if(board[index_1][index_2]!=0):
            print("Space already occupied by player {}\n".format(board[index_1][index_2]))
            continue
        
        # print(co_ord)
        board[index_2][index_1]=player
        
        board_view(board)
        if(check_horizontal(board) or check_vertical(board) or check_diagonal(board)):
            break
        if(player==2):
            player=1
            continue
        
        
        player+=1
        

  
game(board)


# %%
