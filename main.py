class Stu:
    pass
a=[]
n=int(input("Введите кол-во студентов "))
def g(*args):
    for i in range(n):
        a.append(Stu())
    for i in range(n):
        a[i].Surname=input("Введите фамилию ")
        a[i].ball = int(input("Введите балл "))
    for i in range(n):
        print(a[i].Surname,a[i].ball)

g()
