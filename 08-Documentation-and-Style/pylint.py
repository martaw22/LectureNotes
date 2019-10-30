"""
This is code for finding prime numbers.
"""

# Prime number finder with a logic bug
def check_prime(num):
    '''
    Checks to see if a number is prime.
    :param int num:
    :returns bool:
    '''
    is_prime = True
    for i in range(num):
        if (num%i) == 0:
            is_prime = False
            break
        else:
            pass
    return is_prime


# Run the following code if the file is run at the command line. 
#I think there is a bug in here somewhere.
if __name__ == "__main__":
    NUM = int(input("Enter a number: "))
    if check_prime(NUM): 
      print("Is prime!")
    else:
      print("Not a prime.")
