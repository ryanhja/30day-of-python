# Day 21: 30 Days of python programming


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        sum_data = 0
        for d in self.data:
            sum_data += d

        return sum_data


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

s = Statistics(ages)

print("Count: ", s.count())
print("Sum: ", s.sum())
