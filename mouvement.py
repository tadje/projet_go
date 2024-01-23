import re
def est_valide(coup,joueur_actuel,plateau):
    #phase de test voir si coup est dans une place vide
    if not re.match(r"^[A-S][1-9][0-9]?$",coup):
        return False
    lettre, chiffre = coup[0], int(coup[1:])
    if not 1 <= chiffre <= 19:
        return False#TRIVIAL
    #fonction qui regarde si le coup peut etre mis dans plateau='19*;3N....
    place = develope_ligne(plateau[chiffre-1])
    if place[ord(lettre)-ord('A')] !='*':
        return False
    
    return True#TEST

def develope_ligne(ligne):
    zone = ligne.split('/')
    place=''
    for mot in zone:
        if mot in ['N','B','*']:
            place += mot
            
        else:
            place += mot[0]*int(mot[1:])

        
    return place

def placer_pierre(coup,joueur_actuel,plateau):

    plage = develope_ligne(plateau[int(coup[1:])-1])
    plage=plage[:ord(coup[0].upper())-ord('A')] +joueur_actuel +plage[ord(coup[0].upper())-ord('A')+1:]
    plateau[int(coup[1:])-1] = decode_ligne(plage)
    return plateau

def decode_ligne(plage):
    temp = plage[0]
    nombre=1
    resultat =''
    for i in range(1,19):
        if plage[i] == temp:
            nombre += 1
        else:
            if nombre == 1:
                resultat+= '/'+temp
            else:
                resultat += '/'+temp+str(nombre)
            nombre = 1
            temp = plage[i]
    return resultat[1:]+'/'+temp+str(nombre) if nombre != 1 else resultat[1:] +'/'+temp
