from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
for i in range(0,15):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for i in range(0,9):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(0,8):
            robotArm.moveLeft()
    else:robotArm.drop()
    robotArm.moveRight()
robotArm.wait()