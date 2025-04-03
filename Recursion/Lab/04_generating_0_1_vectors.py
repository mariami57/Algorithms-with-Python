from typing import List
#
#
# def vector_generator(idx, vector:List[int], n):
#     if idx == n:
#         print("".join(str(v) for v in vector))
#         return
#
#     for number in range(0,2):
#         vector[idx] = number
#         vector_generator(idx+1, vector, n)
#
# n = int(input())
#
# vector_generator(0, [0]*n, n)

def vector_generator2(n, vector:str=""):
    if len(vector) == n:
        print(vector)
        return

    vector_generator2(n, vector + "0")
    vector_generator2(n, vector + "1")


n = int(input())

vector_generator2(n)