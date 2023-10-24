import random


def from_A_to_Z():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in alphabet:
        file_name = "files/" + i + ".txt"
        with open(file_name, "w") as file:
            file.write(str(random.randint(1, 100)))

    with open('summary.txt', 'w') as summary:
        for i in alphabet:
            filename = "files/" + i + '.txt'
            with open(filename, 'r') as file:
                summary.write(f"{filename}: {int(file.read())}\n")
