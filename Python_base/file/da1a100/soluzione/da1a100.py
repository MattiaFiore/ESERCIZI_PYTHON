
with open("da1a100.txt", "w") as f: 
    for i in range(1,101): 
        print(i)
        f.write(str(i)+"\n")
