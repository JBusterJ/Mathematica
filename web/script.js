/*
    CODE README:
    all functions or code snippets with comments with links on top of them are resources used to fuel that part of the code. Some functions are entirely composed of these snippets because I was unable to implement that feature myself. Sorry :/
    Although all of this code is Vanilla JavaScript, a function is entirely composed of a library called "KaTeX". Katex is technically just another markdown language, similar to HTML, but designed entirely for Mathematical rendering, and is technically a lightweight version of a larger markdown language known as "LaTeX" which is suitable for the creation of full fledged documents, whereas katex only makes use of the Mathematical rendering, making it a great solution for only writing maths. 
    If I'm going to be uploading this on Github, why am I adding the README here? I don't know, ask someone else. Progress so far includes the capability of finding solutions to polynomials using synthetic division and the rational root test. I don't know how to implement a strategy that gets a 100% accuracy in calculating polynomials (even irregular ones, including depressed cubics, and so on). For now, I'll rely on synthetic division for simplifying high-degree polynomials and converting them into trinomials which can be solved using a hardcoded function (which is probably not going to be much of a pain) 
*/

/* https://stackoverflow.com/questions/19846078/how-to-read-from-chromes-console-in-javascript */
/* for the sole purpose of gathering everything being logged into the console (not including error messages) to easily display on UI what is going on in the backend */

console.defaultLog = console.log.bind(console);
console.logs = [];
console.log = function () {
    // default &  console.log()
    console.defaultLog.apply(console, arguments);
    // new & array data
    console.logs.push(Array.from(arguments));
}

testingPolynomialDetection();

/* Onclick of the button */
document.getElementById("calculate").onclick = function () {
    var output = document.createElement("p");
    // output.innerHTML = renderMath("c = a^2+b^2");
    // sigma
    // n = 0
    // goes till 100
    // 0, 1, 2, 3, 4, 5, 6, 7, 8 ...
    // xi
    // output.innerHTML = renderMath("\\sum_{n=0}^{100} (\\frac{n}{100} * 0) = 0");
    // var demo = getCoef(document.getElementById("input").value);
    var demo = getCoef("ax^2+bx+c");
    console.log(JSON.parse(demo));
    for (var i = 0; i < demo.length; i++) {
        console.log(demo[i]);
    }
    // document.body.appendChild(output);
}
/* straight up clone of testingPolynomialDetection but without any hardcoded values - it should work fine */
function polynomial(nomial) {
    /* hard coded polynomial in 'getCoef()' to make sure it is a 100 percent accurate */
    var demo = getCoef(nomial);

    /* https://stackoverflow.com/questions/30861631/object-length-undefined-in-javascript */
    var keys = Object.keys(demo);

    /* for easier accessing of all coefficients */
    var coeff = [];

    /* looping through 'demo' to add all coefficients to the coeff array */
    for (var i = 0; i < keys.length; i++) {
        // console.log(demo[keys[i]]);
        coeff.push(demo[keys[i]]);
    }

    /* printing coeff[keys.length - 1] should return the coefficient of the highest degree term in the polynomial (the term with the highest power) */
    // console.log("First coefficient: " + coeff[keys.length - 1], ", Last coefficient: " + coeff[0]);

    /* although the rational root test function accepts the first and last coefficients, we give it the last coefficient in place of the first coefficient. This is because the place of the leading term coefficient is actually at the end of the array (meaning it's in the last position) whereas it is considered to be the first coefficient. It is confusing to explain without printing into the console what I mean */

    /* performing the rational root test and synthetic division (to get a list of possible answers using an algorithm, and using another algorithm to determine which of those answers are correct solutions for any variable in the place of x (not limited to being only x)) */

    var rationalRoots = rationalRootTest(coeff[keys.length - 1], coeff[0]);

    /* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse */

    /* here we HAVE to make sure to reverse the array (doing this earlier may have saved some confusing, but I forgot to do it) since the order of the coefficients in the 'coeff' array is reversed (meaning that the last term (the constant term) comes first, and the first term (leading term) comes last), but the synthetic division NEEDS an array with the coefficients in order. Otherwise you will get the answer to a polynomial, ax^3+bx^2+cx+d as the answer for dx^3+cx^2+bx+a */

    var syntheticOutcome = syntheticDivision(coeff.reverse(), rationalRoots);

    /* print the outcome of the algorithms - there is a probability that these algorithms do NOT provide all correct answers, and sometimes may not provide any answer at all. This is just due to them not using the respective formulae for their polynomials (for example, these algorithms are NOT coded to perform the cubic equation on cubics, or solve trinomials) which makes them only viable for simplifying high degree polynomials instead of trying to solve them. I will be implementing nearly a feature to increase accuracy later, by using some method other than the rational root test because it does not suffice. */

    // console.log(syntheticOutcome);

    if (syntheticOutcome.length == 0) {
        console.log("%cSynthetic division was unable to find a solution to your polynomial. Please try solving your polynomial with it's respective formula.", "color: #e64343")
    } else {
        console.log(`%cSynthetic Division%c found %c[%c${syntheticOutcome}%c] %cto be a few of the possible answers! %cNOTE: These are not the ONLY answers to the polynomial. Due to the %cRational Root Test%c not being capable of choosing all correct answers in its list of possible answers, %cSynthetic Division%c may not output all possible answers.`, "font-weight: bold", "color: lightgreen; font-weight: default", "color: powderblue", "color: orange", "color: powderblue", "color: lightgreen", "color: yellow", "font-weight: bold", "color: yellow; font-weight: default", "font-weight: bold", "color: yellow")
    }

    var rationalRootTestOutcome = Array.from(rationalRoots);

    console.log(`%cThe %cRational Root Test%c returned %c[%c${rationalRootTestOutcome}%c] %cas some of the potential answers. %cNOTE: These are POTENTIAL answers! Not all of them are necessarily correct!`, "color: lightblue", "font-weight: bold", "color: lightblue; font-weight: default", "color: powderblue", "color: orange", "color: powderblue", "color: lightblue", "color: red")

    // console.log(convertConsoleStyling(console.logs));
    // document.write(convertConsoleStyling(console.logs));
}
/* ONLY for TESTING the detection of coefficients in a polynomial */
function testingPolynomialDetection() {
    /* hard coded polynomial in 'getCoef()' to make sure it is a 100 percent accurate */
    var demo = getCoef("1x^4+1x^3-11x^2-5x+30");

    /* https://stackoverflow.com/questions/30861631/object-length-undefined-in-javascript */
    var keys = Object.keys(demo);

    /* for easier accessing of all coefficients */
    var coeff = [];

    /* looping through 'demo' to add all coefficients to the coeff array */
    for (var i = 0; i < keys.length; i++) {
        // console.log(demo[keys[i]]);
        coeff.push(demo[keys[i]]);
    }

    /* printing coeff[keys.length - 1] should return the coefficient of the highest degree term in the polynomial (the term with the highest power) */
    // console.log("First coefficient: " + coeff[keys.length - 1], ", Last coefficient: " + coeff[0]);

    /* although the rational root test function accepts the first and last coefficients, we give it the last coefficient in place of the first coefficient. This is because the place of the leading term coefficient is actually at the end of the array (meaning it's in the last position) whereas it is considered to be the first coefficient. It is confusing to explain without printing into the console what I mean */

    /* performing the rational root test and synthetic division (to get a list of possible answers using an algorithm, and using another algorithm to determine which of those answers are correct solutions for any variable in the place of x (not limited to being only x)) */

    var rationalRoots = rationalRootTest(coeff[keys.length - 1], coeff[0]);

    /* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse */

    /* here we HAVE to make sure to reverse the array (doing this earlier may have saved some confusing, but I forgot to do it) since the order of the coefficients in the 'coeff' array is reversed (meaning that the last term (the constant term) comes first, and the first term (leading term) comes last), but the synthetic division NEEDS an array with the coefficients in order. Otherwise you will get the answer to a polynomial, ax^3+bx^2+cx+d as the answer for dx^3+cx^2+bx+a */

    var syntheticOutcome = syntheticDivision(coeff.reverse(), rationalRoots);

    /* print the outcome of the algorithms - there is a probability that these algorithms do NOT provide all correct answers, and sometimes may not provide any answer at all. This is just due to them not using the respective formulae for their polynomials (for example, these algorithms are NOT coded to perform the cubic equation on cubics, or solve trinomials) which makes them only viable for simplifying high degree polynomials instead of trying to solve them. I will be implementing nearly a feature to increase accuracy later, by using some method other than the rational root test because it does not suffice. */

    // console.log(syntheticOutcome);

    if (syntheticOutcome.length == 0) {
        console.log("%cSynthetic division was unable to find a solution to your polynomial. Please try solving your polynomial with it's respective formula.", "color: #e64343")
    } else {
        console.log(`%cSynthetic Division%c found %c[%c${syntheticOutcome}%c] %cto be a few of the possible answers! %cNOTE: These are not the ONLY answers to the polynomial. Due to the %cRational Root Test%c not being capable of choosing all correct answers in its list of possible answers, %cSynthetic Division%c may not output all possible answers.`, "font-weight: bold", "color: lightgreen; font-weight: default", "color: powderblue", "color: orange", "color: powderblue", "color: lightgreen", "color: yellow", "font-weight: bold", "color: yellow; font-weight: default", "font-weight: bold", "color: yellow")
    }

    var rationalRootTestOutcome = Array.from(rationalRoots);

    console.log(`%cThe %cRational Root Test%c returned %c[%c${rationalRootTestOutcome}%c] %cas some of the potential answers. %cNOTE: These are POTENTIAL answers! Not all of them are necessarily correct!`, "color: lightblue", "font-weight: bold", "color: lightblue; font-weight: default", "color: powderblue", "color: orange", "color: powderblue", "color: lightblue", "color: red")

    // console.log(convertConsoleStyling(console.logs));
    // document.write(convertConsoleStyling(console.logs));
}
/* https://stackoverflow.com/questions/43444749/getting-coefficients-of-algebraic-term */
function getCoef(str) {
    str = str.replace(/\s+/g, "");                   // remove spaces (optional)

    var parts = str.match(/[+\-]?[^+\-]+/g);         // get the parts: see explanation bellow

    // accumulate the results
    return parts.reduce(function (res, part) {        // for each part in parts
        var coef = parseFloat(part) || +(part[0] + "1") || 1;// the coeficient is the number at the begining of each part (34x => 34), if there is no number it is assumed to be +/-1 depending on the sign (+x^2 => +1)
        var x = part.indexOf('x');                     // the index of "x" in this part (could be -1 if there isn't)
        // calculating the power of this part
        var power = x === -1 ?                         // if the index of "x" is -1 (there is no "x")
            0 :                               // then the power is 0 (Ex: -2)
            part[x + 1] === "^" ?            // otherwise (if there is an "x"), then check if the char right after "x" is "^", if so...
                +part.slice(x + 2) :           // then the power is the number right after it (Ex: 55x^30)
                1;                             // otherwise it's 1 (Ex: 55x)
        res[power] = (res[power] || 0) + coef;         // if we have already encountered this power then add this coeficient to that, if not then just store it 
        return res;
    }, {});
}
/* render katex/latex math w/ the katex library */
function renderMath(str) {
    const render = katex.renderToString(str, {
        throwOnError: false,
    });
    return render
}
/* perform the rational root test */
function rationalRootTest(first, last) {
    var firstFactors = [];
    var lastFactors = [];

    /* push all factors of the leading digit into the array firstFactors. Do the same for lastFactors but push all factors of the constant term instead (if it is 0 it may output 0 and -0 which is obviously not numerically correct, but solutions to that will come later) */
    for (var i = 0; i < first; i++) {
        /* seeing whether or not all numbers from 0 to the leading term coefficient is divisible by i using the modulo operator. This can be found in maths to find the remainder of a division. 9%3 will be 0, since there is no remainder. The mathematical operator is "mod" whereas the programming operator is "%". */
        if (first % i == 0) {
            firstFactors.push(i);
            firstFactors.push(-i);
        }
    }
    /* do the same for the constant term */
    for (var i = 0; i < last; i++) {
        if (last % i == 0) {
            lastFactors.push(i);
            lastFactors.push(-i);
        }
    }

    // regardless of the output from the for loops (factors other than it self) add its negative and positive self to the arrays

    firstFactors.push(-first);
    firstFactors.push(first);

    firstFactors.push(-1);
    firstFactors.push(1);

    lastFactors.push(-last);
    lastFactors.push(last);

    lastFactors.push(-1);
    lastFactors.push(1);

    firstFactors.sort();
    lastFactors.sort();

    /* the above lines push all negative versions of all positive factors into their respective lists as well, alongside adding the positive and negative versions of the main number itself (since any number, n, is a factor of itself) */

    // expected outcome: all factors of the first number and the last number, listed neatly in two seperate lines
    // console.log(firstFactors, lastFactors);

    var totalDividedPossibleOutcomes = [];
    var uniqueDividedPossibleOutcomes = [];

    for (var x = 0; x < firstFactors.length; x++) {
        for (var y = 0; y < lastFactors.length; y++) {
            totalDividedPossibleOutcomes.push(lastFactors[y] / firstFactors[x]);
        }
    }

    uniqueDividedPossibleOutcomes = new Set(totalDividedPossibleOutcomes);

    // expected outcome: the output of results of the rational root test (will most likely show up as decimals) 
    // console.log(uniqueDividedPossibleOutcomes);

    /* this line here returns all data calculated by the rational root test */
    return uniqueDividedPossibleOutcomes;
}
/* perform synthetic division (should be called after the rational root test is complete) */
function syntheticDivision(coefficients, possibilities) {
    /* console.log(coefficients.length, possibilities); */
    let array = Array.from(possibilities);

    /* this for loop was not working properly. I took a different approach after realising I was performing synthetic division in a wrong way */
    /* for (x = 0; x < array.length; x++) {
        // var o = 0;

        // if (coefficients.length == 0) {
        //     o = -1;
        // } else {
        //     o = 0;
        // }
        // for (i = o; i < coefficients.length; i++) {
        //     if (i == 0 || i == -1) {} 
        //     else {
        //         if ((i + coefficients[i] * array[x]) == 0) {
        //             console.log("a solution to the polynomial has been founddddd!" + array[i])
        //         }
        //     }
        // }
    } */

    var additive = [];
    var multiplicative = array;

    /* this for loop wasn't working either - because of the same reasons mentioned in the comment for the for loop above the two variables */
    /* for (i = 1; i < multiplicative.length; i++) {
        additive.push(additive[i - 1] * multiplicative[i]);
        additive.push(coefficients[i]);
        var tofoldineditor = "this is just so that this commented line of code can be folded in my code editor because this comment is required for later use but is also confusing me as I write the code for the following functionalities: high degree polynomial solving using the rational roots test, with synthetic division (no formulae required, just a very complicated-to-think-of algorithm :D)"
    } */

    /* console.log(multiplicative); */

    /* run the synthetic division algorithm (looks simple, works simple, but took very long to make!) */
    for (x = 0; x < multiplicative.length; x++) {
        var results = [];
        results.push(coefficients[0]);
        for (i = 1; i < coefficients.length; i++) {
            // console.log(additive[multiplicative[x]]);
            results.push(coefficients[i] + (results[i - 1] * multiplicative[x]))
        }
        results.push(`Calculated w/ a multiplicative factor of ${multiplicative[x]}`);
        additive.push(results);
    }

    // console.log(additive);

    /* all of this code is simple but kind of hard to explain. I might end up making a YouTube video with some effects showing what this code actually does because my comments don't seem very helpful if I put myself in the shoes of someone trying to read this to understand what exactly I've done here :/ */

    var potentialAnswers = [];

    for (i in additive) {
        // console.log(additive[i][coefficients.length - 1]);
        if (additive[i][coefficients.length - 1] == 0) {
            var toSplit = additive[i][coefficients.length];
            var split = toSplit.split('Calculated w/ a multiplicative factor of ', 2)[1]
            // console.log(split);
            potentialAnswers.push(split);
        }
    }
    return potentialAnswers;
}
/* to convert any decimal numbers / irrational numbers to fractions w/ approximately the same value */
/* https://stackoverflow.com/questions/23575218/convert-decimal-number-to-fraction-in-javascript-or-closest-fraction */
function euclidsTheorem(frac) {
    var gcd = function (a, b) {
        if (!b) return a;
        a = parseInt(a);
        b = parseInt(b);
        return gcd(b, a % b);
    };

    var fraction = frac;
    var len = fraction.toString().length - 2;

    var denominator = Math.pow(10, len);
    var numerator = fraction * denominator;

    var divisor = gcd(numerator, denominator);    // Should be 8

    numerator /= divisor;                         // Should be 439
    denominator /= divisor;                       // Should be 1250

    return `${numerator.toFixed()} / ${denominator.toFixed()}`
}
/* convert console styling to html & css styling */
/* not functional for now - approach has been changed and this function is technically obsolete but I'll eventually come back to work on this later */
function convertConsoleStyling(logs) {
    var results1 = [];
    var results2 = [];

    for (i in logs) {
        var replaceConsoleStyling = logs[i][0];

        for (var x = 1; x < 30; x++) {
            replaceConsoleStyling = replaceConsoleStyling.toString().replace('%c', `<span style="${logs[i][x]}>"`)
            eval(`results${parseFloat(i) + 1}.push(replaceConsoleStyling)`);

            if (x == 29) {
                eval(`results${parseFloat(i) + 1}.length = 0`);
                eval(`results${parseFloat(i) + 1}.push(replaceConsoleStyling)`);
            }
        }
    }
    return [results1, results2];
}

/* making mathematica have some sort of a library interface (being able to call functions from other scripts by doing 'mathematica.syntheticDivision()' instead of doing it from mathematica.js (this file renamed)) */

/* although I've added this I will continue working on the script above this and integrate all additional code into the library. Then, I'll create a new script file just for the library and this will be solely for documentation purposes. That will be pure code - no comments, no logs (except for information-for-user logs). */

class mathematica {
    constructor() { }
    /* ONLY for TESTING the detection of coefficients in a polynomial */
    testingPolynomialDetection() {
        /* hard coded polynomial in 'getCoef()' to make sure it is a 100 percent accurate */
        var demo = getCoef("1x^4+1x^3-11x^2-5x+30");

        /* https://stackoverflow.com/questions/30861631/object-length-undefined-in-javascript */
        var keys = Object.keys(demo);

        /* for easier accessing of all coefficients */
        var coeff = [];

        /* looping through 'demo' to add all coefficients to the coeff array */
        for (var i = 0; i < keys.length; i++) {
            // console.log(demo[keys[i]]);
            coeff.push(demo[keys[i]]);
        }

        /* printing coeff[keys.length - 1] should return the coefficient of the highest degree term in the polynomial (the term with the highest power) */
        // console.log("First coefficient: " + coeff[keys.length - 1], ", Last coefficient: " + coeff[0]);

        /* although the rational root test function accepts the first and last coefficients, we give it the last coefficient in place of the first coefficient. This is because the place of the leading term coefficient is actually at the end of the array (meaning it's in the last position) whereas it is considered to be the first coefficient. It is confusing to explain without printing into the console what I mean */

        /* performing the rational root test and synthetic division (to get a list of possible answers using an algorithm, and using another algorithm to determine which of those answers are correct solutions for any variable in the place of x (not limited to being only x)) */

        var rationalRoots = rationalRootTest(coeff[keys.length - 1], coeff[0]);

        /* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse */

        /* here we HAVE to make sure to reverse the array (doing this earlier may have saved some confusing, but I forgot to do it) since the order of the coefficients in the 'coeff' array is reversed (meaning that the last term (the constant term) comes first, and the first term (leading term) comes last), but the synthetic division NEEDS an array with the coefficients in order. Otherwise you will get the answer to a polynomial, ax^3+bx^2+cx+d as the answer for dx^3+cx^2+bx+a */

        var syntheticOutcome = syntheticDivision(coeff.reverse(), rationalRoots);

        /* print the outcome of the algorithms - there is a probability that these algorithms do NOT provide all correct answers, and sometimes may not provide any answer at all. This is just due to them not using the respective formulae for their polynomials (for example, these algorithms are NOT coded to perform the cubic equation on cubics, or solve trinomials) which makes them only viable for simplifying high degree polynomials instead of trying to solve them. I will be implementing nearly a feature to increase accuracy later, by using some method other than the rational root test because it does not suffice. */

        // console.log(syntheticOutcome);

        if (syntheticOutcome.length == 0) {
            console.log("%cSynthetic division was unable to find a solution to your polynomial. Please try solving your polynomial with it's respective formula.", "color: #e64343")
        } else {
            console.log(`%cSynthetic Division%c found %c[%c${syntheticOutcome}%c] %cto be a few of the possible answers! %cNOTE: These are not the ONLY answers to the polynomial. Due to the %cRational Root Test%c not being capable of choosing all correct answers in its list of possible answers, %cSynthetic Division%c may not output all possible answers.`, "font-weight: bold", "color: lightgreen; font-weight: default", "color: powderblue", "color: orange", "color: powderblue", "color: lightgreen", "color: yellow", "font-weight: bold", "color: yellow; font-weight: default", "font-weight: bold", "color: yellow")
        }

        var rationalRootTestOutcome = Array.from(rationalRoots);

        console.log(`%cThe %cRational Root Test%c returned %c[%c${rationalRootTestOutcome}%c] %cas some of the potential answers. %cNOTE: These are POTENTIAL answers! Not all of them are necessarily correct!`, "color: lightblue", "font-weight: bold", "color: lightblue; font-weight: default", "color: powderblue", "color: orange", "color: powderblue", "color: lightblue", "color: red")

        // console.log(convertConsoleStyling(console.logs));
        // document.write(convertConsoleStyling(console.logs));
    }
    /* https://stackoverflow.com/questions/43444749/getting-coefficients-of-algebraic-term */
    getCoef(str) {
        str = str.replace(/\s+/g, "");                   // remove spaces (optional)

        var parts = str.match(/[+\-]?[^+\-]+/g);         // get the parts: see explanation bellow

        // accumulate the results
        return parts.reduce(function (res, part) {        // for each part in parts
            var coef = parseFloat(part) || +(part[0] + "1") || 1;// the coeficient is the number at the begining of each part (34x => 34), if there is no number it is assumed to be +/-1 depending on the sign (+x^2 => +1)
            var x = part.indexOf('x');                     // the index of "x" in this part (could be -1 if there isn't)
            // calculating the power of this part
            var power = x === -1 ?                         // if the index of "x" is -1 (there is no "x")
                0 :                               // then the power is 0 (Ex: -2)
                part[x + 1] === "^" ?            // otherwise (if there is an "x"), then check if the char right after "x" is "^", if so...
                    +part.slice(x + 2) :           // then the power is the number right after it (Ex: 55x^30)
                    1;                             // otherwise it's 1 (Ex: 55x)
            res[power] = (res[power] || 0) + coef;         // if we have already encountered this power then add this coeficient to that, if not then just store it 
            return res;
        }, {});
    }
    /* render katex/latex math w/ the katex library */
    renderMath(str) {
        const render = katex.renderToString(str, {
            throwOnError: false,
        });
        return render
    }
    /* perform the rational root test */
    rationalRootTest(first, last) {
        var firstFactors = [];
        var lastFactors = [];

        /* push all factors of the leading digit into the array firstFactors. Do the same for lastFactors but push all factors of the constant term instead (if it is 0 it may output 0 and -0 which is obviously not numerically correct, but solutions to that will come later) */
        for (var i = 0; i < first; i++) {
            /* seeing whether or not all numbers from 0 to the leading term coefficient is divisible by i using the modulo operator. This can be found in maths to find the remainder of a division. 9%3 will be 0, since there is no remainder. The mathematical operator is "mod" whereas the programming operator is "%". */
            if (first % i == 0) {
                firstFactors.push(i);
                firstFactors.push(-i);
            }
        }
        /* do the same for the constant term */
        for (var i = 0; i < last; i++) {
            if (last % i == 0) {
                lastFactors.push(i);
                lastFactors.push(-i);
            }
        }

        // regardless of the output from the for loops (factors other than it self) add its negative and positive self to the arrays

        firstFactors.push(-first);
        firstFactors.push(first);

        firstFactors.push(-1);
        firstFactors.push(1);

        lastFactors.push(-last);
        lastFactors.push(last);

        lastFactors.push(-1);
        lastFactors.push(1);

        firstFactors.sort();
        lastFactors.sort();

        /* the above lines push all negative versions of all positive factors into their respective lists as well, alongside adding the positive and negative versions of the main number itself (since any number, n, is a factor of itself) */

        // expected outcome: all factors of the first number and the last number, listed neatly in two seperate lines
        // console.log(firstFactors, lastFactors);

        var totalDividedPossibleOutcomes = [];
        var uniqueDividedPossibleOutcomes = [];

        for (var x = 0; x < firstFactors.length; x++) {
            for (var y = 0; y < lastFactors.length; y++) {
                totalDividedPossibleOutcomes.push(lastFactors[y] / firstFactors[x]);
            }
        }

        uniqueDividedPossibleOutcomes = new Set(totalDividedPossibleOutcomes);

        // expected outcome: the output of results of the rational root test (will most likely show up as decimals) 
        // console.log(uniqueDividedPossibleOutcomes);

        /* this line here returns all data calculated by the rational root test */
        return uniqueDividedPossibleOutcomes;
    }
    /* perform synthetic division (should be called after the rational root test is complete) */
    syntheticDivision(coefficients, possibilities) {
        /* console.log(coefficients.length, possibilities); */
        let array = Array.from(possibilities);

        /* this for loop was not working properly. I took a different approach after realising I was performing synthetic division in a wrong way */
        /* for (x = 0; x < array.length; x++) {
            // var o = 0;

            // if (coefficients.length == 0) {
            //     o = -1;
            // } else {
            //     o = 0;
            // }
            // for (i = o; i < coefficients.length; i++) {
            //     if (i == 0 || i == -1) {} 
            //     else {
            //         if ((i + coefficients[i] * array[x]) == 0) {
            //             console.log("a solution to the polynomial has been founddddd!" + array[i])
            //         }
            //     }
            // }
        } */

        var additive = [];
        var multiplicative = array;

        /* this for loop wasn't working either - because of the same reasons mentioned in the comment for the for loop above the two variables */
        /* for (i = 1; i < multiplicative.length; i++) {
            additive.push(additive[i - 1] * multiplicative[i]);
            additive.push(coefficients[i]);
            var tofoldineditor = "this is just so that this commented line of code can be folded in my code editor because this comment is required for later use but is also confusing me as I write the code for the following functionalities: high degree polynomial solving using the rational roots test, with synthetic division (no formulae required, just a very complicated-to-think-of algorithm :D)"
        } */

        /* console.log(multiplicative); */

        /* run the synthetic division algorithm (looks simple, works simple, but took very long to make!) */
        for (x = 0; x < multiplicative.length; x++) {
            var results = [];
            results.push(coefficients[0]);
            for (i = 1; i < coefficients.length; i++) {
                // console.log(additive[multiplicative[x]]);
                results.push(coefficients[i] + (results[i - 1] * multiplicative[x]))
            }
            results.push(`Calculated w/ a multiplicative factor of ${multiplicative[x]}`);
            additive.push(results);
        }

        // console.log(additive);

        /* all of this code is simple but kind of hard to explain. I might end up making a YouTube video with some effects showing what this code actually does because my comments don't seem very helpful if I put myself in the shoes of someone trying to read this to understand what exactly I've done here :/ */

        var potentialAnswers = [];

        for (i in additive) {
            // console.log(additive[i][coefficients.length - 1]);
            if (additive[i][coefficients.length - 1] == 0) {
                var toSplit = additive[i][coefficients.length];
                var split = toSplit.split('Calculated w/ a multiplicative factor of ', 2)[1]
                // console.log(split);
                potentialAnswers.push(split);
            }
        }
        return potentialAnswers;
    }
    /* to convert any decimal numbers / irrational numbers to fractions w/ approximately the same value */
    /* https://stackoverflow.com/questions/23575218/convert-decimal-number-to-fraction-in-javascript-or-closest-fraction */
    euclidsTheorem(frac) {
        var gcd = function (a, b) {
            if (!b) return a;
            a = parseInt(a);
            b = parseInt(b);
            return gcd(b, a % b);
        };

        var fraction = frac;
        var len = fraction.toString().length - 2;

        var denominator = Math.pow(10, len);
        var numerator = fraction * denominator;

        var divisor = gcd(numerator, denominator);    // Should be 8

        numerator /= divisor;                         // Should be 439
        denominator /= divisor;                       // Should be 1250

        return `${numerator.toFixed()} / ${denominator.toFixed()}`
    }
    /* convert console styling to html & css styling */
    /* not functional for now - approach has been changed and this function is technically obsolete but I'll eventually come back to work on this later */
    convertConsoleStyling(logs) {
        var results1 = [];
        var results2 = [];

        for (i in logs) {
            var replaceConsoleStyling = logs[i][0];

            for (var x = 1; x < 30; x++) {
                replaceConsoleStyling = replaceConsoleStyling.toString().replace('%c', `<span style="${logs[i][x]}>"`)
                eval(`results${parseFloat(i) + 1}.push(replaceConsoleStyling)`);

                if (x == 29) {
                    eval(`results${parseFloat(i) + 1}.length = 0`);
                    eval(`results${parseFloat(i) + 1}.push(replaceConsoleStyling)`);
                }
            }
        }
        return [results1, results2];
    }
}

/* a new instance of "mathematica" - called math (cannot just be called mathematica due to the class being called mathematica) */
math = new mathematica;

/* calling mathematica functions with the "math" object and running the same functions written earlier in this script. It is as easy as that to make a library work. I think. Don't quote me on that. I don't know if I jinxed it */
console.log(math.euclidsTheorem(22 / 7)); // doesn't output expected value... Euclid's theorem is probably not being used properly
console.log(math.rationalRootTest(1, 2)); // outputs what is expected

function bracketBasedCalculating(str) {
    let isBalanced = (input) => {

        let brackets = "[]{}()<>"
        let stack = [];

        for (let bracket of input) {
            let bracketsIndex = brackets.indexOf(bracket)

            if (bracketsIndex === -1) {
                continue
            }

            if (bracketsIndex % 2 === 0) {
                console.log(bracketsIndex + 1);
                stack.push(bracketsIndex + 1);
            } else {
                if (stack.length === 0 || stack.pop() !== bracketsIndex) {
                    return false;
                }
            }
        }
        return stack.length === 0
    }
    console.log(isBalanced("500 * [{(30)*Sin(30)}*Tan(5)]"))
}


// TOMORROW IS SATURDAY BOYS NO SCHOOL LESSGO E E E E EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
