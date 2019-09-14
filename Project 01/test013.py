name = input("Enter your name: ")
last = input("Enter your last name: ")

message1 = "Hello %s %s!" % (name, last)
message2 = "Hello {} {}!".format(name, last)

print(message1)
print(message2)