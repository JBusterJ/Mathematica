# from kivy.app import App
# from kivy.uix.button import Button

# class CoolButton(Button):
#     pass

# class mathApp(App):
#     guiScale = (None, None)

#     def build(self):
#         return Button(
#             text='Hello World',
#             pos=(50, 50),
#             size=(100, 100),
#             size_hint=guiScale
#         )


# if __name__ == "__main__":
#     mathApp().run()
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
        # need to be able to call variables which are index of summation of array")
        # print(callable(function))
        for i in range(sequenceRange + 1)[variable:]:
            if (callable(function)):
                cumulativeAddition += function(i)
            else:
                iSub = 0
                uniqueCalculations = Math().countUniqueSubstrings(function)
                func = function
                print(
                    f"{uniqueCalculations[0]} unique substrings for index functions")
                print(f"{func} has been outputed from the index replacing algorithm")
                print(str(len(args)) + " number of additional arguments")
                if i != 0:
                    iSub = i - 1
                if (len(args) > 0):
                    for num in range(len(args)):
                        if (isinstance(args[num], list)):
                            for anotherNum in range(uniqueCalculations[0]):
                                # print(f"{uniqueCalculations[1]}, with an index of {anotherNum}")
                                # print(f"{args[0]}, with an index of {anotherNum} and a main index of {i}")
                                func = func.replace(
                                    uniqueCalculations[1][anotherNum], str(args[num][iSub]))
                            print("received a list, doing index calculation")
                            # print(function)
                            func = re.sub(
                                r'[^0-9\*\^\/\!\+\-\>\<\=\!=\(\)\[\]\/\\math\\log\. ]+', "i", func)
                            print(func)
                            cumulativeFunc = eval(func)
                            t = time.time() - current_time
                            print(
                                f"Original filtered function: {func} \n Cumulative function: {cumulativeFunc} || [{round(t, 4)}] \n")
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
                    print(
                        f"Original filtered function: {func} \n Cumulative function: {cumulativeFunc} || [{round(t, 4)}] \n")
                    cumulativeAddition += cumulativeFunc
                    # print(func)

        totalTime = time.time() - current_time
        print(f"Time since initial function call: {totalTime}")
        return cumulativeAddition


    def syntheticDivision(self, coefficients, possiblities):
        if len(possiblities) < 3:
            print(
                f"{possiblities} are passed into the function - this number(set) is either too low or invalid")
            pass

        additive = []
        multiplicative = possiblities

        print(coefficients)

        # im working on a super cool math sandbox / calculator thingy that calculates math likew super fast cauyse yes cool and yes and stuff and yeah
        # so what ive added so far:
        # synthetic division
        # summation
        # rational root test (not available in this version of the project (i have two versions, this is PY version and the other version is JS))
        # first I'll showcase summation, then synthetic division

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

        print(f"{len(coefficients)} coefficients were passed into the function")

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
        # (can be used as X-bar)

        return self.summation(0, len(populationSample), digit) / len(populationSample)

    def informationTheory(self, probability):
        entropy = Math().summation(1, 2, f"-(math.log({probability}))")
        return -(entropy)


def digit(i):
    return i


def simpleSummationFormula(n, r):
    def simpleAdd(n):
        return 4 * n + 5
    return Math().summation(n, r, simpleAdd)


print(Math().factorial(5))  # expected output: 120
print(Math().summation(5, 10, digit))  # expected output: 45
print(simpleSummationFormula(1, 100))  # expected output: 20700
print(simpleSummationFormula(Math().summation(5, 10, digit),
      Math().factorial(5)))  # expected output: 25460
# print(Math().populationMean(30))
# expected output: 5.5
print(Math().populationMean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# to use 'populationMean' as 'x-bar' just add in the numbers you want to find the mean of as the dataset, instead of the whole dataset.
theta = 30
# you can plug in any value variable you want, as long as you have an f-string. Non-F-strings can also be used but will be a pain for you to deal with.
print(Math().summation(0, 100, f"3 * {theta} > 30"))
# greater than, less than, equal to, greater than or equal to, less than or equal to, and not equal to signs are not supported as of now. It should be fairly simple to implement them into my code, though
# >, < and != have been implemented. These now allow for you to accept 'true' and 'false' statements as answers. = has not been implemented yet because it will require for me to add some automatic if statement generating, since eval doesn't evaluate = expression

print(Math().syntheticDivision(
    [1, 1, -11, -5, 30], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# so here's how I use it (no user interface or fancy buttons and stuff you can type into and click to get an answer YET)

print(Math().summation(0, 5, "x"))  # should just ouput 0 + 1 + 2 + 3 + 4 + 5 = 15\
# you can do more complicated stuff as well (like algebraic equations/expressions)
print(Math().summation(0, 5, "3 * x + 2 / 38 * 12"))
# sorry i forgot to mention that you cant use coefficients as you would in normal algebraic terms (like 3x + 2) you would need to do (3 * x + 2) which is a pain but i should be able to fix it fast
# you can also prove inequalities (true/false)
print(Math().summation(0, 5, "3 * x > x"))  # should be true
# it says 5 but it outputs true. it says 5 just because thats the number of times it outputed true (it considers true to be 1 for some reason)
print(Math().summation(0, 5, "3 * x < x"))  # should be false
# for the next one != is used, meaning that it is NOT EQUAL TO
print(Math().summation(0, 5, "3 * x != x"))  # should be true

print(Math().syntheticDivision(
    [1, 1, -11, -5, 30], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# trust me, this will output the correct answer. it is testing from these series of possibilities but it wont simplify the polynomial YET. it only verifies if the answer is correct.
# 2 shouold be outputted as the answer
# I probably spent wayu longer than i needed to making this but eh it was cool i think


# print(Math().factorial(5))

# print(Math().summation(0, 5, "x * //", [1, 3, 2, 5, 3, 6]))
# expected output (including the array part): 0+3+4+15+12+30 = 64
# got output: 55
# expected output (excluding the array part): 0+1+2+3+4+5 = 15
# updated code (to fix array part), replace '''{}''' with // because for some reason my genius brain thought that {} (the symbol for formatting) wouldn't cause any problems

# print(Math().countUniqueSubstrings("//a //b //c //d //e //f"))

print(Math().summation(0, 5, "i * //a + //b + //c", [1, 2, 3, 4, 5, 6]))
# 0 * 1 + 2 + 3 = 5
# 1 * 1 + 2 + 3 = 6
# 2 * 1 + 2 + 3 = 7
# 3 * 1 + 2 + 3 = 8
# 4 * 1 + 2 + 3 = 9
# 5 * 1 + 2 + 3 = 10
# expected output: 5+6+7+8+9+10 = 45

# vr 82
# math 55
# nr 54
# rc 80

# print(Math().informationTheory(0.5))
# print(Math().summation(0, 2, "x"))

# print(Math().summation(0, 2, "//a * //b * //c * //d * i", [[0], [3], [8], [12], [16]])) to be added soon
# right now, //a //b are supposed to be list[index i] but right now they're acting in the order they show up so for example:
# e = [0, 3, 8, 12, 16]
# a = 0
# b = 3
# c = 8
# d = 12
# that's not how it should work....

print(Math().summation(0, 10, "x")) #outputs 55
print(Math().summation(1, 10, "x / x")) #outputs 10

# print(Math().summation(1, 2, "//a * //b * //c * //d * i", [1], [2], [3], [4]))
print(Math().summation(1, 5, "//a + //b + //c * 3 / 2", [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))

# SUMMATION IS WORKING!!!!!!

print(Math().summation(1, 10, "x")) # results 1 + 2 + 3 ... all the way up to ten
# upon computing this, you will get the answer to be 55 (I think)
# 1+2+3+4+5+6+7+8+9+10 = 55
# expected output: 55
# got output: 55 (tried and tested)

print(Math().summation(1, 5, "5 * x + 3")) # you can add more complex algebraic expressions as well, and can also plug in functions in the position of the string! though I only recommend using functions when you need to compute complex "things"
# expected output: 8+13+18+23+28....

print(Math().summation(1, 5, "x * //a", [1, 2, 3, 4, 5]))
# you can even plug in indexs of an infinite amount of arrays!
# x * 2, and so on. see the math equation on the bottom right

# using this summation algorithm, you can quite easily recreate other formulae
# including the:
# population mean (doesn't require the summation algorithm to work!)
# information theory / entropy: (work in progress)
# and many more....

# print(Math().informationTheory(probability)) # I am still working on this feature. See more in a new video coming up soon (probably) (I think) (I hope) (I don't know)

# print(Math().factorial(5))

# (bottom summation)= https://quicklatex.com/cache3/f1/ql_c361c0d65fb8eb50ded3bb920f5558f1_l3.png
print(Math().summation(1, 10, "2-n"))