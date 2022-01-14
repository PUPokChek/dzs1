text = input( "Введите строку  ")
length = len(text)
massive = []
massive += text 
massive.insert(0,massive[length-1])
massive.pop(length)
massive.insert(length+1,massive[1])
massive.pop(1)
print(massive)
