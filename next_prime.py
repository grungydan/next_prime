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
    yield 2
    n = 3
    while(True):
        if is_prime(n):
            yield n
        n += 2


def main():
    more = "y"
    generator = gen_primes()
    while more[0].lower == "y":
        print("The next prime number is ", generator.next(),".\n")
        more = input("Would you like to see the next prime number? (Y/N): ")


    
if __name__ == '__main__':
    main()


    

