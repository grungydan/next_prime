'''
A simple program that asks the user if they would like to see the next positive prime number, 
and if so, generates and provides that number.
'''
# initial program output
print("The first positive prime number is 2.\n")



# function to determine prime
def is_prime(num):
    if num % 2 == 0: 
        return False
    
    for i in range (3, int(num**0.5) + 1, 2):
        if num % i == 0: 
            return False

    return True

# generator for prime numbers
def gen_primes():
    n = 3
    while(True):
        if is_prime(n):
            yield n
        n += 2

# something here is broken as shit
# can't get it to give me just one next prime, enters an endless loop
# if I set it up where pressing enter gies the next number, then the break doesn't work


def gimme():
    generator = gen_primes()
    print("Press Enter to see the next prime number or N to quit.")
    
    while True:

        response = input()

        if response.lower() == 'n':
            break
        else:
            print(generator.__next__())

if __name__ == '__main__':
    gimme()
    
