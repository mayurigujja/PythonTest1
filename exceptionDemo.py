from logging import exception

try:
    with open("test.txt", 'r') as reader:
        line = reader.readlines()

except:
    print("File not found")

finally:
    print("I will execute anyways")