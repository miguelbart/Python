def test_1():
    frase = "Bienvenido al proyecto Mision TIC2022 en UTP!"
    str1 = frase[:10]
    str2 = frase[30:37]
    str3 = frase[41:-1]

    out1 = "bienvenido: {}".format(str1)
    out2 = "TIC2022: {}".format(str2)
    out3 = "UTP: {}".format(str3)

    return f"{out1}\n{out2}\n{out3}"

print(test_1())