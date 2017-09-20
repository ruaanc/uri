retorno = []

entrada = input()

while not(entrada == '0 0'):

    processo = list(entrada[2:])

    while(entrada[0] in processo):

        processo.remove(entrada[0])

    if len(processo) == 0:

        retorno.append(0)

    else:

        temp = ""

        for i in processo:

            temp+=i

        retorno.append(int(temp))

    entrada = input()

for i in retorno:

    print (i)
