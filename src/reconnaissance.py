from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    liste=[]
    b=image.binarisation(S)
    l=b.localisation()
    
    for ref in liste_modeles:
        im_resized=l.resize1(ref.H,ref.W)
        s =im_resized.similitude(ref)
        s1 = round(s,3)
        liste.append(s1)
        '''for i in range(len(liste)):
            num = 0
            if liste[i]>liste[num]:
                num=i'''

    return liste.index(max(liste))

