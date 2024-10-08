vector = [10, 3, 4, 0, 1, 99, 3, 1, 0, 102, 7, 5, 6, 4, 8, 7, 3, 2, 4, 0, 1, 5, 13, 22, 11, 33, 44, 15, 231, 3213, 12, 1]

def insertion_sort():
    for i in range(1, len(vector)):         # move para direita
        value = vector[i]  

        j = i - 1                           # Elemento da esquerda
        while j >= 0:                   
            if(vector[j] <= value):         # Se elemento da direita >= esquerda
                break

            vector[j + 1] = vector[j]       # vai empurrando os valores para direita ex: 2 3 4 5 6 1 -> 2 3 4 5 6 6 -> 2 3 4 5 5 6 .. 2 2 3 4 5 6 -> 1 2 3 4 5 6
            j -= 1                          # volta um espaço
                
        vector[j + 1] = value               # finalmente insere value en no devido local

print(vector)
insertion_sort()
print(vector)