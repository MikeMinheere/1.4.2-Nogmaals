import time
kaas = 'kaas'
woord = input("type hier het woord 'kaas' ")
while woord != kaas:
    time.sleep(1)
    woord = input("type hier het woord 'kaas' ")
print("goed gedaan!")