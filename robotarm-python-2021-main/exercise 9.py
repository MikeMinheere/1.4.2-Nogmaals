from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 3
for i1 in range(0,4):
    for i in range(0,1 + i1):
        robotArm.grab()
        for x in range(0,5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()