def updateList(dest, src, listname):
    with open(src, "r") as srcfile:
        lines = [line.strip() for line in srcfile.readlines()]
    with open(dest, "w+") as destfile:
        destfile.write(listname)
        destfile.write(" = [\n")
        for line in lines:
            destfile.write("\t\"")
            destfile.write(line)
            destfile.write("\",\n")
        destfile.write("]")

if __name__ == "__main__":
    updateList("compliments.py", "compliments.txt", "compliments")
    updateList("motivators.py", "motivators.txt", "motivators")