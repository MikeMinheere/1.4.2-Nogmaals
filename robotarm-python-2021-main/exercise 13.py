from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 2
for i1 in range(0,7):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red' or color == 'green' or color == 'yellow' or color == 'blue' or color == 'white':
        for i in range(0,1+i1):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(0,1+i1):
            robotArm.moveLeft()
    else:break
robotArm.wait()