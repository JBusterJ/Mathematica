import re
import time
import math

current_time = time.time()


class Math():
    def factorial(self, n):
        cumulativeMultiplication = 0
        for i in range(n, 0, -1):
            if i == n:
                cumulativeMultiplication += i
            else:
                if i != 0:
                    cumulativeMultiplication *= i
        return cumulativeMultiplication

    # count all unique substrings in a string starting with //
    def countUniqueSubstrings(self, string):
        substringCount = 0
        substrings = []
        for i in range(len(string)):
            if (i + 2 < len(string)):
                if string[i] + string[i + 1] == "//":
                    # check if there are any letters from the alphabet after the //
                    if string[i + 2].isalpha():
                        if substrings.__contains__(string[i + 2]):
                            print(f"{string[i + 2]} is already in the list")
                        else:
                            substringCount += 1
                            substrings.append("//" + string[i + 2])
        return [substringCount, substrings]

    def summation(self, variable, sequenceRange, function, *args):
        cumulativeAddition = 0
        for i in range(sequenceRange + 1)[variable:]:
            if (callable(function)):
                cumulativeAddition += function(i)
            else:
                iSub = 0
                uniqueCalculations = Math().countUniqueSubstrings(function)
                func = function
                if i != 0:
                    iSub = i - 1
                if (len(args) > 0):
                    for num in range(len(args)):
                        if (isinstance(args[num], list)):
                            for anotherNum in range(uniqueCalculations[0]):
                                func = func.replace(
                                    uniqueCalculations[1][anotherNum], str(args[num][iSub]))
                            func = re.sub(
                                r'[^0-9\*\^\/\!\+\-\>\<\=\!=\(\)\[\]\/\\math\\log\. ]+', "i", func)
                            cumulativeFunc = eval(func)
                            t = time.time() - current_time
                            cumulativeAddition += cumulativeFunc
                            break
                        else:
                            print(
                                "Please try again but this time actually give a dataset that can be indexed from")
                else:
                    func = re.sub(
                        r'[^0-9\*\^\/\!\+\-\>\<\=\!=\(\)\[\]\/\\math\\log\. ]+', "i", function)
                    cumulativeFunc = eval(func)
                    t = time.time() - current_time
                    cumulativeAddition += cumulativeFunc

        totalTime = time.time() - current_time
        return cumulativeAddition

    def syntheticDivision(self, coefficients, possiblities):
        if len(possiblities) < 3:
            print(
                f"{possiblities} are passed into the function - this number(set) is either too low or invalid")
            pass

        additive = []
        multiplicative = possiblities

        for x in range(len(multiplicative)):
            results = []
            results.append(coefficients[0])
            for i in range(1, len(coefficients)):
                results.append(
                    coefficients[i] + (results[i - 1] * multiplicative[x]))
            results.append(
                f"Calculated w/ a multiplicative factor of {multiplicative[x]}")
            additive.append(results)

        potentialAnswers = []

        for i in additive:
            if i[len(coefficients) - 1] == 0:
                toSplit = i[len(coefficients)]
                split = toSplit.split(
                    "Calculated w/ a multiplicative factor of ")[1]
                potentialAnswers.append(split)
            else:
                print(f"{i} is not a valid answer")
        return potentialAnswers

    def populationMean(self, populationSample):
        return self.summation(0, len(populationSample), digit) / len(populationSample)

    def informationTheory(self, probability):
        entropy = Math().summation(1, 2, f"-(math.log({probability}))")
        return -(entropy)


def digit(i):
    return i


