pizza = int(input("Number of Pizza slices: "))
students = int(input("Number of students: "))
s_t = pizza // students
s_r = pizza % students

if s_r == 0:
    print(f"Each student gets {s_t}.")
if s_r > 0: 
    print(f"Each student gets {s_t}. There will be {s_r} leftover ")
