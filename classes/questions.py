import random

class Questions:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.operation = (1,2,3,4)
        self.current_operation = 0
        self.answer = 0
        self.wrong_answer = []
        self.symbol = ''

    def generate_numbers(self):
        self.n1 = random.randint(1, 20)
        self.n2 = random.randint(self.n1, self.n1 + 20)

    def generete_question(self):
        self.current_operation = random.choice(self.operation)
        if self.current_operation == 1:
            self.answer = self.n1 + self.n2
            self.symbol = '+'

        elif self.current_operation == 2:
            self.answer = self.n2 - self.n1
            self.symbol = '-'

        elif self.current_operation == 3:
            self.answer = self.n1 * self.n2
            self.symbol = '*'

        elif self.current_operation == 4:
            self.answer = self.n2 // self.n1
            self.symbol = '//'

    def generate_wrong_answers(self):
        self.wrong_answer = [self.answer + 3, self.answer - 5, self.answer + 7 ]
        

    def run(self):
        self.generate_numbers()
        self.generete_question()
        self.generate_wrong_answers()
        print('n1', self.n1)
        print('n2', self.n2)
        print('operação', self.current_operation)
        print('resposta', self.answer)
        print('respostas erradas', self.wrong_answer)