with open('test.txt', 'r') as reader:
    listcontent = reader.readlines()
    reversed(listcontent)
    with open('test.txt', 'w') as writer:
        for line in reversed(listcontent):
           writer.write(line)