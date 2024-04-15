vrsta_kodiranja = ['IBM852', 'iso-8859-2', 'Windows-1250', 'maccentraleurope', 'utf-8', 'UTF-16LE', 'UTF-16BE']

crke = ['Č', 'Š', 'Ž', 'č', 'š', 'ž']

for kodiranje in vrsta_kodiranja:
    for crka in crke:    
        desetiska_vrednost = int.from_bytes(crka.encode(encoding=kodiranje), byteorder='big')
        sestnajstiska = hex(desetiska_vrednost)[2:].upper().zfill(4)
        binarna = bin(desetiska_vrednost)[2:]
        print(f"{crka} s kodiranjem {kodiranje}: dec={desetiska_vrednost}, hex={sestnajstiska}, bin={binarna}")