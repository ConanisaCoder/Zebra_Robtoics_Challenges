num = int(input("Enter number: "))
def show_stars(num):
    star = "*"
    star_add = "*"
    for i in range (1,num,1):
        print(star)
        star += star_add
    print(star)
show_stars(num)
