def produit_entiers(liste_entiers):
    x = liste_entiers[0]
    for n in range(1, len(liste_entiers)):
        x = liste_entiers[n] * x
    return x

print(produit_entiers([a, b, c]))

# rename a, b, and c by your number of your list
