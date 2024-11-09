
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f"Вычисления: CPU = {self.__cpu} и Memory = {self.__memory}, результат = {self.__cpu * self.__memory}"

    def __str__(self):
        return f"Computer: CPU = {self.__cpu}, Memory = {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            operator = "Beeline"
        elif sim_card_number == 2:
            operator = "MegaCom"
        elif sim_card_number == 3:
            operator = "O!"
        else:
            operator = "Неизвестный оператор"

        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {operator}")

    def __str__(self):
        return f"Phone: SIM Cards = {self.__sim_cards_list}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Строится маршрут до {location}..")

    def __str__(self):
        return f"SmartPhone: CPU = {self.cpu}, Memory = {self.memory}, SIM Cards = {self.sim_cards_list}"

computer = Computer(cpu=3.4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MegaCom", "O!"])
smartphone1 = SmartPhone(cpu=2.8, memory=8, sim_cards_list=["Beeline", "MegaCom"])
smartphone2 = SmartPhone(cpu=3.0, memory=12, sim_cards_list=["Beeline", "O!"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer.make_computations())

phone.call(1, "+996 222 38 38 18")
phone.call(2, "+996 555 39 39 19")
phone.call(3, "+996 707 37 37 17")

smartphone1.use_gps("Бишкек")
smartphone2.use_gps("Ош")

print(computer == smartphone1)
print(computer < smartphone2)
print(smartphone1 > smartphone2)
