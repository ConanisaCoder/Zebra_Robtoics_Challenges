program_running = input("Run program (t/f) :")
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
while program_running == "t":
    
    question = input("Enter the Aniaml: ").lower()
    if question in animals_babies:
        print("The baby of a " + (question)  + " is a " + str(animals_babies.get(question, "Animal is not on the list.")))
        program_running = input("Run program (t/f) :")
    else:
        print("Animal not list.")
        question_in = input("Would like to add this animal called " + (question) + ". (y/n): " ).lower()
        if question_in == "y":
            name = input("Enter the babies name: ")
            animals_babies[question] = name
            program_running = input("Run program (t/f) :")
else:
    input("Enter to close: ")
    