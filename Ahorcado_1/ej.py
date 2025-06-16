import random as rd
palabra=["Capuchino", "cafe", "Oreo", "pollos", "programacion"]
indice=rd.randint(0,len(palabra)-1) #  0 1 2 3 4
pal=palabra[indice]
palMayus=pal.upper()#"pollos"
letraPri=palMayus[0] #"p"
letraUlt=palMayus[-1] #"s"
n=(len(palMayus)-2)
subGuio=n * "_" 
pista= letraPri + subGuio + letraUlt
print(pista)
palUser=input("adivine la palabra:").upper()
cond= palUser == palMayus
print("¿Gano?:", cond)