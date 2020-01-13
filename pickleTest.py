import pickle

print("file...")

filename = r"./test.dat"
file = open(filename, "w")

contentToWrite = {"type": "song", 
"title": "Hotel California", 
"artist": "Eagles", 
"albums": ["Eagles Live", "Hotel California", "Greatest Hits"]
}
pickle.dump(contentToWrite, file)

file.close()

file2 = open(filename)

contents = file2.read()

print(contents)

file2.close()

file3 = open(filename)
formattedContent = pickle.load(file3)

print(formattedContent)
file3.close()
