def makeFile(filename):
    file = open(filename, "w")
    file.write("Nothing to see here. Move along.")
    file.close()

makeFile("Waffles.txt")