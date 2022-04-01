from random import randint

class Detali:
    def init(self, height, width, length,weight,color=None):
        self.height=height
        self.width=width
        self.length=length
        self.weight=weight
        self.color=color


    def get_in(self, name_queue):
        name_queue.list.insert((randint (0, name_queue.length - 1)), (self))
        name_queue.length += 1

    def __repr__(self):
        return f' Деталь: {self.color}, {self.width},{self.weight}, {self.height},{self.length}'
class Queue:
    def __init__(self):
        self.items = []  # все детали

    def isEmpty(self): #Наличие элементов в очереди
        return self.items == []

    def add_item(self, detail):
        self.queue.append(detail)
        self.length += 1

    def delete(self):
        if self.length == 0:
            raise ValueError('Список пуст!')
        else:
            self.queue.remove()
            self.length -= 1

    def len(self):
        return self.length

    def repr(self):
        return (self.queue)

    def add_txt(self):
        Myf = open('Detail.txt', 'w', encoding='utf-8')
        Myf.writelines(f'в цеху {len(self.queue)} деталей, {str(self.queue)} ')
        Myf.close()

q = Queue()

g= Detali('12', '12', '12', '11','black')
h = Detali('22','22','222','22','yellow')

q.add_item(g)
q.add_item(h)
b = Detali('10', "23", "10", "10", "white")
q.output()
q.add_txt()