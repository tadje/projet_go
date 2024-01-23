import regle
import mouvement
def main():
    taille_plateau = 19
    plateau = [f'*{taille_plateau}'for _ in range(taille_plateau)]
    print(plateau)
    joueur_noir = 'N'
    joueur_blanc = 'B'
    joueur_actuel = joueur_noir
    jeu_termine = False
    while not jeu_termine:
        coup = regle.obtenir_coup(joueur_actuel)
        print(coup)
        if mouvement.est_valide(coup,joueur_actuel,plateau):
            plateau=mouvement.placer_pierre(coup,joueur_actuel,plateau)
            joueur_actuel = regle.changer_joueur(joueur_actuel)
            print(plateau)
        else:
            print("coup invalide")
            print(plateau)
        
        jeu_termine = regle.verifier_fin_de_jeu(plateau) #test
    pass
if __name__ == "__main__":
    main()