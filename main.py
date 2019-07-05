N = 3
with open("discnt.in", "r+") as fileIn:
    arrayIn = list(map(int, fileIn.readline()[:-1].split()))
    arrayIn.sort()
    discount = int(fileIn.readline()[:-1])

l = len(arrayIn)//N
lowest, biggest = arrayIn[:-l], arrayIn[-l:]
biggestWithDiscount = list(map(lambda i: i*(1-discount/100), biggest))
res = sum(lowest)+sum(biggestWithDiscount)
with open("discnt.out", "w+") as fileOut:
    fileOut.write(f"{res:.02f}")
