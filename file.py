with open("/etc/hosts") as hosts:
   content=hosts.read()
   content+="end"
   print(content)


print("print in lines ----------------------")

with open("/etc/hosts") as f:
    for line in f:
        print(line.rstrip())
