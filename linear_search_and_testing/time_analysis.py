import matplotlib.pyplot as plt

time_list = []

with open('timing.txt', 'r') as time_file:
    
    for i in range(9):
        line = time_file.readline().split()[-1]
        line = float(line[:7].rstrip())
        time_list.append(line)
    
print(time_list)


list_size = [10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000]


plt.plot(list_size, time_list)
plt.show()


