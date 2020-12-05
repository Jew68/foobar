alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def alphabet_replace(a):
    index_counter = 0
    for n in alphabet:
        index_counter += 1
        if n == a:
            return alphabet[-index_counter]


def solution(s):
    return ''.join([alphabet_replace(n) if n in alphabet else n for n in s])
