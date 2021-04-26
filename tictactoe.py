grid={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

def printgrid(a):
    print(a[1]+ ' '+ a[2]+' '+a[3])
    print(a[4]+ ' '+ a[5]+' '+a[6])
    print(a[7]+ ' '+ a[8]+' '+a[9])

#funct for input and checking if won
def player(grid,turn,i):
        
    print('Player '+ turn +', choose the box :')
        
    turn1=int(input())

    if grid[turn1]==' ':
        grid[turn1]=turn
        printgrid(grid)
        

    else:
        print('Already full, Please try again.:')
        player(grid,turn,i)


    if (i >=4):

        if ( grid[1]==grid[2]==grid[3]==turn or grid[4]==grid[5]==grid[6]==turn or grid[7]==grid[8]==grid[9]==turn or grid[1]==grid[4]==grid[7]==turn or grid[2]==grid[5]==grid[8]==turn or 
                grid[3]==grid[6]==grid[9]==turn or grid[1]==grid[5]==grid[9]==turn or grid[3]==grid[5]==grid[7]==turn):
                printgrid(grid)
                print(turn +' WON')
                return 1


def game():

    turn='o'
    
    for i in range(10):

        #if loop runs to end, Tie game
        if i==9:
            print("tie game")
            break

        #if anyone won , exit
        if(player(grid,turn,i)==1):
            break        

            #change player
        if(turn=='x'):
            turn='o'
        else:
            turn='x'     
        
        

    print("Thanks for playing!!")

game()        