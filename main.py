from random import sample

#Нарушен принцип DRY, через цикл решения не реализовал.



test_text = input("Нажмите Enter чтобы прокрутить рулетку первый раз: ")
pem = sample(range(1, 11), 10)
x1 = (pem[0:1])
print(f"Вам выпала ячейка № {x1}")
test_text2 = input("Нажмите Enter чтобы прокрутить рулетку второй раз: ")
surplus2 = [item for item in pem if item not in x1]
x2 = (surplus2[0:1])
print((f"Вам выпала ячейка № {x2}"))
test_text3 = input("Нажмите Enter чтобы прокрутить рулетку третий раз: ")
add1 = (x1 + x2)
surplus3 = [item for item in pem if item not in add1]
x3 = (surplus3[0:1])
print((f"Вам выпала ячейка № {x3}"))
test_text4 = input("Нажмите Enter чтобы прокрутить рулетку четвертый раз: ")
add2 = (x1 + x2 +x3)
surplus4 = [item for item in pem if item not in add2]
x4 = (surplus4[0:1])
print((f"Вам выпала ячейка № {x4}"))
test_text5 = input("Нажмите Enter чтобы прокрутить рулетку пятый раз: ")
add3 = (x1 + x2 +x3+ x4)
surplus5 = [item for item in pem if item not in add3]
x5 = (surplus5[0:1])
print((f"Вам выпала ячейка № {x5}"))
test_text6 = input("Нажмите Enter чтобы прокрутить рулетку шестой раз: ")
add4 = (x1 + x2 + x3 + x4 + x5)
surplus6 = [item for item in pem if item not in add4]
x6 = (surplus6[0:1])
print((f"Вам выпала ячейка № {x6}"))
test_text7 = input("Нажмите Enter чтобы прокрутить рулетку седьмой раз: ")
add5 = (x1 + x2 + x3 + x4 + x5 + x6)
surplus7 = [item for item in pem if item not in add5]
x7 = (surplus7[0:1])
print((f"Вам выпала ячейка № {x7}"))
test_text8 = input("Нажмите Enter чтобы прокрутить рулетку восьмой раз: ")
add6 = (x1 + x2 + x3 + x4 + x5 + x6 +x7)
surplus8 = [item for item in pem if item not in add6]
x8 = (surplus8[0:1])
print((f"Вам выпала ячейка № {x8}"))
test_text9 = input("Нажмите Enter чтобы прокрутить рулетку девятый раз: ")
add7 = (x1 + x2 + x3 + x4 + x5 + x6 +x7 + x8)
surplus9= [item for item in pem if item not in add7]
x9 = (surplus9[0:1])
print((f"Вам выпала ячейка № {x9}"))
test_text10 = input("Нажмите Enter чтобы прокрутить рулетку десятый раз: ")
add8 = (x1 + x2 + x3 + x4 + x5 + x6 +x7 + x8 + x9)
surplus10 = [item for item in pem if item not in add8]
x10 = (surplus10[0:1])
print((f"Вам выпала ячейка № {x10}"))
test_text11 = input("Нажмите Enter чтобы прокрутить рулетку одиннадцатый раз: ")
print("Поздравляем! Вам выпал джекпот!")
