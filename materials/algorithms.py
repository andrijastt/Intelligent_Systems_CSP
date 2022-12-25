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
                    if temp[0][1] in range(helper[0][1], helper[0][1] + helper[2]) and helper[0][0] in range(temp[0][0], temp[0][0] + temp[2]):
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

        domains = {var: [word for word in words if len(word) == variables[var]] for var in variables}
        solution = []
        # all words
        words_count = Algorithm.get_words_count(self, tiles, variables, words)
        # words that already have value
        words_taken = [["", False] for word in words_count]
        # what words were used
        words_used = []
        # what words are bad
        words_bad = []
        # if backtracing is on
        backtracking = False

        i = 0
        while i < len(words_taken):

            if not backtracking:
                if not words_taken[i][1]:
                    j = 0
                    for domain in domains[words_count[i][1]]:

                        flag = True
                        for k in range(0, i):

                            for connection in words_count[k][3]:

                                if connection[0] == words_count[i][1]:
                                    if words_taken[k][0][connection[1]] != domain[connection[2]]:
                                        flag = False
                                        break

                        if flag:
                            solution.append([words_count[i][1], j, domains])
                            words_taken[i][1] = True
                            words_taken[i][0] = domain
                            backtracking = False
                            break

                        j += 1

                    if not words_taken[i][1]:
                        solution.append([words_count[i][1], None, domains])
                        words_used.append([[], []])
                        backtracking = True
                    else:
                        i += 1
            else:
                # what situation happened so it doesn't happened again
                for j in range(i - 1, -1, -1):

                    if not backtracking:
                        continue

                    k = 0
                    for domain in domains[words_count[j][1]]:

                        if domain == words_taken[j][0] or [domain, words_count[j][1]] in words_bad:
                            k += 1
                            continue

                        flag = True
                        for l in range(0, j):
                            for connection in words_count[l][3]:
                                if connection[0] == words_count[j][1]:
                                    if words_taken[l][0][connection[1]] != domain[connection[2]]:
                                        flag = False
                                        break

                        if flag and [domain, words_count[j][1]] not in words_used:
                            words_used[len(words_used) - 1][0] = words_taken[j][0]
                            words_used[len(words_used) - 1][1] = words_count[j][1]
                            words_bad.append([words_taken[j][0], words_count[j][1]])
                            solution.append([words_count[j][1], k, domains])
                            words_taken[j][0] = domain
                            words_bad.append([words_taken[j][0], words_count[j][1]])
                            words_used.append([words_taken[j][0], words_count[j][1]])
                            i = j + 1
                            backtracking = False
                            break

                        k += 1

                    if not flag:
                        solution.append([words_count[j][1], None, domains])
                        words_taken[j][1] = False
                        words_taken[j][0] = ""

                backtracking = False

        return solution


class ForwardChecking(Algorithm):

    def get_algorithm_steps(self, tiles, variables, words):

        domains = {var: [word for word in words if len(word) == variables[var]] for var in variables}
        solution = []
        # all words
        words_count = Algorithm.get_words_count(self, tiles, variables, words)
        # words that already have value
        words_taken = [["", False] for word in words_count]
        # what words were used
        words_used = []
        # what words are bad
        words_bad = []
        # if backtracing is on
        backtracking = False

        i = 0
        while i < len(words_count):
            if not backtracking:
                if not words_taken[i][1]:
                    j = 0
                    for domain in domains[words_count[i][1]]:

                        flag = True
                        for k in range(0, i):
                            for connection in words_count[k][3]:
                                if connection[0] == words_count[i][1]:
                                    if words_taken[k][0][connection[1]] != domain[connection[2]]:
                                        flag = False
                                        break

                        # here we check forward check
                        for connection in words_count[i][3]:
                            if not flag:
                                continue
                            temps = []
                            for possible_words in domains[connection[0]]:
                                if domain[connection[1]] != possible_words[connection[2]]:
                                    temps.append(possible_words)

                            if temps == domains[connection[0]]:
                                flag = False

                        if flag:
                            solution.append([words_count[i][1], j, domains])
                            words_taken[i][1] = True
                            words_taken[i][0] = domain
                            backtracking = False
                            break

                        j += 1

                    if not words_taken[i][1]:
                        solution.append([words_count[i][1], None, domains])
                        words_used.append([[], []])
                        backtracking = True
                    else:
                        i += 1
            else:
                # what situation happened so it doesn't happened again
                for j in range(i - 1, -1, -1):

                    if not backtracking:
                        continue

                    k = 0
                    for domain in domains[words_count[j][1]]:

                        if domain == words_taken[j][0] or [domain, words_count[j][1]] in words_bad:
                            k += 1
                            continue

                        flag = True
                        for l in range(0, j):
                            for connection in words_count[l][3]:
                                if connection[0] == words_count[j][1]:
                                    if words_taken[l][0][connection[1]] != domain[connection[2]]:
                                        flag = False
                                        break

                        for connection in words_count[i][3]:
                            if not flag:
                                continue
                            temps = []
                            for possible_words in domains[connection[0]]:
                                if domain[connection[1]] != possible_words[connection[2]]:
                                    temps.append(possible_words)
                            if temps == domains[connection[0]]:
                                flag = False

                        if flag and [domain, words_count[j][1]] not in words_used:
                            words_used[len(words_used) - 1][0] = words_taken[j][0]
                            words_used[len(words_used) - 1][1] = words_count[j][1]
                            words_bad.append([words_taken[j][0], words_count[j][1]])
                            solution.append([words_count[j][1], k, domains])
                            words_taken[j][0] = domain
                            words_bad.append([words_taken[j][0], words_count[j][1]])
                            words_used.append([words_taken[j][0], words_count[j][1]])
                            i = j + 1
                            backtracking = False
                            break

                        k += 1

                    if not flag:
                        solution.append([words_count[j][1], None, domains])
                        words_taken[j][1] = False
                        words_taken[j][0] = ""

                backtracking = False

        return solution


class ArcConsistency(Algorithm):
    pass