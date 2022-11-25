lst = []
a = int(input("Enter the number of elements:"))
for i in range(a):
    ele = input()
    lst.append(ele)
for x in lst:
    oupt = x[0]
    for y in range(1,len(x)):
        if x[y-1] == " ":
            oupt += x[y]
            oupt = oupt.upper()
    print(f"The acronym for {x} is {oupt}")

