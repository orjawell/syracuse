
reseach_mode = False 
# Mode de recherche, afin de voir toutes les itérations en cours. Cela peut prendre plus de temps à faire la recherche, je vous déconseille de passer cela sur vrai. (Sauf si vous en avez besoin)

import time as t
import matplotlib.pyplot as plt


def convert(sec):
    mins = sec // 60
    sec = round(sec%60,0)
    hours = mins //60
    mins = mins  %60
    return int(hours),int(mins),sec


def syracuse(x,iteration):
   
    """
    Parameters
    ----------
    x : INT
        X de base.
    iteration : INT
        Nombres de vol au quel on souhaite dépasser.

    Returns
    -------
    val : INT
        x au quel le nombre de vol > vol recherché.
    i : INT
        Nombre de vol trouvé..

    """
    if x == 0 or x == 1:
        return
    i = 0
    val = x
    start = t.time()
    while i <= iteration:
        i = 0
        iteration_liste = []
        result = []
        if x != val:
            x = val + 1
            val = val + 1
            if reseach_mode != False:
                print('new x: ', val)
        while x!=1:
            if x%2==0:
                x = x/2
                i = i+1
                iteration_liste.append(i)
                result.append(x)
                if reseach_mode != False:
                    print("intermediate result: ",x)
            else:
                x = (3*x)+1
                i = i+1
                iteration_liste.append(i)
                result.append(x)
                if reseach_mode != False:
                    print("intermediate result: ",x)
    stop = t.time()
    temps_passe_s = stop - start
    temps_final = convert(temps_passe_s)
    plt.plot(iteration_liste, result, label="Résultat/Nb d'itération")
    plt.ylabel("résultat")
    plt.xlabel("itération")
    plt.legend()
    plt.show()
    print('time_elapsed : ', temps_final)
    return val,i