cont = int(input())

saida = []

for i in range(cont):

    entrada = input().split()

    processo = ""

    if len(entrada[0])>len(entrada[1]):

        for j in range(len(entrada[1])):

            processo+=entrada[0][j]+entrada[1][j]

            temp = j

        processo+= entrada[0][temp+1:]

    else:

        for j in range(len(entrada[0])):

            processo+=entrada[0][j]+entrada[1][j]

            temp = j

        processo+= entrada[1][temp+1:]

    saida.append(processo)

for i in saida:

    print(i)
