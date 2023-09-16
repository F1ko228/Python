file1 = open("lab5_2_1.txt", "r")
file2 = open("lab5_2_2.txt", "w+")


def TextDict():
    slovarik = []
    words = (file1.read()).split()
    for i in words:
        if 1 < len(i) < 21:
            slovarik.append(i)
    file1.close()
    return slovarik


def ChangeFile():
    for i in TextDict():
        file2.write(i + "\n")
    file2.close()


ChangeFile()