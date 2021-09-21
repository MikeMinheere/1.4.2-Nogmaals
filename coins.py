# name of student: Mike Minheere
# number of student: 99067548 

toPay = int(float(input('Amount to pay: '))* 100) #
payed = int(float(input('Payed amount: ')) * 100) #
change = payed - toPay #dit is de formule voor het uitrekenen van de hoeveelheid geld watje terugkrijgt

if change > 0: #je moet meer dan 0 cent terug kijgen om de code te starten
  coinValue = 200 #de standaart waarde van de munt
  
  while change > 0 and coinValue > 0: #als er geld is om terug te geven, moet hij de loop uitvoeren.
    nrCoins = change // coinValue #de formule om de hoeveelheid munten van een waarde uit te rekenen.

    if nrCoins > 0: #als er meer dan 0 munten moeten worden teruggegeven print dan dit:
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #hier print die hoeveel munten je van een bepaalde waarde kan terugkrijgen.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #hier vraagt die hoeveel munten van een bepaalde waarde hebt teruggegeven.
      change -= nrCoinsReturned * coinValue #hier word de totale som van aantal munten * waarde van munten, afgetrokken van hoeveel er in totaal teruggegeven moet worden

# hier kijkt hij naar de waarde van de munt en vermindert het.
    if coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als na al die code uitvoeren, nog niet al het geld is teruggegeven, print die regel 38.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')