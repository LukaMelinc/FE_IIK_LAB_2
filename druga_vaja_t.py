import numpy as np


def kodiraj(stevilka):
    """Kodira število v binarno kodo v UTF-8
    primer: kodiraj(65) -> ['01000001']     ali     kodiraj(200) -> ['11000011', '10001000']"""
    min_stevilo_bitov = np.log2(stevilka)
    if min_stevilo_bitov <= 7:
        return [bin(stevilka)[2:]]
    elif min_stevilo_bitov <= 11:
        binarna = bin(stevilka)[2:].zfill(11)
        return ["110"+binarna[:5], "10"+binarna[5:]]
    elif min_stevilo_bitov <= 16:
        binarna = bin(stevilka)[2:].zfill(16)
        return ["1110"+binarna[:4], "10"+binarna[4:10], "10"+binarna[10:]]
    elif min_stevilo_bitov <= 21:
        binarna = bin(stevilka)[2:].zfill(21)
        return ["11110"+binarna[:3], "10"+binarna[3:9], "10"+binarna[9:15], "10"+binarna[15:]]
    else:
        print("Stevilka je prevelika")


if __name__ == "__main__":
    with open("kodne točke.txt", "r") as f:
        besedilo = f.read()
    tabela_stevil = [int(i) for i in besedilo.replace(' ', '').split(',')]

    # TODO: Generiramo besedilno datoteko besedilo.txt, ki vsebuje vse znake, ki nastopajo v tabeli
    with open("besedilo.txt", "wb") as f:
        for stevilka in tabela_stevil:
            # tabelo binarnih kod pretvorimo v tabelo števil in nato v tabelo bajtov (bytes), ki jih zapišemo v datoteko
            f.write(bytes([int(i, 2) for i in kodiraj(stevilka)]))

    # TODO: Generiramo tabelo vseh unikatnih znakov in njihovih kodnih zamenjav, ki v njej nastopajo,
    #  v dvojiškem, desetiškem in šestnajstiškem zapisu.
    unikatni_znaki = list(set(tabela_stevil))  # set() je množica, ki ne vsebuje ponovitev
    #unikatni_znaki.sort()
    with open("tabela_kodiranja.txt", "w", encoding="utf-8") as f:
        for stevilka in unikatni_znaki:
            binarna = "".join(kodiraj(stevilka))  # pretvorimo tabelo binarnih kod v eno veliko binarno število npr. ['11001000', '10100000'] -> '1100100010100000'
            decimalna = int(binarna, 2)  # pretvorimo binarno število v desetiško število
            sestnajstiska = hex(decimalna)[2:].upper().zfill(4)  # pretvorimo desetiško število v šestnajstiško število
            znak = (bytes([int(i, 2) for i in kodiraj(stevilka)]).decode('utf-8')).replace("\n", "\\n").replace("\r", "\\r")
            print(f"Unicode št. {stevilka} = {znak}, dec={decimalna}, hex={sestnajstiska}, bin={binarna}")
            f.write(f"{stevilka};{znak};{binarna};{decimalna};{sestnajstiska}\n")
