"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""
"""
Kas ir klase?
Klase sastāv no konstruktora un metodēm.
Kādas datu struktūras zinat?
    list (saraksts)
    arry (masīvs)
    dict (vārdnīca) tukšu ... {}
                    dict --- ()
Kas ir vārdnīca
    Tā ir datu struktūra kuru mēs varam izteikt kā tabulu
    ar divām kolonām kur svarīga ir atslēga un tās vērtība
Atslēga un tās vērtība- piem. gada 3 mēnesis(atslēga), marts (tās vērtība)
class "teksts"
"""
class AAA:
    def __init__(self):
        self.roma_sk={
            1: 'I',
            4: 'IV', 
            5: 'V', 
            9: 'IX', 
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C',
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    def to_roman(self, num):
        result = ""
        for value, numeral in sorted(self.roman_numerals.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result += numeral
                num -= value
            return result

#piemērs
skaitlis=2023
#definējam objektu
kkk=AAA()
#kkk ir definēts kā klase AAA
#Jaunajam objektam jāizsauc klases metode
romiešu=kkk.to_roman(skaitlis)
#noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romiešu}.")