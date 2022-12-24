import pprint

class Algorithm:

    # gets what words and what their size is and if they are horizontal or vertical
    def get_words_count(self, tiles, variables, words):
        words_count = []

        for var in variables:
            i = 0
            helper = ""
            while var[i].isdigit():
                helper += var[i]
                i += 1
            num = int(helper)
            helper = [[int(num / len(tiles[0])), num % len(tiles[0])], var, variables[var], []]
            words_count.append(helper)

            for temp in words_count:
                if temp == helper:
                    break

                if temp[1][1] == "h" and helper[1][len(helper[1]) - 1] == "v":
                    if temp[0][0] in range(helper[0][0], helper[0][0] + helper[2]) and helper[0][0] in range(temp[0][0], temp[0][0] + temp[2]):
                        temp[3].append([helper[1], helper[0][1] - temp[0][1], helper[0][0] - temp[0][0]])

                if temp[1][1] == "v" and helper[1][len(helper[1]) - 1] == "h":
                    if temp[0][1] in range(helper[0][1], helper[0][1] + helper[2]) and helper[0][1] in range(temp[0][1], temp[0][1] + temp[2]):
                        temp[3].append([helper[1], helper[0][0] - temp[0][0], temp[0][1] - helper[0][1]])

        return words_count

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

        return solution


class Backtracking(Algorithm):

    def get_algorithm_steps(self, tiles, variables, words):

        # domains = {var: [word for word in words if len(word) == variables[var]] for var in variables}
        domains = {var: [word for word in words] for var in variables}

        solution = []
        # all words
        words_count = Algorithm.get_words_count(self, tiles, variables, words)
        # words that already have value
        words_taken = [["", False] for word in words_count]
        # what words are dependent or connected
        words_connected = [word[3] for word in words_count]
        # what words were used
        words_used = []
        # what words are good
        words_good = []
        # if backtracing is on
        backtracking = False

        i = 0
        while i < len(words_taken):

            # if we dont backtrack
            if not backtracking:
                # it doesn't have a word
                if not words_taken[i][1]:
                    # cycle through all words
                    k = 0
                    for word in words:
                        # if word length is good
                        if len(word) == words_count[i][2]:

                            if word in words_good and words_count[i][2] > 1:
                                k += 1
                                continue

                            flag = True
                            for j in range(0, i):
                                for connection in words_connected[j]:

                                    if connection[0] == words_count[i][1] \
                                            and [words_count[i][1], word] not in words_used:
                                            # check if words are good
                                            if words_taken[j][0][connection[1]] != word[connection[2]]:
                                                flag = False
                                            else:
                                                if not flag:
                                                    flag = True

                            if flag:
                                words_good.append(word)
                                words_taken[i][1] = True
                                words_taken[i][0] = word
                                solution.append([words_count[i][1], k, domains])
                                i += 1
                                backtracking = False
                                break
                            else:
                                backtracking = True

                        k += 1

                if backtracking:
                    solution.append([words_count[i][1], None, domains])
            else:
                # we are going backwards and are searching for new words
                for j in range(i - 1, -1, -1):
                    words_used.append([words_count[j][1], words_taken[j][0]])

                    k = 0
                    for word in words:
                        # if word length is good
                        if len(word) == words_count[j][2]:

                            if [words_count[j][1], word] in words_used:
                                continue

                            flag = True
                            for l in range(0, j):
                                for connection in words_connected[l]:

                                    if connection[0] == words_count[j][1] \
                                            and [words_count[j][1], word] not in words_used:
                                        # check if words are good
                                        if words_taken[l][0][connection[1]] != word[connection[2]]:
                                            flag = False
                                        else:
                                            if not flag:
                                                flag = True

                            if flag:
                                words_good.append(word)
                                words_taken[j][1] = True
                                words_taken[j][0] = word
                                solution.append([words_count[j][1], k+1, domains])
                                backtracking = False
                                words_used = [words_count[j][1], word]
                                i = j + 1
                                break
                            else:
                                words_taken[j][1] = False
                                words_taken[j][0] = ""
                        k += 1

                    if backtracking:
                        solution.append([words_count[j][1], None, domains])
                    else:
                        break

        return solution


class ForwardChecking(Algorithm):

    pass


class ArcConsistency(Algorithm):

    pass