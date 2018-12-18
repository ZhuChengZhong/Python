with open("/tmp/test.txt","w") as f:
    while True:
        text=input("why you like programing ?")
        if text=="quit":
            break
        f.write(text+"\n")


with open("/tmp/test.txt","r") as f:
    print(f.read())


