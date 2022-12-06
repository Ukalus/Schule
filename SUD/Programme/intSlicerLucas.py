import re

message = input("gib mir eine nummer mit kontext \n")
value = int(re.search(r"\d+", message).group(0))
print(value)
