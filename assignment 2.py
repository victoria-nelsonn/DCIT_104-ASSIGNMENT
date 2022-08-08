#10958854  Nelson Victoria Esinam
#sum of prime numbers less than a given number



def primenumbers_less_than(n):
    prime_list=[]
    for i in range (2,n):
        for j in range (2,i):
            if i%j==0:
                break
        else:
            prime_list.append(i)
    return sum(prime_list)
print(primenumbers_less_than(11))
