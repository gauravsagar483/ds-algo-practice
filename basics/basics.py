# factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def palindrom(num):
    print(f"is {num} Palindrom?:", end=" ")
    return str(num) == str(num)[::-1]


def comapre(a, b):
    return a == b


def is_anagram(a, b):
    return sorted(a) == sorted(b)


def find_max_inList(arr):
    return max(arr)


def fibonacci(n):
    if n < 0:
        raise ValueError("INVALID_INPUT")
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_seq(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            return False

    return True


def lcm(a, b):
    from math import gcd

    return abs(a * b) // gcd(a, b)


def gcd(a, b):
    from math import gcd

    return gcd(a, b)


if __name__ == "__main__":
    print(factorial(5))
    print(palindrom(123241))
    print(find_max_inList([1, 2, 5]))
    print(is_anagram("cat", "tac"))
    print(fibonacci_seq(10))
    print(is_prime(5))
