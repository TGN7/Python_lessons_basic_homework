# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

# разбиремся в делах... 
def file_handle(file):
    f = open(file, 'r', encoding='UTF-8')
    for i in f.readlines():
        if i.count('Имя') == 1:
            continue
        else:
            name, subname, salary, role, target = i.split()
            workman = Person(name, subname, salary, role, target)
            workman.read_people_hours()
            salary = workman.calc_money()
            workman.write_money(salary)
    f.close()

# создаем класс
class Person:
    def __init__(self, name, subname, salary, role, target):
        self.name = name
        self.subname = subname
        self.money = int(salary)
        self.role = role
        self.target = int(target)
        self.people_hours = 0
 
# читаем файл hours_of, определяем имя name, фамилию subname, выработаные часы people_hours
    def read_people_hours(self):
        with open('hours_of', 'r', encoding='UTF-8') as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.subname:
                    self.people_hours = int(i.split()[2])

# вычисляем зарплату исходя из оклада salary            
    def calc_money(self):
        for_hour = self.money // self.target
        salary = 0
#вычисялем зарплату с учетом переработки overlad
        if self.people_hours > self.target:
            overload = self.people_hours - self.target
            salary = (overload * for_hour) * 2
            return (salary + self.money)
#вычисялем зарплату с учетом недоработок
        elif self.people_hours < self.target:
            overload = self.target - self.people_hours
            salary = overload * for_hour
            return (self.money - salary)
#ну или чистый оклад
        else:
            return (self.money)
 
# записываем зарплату к выдаче в файл payout.txt, файл записываем под ноги
    def write_money(self, salary):
        with open('payout.txt', 'a', encoding='UTF-8') as f:
            f.write(self.name + ' ' + self.subname + ' ' + str(salary) + '\n')
        
file_handle('workers')