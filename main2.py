import numpy as np

def dec_to_bin(vrednost):
    if vrednost == 0:
        return "0"
    bin_vrednost = ""
    while vrednost > 0:
        ostanek = vrednost % 2  # Ostanek pri deljenju z 2
        bin_vrednost = str(ostanek) + bin_vrednost  # Dodajanje ostanka na začetek niza
        vrednost = vrednost // 2  # Celodelno deljenje z 2
    return bin_vrednost

#print(dec_to_bin(269))
def bit_size(vrednost): #calculate the number of bits necesearry to code the number to binary
    min_stevilo_bitov = np.log2(vrednost)
    if min_stevilo_bitov <= 7:
        return [bin(vrednost)[2:]]
    elif min_stevilo_bitov <= 11:
        binarna = bin(vrednost)[2:].zfill(11)
        return ["110"+binarna[:5], "10"+binarna[5:]]
    elif min_stevilo_bitov <= 16:
        binarna = bin(vrednost)[2:].zfill(16)
        return ["1110"+binarna[:4], "10"+binarna[4:10], "10"+binarna[10:]]
    elif min_stevilo_bitov <= 21:
        binarna = bin(vrednost)[2:].zfill(21)
        return ["11110"+binarna[:3], "10"+binarna[3:9], "10"+binarna[9:15], "10"+binarna[15:]]
    else:
        print("Stevilka je prevelika")

if __name__ == "__main__":
    with open("kodne točke.txt", "r") as kodne_tocke:
        besedilo = kodne_tocke.read()
    tabela_stevil = [int(i) for i in besedilo.replace(' ', '').split(',')] # odstramnimo vse presledke, zgradimo slovar znakovnih nizov iz besedila
                                                                           # s split razdelimo besede na znakovne nize
    
    with open("besedilo.txt", "wb") as f:   # postavimo novo datoteko besedilo.txt v repozitoriju, če taka datoteka že obstaja, jo povozimo: wb -> write binary
        for stevilka in tabela_stevil: # iterira skozi vse znakovne nize iz vhodnega besedila, ki smo jih razdelili z vejicami
            # tabelo binarnih kod pretvorimo v tabelo števil in nato v tabelo bajtov (bytes), ki jih zapišemo v datoteko
            f.write(bytes([int(i, 2) for i in bit_size(stevilka)]))

    unikatni_znaki = list(set(tabela_stevil))  # set() je množica, ki ne vsebuje ponovitev
    unikatni_znaki.sort()
    with open("tabela_kodiranja.txt", "w", encoding="utf-8") as f:
        for stevilka in unikatni_znaki:
            binarna = "".join(bit_size(stevilka))  # pretvorimo tabelo binarnih kod v eno veliko binarno število npr. ['11001000', '10100000'] -> '1100100010100000'
            decimalna = int(binarna, 2)  # pretvorimo binarno število v desetiško število
            sestnajstiska = hex(decimalna)[2:].upper().zfill(4)  # pretvorimo desetiško število v šestnajstiško število
            znak = (bytes([int(i, 2) for i in bit_size(stevilka)]).decode('utf-8')).replace("\n", "\\n").replace("\r", "\\r")
            print(f"Unicode št. {stevilka} = {znak}, dec={decimalna}, hex={sestnajstiska}, bin={binarna}")
            f.write(f"{stevilka};{znak};{binarna};{decimalna};{sestnajstiska}\n")



