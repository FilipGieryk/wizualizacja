with open("test.txt", "w") as f:
    f.write("cwiczeniacwiczenie\n 2132153454\n lisat astast")
with open("test.txt") as f:
    for line in f:
        print(line, end='')