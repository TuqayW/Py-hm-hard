import re

def ms(account):
    print("Salam pul chixartmaqa xos gelmisiz")
    try:
        me = int(input("Mebleg daxil edin:"))
    except ValueError:
        print("Zehmet olmasa reqem daxil edin")
        return
    ask = input("Zehmet olmasa paroluvuzu tesdiqleyin:")
    if ask == account["password"]:
        print(f"Hal hazirda balansiniz {account['balance']} manatdir")
        ask = int(input("Tuqayi varli etmek fonduna ne qeder gondermek isdeyirsiz?:"))
        account['balance'] -= ask
        print(f"Balansinizda {account['balance']} manat qaldi")
    else:
        print("E bala sen ozvu ne bilsen hacker zad?sence o boyda bank securitysi bele asandi?")
        return       

def mr(account):
    print("salam balans artirmaqa xos gelmisiz") 
    try:
        me = int(input("Mebleg daxil edin:"))
    except ValueError:
        print("Zehmet olmasa reqem daxil edin")
        return
    ask = input("Zehmet olmasa paroluvuzu tesdiqleyin:")
    if ask == account["password"]:
        print(f"Hal hazirda balansiniz {account['balance']} manatdir")
        ask = int(input("Balans ne qeder artirmaq isdeyirsen?:"))
        account['balance'] += ask
        print(f"Balansinizda {account['balance']} manat var artiq")
    else:
        print("E bala sen ozvu ne bilsen hacker zad?sence o boyda bank securitysi bele asandi?")
        return

def dh(account):
    print("salam hesab silmeye xos gelmisiz") 
    try:
        me = input("Deqiq hesab silmek isdeyirsiz?:")
    except ValueError:
        print("Zehmet olmasa he yox daxil edin")
        return
    if me.lower() == "he":
        ask = input("Zehmet olmasa paroluvuzu tesdiqleyin:")
        if ask == account["password"]:
            print("Hal hazirda hesab silirsiz sonra qaytarmaq olmuyacaq")
            account["password"] = ""
            account["surname"] = ""
            account["name"] = ""
            account["balance"] = 0
            print("Siz artiq yoxsuz The End")
            return
        else:
            print("parol sehvdir")
    else:
        print("aferin senden aldigimiz vergiler bizim maasimizdi thankssss")
        return

def ma(account):
    try:
        ask = input("Zehmet olmasa emr secin(hesab login,hesab yarat,exit): ")
    except ValueError:
        print("zehmet olmasa 3 emrden birini secin reqem daxil etmeyin")
        exit()
    
    if ask.lower() == "hesab yarat":
        age = int(input("Yasivi daxil et zehmet olmasa:"))
        if age < 18:
            raise Exception("Yasin catmir")
        
        print("Yashiviz catir")
        account["name"] = input("Zehmet olmasa adivizi daxil edin:")
        account["surname"] = input("Zehmet olmasa soy-adivizi daxil edin:")
        account["password"] = input("Zehmet olmasa parol daxil edin(minimum 6 herf 1 boyuk herf 1 reqem)")
        
        pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d).{6,}$')
        try:
            if pattern.match(account["password"]):
                print("Parol sertleri oduyur")
                try:
                    account["balance"] = int(input("balans daxil et:"))
                except ValueError:
                    raise Exception("Reqem DAXIL ET BALA REQEM ALLAH SENIN MIN BELAVI VERSIN BIR DAHA SOZUM YOXDU SENE MENIM")
                print("hesabiviz ugurla yarandi")
            else:
                print("Parol sertlere uygun deil")
        except:
            raise Exception("Zehmet olmasa yeniden basliyin")
    
    elif ask.lower() == "hesab login":
        nnn = input("zehmet olmasa adivizi daxil edin:")
        if nnn == account["name"]:
            ppp = input("Sifrevizi daxil edin:")
            if ppp == account["password"]:
                try:
                    ask = input("Ne etmek isdeyirsiz(pul kocur,balans artir,hesab sil):")
                except ValueError:
                    raise Exception("zehmet olmasa emrlerden birini daxil et")
                
                if ask.lower() == "pul kocur":
                    ms(account)
                elif ask.lower() == "balans artir":
                    mr(account)
                elif ask.lower() == "hesab sil":
                    dh(account)
            else:
                print("parol veya username sehvdir")
        else:
            print("bele bir username yoxdur")

# Creating an account dictionary to store user information
account_info = {
    "name": "",
    "surname": "",
    "password": "",
    "balance": 0
}

while True:
    ma(account_info)
