# gcd: calculate greatest common divisor of two numbers
# O(log(min(a, b)))
def gcd(a, b):
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a


# lcm: calculate least common multiple of two numbers
#  O(log(min(a, b)))
def lcm(a, b):
    return a * b // gcd(a, b)


# is_prime: judge the given number is prime or not
# O(sqrt(n))
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True


# eratosthenes_sieve: return 1 to given number are prime or not
# O(Nlog(log(N)))
def eratosthenes_sieve(n):
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        j = i + i
        while j <= n:
            is_prime[j] = False
            j += i
    return is_prime


# divisor: get all divisor of given number
# O(log(N))
def divisor(n):
    divisor_list = set()
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            divisor_list.add(i)
            divisor_list.add(n // i)
    return list(divisor_list)


# prime_decomposition: calculate prime decomposition for given number
# O(sqrt(N))
def prime_decomposition(n):
    prime_list = []
    for i in range(2, n + 1):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            prime_list.append(i)
    if n > 1:
        prime_list.append(n)
    return prime_list

