'''
создайте класс Soda  для определение газированый воды,
принимающий 1 аргумент отвечающий за добавку.
В этом классе реализуйте метод show_my_drink(), выводящий на печать
Газировка и {Добавка} в случае наличии добавки и Обычная газировка если нет добавки
'''

class Soda:
    def __init__(self, admixture: str=None) -> None:
        if isinstance(admixture, str):
            self.admixture = admixture
        else:
            self.admixture = None
    
    
    def show_my_drink(self):
        return 'Обычная газировка'if self.admixture is None else f'Газировка и {self.admixture}' 
    
    
t = Soda(99889)
print(t.show_my_drink())    