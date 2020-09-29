def full_name(name, surname):
    print(f" Welcome {name} {surname}!")


if __name__ == "__main__":
    input_name = input("Please put your name:")
    input_surname = input("Please put your surname:")

    full_name(input_name,input_surname)