tipi_kodiranja = ['IBM852', 'ISO-8859-2', 'Windows-1250', 'maccentraleurope', 'UTF-16LE', 'UTF-16BE', 'utf-8']

crke = ['Č', 'Ž', 'Š', 'č', 'ž', 'š']

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

def dec_to_bin(vrednost):
    if vrednost == 0:
        return "0"
    bin_vrednost = ""
    while vrednost > 0:
        ostanek = vrednost % 2  # Ostanek pri deljenju z 2
        bin_vrednost = str(ostanek) + bin_vrednost  # Dodajanje ostanka na začetek niza
        vrednost = vrednost // 2  # Celodelno deljenje z 2
    return bin_vrednost




for kod in tipi_kodiranja:
    for znak in crke:
        desetiska_vrednost = int.from_bytes(znak.encode(encoding=kod), byteorder='big')
        heks_vrednost = dec_to_hex(desetiska_vrednost)
        binarna_vrednost = dec_to_bin(desetiska_vrednost)
        print(f"Tip kodiranja je {kod}, znak je {znak}. DESETIŠKA vrednost je {desetiska_vrednost}, HEX vrednost vrednost je 0x{heks_vrednost}, BINARNA vrednost je {binarna_vrednost}")

        

    



