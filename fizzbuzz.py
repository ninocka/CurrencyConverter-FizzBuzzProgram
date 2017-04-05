def play():
    while True:
        number = int(raw_input('Pick a number in range 1-100 >>> '))
        if number < 1 or number > 100:
            print "Out of range!Try one more time!"
            break
        else:
            try:
                for number in range(1, number + 1):
                    if number % 3 == 0 and number % 5 == 0:
                        print "FizzBuzz"
                    elif number % 3 == 0:
                        print "Fizz"
                    elif number % 5 == 0:
                        print "Buzz"
                    else:
                        print str(number)
                break
            except ValueError:
                print "That\'s not a number!"


while True:
    try:
        game = raw_input("Want to play FizzBuzz game? 'y' for yes or 'n' for no >>> ")
        if game.lower() == "y":
            play()
        if game.lower() == "n":
            print "Thank you and goodbye"
            break
    except ValueError:
        print "That\'s not a number!"
