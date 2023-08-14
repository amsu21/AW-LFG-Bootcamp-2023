# INITIAL MENU
prime = int(input('Please enter a number: '))

if prime > 1:
    for index in range(2, prime):
        if (prime % index) == 0:
            print(prime, "is not a prime number")
            break
    else:
        print(prime, "is a prime number")
else:
    print(prime, "is not a prime number")