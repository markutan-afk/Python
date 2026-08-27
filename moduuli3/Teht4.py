vuosi = int(input("Anna vuosi luku: "))

if vuosi % 100 == 0 and vuosi % 400 == 0:
    print("Vuosi on karkaus vuosi")
elif vuosi % 4 == 0:
    print("Vuosi on karkaus vuosi")
else:
    print("Vuosi ei ole karkaus vuosi")