leiviskät = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
leiviskä = leiviskät * 20 * 32 * 13.3
naula = naulat * 32 * 13.3
luoti = luodit * 13.3
gramma = leiviskä + naula + luoti
kilogramma = gramma // 1000
grammat = kilogramma * 1000
gramma = gramma - grammat
print(f"Massa nykymittojen mukaan: {kilogramma} kilogrammaa ja {gramma} grammaa.")