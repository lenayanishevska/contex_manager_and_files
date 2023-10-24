def copy_files():
    with open("first_file.txt", "r") as source, open("second_file.txt", "w") as destination:
        destination.write(source.read().upper())
