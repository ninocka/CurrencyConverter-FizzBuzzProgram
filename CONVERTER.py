# -*- coding: utf-8 -*-

def play():
    conversion_choice = raw_input("Please choose between two possible conversions: EUR to USD (a) and USD to EUR (b): ")
    while True:
        if conversion_choice.lower() == "a":
            try:
                eur_you_have = float(raw_input("This is EUR to USD converter. \
                Please insert EUR you want to convert into USD:"))
                eur_per_usd = 1.06
                usd = eur_you_have * eur_per_usd
                print str(eur_you_have) + " EUR " + "is " + str(usd) + " USD"
                break
            except ValueError:
                print "This is not a number!"
                continue

        if conversion_choice.lower() == "b":
            try:
                usd_you_have = float(raw_input("This is USD to EUR converter. \
                Please insert USD you want to convert into EUR:"))
                usd_per_eur = 0.94
                eur = usd_you_have * usd_per_eur
                print str(usd_you_have) + " USD " + "is " + str(eur) + " EUR"
                break
            except ValueError:
                print "This is not a number!"
                continue

        else:
            print "a or b, please"
            conversion_choice = raw_input("Please choose between two possible convertions: EUR to USD (a) and USD to EUR (b): ")



print "Hello! This is UnitConverter. I convert EUR to USD and USD to EUR."

while True:
    new_conversion = str(raw_input("Would you like to make a conversion? Choose 'y' for yes and 'n' for no >>> "))
    if new_conversion.lower() == "y":
        play()

    elif new_conversion.lower() == "n":
        print "Thank you and goodbye"
        break



