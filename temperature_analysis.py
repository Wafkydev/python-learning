temperatures = [
    30, 31, 29, 33, 35,
    32, 30, 28, 29, 31,
    34, 36, 35, 33, 32,
    31, 30, 29, 28, 27
]

def temperature_at(day):
    return temperatures[day - 1]

def highest_temperature(a, b):
    return max(temperatures[a - 1:b])

def lowest_temperature(a, b):
    return min(temperatures[a - 1:b])

def average_temperature(a, b):
    selected = temperatures[a - 1:b]
    return sum(selected) / len(selected)#len = count(the number you selected)

print(temperature_at(7))
print(highest_temperature(1, 10))
print(lowest_temperature(11, 20))
print(average_temperature(1, 5))

