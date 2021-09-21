import time
aantal = 0
week = "ma","di","wo","do","vr","za","zo"
dag = input('type hier uw dag met een afkorting. bijv. ma of wo ')
while dag != week[aantal]:
    print(week[aantal])
    aantal += 1
    time.sleep(1)
print(dag)

#getest door martijn4