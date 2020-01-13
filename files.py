textFile = open("text.dat", "w")
textFile.write("Hello text file.")
textFile.close()

file = open("text.dat")
print(file.read())
file.close()