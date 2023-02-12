import math

def is_prime(num):
    if num > 9999999900000001:
        raise ValueError("Input number is too large for this implementation")
    if num < 2:
        return False
    if num == 2:
        return True

    check_list = list(range(2, math.floor(math.sqrt(num))+1))
    for x in check_list:
        if (num % x) == 0:
            return False
    return True

def get_primes_from_list(list):
    return filter(is_prime, list)

if __name__ == "__main__":
    my_list = list(range(2,5000))
    my_prime = list(get_primes_from_list(my_list))
    if len(my_prime) < 500:
        print(my_prime)
    print(len(my_prime))
