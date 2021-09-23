from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 2
for i in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
    else:robotArm.drop()
    robotArm.moveRight()
robotArm.wait()