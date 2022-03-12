file = open("D:\Project\AI\data\_small_ds.txt", "r+")
newfile = open("D:\Project\AI\data\\new_small_ds.txt", "w")
lines = file.readlines()
for line in lines:
    new_line = line.replace(
        "C:\\Users/84982/Documents/github/arcface_experiment/", "D:/Project/AI/"
    )
    newfile.write(new_line)
file.close()
newfile.close()
