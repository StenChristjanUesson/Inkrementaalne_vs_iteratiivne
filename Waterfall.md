Lähme nüüd *waterfall* (kosemudeli) arendusprotsessi vaatepunktist seda sama dokumentatsiooni hindamise teemat käsitlema. 
Erinevalt iteratiivsest lähenemisest, kus töö toimub tsüklitena ja pideva tagasiside alusel, eeldab waterfall lähenemine selgelt määratletud ja järjestikuseid etappe, 
kus iga etapp viiakse lõpule enne järgmise alustamist.

Kosemudeli (Waterfall) põhine lähenemine GitHub Wiki dokumentatsiooni hindamisele

Waterfall arendusmudeli rakendamine dokumentatsiooni arendamise ja hindamise puhul tähendab selgelt struktureeritud ja järjestikust protsessi, 
kus iga faas järgneb loogiliselt eelmisele. See sobib hästi stabiilsematesse keskkondadesse, kus muudatusi on harvem ja nõuded selgelt määratletud juba alguses.

1. Nõuete kogumine ja planeerimine

Selles etapis selgitatakse välja kogu dokumentatsiooni ulatus ja eesmärk. Koostatakse põhjalik plaan, mis määratleb:

Milliseid teemasid dokumentatsioon katab (nt projekti eesmärgid, installatsioon, kasutusjuhised, API-d).
Kellele dokumentatsioon on suunatud (arendajad, lõppkasutajad, partnerid).
Milliseid standardeid ja stiilijuhiseid järgitakse.

💡 Selles faasis ei koostata veel sisu, vaid dokumentatsiooni “raamistik” ja ootused.

2. Dokumentatsiooni koostamine (Design & Implementation)

Dokumentatsioon kirjutatakse vastavalt eelnevalt määratud nõuetele ja struktuurile. See hõlmab:

Teksti koostamist kõigi vajalike jaotiste kaupa.
Stiilide ja vormingu ühtlustamist.
Tehnilise sisu loomist vastavuses projekti lähtekoodiga.

📌 Etapis tehakse töö ühe korraga valmiskujule – mitte osade kaupa tagasiside põhjal.

3. Kontroll ja valideerimine (Verification)

Pärast dokumentatsiooni koostamist tehakse kontroll:

Lingid, viited ja koodinäited testitakse.
Vaadatakse üle ortograafia ja stiililine kooskõla.
Tehniline täpsus kinnitatakse koostöös arendajate ja süsteemiadministraatoritega.

🛠 Selle faasi eesmärk on leida ja parandada vead enne avalikustamist.

4. Avaldamine ja kasutuselevõtt

Kui kontroll on läbitud, avaldatakse dokumentatsioon GitHub Wiki-s. Avaldamise käigus:

Märgitakse dokumentatsioon ametlikuks versiooniks.
Tehakse muudatused nähtavaks kogu tiimile ja/või kasutajatele.
Vajadusel lisatakse teated või juhised muudatuste kohta.

5. Hooldus (Maintenance)

Dokumentatsiooni ei muudeta pidevalt, vaid vajaduspõhiselt. Uusi muudatusi käsitletakse järgmise waterfall-tsükli käigus. See tähendab:

Vead või puudused fikseeritakse, kuid mitte kohe – need planeeritakse uude tsüklisse.
Uued funktsionaalsused või muudatused projektis eeldavad uut dokumentatsiooni arendustsüklit.

📎 Versioonihaldus (GitHubi commit’id ja Wiki ajalugu) võimaldavad võrrelda versioone, kuid muudatused on planeeritud ja mitte spontaansed.
