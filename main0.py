# ## **Ehita samm-sammult "Mini Kalkulaator" iteratiivse meetodi järgi**
#
# ### **Iteratsioon 1 - Lihtne liitmine**
#
# - Kirjuta programm, mis küsib kasutajalt kaks arvu ja tagastab nende summa.
#
def mySum(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        print("vale sissestus!")

print(mySum(1,3));

### **Iteratsioon 2 - rohkem tehteid**

# - Lisa lahutamine, korrutamine ja jagamine.
# - Loo valikumenüü (1.liida, 2.lahuta, 3.korruta, 4. jaga).

def myFinalSum(a, b, operation):
    if not isinstance(a, int) or not isinstance(b, int):  # Ensure both inputs are integers
        print("Vale sisestus! Peavad olema täisarvud.")
        return None

    if operation == 1:  # Liida
        return a + b
    elif operation == 2:  # Lahuta
        return a - b
    elif operation == 3:  # Korruta
        return a * b
    elif operation == 4:  # Jaga
        if b == 0:  # Avoid division by zero
            print("Jagamine nulliga on keelatud!")
            return None
        return a / b
    else:
        print("Vale valik!")
        return None

# User interface
def main():
    print("1 - Liida, 2 - Lahuta, 3 - Korruta, 4 - Jaga")
    try:
        operation = int(input("Sisesta valik (1-4): "))
        a = int(input("Sisesta esimene number: "))
        b = int(input("Sisesta teine number: "))
        result = myFinalSum(a, b, operation)
        if result is not None:
            print("Tulemus: ", result)
    except ValueError:
        print("Sisestatud väärtused ei olnud numbrid!")

# Test the function
main()

### **Iteratsioon 3 - Sisendi valdieerimine**
#
# - Kontrolli, et kasutaja sisestab numbreid

def main():
    print("Vali tehe: 1 - Liida, 2 - Lahuta, 3 - Korruta, 4 - Jaga")
    try:
        operation = int(input("Sisesta valik (1-4): "))
        a = int(input("Sisesta esimene number: "))
        b = int(input("Sisesta teine number: "))
        result = myFinalSum(a, b, operation)
        if result is not None:
            print("Tulemus: ", result)
    except ValueError:
        print("Sisestatud väärtused ei olnud numbrid!")

# Test the function
main()

# **Iteratsioon 4 - Loogiline Täiendus
# Global array to track operations count

myArr = [0, 0, 0, 0]

def displayInfo():
    print("Kokku oli", sum(myArr), "operatsiooni.")
    print(f"Liitmine: {myArr[0]} korda")
    print(f"Lahutamine: {myArr[1]} korda")
    print(f"Korrutamine: {myArr[2]} korda")
    print(f"Jagamine: {myArr[3]} korda")

def myFinalSum(a, b, operation):
    if not isinstance(a, int) or not isinstance(b, int):  # Ensure both inputs are integers
        print("Vale sisestus! Peavad olema täisarvud.")
        return None

    if operation == 1:  # Liida
        myArr[0] += 1
        return a + b
    elif operation == 2:  # Lahuta
        myArr[1] += 1
        return a - b
    elif operation == 3:  # Korruta
        myArr[2] += 1
        return a * b
    elif operation == 4:  # Jaga
        if b == 0:  # Avoid division by zero
            print("Jagamine nulliga on keelatud!")
            return None
        myArr[3] += 1
        return a / b
    else:
        print("Vale valik!")
        return None

def main():
    print("Vali tehe: 1 - Liida, 2 - Lahuta, 3 - Korruta, 4 - Jaga")
    try:
        operation = int(input("Sisesta valik (1-4): "))
        a = int(input("Sisesta esimene number: "))
        b = int(input("Sisesta teine number: "))
        result = myFinalSum(a, b, operation)
        if result is not None:
            print("Tulemus: ", result)
        displayInfo()  # Display operation counts
    except ValueError:
        print("Sisestatud väärtused ei olnud numbrid!")

# Test the function
main()

# inkrement 1 - Patsientide lisamine ja vaatamine
# inkrement 2 - Arstide lisamine ja vaatamine
# inkrement 3 - kohtumiste haldamine

class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus

class Arst:
    def __init__(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = aeg

class Haigla:
    def __init__(self):
        self.patsientideList = []
        self.arstideList = []

    def addPatsient(self, patsient):
        self.patsientideList.append(patsient)

    def addArst(self, arst):
        self.arstideList.append(arst)

    def showAllPatsiendid(self):
        for patsient in self.patsientideList:
            print(f"Patsient: {patsient.nimi}, Vanus: {patsient.vanus}")

    def showAllArstid(self):
        for arst in self.arstideList:
            print(f"Arst: {arst.nimi}, Eriala: {arst.eriala}, Vanus: {arst.vanus}")

    def showArstiAeg(self, arstiNimi):
        for arst in self.arstideList:
            if arst.nimi == arstiNimi:
                print(f"Arsti {arstiNimi} aeg: {arst.aeg}")
                return
        print(f"Arst {arstiNimi} ei leitud.")

# Test the functionality
haigla1 = Haigla()
patsient1 = Patsient("Thomas", 99)
haigla1.addPatsient(patsient1)
haigla1.showAllPatsiendid()

arst1 = Arst("Ahmed", 45, "Kiirurg", "10:00 - 12:00")
haigla1.addArst(arst1)
haigla1.showAllArstid()
haigla1.showArstiAeg("Ahmed")

#Iteratiivne/Inkrementaalne lähenemine

#mis see on
#paar pilte
#plussid ja miinused
#erinevused nende vahel
#kus seda kasutatakse

