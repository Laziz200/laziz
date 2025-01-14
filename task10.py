text = input("Matn kiriting: ")
sozlar = text.split()
print(sozlar)

max_length = 0 

for i in sozlar:
    print(i)
    b =len(i)
    print(b)
    
    if max_length < b:
        max_length = b 

for i in sozlar:
    if max_length == len(i):
        print(i)

print("Eng uzun so'zning uzunligi:",max_length)
