from Algoritmos.Poo.Back import Metodo_de_ordenamiento


class InsertionSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):                              #complejidad  0(n)
        for i in range(1, len(arr)):            # O(n)
            key = arr[i]                        #O(1)
            j = i - 1                           #O(1)
            while j >= 0 and key < arr[j]:      #O(n)
                arr[j + 1] = arr[j]             #O(1)
                j -= 1                          #O(1)
            arr[j + 1] = key                    #O(1)
        return arr