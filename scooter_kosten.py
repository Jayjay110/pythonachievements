invoer = "";

while not isinstance(invoer, float):
    
    try:
        invoer = input("hoeveel kilometer rij je per maand? ")
        
        invoer = float(invoer)

        
        print("Ja, de invoer " + str(invoer) + " is een getal, want ik kan het omzetten naar een float")

    except ValueError:
        print(invoer + " is geen geldig getal!")

verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2 

maandkosten = (invoer * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand

print ("je maandkosten zijn €" , maandkosten )

