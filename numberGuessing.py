import random

computer = random.randint(1, 10)

for i in range(3):
    print(f"Percubaan {i + 1}/3")

    user = int(input("Teka nombor (1-10): "))


    if user == computer:
        print("Tahniah! Anda Menang!")
        break
    else:
         print("Salah! Cuba lagi.")