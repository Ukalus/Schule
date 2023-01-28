
decimal = 12347
rest = -1
solution = []
base = 2

while decimal != 0:
    rest = decimal % base
    decimal = (decimal - rest) / base
    solution.append(int(rest))
    

solution.reverse()
str(solution)
print(solution)