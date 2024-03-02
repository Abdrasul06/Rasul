a = int(input(a))
b = int(input(b))
c = int(input(c))

def TriangleChecker():
    if a + b > c && b + c > a && a + c > b:
        print("Ура, можно построить треугольник!")
        break
    if else a < 0 or b < 0 or c < 0:
        print("С отрицательными числами ничего не выйдет!;")
        break         
    else:
        print("Жаль, но из этого треугольник не сделать")
        break 
