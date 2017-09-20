x = int(input())

saida = []

for k in range(x):

    entrada = input()

    temp =0

    for i in entrada:

        if i in'069':

            temp+=6

        elif i=='1':

            temp+=2

        elif i in'235':

            temp+=5

        elif i=='4':

            temp+=4

        elif i=='7':

            temp+=3

        else:

            temp+=7

    saida.append(temp)

for i in saida:

    print(i,'leds')
