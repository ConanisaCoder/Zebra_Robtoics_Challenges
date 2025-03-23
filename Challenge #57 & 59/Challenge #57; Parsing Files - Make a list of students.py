open_file = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #57 & 59/text.txt","r")
write_file = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #57 & 59/text.txt","a") 
readlines = open_file.readlines()
val_dict = {} 
x = True
for i in readlines:
        i.replace("\n","")
        student = i[:i.index(" ")].strip()
        student_grade = int(i[i.index(" ")+1:])
        val_dict[student] = student_grade
while x == True:
    def Avg_Grade():
            total_len = len(val_dict)
            total_num = 0
            for i in val_dict.values():
                total_num += i
            avg = total_num / total_len
            return avg
    def Top_Students():
            list_students = []
            grades = list(val_dict.values())
            grades.sort(reverse=True)
            val = 0
            for i in range(0,3,1):
                grade_index = grades[val]
                for students in val_dict:
                    if val_dict[students] == grade_index:
                        list_students.append(str(students) + ": " +str(grade_index))
                val += 1
            return list_students
    def List_Fail():
            students = val_dict.keys()
            failing_students = ""
            for student_var_1 in students:
                grade = val_dict[student_var_1]
                if grade < 50:
                    failing_students += student_var_1 + " "
            return failing_students
    def Add_Student_Add_grade():
            enter_student_name_first = input("Enter Student First Name: ").strip()
            enter_student_name_last = input("Enter Student Last Name: ").strip()
            while True:
                try:
                    grade =int(input("Enter grade: "))
                    break
                except ValueError:
                    print("Enter Int")
            line = "\n{}-{} {}".format(enter_student_name_first,enter_student_name_last,grade) 
            write_file.writelines(line)
            val_dict[str((enter_student_name_first)+"-"+(enter_student_name_last))] = grade
            return val_dict
    def Update_Score():
            new_dict = {}
            writetofile = []
            student_num = 0
            for student in val_dict:
                student_num_val = str(student_num)
                new_dict[student_num_val] = student
                student_num += 1
            for valkey in new_dict:
                print(f"{valkey}:{new_dict[valkey]}")
            print(f"Enter number between 0 - {student_num}: ")
            while True:
                try:
                    get_studentkey = int(input("Enter student number: "))
                    break
                except ValueError:
                    print("Enter int")
            if get_studentkey <0:
                get_studentkey = 0
            elif get_studentkey>student_num:
                get_studentkey = student_num
            get_studentkey = str(get_studentkey)
            while True:
                try:
                    new_grade = int(input("Enter new Grade: "))
                    break
                except ValueError:
                    print("Enter int")
            if new_grade<0:
                new_grade = 0
            elif new_grade > 100:
                new_grade = 100
            val_dict[new_dict[get_studentkey]] = new_grade
            for student in val_dict:
                line = "{} {}".format(student,val_dict[student])
                writetofile.append(line)
            writefile_new = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #57 & 59/text.txt","w")
            writefile_new.writelines("\n".join(writetofile))
            writefile_new.close()
    print("1) The Average Grade\n2) Top 3 performing students\n3) List of students Failing\n4) Add student and grade\n5) Update Score\n6) Exit")
    input_file = int(input("What would like to Know/Do: "))
    match input_file:
            case 1:
                print(Avg_Grade())
            case 2:
                print(Top_Students())
            case 3:
                print(List_Fail())
            case 4:
                print(Add_Student_Add_grade())
            case 5:
                Update_Score()
            case 6:
                x = False
write_file.close()
open_file.close()
exit()