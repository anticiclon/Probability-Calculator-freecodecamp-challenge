# -*- coding: utf-8 -*-
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colores):
        self.contents = []
        for key, value in colores.items():
            for i in range(value):
                self.contents.append(key)
        
    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        resultado = []
        for i in range(number):
            idx = random.choice(range(0, len(self.contents)))
            resultado.append(self.contents[idx])
            self.contents = self.contents[:idx] + self.contents[idx+1:]
        return resultado


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        
        expected_copy = copy.deepcopy(expected_balls)
        for colour in balls:
            if colour in expected_copy:
                expected_copy[colour] -= 1
        
        if all([x < 1 for x in expected_copy.values()]):
            count += 1
    return count/num_experiments
