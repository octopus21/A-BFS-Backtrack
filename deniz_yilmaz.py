import numpy as np
import math

class BinaryMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(row))
        print()

    def mark_walls(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.matrix[r][c] == '1':
                    self.matrix[r][c] = 'X'

    def find_closest_path(self, start, destination):
        def backtrack(x, y):
            if x == destination[0] and y == destination[1]:
                return True
            if self.matrix[x][y] in ['#', 'X']:
                return False

            self.matrix[x][y] = '#'  # Dugum gecildi

            if x > 0 and backtrack(x - 1, y):  # Yukari
                return True
            if x < self.rows - 1 and backtrack(x + 1, y):  # Asagi
                return True
            if y > 0 and backtrack(x, y - 1):  # Sol
                return True
            if y < self.cols - 1 and backtrack(x, y + 1):  # Sag
                return True

            self.matrix[x][y] = '.'  # Donuste ugranmayan dugumler
            return False

        start_x, start_y = start
        if not (0 <= start_x < self.rows and 0 <= start_y < self.cols):
            print("Baslangic noktasi disarda.")
            return

        dest_x, dest_y = destination
        if not (0 <= dest_x < self.rows and 0 <= dest_y < self.cols):
            print("Varis noktasi disarda.")
            return

        if self.matrix[start_x][start_y] == 'X' or self.matrix[dest_x][dest_y] == 'X':
            print("Varis ya da baslangic noktasi cakisiyor")
            return

        if backtrack(start_x, start_y):
            self.print_matrix()
        else:
            print("Patika yok.")


if __name__ == "__main__":
    input_stringmap = input("Lutfen haritayı giriniz, baslangic A, bitis B olarak isaretlenmeli [n*n olmalı ve örnek input 1 0 A 0 1 1 B 0 0 seklinde olabilir.]")
    input_matrix = np.array(input_stringmap.split(), dtype=object)
    n = int(math.sqrt(len(input_matrix)))
    input_matrix = input_matrix.reshape(n, n)  # matrixi n*n hale getiriyoruz.

    bm = BinaryMatrix(input_matrix)
    print("Girilen Harita:")
    bm.print_matrix()

    bm.mark_walls()
    print("Dönüştürülen Harita:")
    bm.print_matrix()

    for j in range(n):
        for i in range(n):
            if input_matrix[j][i] == 'A':
                start_coords = (j, i)
            elif input_matrix[j][i] == 'B':
                dest_coords = (j, i)


    print("A'dan B'ye gidilen patika:")
    bm.find_closest_path(start_coords, dest_coords)
