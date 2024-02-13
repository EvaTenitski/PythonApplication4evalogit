import random

print("Tere tulemast matemaatika testi!")

küsimuste_arv = int(input("Mitu küsimust soovite vastata? "))
raskustase = int(input("Valige raskustase (1-Kerge, 2-Keskmine, 3-Raske): "))

if raskustase == 1:
    num_range = (1, 10)
elif raskustase == 2:
    num_range = (10, 100)
elif raskustase == 3:
    num_range = (100, 1000)
else:
    print("Vigane raskustase. Seadistatakse keskmisele.")
    num_range = (10, 100)

tehted = ['+', '-', '', '/', '*']
õiged_vastused = 0

for i in range(küsimuste_arv):
    tehe = random.choice(tehted)
    num1 = random.randint(num_range[0], num_range[1])
    num2 = random.randint(num_range[0], num_range[1])

    if tehe == '+':
        vastus = num1 + num2
    elif tehe == '-':
        vastus = num1 - num2
    elif tehe == '*':
        vastus = num1 * num2
    elif tehe == '/':
      
        num2 = random.randint(1, num_range[1])
        vastus = num1 / num2
    elif tehe == '**':
        vastus = num1 ** num2

    print(f"Mis on {num1} {tehe} {num2}?")
    kasutaja_vastus = float(input("Teie vastus: "))

    if kasutaja_vastus == vastus:
        print("Õige!")
        õiged_vastused += 1
    else:
        print("Vale!")

tulemus = (õiged_vastused / küsimuste_arv) * 100
print("\nTest lõpetatud!")
print("Teie tulemus:", tulemus)
if tulemus < 60:
    print("Hinne: 2")
elif tulemus < 75:
    print("Hinne: 3")
elif tulemus < 90:
    print("Hinne: 4")
else:
    print("Hinne: 5")