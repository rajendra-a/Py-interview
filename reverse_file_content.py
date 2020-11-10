for line in reversed(list(open('./Py-interview-progs/demofile.txt'))):
    print(line.rstrip())

g = open('out.txt', 'w')
with open("demofile.txt", "r") as f:
    data = f.read()

data_1 = data[::-1]
g.write(data_1)
g.close()