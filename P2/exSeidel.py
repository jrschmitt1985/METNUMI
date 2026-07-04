while np.max(Epest) > Eppara:

    for i in range(n):

        soma1 = 0
        soma2 = 0

        for j in range(n):

            if j < i:

                soma1 += 1

            elif j > i:

                soma2 += 2

        x_new[i] = (soma1 - soma2)/soma1