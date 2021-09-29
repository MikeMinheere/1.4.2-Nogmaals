from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
for i in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for x in range(0,9):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,9-i):
            robotArm.moveLeft()
    else:robotArm.drop()
    robotArm.moveRight()
robotArm.wait()