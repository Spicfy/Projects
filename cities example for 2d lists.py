def frequency(a):
    f = []
    for i in range(len(a)):
        city = a[i]
        flag = False
        for j in range(len(f)):
            if city == f[j][0]
            f[j][1] += 1
            flag = True

#main
cities = ["mostar", "sarajevo", "mostar", "paris", "melbourne", "ottawa", "budapest", "NYC", "melbourne"]
freq = frequency(cities)
print(freq)
#expected output: [["mostar", 2], ["paris", 2], ["melbourne", 3], ["ottawa", 1], ["NYC", 1]]
