###Programme de déplacements et d'affichage de boids
import random

###Paramètres modifiables selon la simulation
r1_vers_centre = 1 #Pourcentage de chemin parcouru vers le centre déterminé par r1
r2_min_dist = 10 #Distance minimale entre deux boids avant qu'ils ne se "repoussent"
nb_boids = 50 #Nombre de boids
largeur = 500 #Dimensions de l'espace
hauteur = 500 #Dimensions de l'espace
boids = [] #Tableau contenant les boids
class Point:
    """Classe représentant un point sur le plan"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

###Fonction sur les points
def sum_points(p1,p2):
    """Fonction prenant deux Point en paramètres et renvoyant un autre point avec des coordonnées égales à leur somme"""
    return Point(p1.x + p2.x, p1.y + p2.y)

def sub_points(p1,p2):
    """Fonction prenant deux Point en paramètres et renvoyant un autre point avec des coordonnées égales à la différence entre p1 et p2"""
    return Point(p1.x - p2.x, p1.y - p2.y)

def div_point_scal(p,n):
    """Fonction prenant un point en paramètre et renvoyant un point avec des coordonnées divisées par un scalaire n"""
    return Point(p.x / n, p.y / n)

class Boid:
    """Classe représentant un boid"""
    def __init__(self):
        self.position = Point(0,0) #Point représentant la position du boid
        self.vitesse = Point(0,0) #Point représentant le vecteur vitesse du boid
        self.id = 0 #Numéro unique caractérisant le boid

###Fonctions définissant les règles de déplacement des boids
def r1(b):
    """¨Première règle : le boid essaye de se rapprocher du centre de masse des boids voisins
    Argument : b le boid à traiter et boids le tableau contenant tous les boids"""
    centre = Point(0,0)
    for bp in boids:
        if bp.id != b.id:
            centre = sum_points(centre, bp.position)
    centre = div_point_scal(centre, nb_boids - 1)

    return (r1_vers_centre * div_point_scal(sub_points(centre, b.position),100))

def r2(b):
    """Seconde règle : garder une petite distance avec les autres objets (en particulier : les boids)"""
    c = Point(0,0)
    for bp in boids:
        if b.id != bp.id:
            if abs(sub_points(bp,b)) < r2_min_dist:
                c = sub_points(c, sub_points(bp,b))
    return c

def r3(b):
    """Troisième règle : Les Boids essaient de de faire correspondre leur vitesse avec leur voisins"""
    v_percue = Point(0,0)
    for bp in boids:
        if b.id != bp.id:
            v_percue = sum_points(v_percue, bp.vitesse)

    v_percue = div_point_scal(v_percue, nb_boids - 1)

    return (r2_vers_vit * v_percue)

def initialise_positions():
    """Fonction qui initialise les boids au démarrage du programme en remplissant le tableau boids"""
    boids = [Boid() for i in range(nb_boids)]
    for b in boids:
        b.position = Point(random.randint(0,largeur),random.randint(0,hauteur))
        b.vitesse =  div_point_scal(sub_points(Point(largeur/2,hauteur/2),b.position),100)

def deplace_boids():
    """Fonction déplaçant les boids.
    Arguments : boids un tableau contenant tout les boids
    """

    for b in boids:
        v1, v2, v3 = r1(b), r2(b), r3(b)

        b.vitesse = sum_points(sum_points(sum_points(b.vitesse,v1),v2),v3)
        b.position = sum_points(b.position, b.vitesse)

def affiche_boids():
    """Fonction affichant les boids à l'aide de pygame"""
    pass

def main():
    """Fonction principale"""
    initialise_positions()

    while True :
        affiche_boids()
        deplace_boids()
