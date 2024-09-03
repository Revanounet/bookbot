def main():
    chemin = "/home/revanounet/workspace/github.com/Revanounet/bookbot/books/frankenstein.txt"
    text = lecture(chemin)
    compteur_mot = count(text)
    print(f"il y {compteur_mot} mots dans le livre")
    compteur_specifique = alphabet(text)
    list_non_sorted = conversion(compteur_specifique)
    list_non_sorted.sort(reverse=True, key=sorting)

    for i in range(0,len(list_non_sorted)):
        print(f"The '{list_non_sorted[i]['name']}' character was found {list_non_sorted[i]['Valeur']} times ")

   
def count(text):
    words = text.split()
    return(len(words))

def lecture(chemin):
     with open(chemin) as f:
        file_contents = f.read()
        return file_contents

def alphabet(text):
    Dico = {}
    for c in text:
        petit = c.lower()
        if petit in Dico:
            Dico[petit] += 1
        else:
            Dico[petit] = 1
    
    return Dico

def conversion(Dico):
    list_name = list(Dico)
    list_valeur = []
    fkcdico = {}
    fkclist = []
    for value in Dico:
        list_valeur.append(Dico[value])
    for value in range(0,len(Dico)):
        if list_name[value].isalpha():
            fkcdico = {}
            fkcdico["name"] = list_name[value]
            fkcdico["Valeur"] = list_valeur[value]
            fkclist.append(fkcdico)
    return fkclist

def sorting(list):
    return list["Valeur"]

    

 
main()


