def insercao(input):
    for i in range(0, len(input)):
        elemento_atual = input[i]
        
        aux = 0
        while i > 0 and input[i - 1] < elemento_atual:
            input[i] = input[i - 1]
            i -= 1
            aux +=1

        input[i] = elemento_atual

input = [100,80,90]
insercao(input)
        
print(input)
