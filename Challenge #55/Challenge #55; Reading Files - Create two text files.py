read_Odd_words = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #55/oddWords.txt","r")
read_Even_words =open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #55/evenWords.txt","r")
string = ""

while True:
    read_even = read_Even_words.readline()
    read_Odd_word = read_Odd_words.readline()
    if not read_even and not read_Odd_word:
        break
    print(read_Odd_word,end="")
    print(read_even,end="")
read_Odd_words.close()
read_Even_words.close()
