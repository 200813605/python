max_people = 10
family = []
def fun1():
    print 'Your family consists of ' + str(people) + ' person:'

def func2():
    print 'Your family consists of ' + str(people) + ' people:'

def func3():
    family = answer
    family += ', '
    func1()
def func4():
    family += ', '
    func2()
def func5():
    family += (answer)
    family += ', '
    func2()
for people in range(max_people):
    answer = raw_input ('Type one person\'s name that is in your family ')
    if people == 1:
        func3()
    elif people == max_people:
        func4()
        break
    else:
        func5()
    print (family)
