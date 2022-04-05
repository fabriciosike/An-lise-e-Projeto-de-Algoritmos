matriz = {}
rotas = []

t = int(input())

for i in range(t):
    l = 0
    while(l < 5):
        l+=1
        e = input().split()
        matriz[l] = e

    if (matriz[0][0] == "1"): 
        print("ROBBERS")

    else:
        resultado = "ROBBERS"
        rotas.append([0, 0])
        matriz[0][0] = "*"

        for posicao in rotas: 
            cima = posicao[0] - 1
            baixo = posicao[0] + 1
            esquerda = posicao[1] - 1
            direita = posicao[1] + 1 

        if (cima > -1 and cima < 5): 
            if (matriz[cima][posicao[1]] == "0"):
                rotas.append([cima, posicao[1]])
                matriz[cima][posicao[1]] = '*'
        
        if (baixo > -1 and baixo < 5): 
            if (matriz[baixo][posicao[1]] == "0"):
                rotas.append([baixo, posicao[1]])
                matriz[baixo][posicao[1]] = '*'

        if (esquerda > -1 and esquerda < 5): 
            if (matriz[posicao[0][esquerda]] == "0"):
                rotas.append([posicao[0], esquerda])
                matriz[posicao[0]][esquerda] = '*'
        
        if (direita > -1 and direita < 5): 
            if (matriz[posicao[0][direita]] == "0"):
                rotas.append([posicao[0], direita])
                matriz[posicao[0]][direita] = '*'

        if ([4, 4]) in rotas: 
            resultado = "COPS"
            break

        print(resultado)
        rotas.clear()
        matriz.clear()

        

        

            

        







