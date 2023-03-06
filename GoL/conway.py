"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import datetime

ON = 255
OFF = 0
vals = [ON, OFF]
grid_size = 200
frame = True
input = 'config/input3.txt'
output = 'config/output3.txt'
time = datetime.today().strftime('%Y-%m-%d')

#Still lifes
block = np.array([[0,   0,   0,   0],
                  [0, 255, 255,   0], 
                  [0, 255, 255,   0], 
                  [0,   0,   0,   0]])

beehive = np.array([[0,   0,   0,   0,   0,   0],
                    [0, 255,   0,   0, 255,   0],
                    [0,   0, 255,   0, 255,   0],
                    [0,   0,   0, 255,   0,   0],
                    [0,   0,   0,   0,   0,   0]])

loaf = np.array([[0,   0,   0,   0,   0,   0],
                 [0,   0, 255, 255,   0,   0],
                 [0, 255,   0,   0, 255,   0],
                 [0,   0, 255,   0, 255,   0],
                 [0,   0,   0, 255,   0,   0],
                 [0,   0,   0,   0,   0,   0]])

boat = np.array([[0,   0,   0,   0, 0],
                 [0, 255, 255,   0, 0], 
                 [0, 255,   0, 255, 0], 
                 [0,   0, 255,   0, 0],
                 [0,   0,   0,   0, 0]])

tub = np.array([[0,   0,   0,   0, 0],
                [0,   0, 255,   0, 0], 
                [0, 255,   0, 255, 0], 
                [0,   0, 255,   0, 0],
                [0,   0,   0,   0, 0]])

#Oscilators
blinker1 = np.array([[0,   0, 0],
                     [0, 255, 0], 
                     [0, 255, 0], 
                     [0, 255, 0],
                     [0,   0, 0]])
        
blinker2 = np.array([[0,   0,   0,   0, 0],
                     [0, 255, 255, 255, 0],
                     [0,   0,   0,   0, 0]])

toad1 = np.array([[0,   0,   0,   0,   0,   0],
                  [0,   0,   0, 255,   0,   0],
                  [0, 255,   0,   0, 255,   0],
                  [0, 255,   0,   0, 255,   0],
                  [0,   0, 255,   0,   0,   0],
                  [0,   0,   0,   0,   0,   0]])
        
toad2 = np.array([[0,   0,   0,   0,   0,   0],
                  [0,   0, 255, 255, 255,   0],
                  [0, 255, 255, 255,   0,   0],
                  [0,   0,   0,   0,   0,   0]])

beacon1 = np.array([[0,   0,   0,   0,   0,   0],
                    [0, 255, 255,   0,   0,   0],
                    [0, 255, 255,   0,   0,   0],
                    [0,   0,   0, 255, 255,   0],
                    [0,   0,   0, 255, 255,   0],
                    [0,   0,   0,   0,   0,   0]])

beacon2 = np.array([[0,   0,   0,   0,   0,   0],
                    [0, 255, 255,   0,   0,   0],
                    [0, 255,   0,   0,   0,   0],
                    [0,   0,   0,   0, 255,   0],
                    [0,   0,   0, 255, 255,   0],
                    [0,   0,   0,   0,   0,   0]])

#Spaceships
glider1 = np.array([[0,   0,   0,   0, 0],
                    [0,   0,   0, 255, 0], 
                    [0, 255,   0, 255, 0], 
                    [0,   0, 255, 255, 0],
                    [0,   0,   0,   0, 0]])

glider2 = np.array([[0,   0,   0,   0, 0],
                    [0, 255,   0, 255, 0], 
                    [0,   0, 255, 255, 0], 
                    [0,   0, 255,   0, 0],
                    [0,   0,   0,   0, 0]])
        
glider3 = np.array([[0,   0,   0,   0, 0],
                    [0,   0, 255,   0, 0], 
                    [0,   0,   0, 255, 0], 
                    [0, 255, 255, 255, 0],
                    [0,   0,   0,   0, 0]])
        
glider4 = np.array([[0,   0,   0,   0, 0],
                    [0, 255,   0,   0, 0], 
                    [0,   0, 255, 255, 0], 
                    [0, 255, 255,   0, 0],
                    [0,   0,   0,   0, 0]])

lwspaceship1 = np.array([[0,   0,   0,   0,   0,   0,   0],
                         [0, 255,   0,   0, 255,   0,   0], 
                         [0,   0,   0,   0,   0, 255,   0], 
                         [0, 255,   0,   0,   0, 255,   0],
                         [0,   0, 255, 255, 255, 255,   0],
                         [0,   0,   0,   0,   0,   0,   0]])
                    
lwspaceship2 = np.array([[0,   0,   0,   0,   0,   0,   0],
                         [0,   0,   0, 255, 255,   0,   0], 
                         [0, 255, 255,   0, 255, 255,   0], 
                         [0, 255, 255, 255, 255,   0,   0],
                         [0,   0, 255, 255,   0,   0,   0],
                         [0,   0,   0,   0,   0,   0,   0]])
                
lwspaceship3 = np.array([[0,   0,   0,   0,   0,   0,   0],
                         [0,   0, 255, 255, 255, 255,   0], 
                         [0, 255,   0,   0,   0, 255,   0], 
                         [0,   0,   0,   0,   0, 255,   0],
                         [0, 255,   0,   0, 255,   0,   0],
                         [0,   0,   0,   0,   0,   0,   0]])
            
lwspaceship4 = np.array([[0,   0,   0,   0,   0,   0,   0],
                         [0,   0, 255, 255,   0,   0,   0], 
                         [0, 255, 255, 255, 255,   0,   0], 
                         [0, 255, 255,   0, 255, 255,   0],
                         [0,   0,   0, 255, 255,   0,   0],
                         [0,   0,   0,   0,   0,   0,   0]])

def count(N, M, grid):
    blockCount = 0
    beehiveCount = 0
    loafCount = 0
    boatCount = 0
    tubCount = 0
    blinkerCount = 0
    toadCount = 0
    beaconCount = 0
    gliderCount = 0
    lwspaceshipCount = 0
    totalCount = 0
    for i in range(0, N):
        for j in range(0, M):
            if(np.array_equal(grid[i:i+4, j:j+4], block, equal_nan=True) ):
                blockCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+6], beehive, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+5], np.rot90(beehive), equal_nan=True) ):
                beehiveCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+6], loaf, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6], np.rot90(loaf), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6], np.rot90(loaf, 2), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6], np.rot90(loaf, 3), equal_nan=True)):
                loafCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+5], boat, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(boat), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(boat, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(boat, 3), equal_nan=True)):
                boatCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+5], tub, equal_nan=True) ):
                tubCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+3], blinker1, equal_nan=True) or np.array_equal(grid[i:i+3, j:j+5] , blinker2, equal_nan=True)):
                blinkerCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+6], toad1, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(toad1), equal_nan=True)):
                toadCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+4, j:j+6], toad2, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+4] , np.rot90(toad2), equal_nan=True)):
                toadCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+6], beacon1, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(beacon1), equal_nan=True)):
                beaconCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+6], beacon2, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(beacon2), equal_nan=True)):
                beaconCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+5], glider1, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider1), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider1, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5], np.rot90(glider1, 3), equal_nan=True)):
                gliderCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+5], glider2, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider2, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5], np.rot90(glider2, 3), equal_nan=True)):
                gliderCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+5], glider3, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider3), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider3, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5], np.rot90(glider3, 3), equal_nan=True)):
                gliderCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+5, j:j+5], glider4, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider4), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider4, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5], np.rot90(glider4, 3), equal_nan=True)):
                gliderCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+7], lwspaceship1, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lwspaceship1), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+7] , np.rot90(lwspaceship1, 2), equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6], np.rot90(lwspaceship1, 3), equal_nan=True)):
                lwspaceshipCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+7], lwspaceship2, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lwspaceship2), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+7] , np.rot90(lwspaceship2, 2), equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6], np.rot90(lwspaceship2, 3), equal_nan=True)):
                lwspaceshipCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+7], lwspaceship3, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lwspaceship3), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+7] , np.rot90(lwspaceship3, 2), equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6], np.rot90(lwspaceship3, 3), equal_nan=True)):
                lwspaceshipCount+=1
                totalCount+=1
                continue
            if(np.array_equal(grid[i:i+6, j:j+7], lwspaceship4, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lwspaceship4), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+7] , np.rot90(lwspaceship4, 2), equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6], np.rot90(lwspaceship4, 3), equal_nan=True)):
                lwspaceshipCount+=1
                totalCount+=1
                continue
    return totalCount, blockCount, beehiveCount, boatCount, tubCount, gliderCount, lwspaceshipCount, blinkerCount, toadCount, beaconCount, loafCount


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, N, M):

    global frame
    if frame: 
        frame = False
        return 

    resultado = count(N, M, grid)
    print("totalCount, blockCount, beehiveCount, boatCount, tubCount, gliderCount, lwspaceshipCount, blinkerCount, toadCount, beaconCount, loafCount")
    print(resultado)
    if frameNum+1 == grid_size:
        return
    
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    for i in range(0, N+2):
        for j in range(0, M+2):
            neighbourd = int((grid[i, (j-1)%M] + grid[i, (j+1)%M]+grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                              grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                              grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M])/ON)
            if(grid[i][j] == OFF):
                if(neighbourd == 3):
                    newGrid[i][j] = ON
            else:
                if(neighbourd < 2 or neighbourd > 3):
                    newGrid[i][j] = OFF
    
    # update data
    img.set_data(newGrid[1:N+1, 1:M+1])
    grid[:] = newGrid[:]
    print(frameNum+2)
    return img,

def readFile():
    file = open(input, "r")
    width, height = map(int, file.readline().split()[ : 2])
    gens = int(file.readline().split()[0])

    grid = np.zeros((width + 2) * (height + 2)).reshape(width + 2, height + 2)
    for line in file: 
        i,j = map(int, line.split()[:2])
        grid[i + 1][j + 1] = ON
    file.close()
    return width, height, gens, grid


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    
    if len(sys.argv) == 3:
        global input
        global output 
        input = sys.argv[1]
        output = sys.argv[2]

    # set animation update interval
    updateInterval = 100

    global grid_size
    N, M, grid_size, grid = readFile()
    writefile = open(output, "w")
    writefile.write(f"Simulation at {time}\n")
    writefile.write(f"Universe size {N} x {M}\n")
    writefile.write("\n")
    resultado = count(N, M, grid)
    writefile.write(f"totalCount, blockCount, beehiveCount, boatCount, tubCount, gliderCount, lwspaceshipCount, blinkerCount, toadCount, beaconCount, loafCount\n")
    writefile.write(f"Result: {resultado}")
    writefile.close()
   
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid[1:N + 1, 1:M+1], interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M),
                                  frames = grid_size,
                                  interval=updateInterval,
                                  save_count=100)

    plt.show()

# call main
if __name__ == '__main__':
    main()



   