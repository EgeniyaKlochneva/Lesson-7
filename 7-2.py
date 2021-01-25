from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def tissue_consumption(self):
        return f"Суммарго ткани{self.param / 6.5 + 0.5 + 2 * self.param + 0.3}"
     #не считает суммарный расход ткани..
    # не могу сообразить как вывести. или какой параметр передать, чтоб считал

    @abstractmethod
    def abstract(self):
        pass


class Coat(Clothes):
    def tissue_consumption(self):
        return f'Для пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        pass


class Costume(Clothes):
    def tissue_consumption(self):
        return f'Для костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(48)
costume = Costume(1.65)


print(coat.tissue_consumption())
print(costume.tissue_consumption())
print(Clothes.tissue_consumption)
a = Clothes
print(a.tissue_consumption)




