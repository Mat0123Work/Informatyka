import random
nazwa_pliku = "potegi.txt"
# funkcja do generowania liczb w pliku "potegi.txt"
def gen_example_numbers():
    with open(nazwa_pliku, 'w', encoding="utf-8") as open_file:
        for _ in range(5000):
            open_file.write(str(random.randint(1, 1000))+ "\n")

gen_example_numbers()