run_program = input("Run program (y/n): ").lower()
animals_babies = {'hippo' : "calf",
                    "horse" : "foal ",
                    "dog" : "pup",
                    "kangaroo" : "joey",
                    "monkey" : "infant",
                    "owl" : "owlet",
                    "parrot" : "chick",
                    "rabbit" : "bunny",
                    "rat" : "pup",
                    "cow" : "calf",
                    "shunk" : "kit",
                    "sheep" : "lamb"}
while run_program == "y":
    print("1) Look up animal babies\n2) Add animal and baby\n3) Delete animal and baby\n4) Quit")
    input_ = input("Enter: ")
    if input_ == "1":
        find = input("Enter animal: ")
        print(str(animals_babies.get(find, "Animal not Dictionarie")))
    elif input_ == "2":
        animal = input("Enter Animal: ")
        baby = input("Enter baby: ")
        animals_babies[animal] = baby
    elif input_ == "3":
        print(animals_babies)
        remove = input("Enter item to remove: ")
        animals_babies.pop(remove)
    elif input_ == "4":
        break