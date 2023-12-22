
# List of all letters of the alphabet
liste = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m","n", "o", "p","q","r","s","t","u","v","w","x","y","z"]

# The user can write his password
mot = input('Enter your password')
chaine = str()

# We set "test" so that if "chaine" = "mot" we give to the user his password
def test(chaine,mot):
    if chaine == mot:
        print('Your password is :', chaine)

# We test all possible combination
for l in liste:
    chaine = l
    test(chaine,mot)

    for l2 in liste:
        chaine = l + l2
        test(chaine,mot)

        for l3 in liste:
            chaine = l + l2 + l3
            test(chaine,mot)

            for l4 in liste:
                chaine = l + l2 + l3 + l4
                test(chaine,mot)

                for l5 in liste:
                    chaine = l + l2 + l3 + l4 + l5
                    test(chaine,mot)



