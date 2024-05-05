from Algoritmos.Poo.Back import Metodo_de_ordenamiento


class HeapSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):                                                          #Complejidad O(log n)
        def heapify(arr, n, i):                                             #O(1)

            largest = i                                                     #O(1)                                                             
            left = 2 * i + 1                                                #O(1)
            right = 2 * i + 2                                               #O(1)

            if left < n and arr[left] > arr[largest]:                        #O(1)             
                largest = left                                               #O(1)

            if right < n and arr[right] > arr[largest]:                      #O(1)
                largest = right                                               #O(1) 

            if largest != i:                                                 #O(1)
                arr[i], arr[largest] = arr[largest], arr[i]                  #O(1)
                heapify(arr, n, largest)                                     #O(log n)

        n = len(arr)                                                        #O(1)

        for i in range(n // 2 - 1, -1, -1):                                 #O(n)
            heapify(arr, n, i)                                              #O(n)

        for i in range(n - 1, 0, -1):                                       #O(n)
            arr[i], arr[0] = arr[0], arr[i]                                 #O(n)
            heapify(arr, i, 0)                                              #O(n)

        return arr