import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # if request exceeds available balls, return everything
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        drawn = []

        for _ in range(num_balls):
            index = random.randrange(len(self.contents))
            drawn.append(self.contents.pop(index))

        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0

    for _ in range(num_experiments):
        # deep copy so original hat is never modified
        hat_copy = copy.deepcopy(hat)

        drawn = hat_copy.draw(num_balls_drawn)

        drawn_count = {}
        for ball in drawn:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1

        match = True
        for color, required_count in expected_balls.items():
            if drawn_count.get(color, 0) < required_count:
                match = False
                break

        if match:
            success += 1

    return success / num_experiments