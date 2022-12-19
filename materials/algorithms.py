import pprint

class Algorithm:
    def get_algorithm_steps(self, tiles, variables, words):
        pass

class ExampleAlgorithm(Algorithm):

    def get_algorithm_steps(self, tiles, variables, words):
        moves_list = [['0h', 0], ['0v', 2], ['1v', 1], ['2h', 1], ['4h', None],
                 ['2h', None], ['1v', None], ['0v', 3], ['1v', 1], ['2h', 1],
                 ['4h', 4], ['5v', 5]]
        domains = {var: [word for word in words] for var in variables}
        solution = []
        for move in moves_list:
            solution.append([move[0], move[1], domains])

        # print(tiles)
        # print(variables)
        # print(words)
        # pprint.pprint(domains)
        pprint.pprint(solution)

        return solution


class Backtracking(Algorithm):

    def get_algorithm_steps(self, tiles, variables, words):

        domains = {var: [word for word in words] for var in variables}

        # sta je cilj, ja prvo moram da napravim koliko polja mora da popuni neka rec u kom smeru
        # posle kada to uradim treba da isprobavam

        solution = []

        words_count = []
        counter = 0
        i = 0
        for tile_row in tiles:
            j = 0
            for tile in tile_row:
                if not tile:

                    # if it is first in row or has a black rectangle behind it, adds new horizontal word
                    if (counter % len(tile_row) == 0) or (j != 0 and tile_row[j - 1]):
                        helper = str(counter) + "h"
                        size = 0
                        words_count.append([helper, size])

                    # if it is first in column or has a black rectangle above it adds new vertical word
                    if (i == 0) or (i != 0 and tiles[i-1][j]):
                        helper = str(counter) + "v"
                        size = 0
                        words_count.append([helper, size])

                    # add to size of the adequate word
                    # for words in words_count:

                        # checking if it is a horizontal word or vertical
                        # if words[0][1] == "h":


                else: # if it is a black block it needs to
                    tile = True
                counter += 1
                i += 1

        while(True):

            for word in words:
                word = 1


        return solution


class ForwardChecking(Algorithm):

    pass


class ArcConsistency(Algorithm):

    pass