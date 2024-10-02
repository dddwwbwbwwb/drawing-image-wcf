from turtle import *

screensize(2000, 2000, 'white')
speed(9)
pencolor('red')
# pu()
goto(-300, -200)
pd()
fillcolor('red')
begin_fill()
for i in range(0, 2):
    fd(600)
    lt(90)
    fd(400)
    lt(90)
end_fill()

pu()
pencolor('yellow')
goto(-260, 120)
pd()
fillcolor('yellow')
begin_fill()
for i in range(0, 5):
    fd(113.137)
    rt(144)
end_fill()

list1 = [(-100, 160), (-60, 120), (-60, 60), (-100, 20)]
list2 = [31.98, 8.13, -15.59, -38.66]

for j in range(0, 4):
    seth(0)
    pu()
    goto(list1[j])
    lt(list2[j])
    bk(20)
    lt(18)
    pd()
    begin_fill()
    for i in range(0, 5):
        fd(113.137 / 3)  
        rt(144)
    end_fill()
pu()
ht()
done()

