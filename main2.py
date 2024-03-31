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

def dec_to_hex(vrednost):
    if vrednost == 0:
        return "0"
    hex_znaki = "0123456789ABCDEF"  # nabor hex znakov za filanje hex vrednosti
    hex_vrednost = ""   # prazna postavljena hex vrednost
    while vrednost > 0:
        ostanek = vrednost % 16 # ostanek pri deljenju z 16 nam pove naslednji znak v hex vrednosti
        hex_vrednost = hex_znaki[ostanek] + hex_vrednost       # dodajanje znaka v hex vredndost
        vrednost = vrednost // 16   # 
    return hex_vrednost


def pretvori_v_bajte_in_znak(stevilka):
    bajti = bytes([int(i, 2) for i in bit_size(stevilka)])
    znak = bajti.decode('utf-8').replace("\n", "\\n").replace("\r", "\\r")
    return bajti, znak


#print(dec_to_bin(269))
# UTF-8 strukturea predpon (glej tabelo v navodilih)
def bit_size(vrednost): #calculate the number of bits necesearry to code the number to binary

    min_stevilo_bitov = np.log2(vrednost)       # minimalno število bitov, da se lahko zapiše vrednost
    #    glede na tabelo porežemo ustrezne bite v posamezne bajte
    if min_stevilo_bitov <= 7:
        return [dec_to_bin(vrednost)[2:]]
    elif min_stevilo_bitov <= 11:
        binarna = dec_to_bin(vrednost)[2:].zfill(11)
        return ["110"+binarna[:5], "10"+binarna[5:]]
    elif min_stevilo_bitov <= 16:
        binarna = dec_to_bin(vrednost)[2:].zfill(16)
        return ["1110"+binarna[:4], "10"+binarna[4:10], "10"+binarna[10:]]
    elif min_stevilo_bitov <= 21:
        binarna = dec_to_bin(vrednost)[2:].zfill(21)
        return ["11110"+binarna[:3], "10"+binarna[3:9], "10"+binarna[9:15], "10"+binarna[15:]]
    else:
        print("Prevelika vrednost")

if __name__ == "__main__":
    with open("kodne točke.txt", "r") as kodne_tocke:
        besedilo = kodne_tocke.read()
    tabela_stevil = [int(i) for i in besedilo.replace(' ', '').split(',')] # odstramnimo vse presledke, zgradimo slovar znakovnih nizov iz besedila
                                                                           # s split razdelimo besede na znakovne nize
    
    with open("besedilo.txt", "wb") as besedilo:   # postavimo novo datoteko besedilo.txt v repozitoriju, če taka datoteka že obstaja, jo povozimo: wb -> write binary
        for stevilka in tabela_stevil: # iterira skozi vse znakovne nize iz vhodnega besedila, ki smo jih razdelili z vejicami
            # tabelo binarnih kod pretvorimo v tabelo števil in nato v tabelo bajtov (bytes), ki jih zapišemo v datoteko
            besedilo.write(bytes([int(i, 2) for i in bit_size(stevilka)]))

    unikatni_znaki = list(set(tabela_stevil))  # set() je množica, ki ne vsebuje ponovitev
    unikatni_znaki.sort()

    with open("tabela_kodiranja.txt", "w", encoding="utf-8") as datoteka:
        for stevilka in unikatni_znaki:
            binarna = "".join(bit_size(stevilka))
            decimalna = int(binarna, 2)
            sestnajstiska = hex(decimalna)[2:].upper().zfill(4)
            _, znak = pretvori_v_bajte_in_znak(stevilka)  # '_' ignorira bajte, ker jih tukaj ne potrebujemo

            print(f"Unicode št. {stevilka} = {znak}, dec={decimalna}, hex={sestnajstiska}")
            datoteka.write(f"{stevilka};{znak};{binarna};{decimalna};{sestnajstiska}\n")   



