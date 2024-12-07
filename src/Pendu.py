"""StratosMaestro"""

import random
from typing import List, Set

def afficher_pendu(erreurs: int) -> None:
    """
    Affiche l'état du pendu en fonction du nombre d'erreurs...

    Args:
        erreurs (int): Nombre d'erreurs commises.
    """
    etats = [
        """
           ------
           |    |
           |
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ---------
        """
    ]
    print(etats[erreurs])

def choisir_mot() -> str:
    """
    Retourne un mot aléatoire parmi une liste prédéfinie.

    Returns:
        str: Le mot choisi aléatoirement.
    """
    mots = [
    "abeille", "abricot", "aigle", "album", "amphibien", "ananas", "ange", "antilope", "archer", "argent", "armoire", "ascenseur", "avalanche", "avion",
    "baleine", "ballon", "banane", "barbecue", "basilic", "batterie", "bijou", "biscuit", "blason", "boisson", "bonbon", "boucherie", "bougie", "bouteille", "boutique", "brindille", "brochure", "brouillard",
    "cactus", "cadence", "cadran", "camion", "campagne", "canard", "canyon", "caravane", "carotte", "cascade", "cerf", "cerisier", "chaise", "chameau", "champignon", "chandelier", "chapiteau", "charbon", "chaussette", "cheval", "chocolat", "cigogne", "citrouille", "clavier", "clown", "coccinelle", "coffre", "colibri", "compas", "confiture", "corail", "cornichon", "coussin", "crayon", "cristal", "croissant", "crocodile", "cyclone", 
    "danseur", "dauphin", "dindon", "drapeau", 
    "encrier", "enveloppe", "escargot", "escalier",
    "feuille", "fleur", "fourchette", "framboise", "fuseau",
    "galaxie", "girafe", "glacier", "grenouille", "guitare", 
    "hibou", "horloge", "horizon", 
    "iguane", "insecte", 
    "jardin", "jonquille", "jument",
    "kangourou", "kayak", "koala",
    "labyrinthe", "lac", "lance", "lanterne", "lierre", "limace", "livre", "luciole", "lyre", 
    "mammouth", "mandarine", "mante", "marin", "marmotte", "masque", "mer", "miroir", "montagne", "moustique", "musicien", 
    "neptune", "nuage", 
    "oiseau", "ours", 
    "paon", "papillon", "parapluie", "patinoire", "piano", "pirate", "pluie", "plume", "poisson", "pyramide",
    "quartz", 
    "raisin", "raton", "requin", "robot", "rouge-gorge",
    "sable", "sapin", "sauterelle", "savane", "serpent", "soleil", "soucoupe", "squelette", 
    "tambour", "tapis", "tortue", "train", "tulipe",
    "uniforme", "univers", 
    "valise", "vent", "verre", "village", "vortex", 
    "wagon", 
    "zoo"
]
    return random.choice(mots)

def jouer() -> None:
    """
    Lance une partie de pendu.
    """
    mot_a_deviner: str = choisir_mot()
    lettres_trouvees: List[str] = ["_"] * len(mot_a_deviner)
    lettres_tentees: Set[str] = set()
    erreurs: int = 0
    max_erreurs: int = 6

    print("Bienvenue dans le jeu du pendu !")
    print("Vous avez 6 chances pour deviner le mot.")

    while erreurs < max_erreurs and "_" in lettres_trouvees:
        afficher_pendu(erreurs)
        print("\nMot à deviner :", " ".join(lettres_trouvees))
        print("Lettres tentées :", ", ".join(sorted(lettres_tentees)))

        lettre: str = input("Proposez une lettre : ").lower()
        
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue

        if lettre in lettres_tentees:
            print("Vous avez déjà proposé cette lettre.")
            continue

        lettres_tentees.add(lettre)

        if lettre in mot_a_deviner:
            print(f"Bien joué ! La lettre '{lettre}' est dans le mot.")
            for i, l in enumerate(mot_a_deviner):
                if l == lettre:
                    lettres_trouvees[i] = lettre
        else:
            print(f"Raté ! La lettre '{lettre}' n'est pas dans le mot.")
            erreurs += 1

    afficher_pendu(erreurs)
    if "_" not in lettres_trouvees:
        print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
    else:
        print("\nDommage ! Vous avez perdu. Le mot était :", mot_a_deviner)

if __name__ == "__main__":
    jouer()
