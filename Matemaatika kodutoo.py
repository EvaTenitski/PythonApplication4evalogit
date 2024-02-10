import random

print("*** Proverka znanij po matematike ***")
print()
print("Vali raskustase:")
print("1. Prosto")
print("2. Srendnee")
print("3. Tazelo")
difficulty = int(input("Sisesta raskustaseme number (1/2/3): "))
while difficulty not in [1, 2, 3]:
    print("viga! Sisesta korrektne raskustaseme number.")
    difficulty = int(input("Sisesta raskustaseme number (1/2/3): "))

total_problems = int(input("Sisesta lahendamiseks vajalike ülesannete arv: "))
correct_answers = 0

for _ in range(total_problems):
    num1 = random.randint(1, 10 ** difficulty)
    num2 = random.randint(1, 10 ** difficulty)
    if difficulty == 3:
        operation = random.choice(['+', '-', '*', '/', '**'])
    else:
        operation = random.choice(['+', '-', '*', '/'])
    problem = f"{num1} {operation} {num2}"
    correct_answer = eval(problem)
    user_answer = float(input(f"Lahenda ülesanne: {problem} = "))
    if user_answer == correct_answer:
        print("Pravilno!")
        correct_answers += 1
    else:
        print("Nepravilno.")

percentage_correct = (correct_answers / total_problems) * 100

print("\nTulemused:")
print(f"Said lahendatud {correct_answers} ülesannet {total_problems}-st.")
print(f"Sinu õigete vastuste protsent: {percentage_correct}%")
if percentage_correct < 60:
    print("Hinne 2")
elif percentage_correct < 75:
    print("Hinne 3")
elif percentage_correct < 90:
    print("Hinne 4")
else:
    print("Hinne 5")