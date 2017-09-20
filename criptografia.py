cont = int(input())

x,y = range(65,91),range(97,123)

saida=""

while cont>0:

    entrada = input()

    i = len(entrada)-1

    while i>0:

        a = entrada[i]

        a = ord(a)

        if (a in x)or(a in y):

            a+=3

            if a>127:

                a-=128

        if i not in range(len(entrada)//2):

            a-=1

            if a<0:

                a = 127
                
        saida+=chr(a)

        i-=1

    saida+="\n"

    cont-=1

print(saida)
