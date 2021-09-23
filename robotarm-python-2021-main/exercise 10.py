from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 3
for i1 in range(0,5):
    robotArm.grab()
    for i in range(0,9-i1*2):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(0,8-i1*2):
        robotArm.moveLeft()
robotArm.wait()