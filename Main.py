import Algorithm as MyAlgo
import matplotlib.pyplot as plt
import time
"""
    The A * algorithm is that the robot located in a certain position only
reaches the target in the shortest way by going to the right, left, up and down.
    In the A * algorithm, this is found with h (n) + g (n).
    So it is a combination of Greedy Approach and Bert First Search Algorithm.
    Hakan SERAY
"""
#A * Algorithm is a combination of two different approaches, resulting in a higher quality approach.
#1-) Uniform Cost Search = g(n) Greedy Approach (Gerçekler)
#2-) Best First Search = h(n) Best First Search (Sezgisel(Kuş uçuşu mesafe))
#3-) A* Algorithm = g(n) + h(n)

X_Yol = []
Y_Yol = []

# The robot's starting point
MyRobot = MyAlgo.Robot(1, 0)
# The robot's starting point
# Everthing is Auto




Start_X = [MyRobot.x+.5]
Start_Y = [MyRobot.y+.5]
for i in range(150000):
    MyRobot.printLocation()
    if (MyRobot.x == 2 and MyRobot.y == 12):
        print( "I reached my goal in",i,"steps")
        i = 150000
        break
    yonler = MyAlgo.Yonler(MyRobot.x, MyRobot.y)
    print(yonler)
    min = 100
    hareket = "Stop"  # q nun değeri  0 = left , 1 = up, 2 = right, 3 = down
    for q in range(4):
        if (yonler[q][0] > 0):
            if (min > yonler[q][1]):
                min = yonler[q][1]
                if (q == 0):
                    hareket = "Go Left"
                if (q == 1):
                    hareket = "Go Up"
                if (q == 2):
                    hareket = "Go Right"
                if (q == 3):
                    hareket = "Go Down"

    print(hareket, min)
    if (hareket == "Go Left"):
        MyRobot.y = MyRobot.y - 1
    if (hareket == "Go Up"):
        MyRobot.x = MyRobot.x - 1
    if (hareket == "Go Right"):
        MyRobot.y = MyRobot.y + 1
    if (hareket == "Go Down"):
        MyRobot.x = MyRobot.x + 1
        
    X_Yol.append(MyRobot.x+0.5)
    Y_Yol.append(MyRobot.y+0.5)




Blocks_X = [2.5,1.5,2.5,3.5,1.5,2.5,1.5,2.5,1.5,2.5,3.5,1.5]
Blocks_Y = [1.5,3.5,3.5,3.5,6.5,6.5,7.5,7.5,10.5,10.5,10.5,11.5]
Goal_Y =[2.5,2.5,2.66,2.35]
Goal_X=[12.8,12.25,12.5,12.5]

print("Drawing Begins")
numb = len(X_Yol)
#Drawing of the target and walls
for x in range(numb):
    print(x+1,"Steps")
    axes = plt.gca()
    axes.set_xlim([0,14])
    axes.set_ylim([0,5])
    plt.arrow(1,0,1,1000000)
    plt.arrow(2,0,1,1000000)
    plt.arrow(3,0,1,1000000)
    plt.arrow(4,0,1,1000000)
    plt.arrow(5,0,1,1000000)
    plt.arrow(6,0,1,1000000)
    plt.arrow(7,0,1,1000000)
    plt.arrow(8,0,1,1000000)
    plt.arrow(9,0,1,1000000)
    plt.arrow(10,0,1,1000000)
    plt.arrow(11,0,1,1000000)
    plt.arrow(12,0,1,1000000)
    plt.arrow(13,0,1,1000000)
    
    
    plt.arrow(0,1,1000000,1)
    plt.arrow(0,2,1000000,1)
    plt.arrow(0,3,1000000,1)
    plt.arrow(0,4,1000000,1)
    
    plt.scatter(Start_Y,Start_X)
    plt.scatter(Blocks_Y,Blocks_X)
    plt.scatter(Goal_X,Goal_Y)
    plt.scatter(Y_Yol[x],X_Yol[x],c='#8c564b')
    plt.show()
    time.sleep(1)
print("The table drawn is the symmetrical version of the table drawn with plt.")                
                                                















