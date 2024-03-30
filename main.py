tipi_kodiranja = ['IBM852', 'ISO-8859-2', 'Windows-1250', 'maccentraleurope', 'UTF-16LE', 'UTF-16BE', 'utf-8']

crke = ['Č', 'Ž', 'Š', 'č', 'ž', 'š']

def dec_to_hex(decimal_value):
    if decimal_value == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_string = ""
    while decimal_value > 0:
        remainder = decimal_value % 16
        hex_string = hex_chars[remainder] + hex_string
        decimal_value = decimal_value // 16
    return hex_string

def dec_to_bin(decimal_value):
    if decimal_value == 0:
        return "0"
    binary_string = ""
    while decimal_value > 0:
        remainder = decimal_value % 2  # Ostanek pri deljenju z 2
        binary_string = str(remainder) + binary_string  # Dodajanje ostanka na začetek niza
        decimal_value = decimal_value // 2  # Celodelno deljenje z 2
    return binary_string




for kod in tipi_kodiranja:
    for znak in crke:
        desetiska_vrednost = int.from_bytes(znak.encode(encoding=kod), byteorder='big')
        heks_vrednost = dec_to_hex(desetiska_vrednost)
        binarna_vrednost = dec_to_bin(desetiska_vrednost)
        print(f"Tip kodiranja je {kod}, znak je {znak}. DESETIŠKA vrednost je {desetiska_vrednost}, HEX vrednost vrednost je {heks_vrednost}, BINARNA vrednost je {binarna_vrednost}")

        

    



