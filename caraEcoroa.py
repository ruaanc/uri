i = int(input())

while not(i==0):

    maria = 0

    joao = 0

    entrada = input()

    j = len(entrada)-1

    while j>=0:

        if entrada[j]=='0':

            maria+=1

        else:

            joao+=1

        j-=2

    print("Mary won {0} times and John won {1} times".format(maria,joao))

    i = int(input())
