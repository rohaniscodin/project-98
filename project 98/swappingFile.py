def swapFileData():
    with open("banana.txt","r")as a:
        data_a=a.read()
    with open("monkey.txt","r")as b:
        data_b=b.read()
    with open("banana.txt","w")as a:
        a.write(data_b)
    with open("monkey.txt","w")as b:
        b.write(data_a)
swapFileData()