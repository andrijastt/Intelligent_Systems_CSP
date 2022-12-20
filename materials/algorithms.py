import pprint

class Algorithm:

    # gets what words and what their size is and if they are horizontal or vertical
    def get_words_count(self, tiles, variables, words):
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
                        if helper == "0h":
                            words_count.append([[i, j], helper, 1, [["0v", 0]]])
                        else:
                            words_count.append([[i, j], helper, 1, []])

                    # if it is first in column or has a black rectangle above it adds new vertical word
                    if (i == 0) or (i != 0 and tiles[i - 1][j]):
                        helper = str(counter) + "v"
                        words_count.append([[i, j], helper, 1, []])

                    # add to size of the adequate word
                    for words in words_count:

                        should_add = True
                        # checking if a space is in the same row where the start of a word is
                        if words[0][0] == i and words[1][1] == "h" and ([i, j] != words[0]):
                            for k in range(words[0][1], j):
                                if tile_row[k]:
                                    should_add = False
                                    break

                            if should_add:
                                words[3].append([helper, words[2]])
                                words[2] += 1

                        should_add = True
                        # checking if a space is in the same column where the start of a word is
                        if words[0][1] == j and words[1][1] == "v" and ([i, j] != words[0]):
                            for k in range(words[0][0], i):
                                if tiles[k][j]:
                                    should_add = False
                                    break

                            if should_add:
                                words[3].append([helper, words[2]])
                                words[2] += 1

                j += 1
                counter += 1

            i += 1

        return words_count

    def get_algorithm_steps(self, tiles, variables, words):
        pass

class ExampleAlgorithm(Algorithm):

    def get_algorithm_steps(self, tiles, variables, words):

        test = Algorithm.get_words_count(self, tiles, variables, words)
        pprint.pprint(test)

        moves_list = [['0h', 0], ['0v', 2], ['1v', 1], ['2h', 1], ['4h', None],
                 ['2h', None], ['1v', None], ['0v', 3], ['1v', 1], ['2h', 1],
                 ['4h', 4], ['5v', 5]]
        domains = {var: [word for word in words] for var in variables}
        solution = []
        for move in moves_list:
            solution.append([move[0], move[1], domains])

        return solution


class Backtracking(Algorithm):

    def get_algorithm_steps(self, tiles, variables, words):

        domains = {var: [word for word in words] for var in variables}

        solution = []
        # all words
        words_count = Algorithm.get_words_count(self, tiles, variables, words)
        # words that already have value
        words_taken = [False for word in words_count]
        # what words are dependent or connected
        words_connected = [word[3] for word in words_count]
        # what words were used
        words_used = []
        # what words are good
        words_good = []

        while(True):

            i = 0
            for i in range(0, len(words_taken)):
                # it doesn't have a word
                if not words_taken[i]:
                    # cycle through all words
                    for word in words:
                        if len(word) == words_count[i][2]:

                            flag = True
                            for j in range(0, i):
                                for connection in words_connected[j]:

                                    # if connection[0] == words_count[i][1] and words_good[j][connection[1]] :




                                pass

                            if flag:
                                words_used.append([words_count[i][1], word])
                                words_good.append([words_count[i][1], word])
                                words_taken[i] = True
                                break


            # last element has taken its word, break cycle
            if words_taken[len(words_taken) - 1]:
                break


        return solution


class ForwardChecking(Algorithm):

    pass


class ArcConsistency(Algorithm):

    pass