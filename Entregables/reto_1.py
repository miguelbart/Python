def reto_1(f1: float, d: int, c1: float) -> str:
    fuerza1 = f1
    F1 = f"F1 = {fuerza1:.1f} N"
    pi = 3.14
    d = float(d/100)
    area1 = round((d / 2) * (d / 2) * pi,4)
    A1=f"A1 = {area1} m2"
    area2 = round(((d * c1)/2) * ((d * c1)/2) * pi,4)
    A2 = f"A2 = {area2} m2"
    radio1 = d/2
    perimetro1 = round(2*pi*radio1,3)
    P1 = f"P1 = {perimetro1} m2"
    R1 = f"r1 = {radio1} m2"
    fuerza2 = round((area2 / area1) * fuerza1,1)
    F2 = f"F2 = {fuerza2:.1f} N"
    return F1, A1, R1, P1, F2, A2



print(reto_1(-235,345,1/8))