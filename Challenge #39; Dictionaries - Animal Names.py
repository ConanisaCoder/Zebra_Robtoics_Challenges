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
question = input("Enter the Aniaml: ").lower()
if question in animals_babies:
    print("The baby of a " + (question)  + " is a " + str(animals_babies.get(question, "Animal is not on the list.")))
else:
    print("Animal not list.")