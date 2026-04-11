"""Study materials for all 60 placement topics — 5 chapters per topic."""

STUDY_CONTENT = {
    0: {
        "title": "Numbers",
        "overview": "Number system is the foundation of quantitative aptitude. It covers classification of numbers, divisibility rules, and properties of integers.",
        "chapters": [
            {
                "title": "Types of Numbers & Classification",
                "content": "The number system forms the bedrock of quantitative aptitude. Understanding the classification of numbers is essential for placement exams.\n\nNatural Numbers (N): The counting numbers 1, 2, 3, 4, ... are called natural numbers. The set does not include 0 or negative numbers.\n\nWhole Numbers (W): When we include 0 with natural numbers, we get whole numbers: 0, 1, 2, 3, ...\n\nIntegers (Z): The set of all positive and negative whole numbers including zero: ..., -3, -2, -1, 0, 1, 2, 3, ...\n\nRational Numbers (Q): Numbers that can be expressed as p/q where p and q are integers and q \u2260 0. Examples: 1/2, -3/4, 0.75 (which is 3/4). All terminating and repeating decimals are rational.\n\nIrrational Numbers: Numbers that cannot be expressed as p/q. Their decimal expansion is non-terminating and non-repeating. Examples: \u221a2 = 1.41421356..., \u03c0 = 3.14159265..., e = 2.71828...\n\nReal Numbers (R): The union of rational and irrational numbers. Every point on the number line corresponds to a real number.\n\nComplex Numbers: Numbers of the form a + bi where i = \u221a(-1). These are beyond the scope of most placement exams but are occasionally tested in IT company rounds.",
                "key_points": ["Natural \u2282 Whole \u2282 Integer \u2282 Rational \u2282 Real", "0 is a whole number but NOT a natural number", "Every integer is a rational number (can be written as n/1)", "\u221a2, \u221a3, \u221a5, \u03c0, e are all irrational numbers", "Between any two rational numbers, there are infinite rational numbers"],
                "examples": [{"question": "Classify the following: -7, 0, 3/5, \u221a3, 2.333..., \u03c0", "solution": "-7: Integer, Rational\n0: Whole, Integer, Rational\n3/5: Rational (not integer)\n\u221a3: Irrational (\u221a3 = 1.7320508...)\n2.333... = 7/3: Rational (repeating decimal)\n\u03c0: Irrational"}, {"question": "Is 0.101001000100001... rational or irrational?", "solution": "Irrational. The pattern never repeats \u2014 each time, one more 0 is added. Since the decimal is non-terminating and non-repeating, it is irrational."}],
            },
            {
                "title": "Divisibility Rules",
                "content": "Divisibility rules are shortcuts that help determine whether a number is divisible by another without performing actual division. These save significant time in competitive exams.\n\nDivisibility by 2: A number is divisible by 2 if its last digit is even (0, 2, 4, 6, 8).\n\nDivisibility by 3: A number is divisible by 3 if the sum of its digits is divisible by 3. Example: 726 \u2192 7+2+6 = 15, and 15 \u00f7 3 = 5, so 726 is divisible by 3.\n\nDivisibility by 4: A number is divisible by 4 if the last two digits form a number divisible by 4. Example: 1324 \u2192 last two digits = 24, 24 \u00f7 4 = 6, so 1324 is divisible by 4.\n\nDivisibility by 5: A number is divisible by 5 if it ends in 0 or 5.\n\nDivisibility by 6: A number is divisible by 6 if it is divisible by BOTH 2 and 3.\n\nDivisibility by 8: A number is divisible by 8 if the last three digits form a number divisible by 8.\n\nDivisibility by 9: A number is divisible by 9 if the sum of its digits is divisible by 9.\n\nDivisibility by 11: A number is divisible by 11 if the difference between the sum of digits at odd positions and the sum of digits at even positions is 0 or a multiple of 11. Example: 121 \u2192 (1+1) - 2 = 0, divisible by 11.",
                "key_points": ["For 2: check last digit is even", "For 3 and 9: check sum of digits", "For 4: check last 2 digits; for 8: check last 3 digits", "For 11: alternating sum of digits = 0 or multiple of 11", "For 6: must satisfy BOTH rules for 2 and 3"],
                "examples": [{"question": "Is 4,83,269 divisible by 11?", "solution": "Digits from right: 9, 6, 2, 3, 8, 4\nOdd positions (1st, 3rd, 5th from right): 9 + 2 + 8 = 19\nEven positions (2nd, 4th, 6th): 6 + 3 + 4 = 13\nDifference: 19 - 13 = 6 \u2260 0 or 11\nSo 4,83,269 is NOT divisible by 11."}, {"question": "Find the smallest 6-digit number divisible by 12.", "solution": "Smallest 6-digit number = 100000.\n100000 \u00f7 12 = 8333.33...\nSo 8334 \u00d7 12 = 100008.\nThe smallest 6-digit number divisible by 12 is 100008."}],
            },
            {
                "title": "Prime Numbers & Factorization",
                "content": "A prime number is a natural number greater than 1 that has exactly two factors: 1 and itself. Understanding primes is crucial for problems on HCF, LCM, and number properties.\n\nFirst 25 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.\n\nKey facts about primes:\n\u2022 2 is the only even prime number\n\u2022 1 is NOT a prime number (it has only one factor)\n\u2022 Every even number greater than 2 can be expressed as the sum of two primes (Goldbach's Conjecture)\n\u2022 There are infinitely many primes\n\nPrime Factorization: Every composite number can be expressed as a unique product of prime factors. This is called the Fundamental Theorem of Arithmetic.\n\nFinding number of factors: If N = p^a \u00d7 q^b \u00d7 r^c, then:\n\u2022 Total number of factors = (a+1)(b+1)(c+1)\n\u2022 Sum of factors = [(p^(a+1) - 1)/(p-1)] \u00d7 [(q^(b+1) - 1)/(q-1)] \u00d7 ...\n\nTo check if a number n is prime: Check divisibility by all primes up to \u221an. If none divide n, it is prime.",
                "key_points": ["2 is the smallest and only even prime", "1 is NOT prime (has only 1 factor)", "To test primality of n, check primes up to \u221an", "Number of factors of p^a \u00d7 q^b = (a+1)(b+1)", "Twin primes differ by 2: (3,5), (5,7), (11,13), (17,19), (29,31)"],
                "examples": [{"question": "Find the number of factors of 360.", "solution": "360 = 2\u00b3 \u00d7 3\u00b2 \u00d7 5\u00b9\nNumber of factors = (3+1)(2+1)(1+1) = 4 \u00d7 3 \u00d7 2 = 24 factors."}, {"question": "Is 397 prime?", "solution": "\u221a397 \u2248 19.9. Check primes up to 19: 2, 3, 5, 7, 11, 13, 17, 19.\n397 is odd (not \u00f72), digit sum=19 (not \u00f73), doesn't end in 0/5 (not \u00f75).\n397\u00f77=56.7, 397\u00f711=36.09, 397\u00f713=30.5, 397\u00f717=23.4, 397\u00f719=20.9.\nNone divide evenly. 397 is PRIME."}],
            },
            {
                "title": "Remainders & Modular Arithmetic",
                "content": "When a number N is divided by D, we get: N = D \u00d7 Q + R, where Q is the quotient and R is the remainder (0 \u2264 R < D). Remainder problems are extremely common in placement exams.\n\nKey Remainder Properties:\n\u2022 Remainder of (a+b) \u00f7 n = [Rem(a\u00f7n) + Rem(b\u00f7n)] mod n\n\u2022 Remainder of (a\u00d7b) \u00f7 n = [Rem(a\u00f7n) \u00d7 Rem(b\u00f7n)] mod n\n\u2022 Remainder of (a^k) \u00f7 n: Find the cycle of remainders\n\nCyclicity of Remainders: When we compute a^1, a^2, a^3, ... mod n, the remainders eventually repeat in a cycle. This is key for solving problems like 'Find remainder when 2^100 is divided by 7.'\n\nPowers of 2 mod 7: 2^1=2, 2^2=4, 2^3=1, 2^4=2, 2^5=4, 2^6=1... Cycle length = 3.\n\nFermat's Little Theorem: If p is prime and gcd(a,p)=1, then a^(p-1) \u2261 1 (mod p). This is powerful for large exponents.\n\nWilson's Theorem: (p-1)! \u2261 -1 (mod p) for any prime p.",
                "key_points": ["N = D \u00d7 Q + R where 0 \u2264 R < D", "Remainders of sum/product = sum/product of remainders (mod divisor)", "Find cyclicity pattern for power-remainder problems", "Fermat's Little: a^(p-1) \u2261 1 (mod p) when p is prime", "Negative remainders: if R is negative, add D to get positive remainder"],
                "examples": [{"question": "Find the remainder when 7^222 is divided by 5.", "solution": "7 mod 5 = 2. So we need 2^222 mod 5.\nCycle of 2^n mod 5: 2, 4, 3, 1, 2, 4, 3, 1, ... (cycle length 4)\n222 \u00f7 4 = 55 remainder 2.\nSo 2^222 mod 5 = 2^2 mod 5 = 4.\nRemainder = 4."}, {"question": "What is the remainder when 17 \u00d7 23 \u00d7 31 is divided by 7?", "solution": "17 mod 7 = 3, 23 mod 7 = 2, 31 mod 7 = 3.\nProduct of remainders: 3 \u00d7 2 \u00d7 3 = 18.\n18 mod 7 = 4.\nRemainder = 4."}],
            },
            {
                "title": "Number System Practice & Exam Patterns",
                "content": "Placement exams test number systems through various question patterns. Here we cover the most frequently tested patterns with strategies.\n\nPattern 1 \u2014 Finding the Largest/Smallest Number: 'Find the largest 4-digit number divisible by 88.' Strategy: Divide the boundary number by the divisor, take floor/ceil, multiply back.\n\nPattern 2 \u2014 Sum of Numbers in a Range: 'Find sum of all 3-digit numbers divisible by 7.' Use AP formula: count = (last-first)/d + 1, sum = count \u00d7 (first+last)/2.\n\nPattern 3 \u2014 Unit Digit Problems: The unit digit of a product depends only on the unit digits of the factors. Powers of numbers have cyclicity in their unit digits: 2\u2192{2,4,8,6}, 3\u2192{3,9,7,1}, 7\u2192{7,9,3,1}, 8\u2192{8,4,2,6}.\n\nPattern 4 \u2014 Factorial Problems: 'How many trailing zeros in 100!?' Count = \u230a100/5\u230b + \u230a100/25\u230b + \u230a100/125\u230b = 20 + 4 + 0 = 24 zeros.\n\nPattern 5 \u2014 Number of Digits: Number of digits in N = \u230alog\u2081\u2080(N)\u230b + 1.",
                "key_points": ["Unit digit cycles: 2\u2192cycle 4, 3\u2192cycle 4, powers of 4 and 9\u2192cycle 2", "Trailing zeros in n! = \u03a3\u230an/5^k\u230b for k=1,2,3...", "For sum of AP: S = n(first+last)/2", "Highest power of p in n! = \u03a3\u230an/p^k\u230b", "LCM questions often hide in 'bells ringing together' problems"],
                "examples": [{"question": "How many trailing zeros does 250! have?", "solution": "Count factors of 5 in 250!:\n\u230a250/5\u230b = 50\n\u230a250/25\u230b = 10\n\u230a250/125\u230b = 2\n\u230a250/625\u230b = 0\nTotal = 50 + 10 + 2 = 62 trailing zeros."}, {"question": "Find the unit digit of 7^95.", "solution": "Unit digit cycle of 7: 7, 9, 3, 1 (cycle length 4)\n95 \u00f7 4 = 23 remainder 3\nUnit digit = 3rd in cycle = 3."}],
            },
        ],
        "key_concepts": [{"name": "Types of Numbers", "explanation": "Natural numbers (1,2,3...), Whole numbers (0,1,2...), Integers (...-2,-1,0,1,2...), Rational numbers (p/q form), Irrational numbers (non-terminating, non-repeating decimals like \u221a2, \u03c0)."}, {"name": "Divisibility Rules", "explanation": "By 2: last digit even. By 3: sum of digits divisible by 3. By 4: last 2 digits divisible by 4. By 5: ends in 0 or 5. By 6: divisible by both 2 and 3. By 8: last 3 digits divisible by 8. By 9: sum of digits divisible by 9. By 11: difference of sums of alternate digits divisible by 11."}, {"name": "Prime Numbers", "explanation": "A prime number has exactly two factors: 1 and itself. First few primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. Note: 2 is the only even prime. 1 is NOT prime."}, {"name": "Remainder Theorem", "explanation": "When a number N is divided by D: N = D \u00d7 Q + R, where Q is quotient and R is remainder (0 \u2264 R < D). Example: 17 \u00f7 5 gives Q=3, R=2."}],
        "formulas": ["Sum of first n natural numbers = n(n+1)/2", "Sum of squares of first n naturals = n(n+1)(2n+1)/6", "Sum of cubes of first n naturals = [n(n+1)/2]\u00b2", "Number of prime factors of N = find prime factorization N = p\u2081^a \u00d7 p\u2082^b \u00d7 ..."],
        "solved_examples": [{"question": "Find the largest 4-digit number exactly divisible by 88.", "solution": "Largest 4-digit number = 9999. Divide: 9999 \u00f7 88 = 113 remainder 55. So answer = 9999 - 55 = 9944."}, {"question": "What is the sum of all prime numbers between 30 and 50?", "solution": "Primes between 30 and 50: 31, 37, 41, 43, 47. Sum = 31 + 37 + 41 + 43 + 47 = 199."}],
        "tips": ["Learn divisibility rules by heart \u2014 they save time in exams.", "For finding number of factors: if N = p^a \u00d7 q^b, total factors = (a+1)(b+1).", "Even \u00d7 anything = Even. Odd \u00d7 Odd = Odd."],
    },
    1: {
        "title": "HCF & LCM",
        "overview": "HCF (Highest Common Factor) and LCM (Least Common Multiple) are fundamental concepts for solving problems involving divisibility, fractions, and scheduling.",
        "chapters": [
            {
                "title": "Finding HCF \u2014 Methods & Shortcuts",
                "content": "This chapter covers finding hcf \u2014 methods & shortcuts as part of the HCF & LCM topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of finding hcf \u2014 methods & shortcuts thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other HCF & LCM concepts"],
                "examples": [{"question": "Sample placement question on Finding HCF \u2014 Methods & Shortcuts", "solution": "Approach: Identify the concept from Finding HCF \u2014 Methods & Shortcuts, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Finding LCM \u2014 Prime Factorization & Division",
                "content": "This chapter covers finding lcm \u2014 prime factorization & division as part of the HCF & LCM topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of finding lcm \u2014 prime factorization & division thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other HCF & LCM concepts"],
                "examples": [{"question": "Sample placement question on Finding LCM \u2014 Prime Factorization & Division", "solution": "Approach: Identify the concept from Finding LCM \u2014 Prime Factorization & Division, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "HCF \u00d7 LCM Relationship & Applications",
                "content": "This chapter covers hcf \u00d7 lcm relationship & applications as part of the HCF & LCM topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of hcf \u00d7 lcm relationship & applications thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other HCF & LCM concepts"],
                "examples": [{"question": "Sample placement question on HCF \u00d7 LCM Relationship & Applications", "solution": "Approach: Identify the concept from HCF \u00d7 LCM Relationship & Applications, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Word Problems on HCF & LCM",
                "content": "This chapter covers word problems on hcf & lcm as part of the HCF & LCM topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of word problems on hcf & lcm thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other HCF & LCM concepts"],
                "examples": [{"question": "Sample placement question on Word Problems on HCF & LCM", "solution": "Approach: Identify the concept from Word Problems on HCF & LCM, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced HCF-LCM Problems for Placement",
                "content": "This chapter covers advanced hcf-lcm problems for placement as part of the HCF & LCM topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced hcf-lcm problems for placement thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other HCF & LCM concepts"],
                "examples": [{"question": "Sample placement question on Advanced HCF-LCM Problems for Placement", "solution": "Approach: Identify the concept from Advanced HCF-LCM Problems for Placement, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "HCF (GCD)", "explanation": "The largest number that divides two or more numbers exactly. Methods: Prime factorization (take lowest powers of common primes) or Euclid's division algorithm."}, {"name": "LCM", "explanation": "The smallest number that is a multiple of two or more numbers. Method: Prime factorization (take highest powers of all primes present)."}, {"name": "Relationship", "explanation": "For two numbers a and b: HCF(a,b) \u00d7 LCM(a,b) = a \u00d7 b. This is extremely useful for competitive exams."}, {"name": "Co-prime Numbers", "explanation": "Two numbers whose HCF is 1. Example: 8 and 15 are co-prime. Note: co-prime numbers need not be prime themselves."}],
        "formulas": ["HCF \u00d7 LCM = Product of two numbers", "HCF of fractions = HCF of numerators / LCM of denominators", "LCM of fractions = LCM of numerators / HCF of denominators"],
        "solved_examples": [{"question": "Find HCF and LCM of 12, 18, and 24.", "solution": "12 = 2\u00b2 \u00d7 3, 18 = 2 \u00d7 3\u00b2, 24 = 2\u00b3 \u00d7 3. HCF = 2\u00b9 \u00d7 3\u00b9 = 6. LCM = 2\u00b3 \u00d7 3\u00b2 = 72."}, {"question": "Two numbers are in ratio 3:4. Their HCF is 5. Find LCM.", "solution": "Numbers are 15 and 20. LCM = (15 \u00d7 20)/5 = 60."}],
        "tips": ["Always simplify using prime factorization for accuracy.", "HCF divides both numbers. Both numbers divide LCM.", "For 3+ numbers, find HCF/LCM of first two, then with the third."],
    },
    2: {
        "title": "Percentages",
        "overview": "Percentage means 'per hundred'. It's used extensively in profit/loss, data interpretation, and real-life calculations like discounts and interest.",
        "chapters": [
            {
                "title": "Basic Percentage Conversions",
                "content": "This chapter covers basic percentage conversions as part of the Percentages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of basic percentage conversions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Percentages concepts"],
                "examples": [{"question": "Sample placement question on Basic Percentage Conversions", "solution": "Approach: Identify the concept from Basic Percentage Conversions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Percentage Change & Increase/Decrease",
                "content": "This chapter covers percentage change & increase/decrease as part of the Percentages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of percentage change & increase/decrease thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Percentages concepts"],
                "examples": [{"question": "Sample placement question on Percentage Change & Increase/Decrease", "solution": "Approach: Identify the concept from Percentage Change & Increase/Decrease, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Successive Percentage Changes",
                "content": "This chapter covers successive percentage changes as part of the Percentages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of successive percentage changes thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Percentages concepts"],
                "examples": [{"question": "Sample placement question on Successive Percentage Changes", "solution": "Approach: Identify the concept from Successive Percentage Changes, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Percentages in Data Interpretation",
                "content": "This chapter covers percentages in data interpretation as part of the Percentages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of percentages in data interpretation thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Percentages concepts"],
                "examples": [{"question": "Sample placement question on Percentages in Data Interpretation", "solution": "Approach: Identify the concept from Percentages in Data Interpretation, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Percentage Problems",
                "content": "This chapter covers advanced percentage problems as part of the Percentages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced percentage problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Percentages concepts"],
                "examples": [{"question": "Sample placement question on Advanced Percentage Problems", "solution": "Approach: Identify the concept from Advanced Percentage Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Basic Conversion", "explanation": "To convert fraction to %: multiply by 100. To convert % to fraction: divide by 100. Example: 3/5 = 60%, 25% = 1/4."}, {"name": "Percentage Change", "explanation": "% Change = (Change / Original) \u00d7 100. Increase: new = original \u00d7 (1 + r/100). Decrease: new = original \u00d7 (1 - r/100)."}, {"name": "Successive Percentages", "explanation": "If value changes by a% then b%, net change = a + b + ab/100. Example: 20% increase then 10% decrease: 20 + (-10) + (20\u00d7-10)/100 = 8% net increase."}, {"name": "Fraction-Percentage Equivalents", "explanation": "1/2=50%, 1/3=33.33%, 1/4=25%, 1/5=20%, 1/6=16.67%, 1/7=14.28%, 1/8=12.5%, 1/9=11.11%, 1/10=10%. Memorize these!"}],
        "formulas": ["Percentage = (Part / Whole) \u00d7 100", "% Increase = ((New - Old) / Old) \u00d7 100", "If A is x% more than B, then B is (x/(100+x)) \u00d7 100 % less than A", "Successive changes: a + b + ab/100"],
        "solved_examples": [{"question": "A's salary is 20% less than B's. By what % is B's salary more than A's?", "solution": "If B = 100, A = 80. B is more than A by: (20/80)\u00d7100 = 25%."}, {"question": "Price increases by 25%, then decreases by 20%. Net change?", "solution": "Net = 25 + (-20) + (25\u00d7-20)/100 = 25 - 20 - 5 = 0%. No change!"}],
        "tips": ["Memorize fraction-percentage equivalents for speed.", "In successive changes, always use the formula a + b + ab/100.", "\"x% of y\" = \"y% of x\" \u2014 use whichever is easier to calculate."],
    },
    3: {
        "title": "Profit & Loss",
        "overview": "Profit and Loss problems involve buying and selling goods. Understanding cost price, selling price, and markup is essential for aptitude exams.",
        "chapters": [
            {
                "title": "Cost Price, Selling Price & Profit/Loss",
                "content": "This chapter covers cost price, selling price & profit/loss as part of the Profit & Loss topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of cost price, selling price & profit/loss thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Profit & Loss concepts"],
                "examples": [{"question": "Sample placement question on Cost Price, Selling Price & Profit/Loss", "solution": "Approach: Identify the concept from Cost Price, Selling Price & Profit/Loss, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Markup, Discount & Selling Price",
                "content": "This chapter covers markup, discount & selling price as part of the Profit & Loss topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of markup, discount & selling price thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Profit & Loss concepts"],
                "examples": [{"question": "Sample placement question on Markup, Discount & Selling Price", "solution": "Approach: Identify the concept from Markup, Discount & Selling Price, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Successive Discounts",
                "content": "This chapter covers successive discounts as part of the Profit & Loss topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of successive discounts thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Profit & Loss concepts"],
                "examples": [{"question": "Sample placement question on Successive Discounts", "solution": "Approach: Identify the concept from Successive Discounts, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Dishonest Dealing & Faulty Weights",
                "content": "This chapter covers dishonest dealing & faulty weights as part of the Profit & Loss topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of dishonest dealing & faulty weights thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Profit & Loss concepts"],
                "examples": [{"question": "Sample placement question on Dishonest Dealing & Faulty Weights", "solution": "Approach: Identify the concept from Dishonest Dealing & Faulty Weights, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Mixed Profit/Loss Problems",
                "content": "This chapter covers mixed profit/loss problems as part of the Profit & Loss topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of mixed profit/loss problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Profit & Loss concepts"],
                "examples": [{"question": "Sample placement question on Mixed Profit/Loss Problems", "solution": "Approach: Identify the concept from Mixed Profit/Loss Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Basic Terms", "explanation": "Cost Price (CP): Price at which item is bought. Selling Price (SP): Price at which item is sold. Profit = SP - CP (when SP > CP). Loss = CP - SP (when CP > SP)."}, {"name": "Profit/Loss Percentage", "explanation": "Always calculated on Cost Price. Profit% = (Profit/CP) \u00d7 100. Loss% = (Loss/CP) \u00d7 100."}, {"name": "Markup & Discount", "explanation": "Marked Price (MP) is the listed/sticker price. Discount is given on MP. SP = MP \u00d7 (1 - discount%). Markup% = ((MP - CP)/CP) \u00d7 100."}, {"name": "Dishonest Dealer", "explanation": "If dealer uses false weight w instead of true weight W: Profit% = ((W-w)/w) \u00d7 100. Example: 900g instead of 1kg \u2192 (100/900)\u00d7100 = 11.11% profit."}],
        "formulas": ["Profit = SP - CP, Loss = CP - SP", "SP = CP \u00d7 (100 + Profit%) / 100", "SP = CP \u00d7 (100 - Loss%) / 100", "If two items sold at same SP, one at x% profit and other at x% loss: Net loss = x\u00b2/100 %"],
        "solved_examples": [{"question": "A shopkeeper buys 10 items for the cost of 8 and sells 8 items for the cost of 10. Find profit%.", "solution": "Let CP of 1 item = \u20b91. Buys 10 for \u20b98, so CP per item = \u20b90.8. Sells 8 for \u20b910, so SP per item = \u20b91.25. Profit% = (1.25-0.8)/0.8 \u00d7 100 = 56.25%."}, {"question": "An item is marked up by 50% and then a 20% discount is given. Find profit%.", "solution": "Let CP = 100. MP = 150. SP = 150 \u00d7 0.8 = 120. Profit = 20%."}],
        "tips": ["Profit/Loss % is ALWAYS on CP, not SP.", "Successive discounts: use formula like successive percentages.", "If you sell at loss and want to find what SP gives profit, recalculate from CP."],
    },
    4: {
        "title": "Ratio & Proportion",
        "overview": "Ratio compares two quantities. Proportion states that two ratios are equal. These concepts are fundamental to mixture problems and partnerships.",
        "chapters": [
            {
                "title": "Ratio Fundamentals",
                "content": "This chapter covers ratio fundamentals as part of the Ratio & Proportion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of ratio fundamentals thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Ratio & Proportion concepts"],
                "examples": [{"question": "Sample placement question on Ratio Fundamentals", "solution": "Approach: Identify the concept from Ratio Fundamentals, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Proportion \u2014 Direct & Inverse",
                "content": "This chapter covers proportion \u2014 direct & inverse as part of the Ratio & Proportion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of proportion \u2014 direct & inverse thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Ratio & Proportion concepts"],
                "examples": [{"question": "Sample placement question on Proportion \u2014 Direct & Inverse", "solution": "Approach: Identify the concept from Proportion \u2014 Direct & Inverse, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Mixtures & Alligation",
                "content": "This chapter covers mixtures & alligation as part of the Ratio & Proportion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of mixtures & alligation thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Ratio & Proportion concepts"],
                "examples": [{"question": "Sample placement question on Mixtures & Alligation", "solution": "Approach: Identify the concept from Mixtures & Alligation, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Compounded Ratios",
                "content": "This chapter covers compounded ratios as part of the Ratio & Proportion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of compounded ratios thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Ratio & Proportion concepts"],
                "examples": [{"question": "Sample placement question on Compounded Ratios", "solution": "Approach: Identify the concept from Compounded Ratios, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Ratio Word Problems",
                "content": "This chapter covers advanced ratio word problems as part of the Ratio & Proportion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced ratio word problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Ratio & Proportion concepts"],
                "examples": [{"question": "Sample placement question on Advanced Ratio Word Problems", "solution": "Approach: Identify the concept from Advanced Ratio Word Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Ratio Basics", "explanation": "a:b means a/b. Ratios have no units. a:b = ka:kb for any k. To compare ratios, convert to same denominator or cross-multiply."}, {"name": "Proportion", "explanation": "a:b = c:d means ad = bc (cross multiplication). Here a,d are extremes and b,c are means. Product of means = Product of extremes."}, {"name": "Componendo-Dividendo", "explanation": "If a/b = c/d, then (a+b)/(a-b) = (c+d)/(c-d). Very useful shortcut for competitive exams."}, {"name": "Mixtures (Alligation)", "explanation": "When mixing two quantities at different rates, the ratio of quantities = (Dearer price - Mean price) : (Mean price - Cheaper price)."}],
        "formulas": ["If a:b = c:d then ad = bc", "Duplicate ratio of a:b = a\u00b2:b\u00b2", "Sub-duplicate ratio of a:b = \u221aa:\u221ab", "Alligation: Q1/Q2 = (A2 - Avg)/(Avg - A1)"],
        "solved_examples": [{"question": "Divide \u20b92400 among A, B, C in ratio 2:3:5.", "solution": "Total parts = 2+3+5 = 10. A = 2400\u00d72/10 = \u20b9480. B = 2400\u00d73/10 = \u20b9720. C = 2400\u00d75/10 = \u20b91200."}, {"question": "If A:B = 3:4 and B:C = 5:6, find A:B:C.", "solution": "Make B common: A:B = 15:20, B:C = 20:24. So A:B:C = 15:20:24."}],
        "tips": ["Always reduce ratios to simplest form.", "To combine ratios, make the common term equal.", "In partnership, profit sharing ratio = (capital \u00d7 time) ratio."],
    },
    5: {
        "title": "Time & Work",
        "overview": "Time and Work problems involve calculating how long it takes for people/machines to complete tasks individually or together.",
        "chapters": [
            {
                "title": "Work Rate Fundamentals",
                "content": "This chapter covers work rate fundamentals as part of the Time & Work topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of work rate fundamentals thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Work concepts"],
                "examples": [{"question": "Sample placement question on Work Rate Fundamentals", "solution": "Approach: Identify the concept from Work Rate Fundamentals, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Multiple Workers & Combined Work",
                "content": "This chapter covers multiple workers & combined work as part of the Time & Work topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of multiple workers & combined work thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Work concepts"],
                "examples": [{"question": "Sample placement question on Multiple Workers & Combined Work", "solution": "Approach: Identify the concept from Multiple Workers & Combined Work, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Pipes & Cisterns",
                "content": "This chapter covers pipes & cisterns as part of the Time & Work topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of pipes & cisterns thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Work concepts"],
                "examples": [{"question": "Sample placement question on Pipes & Cisterns", "solution": "Approach: Identify the concept from Pipes & Cisterns, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Efficiency, Wages & Work Sharing",
                "content": "This chapter covers efficiency, wages & work sharing as part of the Time & Work topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of efficiency, wages & work sharing thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Work concepts"],
                "examples": [{"question": "Sample placement question on Efficiency, Wages & Work Sharing", "solution": "Approach: Identify the concept from Efficiency, Wages & Work Sharing, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Complex Time & Work Problems",
                "content": "This chapter covers complex time & work problems as part of the Time & Work topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of complex time & work problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Work concepts"],
                "examples": [{"question": "Sample placement question on Complex Time & Work Problems", "solution": "Approach: Identify the concept from Complex Time & Work Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Basic Principle", "explanation": "If A can do work in 'n' days, A's 1 day work = 1/n. If A and B work together: combined 1 day work = 1/a + 1/b. Total time = ab/(a+b)."}, {"name": "Efficiency Method (LCM)", "explanation": "Take LCM of days as total work. Calculate per-day efficiency. Add efficiencies for combined work. Time = Total work / Combined efficiency."}, {"name": "Pipes & Cisterns", "explanation": "Inlet pipe fills, outlet pipe empties. If pipe fills in a hours: rate = 1/a. If pipe empties in b hours: rate = -1/b. Net rate = 1/a - 1/b."}, {"name": "Alternate Day Work", "explanation": "If A and B work on alternate days: find 2-day combined work, then multiply. Handle the last incomplete cycle separately."}],
        "formulas": ["Combined time = (a \u00d7 b) / (a + b) for two workers", "If A is x times as efficient as B, and B takes n days, A takes n/x days", "Work = Rate \u00d7 Time", "MDH formula: M\u2081D\u2081H\u2081/W\u2081 = M\u2082D\u2082H\u2082/W\u2082"],
        "solved_examples": [{"question": "A can do a job in 12 days, B in 15 days. Together how long?", "solution": "LCM(12,15) = 60 units total work. A's rate = 5 units/day, B's rate = 4 units/day. Together = 9 units/day. Time = 60/9 = 6\u2154 days."}, {"question": "A pipe fills a tank in 6 hours, another empties it in 8 hours. If both open, how long to fill?", "solution": "Net rate per hour = 1/6 - 1/8 = (4-3)/24 = 1/24. Time = 24 hours."}],
        "tips": ["LCM method is faster than fraction method for most problems.", "If someone leaves/joins midway, calculate work done in each phase separately.", "Negative work means destruction/emptying."],
    },
    6: {
        "title": "Time & Distance",
        "overview": "Problems involving speed, distance, and time. Includes trains, boats & streams, and relative speed concepts.",
        "chapters": [
            {
                "title": "Speed, Distance & Time Basics",
                "content": "This chapter covers speed, distance & time basics as part of the Time & Distance topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of speed, distance & time basics thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Distance concepts"],
                "examples": [{"question": "Sample placement question on Speed, Distance & Time Basics", "solution": "Approach: Identify the concept from Speed, Distance & Time Basics, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Relative Speed & Meeting Problems",
                "content": "This chapter covers relative speed & meeting problems as part of the Time & Distance topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of relative speed & meeting problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Distance concepts"],
                "examples": [{"question": "Sample placement question on Relative Speed & Meeting Problems", "solution": "Approach: Identify the concept from Relative Speed & Meeting Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Problems on Trains",
                "content": "This chapter covers problems on trains as part of the Time & Distance topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of problems on trains thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Distance concepts"],
                "examples": [{"question": "Sample placement question on Problems on Trains", "solution": "Approach: Identify the concept from Problems on Trains, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Boats & Streams",
                "content": "This chapter covers boats & streams as part of the Time & Distance topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of boats & streams thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Distance concepts"],
                "examples": [{"question": "Sample placement question on Boats & Streams", "solution": "Approach: Identify the concept from Boats & Streams, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Races & Circular Motion",
                "content": "This chapter covers races & circular motion as part of the Time & Distance topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of races & circular motion thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Time & Distance concepts"],
                "examples": [{"question": "Sample placement question on Races & Circular Motion", "solution": "Approach: Identify the concept from Races & Circular Motion, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Basic Formula", "explanation": "Speed = Distance / Time. Distance = Speed \u00d7 Time. Time = Distance / Speed. Units: km/hr to m/s multiply by 5/18."}, {"name": "Relative Speed", "explanation": "Same direction: relative speed = |s1 - s2|. Opposite direction: relative speed = s1 + s2. Used in trains passing each other."}, {"name": "Average Speed", "explanation": "Average speed = Total distance / Total time. For equal distances at speeds a and b: Average = 2ab/(a+b). NOT simply (a+b)/2!"}, {"name": "Trains", "explanation": "Train passing a pole: distance = length of train. Train passing a platform: distance = train length + platform length. Two trains passing each other: distance = sum of lengths."}],
        "formulas": ["Speed = Distance / Time", "km/hr to m/s: multiply by 5/18", "Average speed for equal distances = 2ab/(a+b)", "Boats: Downstream speed = u+v, Upstream = u-v (u=boat, v=stream)"],
        "solved_examples": [{"question": "A train 150m long passes a platform of 250m in 20 seconds. Find speed.", "solution": "Total distance = 150 + 250 = 400m. Speed = 400/20 = 20 m/s = 20 \u00d7 18/5 = 72 km/hr."}, {"question": "A car covers half the distance at 60 km/hr and rest at 40 km/hr. Average speed?", "solution": "Average = 2\u00d760\u00d740/(60+40) = 4800/100 = 48 km/hr."}],
        "tips": ["Always convert units consistently (km/hr or m/s).", "For trains: identify what the train is passing to determine distance.", "Average speed \u2260 average of speeds (unless time is equal, not distance)."],
    },
    7: {
        "title": "Simple Interest",
        "overview": "Simple Interest is calculated only on the principal amount. It's straightforward but forms the basis for understanding compound interest.",
        "chapters": [
            {
                "title": "Simple Interest Formula & Basics",
                "content": "This chapter covers simple interest formula & basics as part of the Simple Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of simple interest formula & basics thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Simple Interest concepts"],
                "examples": [{"question": "Sample placement question on Simple Interest Formula & Basics", "solution": "Approach: Identify the concept from Simple Interest Formula & Basics, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Finding Principal, Rate & Time",
                "content": "This chapter covers finding principal, rate & time as part of the Simple Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of finding principal, rate & time thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Simple Interest concepts"],
                "examples": [{"question": "Sample placement question on Finding Principal, Rate & Time", "solution": "Approach: Identify the concept from Finding Principal, Rate & Time, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Comparing Simple Interest Amounts",
                "content": "This chapter covers comparing simple interest amounts as part of the Simple Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of comparing simple interest amounts thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Simple Interest concepts"],
                "examples": [{"question": "Sample placement question on Comparing Simple Interest Amounts", "solution": "Approach: Identify the concept from Comparing Simple Interest Amounts, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "SI in Banking & Investment",
                "content": "This chapter covers si in banking & investment as part of the Simple Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of si in banking & investment thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Simple Interest concepts"],
                "examples": [{"question": "Sample placement question on SI in Banking & Investment", "solution": "Approach: Identify the concept from SI in Banking & Investment, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Mixed SI Problems",
                "content": "This chapter covers mixed si problems as part of the Simple Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of mixed si problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Simple Interest concepts"],
                "examples": [{"question": "Sample placement question on Mixed SI Problems", "solution": "Approach: Identify the concept from Mixed SI Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Simple Interest Formula", "explanation": "SI = (P \u00d7 R \u00d7 T) / 100, where P = Principal, R = Rate per annum, T = Time in years."}, {"name": "Amount", "explanation": "Amount (A) = Principal + Interest = P + (PRT/100) = P(1 + RT/100)."}, {"name": "Finding P, R, or T", "explanation": "P = (100 \u00d7 SI)/(R \u00d7 T). R = (100 \u00d7 SI)/(P \u00d7 T). T = (100 \u00d7 SI)/(P \u00d7 R)."}],
        "formulas": ["SI = PRT / 100", "Amount = P(1 + RT/100)", "P = 100 \u00d7 SI / (R \u00d7 T)", "If amount doubles in T years at SI: R = 100/T"],
        "solved_examples": [{"question": "Find SI on \u20b95000 at 8% per annum for 3 years.", "solution": "SI = 5000 \u00d7 8 \u00d7 3 / 100 = \u20b91200. Amount = 5000 + 1200 = \u20b96200."}, {"question": "A sum doubles itself in 10 years at SI. Find rate.", "solution": "SI = P (doubles means interest = principal). P = P \u00d7 R \u00d7 10/100. R = 10%."}],
        "tips": ["SI grows linearly with time \u2014 it's the same amount of interest each year.", "If a sum becomes n times in T years: Rate = (n-1) \u00d7 100/T.", "Compare with CI to understand the difference."],
    },
    8: {
        "title": "Compound Interest",
        "overview": "Compound Interest is calculated on principal plus accumulated interest. Money grows faster than simple interest \u2014 'interest on interest'.",
        "chapters": [
            {
                "title": "Compound Interest Formula",
                "content": "This chapter covers compound interest formula as part of the Compound Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of compound interest formula thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Compound Interest concepts"],
                "examples": [{"question": "Sample placement question on Compound Interest Formula", "solution": "Approach: Identify the concept from Compound Interest Formula, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "CI vs SI \u2014 Finding the Difference",
                "content": "This chapter covers ci vs si \u2014 finding the difference as part of the Compound Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of ci vs si \u2014 finding the difference thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Compound Interest concepts"],
                "examples": [{"question": "Sample placement question on CI vs SI \u2014 Finding the Difference", "solution": "Approach: Identify the concept from CI vs SI \u2014 Finding the Difference, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Half-yearly & Quarterly Compounding",
                "content": "This chapter covers half-yearly & quarterly compounding as part of the Compound Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of half-yearly & quarterly compounding thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Compound Interest concepts"],
                "examples": [{"question": "Sample placement question on Half-yearly & Quarterly Compounding", "solution": "Approach: Identify the concept from Half-yearly & Quarterly Compounding, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Growth, Depreciation & Population",
                "content": "This chapter covers growth, depreciation & population as part of the Compound Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of growth, depreciation & population thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Compound Interest concepts"],
                "examples": [{"question": "Sample placement question on Growth, Depreciation & Population", "solution": "Approach: Identify the concept from Growth, Depreciation & Population, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced CI Problems",
                "content": "This chapter covers advanced ci problems as part of the Compound Interest topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced ci problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Compound Interest concepts"],
                "examples": [{"question": "Sample placement question on Advanced CI Problems", "solution": "Approach: Identify the concept from Advanced CI Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "CI Formula", "explanation": "A = P(1 + R/100)^T. CI = A - P = P[(1 + R/100)^T - 1]."}, {"name": "Half-yearly Compounding", "explanation": "Rate becomes R/2, Time becomes 2T. A = P(1 + R/200)^(2T)."}, {"name": "CI vs SI Difference", "explanation": "For 2 years: CI - SI = P(R/100)\u00b2. For 3 years: CI - SI = PR\u00b2(300+R)/100\u00b3."}],
        "formulas": ["A = P(1 + R/100)^T", "CI = A - P", "For 2 years: CI - SI = P(R/100)\u00b2", "Effective rate for 2 years = 2R + R\u00b2/100"],
        "solved_examples": [{"question": "Find CI on \u20b910000 at 10% for 2 years.", "solution": "A = 10000(1.1)\u00b2 = 10000 \u00d7 1.21 = 12100. CI = 12100 - 10000 = \u20b92100."}, {"question": "Difference between CI and SI for 2 years on \u20b95000 at 4%?", "solution": "Diff = 5000 \u00d7 (4/100)\u00b2 = 5000 \u00d7 0.0016 = \u20b98."}],
        "tips": ["For 2 years, compute year by year if the formula seems complex.", "Population growth uses CI: P_new = P(1+R/100)^T.", "Depreciation: Value = P(1-R/100)^T."],
    },
    9: {
        "title": "Averages",
        "overview": "Average (arithmetic mean) is the sum of observations divided by the number of observations. Central to data interpretation.",
        "chapters": [
            {
                "title": "Basic Average Calculation",
                "content": "This chapter covers basic average calculation as part of the Averages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of basic average calculation thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Averages concepts"],
                "examples": [{"question": "Sample placement question on Basic Average Calculation", "solution": "Approach: Identify the concept from Basic Average Calculation, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Weighted Average",
                "content": "This chapter covers weighted average as part of the Averages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of weighted average thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Averages concepts"],
                "examples": [{"question": "Sample placement question on Weighted Average", "solution": "Approach: Identify the concept from Weighted Average, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Average of Combined Groups",
                "content": "This chapter covers average of combined groups as part of the Averages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of average of combined groups thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Averages concepts"],
                "examples": [{"question": "Sample placement question on Average of Combined Groups", "solution": "Approach: Identify the concept from Average of Combined Groups, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Running Average & Data Changes",
                "content": "This chapter covers running average & data changes as part of the Averages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of running average & data changes thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Averages concepts"],
                "examples": [{"question": "Sample placement question on Running Average & Data Changes", "solution": "Approach: Identify the concept from Running Average & Data Changes, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Average in Data Interpretation",
                "content": "This chapter covers average in data interpretation as part of the Averages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of average in data interpretation thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Averages concepts"],
                "examples": [{"question": "Sample placement question on Average in Data Interpretation", "solution": "Approach: Identify the concept from Average in Data Interpretation, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Basic Average", "explanation": "Average = Sum of all values / Number of values. Sum = Average \u00d7 Count."}, {"name": "Weighted Average", "explanation": "When groups have different sizes: Weighted avg = (n\u2081\u00d7a\u2081 + n\u2082\u00d7a\u2082) / (n\u2081 + n\u2082)."}, {"name": "Adding/Removing Elements", "explanation": "If a new person joins and average increases by x: New person's value = Old average + x \u00d7 (new count)."}],
        "formulas": ["Average = Sum / Count", "Sum = Average \u00d7 Count", "Average of first n naturals = (n+1)/2", "Average of consecutive numbers from a to b = (a+b)/2"],
        "solved_examples": [{"question": "Average of 5 numbers is 20. If one number is removed, average becomes 18. Find removed number.", "solution": "Sum of 5 = 100. Sum of 4 = 72. Removed number = 100 - 72 = 28."}, {"question": "Average age of 30 students is 15. Teacher joins, average becomes 16. Teacher's age?", "solution": "Sum of students = 450. New sum = 16 \u00d7 31 = 496. Teacher's age = 496 - 450 = 46."}],
        "tips": ["Average of an arithmetic progression = (first + last)/2.", "If all values increase by k, average increases by k.", "If all values multiply by k, average multiplies by k."],
    },
    10: {
        "title": "Problems on Ages",
        "overview": "Age problems involve setting up equations based on present, past, or future ages. A very common topic in placement exams.",
        "chapters": [
            {
                "title": "Age Relationships & Basic Equations",
                "content": "This chapter covers age relationships & basic equations as part of the Problems on Ages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of age relationships & basic equations thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Problems on Ages concepts"],
                "examples": [{"question": "Sample placement question on Age Relationships & Basic Equations", "solution": "Approach: Identify the concept from Age Relationships & Basic Equations, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Past & Future Age Problems",
                "content": "This chapter covers past & future age problems as part of the Problems on Ages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of past & future age problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Problems on Ages concepts"],
                "examples": [{"question": "Sample placement question on Past & Future Age Problems", "solution": "Approach: Identify the concept from Past & Future Age Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Ratio-based Age Problems",
                "content": "This chapter covers ratio-based age problems as part of the Problems on Ages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of ratio-based age problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Problems on Ages concepts"],
                "examples": [{"question": "Sample placement question on Ratio-based Age Problems", "solution": "Approach: Identify the concept from Ratio-based Age Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Family Age Problems",
                "content": "This chapter covers family age problems as part of the Problems on Ages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of family age problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Problems on Ages concepts"],
                "examples": [{"question": "Sample placement question on Family Age Problems", "solution": "Approach: Identify the concept from Family Age Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Complex Multi-person Age Equations",
                "content": "This chapter covers complex multi-person age equations as part of the Problems on Ages topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of complex multi-person age equations thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Problems on Ages concepts"],
                "examples": [{"question": "Sample placement question on Complex Multi-person Age Equations", "solution": "Approach: Identify the concept from Complex Multi-person Age Equations, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Setting Up Equations", "explanation": "Let present age = x. Age 'n' years ago = x - n. Age 'n' years later = x + n. The key is translating English statements into equations."}, {"name": "Ratio-based Problems", "explanation": "If current age ratio is a:b, ages can be written as ax and bx. Apply conditions to find x."}, {"name": "Common Patterns", "explanation": "Sum of ages changes: sum increases by (number of people \u00d7 years passed). Difference of ages stays constant regardless of time."}],
        "formulas": ["Present age = x, Past = x - n, Future = x + n", "Age difference remains constant over time", "If A is twice B's age now: A = 2B"],
        "solved_examples": [{"question": "Father is 3 times son's age. After 15 years, he'll be twice son's age. Find ages.", "solution": "Let son = x, father = 3x. After 15: 3x+15 = 2(x+15). 3x+15 = 2x+30. x = 15. Son=15, Father=45."}, {"question": "A is 5 years older than B. 3 years ago, A was 4 times B's age. Find present ages.", "solution": "A = B+5. Three years ago: (B+5-3) = 4(B-3). B+2 = 4B-12. 3B = 14. B = 14/3 \u2248 4.67 years, A \u2248 9.67 years."}],
        "tips": ["Always define variables clearly (present age = x).", "Difference of ages NEVER changes \u2014 use this to verify.", "Read the question twice \u2014 'was' means past, 'will be' means future."],
    },
    11: {
        "title": "Permutations & Combinations",
        "overview": "Permutations count arrangements (order matters). Combinations count selections (order doesn't matter). Essential for probability.",
        "chapters": [
            {
                "title": "Factorial & Fundamental Counting",
                "content": "This chapter covers factorial & fundamental counting as part of the Permutations & Combinations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of factorial & fundamental counting thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Permutations & Combinations concepts"],
                "examples": [{"question": "Sample placement question on Factorial & Fundamental Counting", "solution": "Approach: Identify the concept from Factorial & Fundamental Counting, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Permutations (nPr)",
                "content": "This chapter covers permutations (npr) as part of the Permutations & Combinations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of permutations (npr) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Permutations & Combinations concepts"],
                "examples": [{"question": "Sample placement question on Permutations (nPr)", "solution": "Approach: Identify the concept from Permutations (nPr), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Combinations (nCr)",
                "content": "This chapter covers combinations (ncr) as part of the Permutations & Combinations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of combinations (ncr) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Permutations & Combinations concepts"],
                "examples": [{"question": "Sample placement question on Combinations (nCr)", "solution": "Approach: Identify the concept from Combinations (nCr), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Special Cases \u2014 Circular, Identical Objects",
                "content": "This chapter covers special cases \u2014 circular, identical objects as part of the Permutations & Combinations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of special cases \u2014 circular, identical objects thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Permutations & Combinations concepts"],
                "examples": [{"question": "Sample placement question on Special Cases \u2014 Circular, Identical Objects", "solution": "Approach: Identify the concept from Special Cases \u2014 Circular, Identical Objects, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Probability Basics",
                "content": "This chapter covers probability basics as part of the Permutations & Combinations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of probability basics thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Permutations & Combinations concepts"],
                "examples": [{"question": "Sample placement question on Probability Basics", "solution": "Approach: Identify the concept from Probability Basics, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Factorial", "explanation": "n! = n \u00d7 (n-1) \u00d7 (n-2) \u00d7 ... \u00d7 1. 0! = 1. 5! = 120."}, {"name": "Permutation", "explanation": "nPr = n!/(n-r)!. Arranging r items from n items where order matters."}, {"name": "Combination", "explanation": "nCr = n!/[r!(n-r)!]. Selecting r items from n items where order doesn't matter."}, {"name": "Key Difference", "explanation": "Selecting a committee of 3 from 10 = C(10,3) = 120. Arranging 3 people in 3 positions from 10 = P(10,3) = 720. Combination \u00d7 r! = Permutation."}],
        "formulas": ["nPr = n!/(n-r)!", "nCr = n!/[r!(n-r)!]", "nCr = nC(n-r)", "nC0 = nCn = 1"],
        "solved_examples": [{"question": "In how many ways can 5 people be seated in a row?", "solution": "5! = 120 ways (permutation since order/position matters)."}, {"question": "How many ways to select 3 books from 8?", "solution": "C(8,3) = 8!/(3!5!) = (8\u00d77\u00d76)/(3\u00d72\u00d71) = 56 ways."}],
        "tips": ["Ask: does order matter? Yes \u2192 Permutation. No \u2192 Combination.", "Circular arrangement of n items = (n-1)!", "For 'at least' problems, sometimes it's easier to calculate total - unwanted cases."],
    },
    12: {
        "title": "Coding-Decoding",
        "overview": "In coding-decoding, letters/words are encoded following a pattern. You must identify the pattern and decode or encode the given input.",
        "chapters": [
            {
                "title": "Letter Coding Patterns",
                "content": "This chapter covers letter coding patterns as part of the Coding-Decoding topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of letter coding patterns thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Coding-Decoding concepts"],
                "examples": [{"question": "Sample placement question on Letter Coding Patterns", "solution": "Approach: Identify the concept from Letter Coding Patterns, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Number Coding",
                "content": "This chapter covers number coding as part of the Coding-Decoding topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of number coding thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Coding-Decoding concepts"],
                "examples": [{"question": "Sample placement question on Number Coding", "solution": "Approach: Identify the concept from Number Coding, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Mixed Coding Systems",
                "content": "This chapter covers mixed coding systems as part of the Coding-Decoding topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of mixed coding systems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Coding-Decoding concepts"],
                "examples": [{"question": "Sample placement question on Mixed Coding Systems", "solution": "Approach: Identify the concept from Mixed Coding Systems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Sentence & Condition Coding",
                "content": "This chapter covers sentence & condition coding as part of the Coding-Decoding topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of sentence & condition coding thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Coding-Decoding concepts"],
                "examples": [{"question": "Sample placement question on Sentence & Condition Coding", "solution": "Approach: Identify the concept from Sentence & Condition Coding, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Pattern Recognition",
                "content": "This chapter covers advanced pattern recognition as part of the Coding-Decoding topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced pattern recognition thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Coding-Decoding concepts"],
                "examples": [{"question": "Sample placement question on Advanced Pattern Recognition", "solution": "Approach: Identify the concept from Advanced Pattern Recognition, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Letter Shifting", "explanation": "Each letter shifted by a fixed number. A+2=C, B+2=D, etc. Can shift forward or backward."}, {"name": "Position-based Coding", "explanation": "Letters replaced by their position numbers: A=1, B=2... Z=26, or reversed: A=26, B=25... Z=1."}, {"name": "Mirror/Opposite Coding", "explanation": "Each letter replaced by its opposite: A\u2194Z, B\u2194Y, C\u2194X... The pair always sums to 27."}, {"name": "Mixed Pattern", "explanation": "Different positions may have different shifts: 1st letter +1, 2nd letter +2, 3rd letter +3, etc."}],
        "formulas": ["Position of letter = ASCII value - 64 (for uppercase)", "Opposite letter position = 27 - current position", "A=1, B=2, ..., Z=26"],
        "solved_examples": [{"question": "If COMPUTER is coded as DPNQVUFS, how is LAPTOP coded?", "solution": "Each letter +1: C\u2192D, O\u2192P, M\u2192N... So LAPTOP \u2192 MBQUPQ."}, {"question": "If MOUSE is coded as PRUVM, find the pattern.", "solution": "M+3=P, O+3=R, U+0=U, S+3=V, E+8=M. Pattern: +3,+3,+0,+3,+8. Actually checking: M(13)+3=P(16), O(15)+3=R(18), U(21)+0=U(21), S(19)+3=V(22), E(5)+8=M(13)."}],
        "tips": ["Write the alphabet with numbers underneath for quick reference.", "Check if the pattern is consistent or position-dependent.", "Look for reverse, mirror, or vowel/consonant specific rules."],
    },
    13: {
        "title": "Blood Relations",
        "overview": "Blood relation problems test your ability to trace family relationships from given clues. Drawing a family tree diagram is the key technique.",
        "chapters": [
            {
                "title": "Relation Types & Terminology",
                "content": "This chapter covers relation types & terminology as part of the Blood Relations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of relation types & terminology thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Blood Relations concepts"],
                "examples": [{"question": "Sample placement question on Relation Types & Terminology", "solution": "Approach: Identify the concept from Relation Types & Terminology, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Single Person Blood Relations",
                "content": "This chapter covers single person blood relations as part of the Blood Relations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of single person blood relations thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Blood Relations concepts"],
                "examples": [{"question": "Sample placement question on Single Person Blood Relations", "solution": "Approach: Identify the concept from Single Person Blood Relations, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Family Tree Construction",
                "content": "This chapter covers family tree construction as part of the Blood Relations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of family tree construction thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Blood Relations concepts"],
                "examples": [{"question": "Sample placement question on Family Tree Construction", "solution": "Approach: Identify the concept from Family Tree Construction, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Coded Blood Relations",
                "content": "This chapter covers coded blood relations as part of the Blood Relations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of coded blood relations thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Blood Relations concepts"],
                "examples": [{"question": "Sample placement question on Coded Blood Relations", "solution": "Approach: Identify the concept from Coded Blood Relations, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Complex Family Puzzles",
                "content": "This chapter covers complex family puzzles as part of the Blood Relations topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of complex family puzzles thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Blood Relations concepts"],
                "examples": [{"question": "Sample placement question on Complex Family Puzzles", "solution": "Approach: Identify the concept from Complex Family Puzzles, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Basic Relationships", "explanation": "Father's/Mother's father = Grandfather. Father's/Mother's mother = Grandmother. Father's brother = Uncle. Mother's brother = Maternal uncle. Father's sister = Aunt."}, {"name": "Drawing Family Trees", "explanation": "Use + for male, - for female. Horizontal line = married couple. Vertical line = parent-child. Always draw the tree from the clues given."}, {"name": "Coded Relationships", "explanation": "A+B means A is father of B. A-B means A is mother of B. A*B means A is husband of B. Learn the symbols specific to each question."}],
        "formulas": [],
        "solved_examples": [{"question": "Pointing to a photo, A said 'He is the son of my father's only daughter.' Who is in the photo?", "solution": "My father's only daughter = myself (A). Son of A = A's son. The photo shows A's son."}, {"question": "B is the brother of A. C is the daughter of B. D is the sister of C. What is D to A?", "solution": "B is A's brother. C is B's daughter. D is C's sister = B's daughter. So D is A's niece."}],
        "tips": ["ALWAYS draw a family tree \u2014 don't try to solve in your head.", "Gender matters: 'only daughter' vs 'only child' are different.", "'Father's only son' = the person themselves (if they have no brothers)."],
    },
    14: {
        "title": "Direction Sense",
        "overview": "Direction sense problems involve tracking movement and turns to determine final position or direction facing. Spatial reasoning is key.",
        "chapters": [
            {
                "title": "Basic Directions & Compass Points",
                "content": "This chapter covers basic directions & compass points as part of the Direction Sense topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of basic directions & compass points thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Direction Sense concepts"],
                "examples": [{"question": "Sample placement question on Basic Directions & Compass Points", "solution": "Approach: Identify the concept from Basic Directions & Compass Points, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Distance Calculation & Displacement",
                "content": "This chapter covers distance calculation & displacement as part of the Direction Sense topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of distance calculation & displacement thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Direction Sense concepts"],
                "examples": [{"question": "Sample placement question on Distance Calculation & Displacement", "solution": "Approach: Identify the concept from Distance Calculation & Displacement, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Shadow & Time-based Direction",
                "content": "This chapter covers shadow & time-based direction as part of the Direction Sense topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of shadow & time-based direction thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Direction Sense concepts"],
                "examples": [{"question": "Sample placement question on Shadow & Time-based Direction", "solution": "Approach: Identify the concept from Shadow & Time-based Direction, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Complex Path Problems",
                "content": "This chapter covers complex path problems as part of the Direction Sense topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of complex path problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Direction Sense concepts"],
                "examples": [{"question": "Sample placement question on Complex Path Problems", "solution": "Approach: Identify the concept from Complex Path Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Direction Sense",
                "content": "This chapter covers advanced direction sense as part of the Direction Sense topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced direction sense thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Direction Sense concepts"],
                "examples": [{"question": "Sample placement question on Advanced Direction Sense", "solution": "Approach: Identify the concept from Advanced Direction Sense, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Cardinal Directions", "explanation": "North (up), South (down), East (right), West (left). NE, NW, SE, SW are the four intermediate directions."}, {"name": "Turns", "explanation": "Right turn from North \u2192 East \u2192 South \u2192 West \u2192 North. Left turn is opposite: North \u2192 West \u2192 South \u2192 East \u2192 North. Each turn = 90\u00b0."}, {"name": "Shadow-based Direction", "explanation": "Morning: sun in East, shadow falls West. Evening: sun in West, shadow falls East. Noon: no shadow (sun overhead)."}],
        "formulas": ["Distance between two points = \u221a(x\u00b2 + y\u00b2) using Pythagoras", "Right turn: N\u2192E\u2192S\u2192W\u2192N", "Left turn: N\u2192W\u2192S\u2192E\u2192N"],
        "solved_examples": [{"question": "A man walks 5km North, turns right walks 3km, turns right walks 5km. How far from start?", "solution": "He's made a U-shape: 5N, 3E, 5S. Net displacement = 3km East from start."}, {"question": "At 6 AM, a man's shadow falls to his left. Which direction is he facing?", "solution": "6 AM: Sun in East, shadow falls West. Shadow is to his left, so his left = West. He faces South."}],
        "tips": ["Draw the path on paper \u2014 always start by marking North.", "Keep track of which direction you're facing after each turn.", "Use coordinate geometry for complex paths: assign (0,0) to start."],
    },
    15: {
        "title": "Seating Arrangement",
        "overview": "Seating arrangement problems involve placing people in a line or circle based on given conditions. Logical elimination is the approach.",
        "chapters": [
            {
                "title": "Linear Arrangement Basics",
                "content": "This chapter covers linear arrangement basics as part of the Seating Arrangement topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of linear arrangement basics thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Seating Arrangement concepts"],
                "examples": [{"question": "Sample placement question on Linear Arrangement Basics", "solution": "Approach: Identify the concept from Linear Arrangement Basics, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Circular Seating Arrangement",
                "content": "This chapter covers circular seating arrangement as part of the Seating Arrangement topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of circular seating arrangement thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Seating Arrangement concepts"],
                "examples": [{"question": "Sample placement question on Circular Seating Arrangement", "solution": "Approach: Identify the concept from Circular Seating Arrangement, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Double Row Arrangement",
                "content": "This chapter covers double row arrangement as part of the Seating Arrangement topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of double row arrangement thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Seating Arrangement concepts"],
                "examples": [{"question": "Sample placement question on Double Row Arrangement", "solution": "Approach: Identify the concept from Double Row Arrangement, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Conditional Arrangements",
                "content": "This chapter covers conditional arrangements as part of the Seating Arrangement topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of conditional arrangements thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Seating Arrangement concepts"],
                "examples": [{"question": "Sample placement question on Conditional Arrangements", "solution": "Approach: Identify the concept from Conditional Arrangements, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Complex Multi-constraint Puzzles",
                "content": "This chapter covers complex multi-constraint puzzles as part of the Seating Arrangement topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of complex multi-constraint puzzles thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Seating Arrangement concepts"],
                "examples": [{"question": "Sample placement question on Complex Multi-constraint Puzzles", "solution": "Approach: Identify the concept from Complex Multi-constraint Puzzles, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Linear Arrangement", "explanation": "People sit in a row. 'Left of' and 'right of' are from the perspective of the people sitting (facing you = reversed)."}, {"name": "Circular Arrangement", "explanation": "People sit around a table. 'Left' and 'right' are from each person's perspective. Clockwise/anticlockwise matters."}, {"name": "Approach", "explanation": "1. Read ALL clues first. 2. Start with the most definite clue. 3. Place people one by one. 4. Use elimination for remaining positions."}],
        "formulas": [],
        "solved_examples": [{"question": "5 people A,B,C,D,E sit in a row. B is to the right of A. C is between A and B. D is at one end. Where is E?", "solution": "From clues: A _ C _ B arrangement. D at one end. So: D A C B E or E B C A D. Since B is right of A: D A C B E."}],
        "tips": ["Always draw the arrangement visually.", "For circular, fix one person and arrange others relative to them.", "'Immediately left/right' means adjacent. 'To the left' can have gaps."],
    },
    16: {
        "title": "Syllogism",
        "overview": "Syllogism involves drawing conclusions from given statements using Venn diagrams. It tests logical deduction ability.",
        "chapters": [
            {
                "title": "Venn Diagrams for Syllogism",
                "content": "This chapter covers venn diagrams for syllogism as part of the Syllogism topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of venn diagrams for syllogism thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Syllogism concepts"],
                "examples": [{"question": "Sample placement question on Venn Diagrams for Syllogism", "solution": "Approach: Identify the concept from Venn Diagrams for Syllogism, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "All/Some/No Statements",
                "content": "This chapter covers all/some/no statements as part of the Syllogism topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of all/some/no statements thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Syllogism concepts"],
                "examples": [{"question": "Sample placement question on All/Some/No Statements", "solution": "Approach: Identify the concept from All/Some/No Statements, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Definite Conclusions",
                "content": "This chapter covers definite conclusions as part of the Syllogism topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of definite conclusions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Syllogism concepts"],
                "examples": [{"question": "Sample placement question on Definite Conclusions", "solution": "Approach: Identify the concept from Definite Conclusions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Possibility-based Conclusions",
                "content": "This chapter covers possibility-based conclusions as part of the Syllogism topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of possibility-based conclusions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Syllogism concepts"],
                "examples": [{"question": "Sample placement question on Possibility-based Conclusions", "solution": "Approach: Identify the concept from Possibility-based Conclusions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Complex Multi-Statement Syllogisms",
                "content": "This chapter covers complex multi-statement syllogisms as part of the Syllogism topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of complex multi-statement syllogisms thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Syllogism concepts"],
                "examples": [{"question": "Sample placement question on Complex Multi-Statement Syllogisms", "solution": "Approach: Identify the concept from Complex Multi-Statement Syllogisms, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Statement Types", "explanation": "All A are B (Universal Positive). No A is B (Universal Negative). Some A are B (Particular Positive). Some A are not B (Particular Negative)."}, {"name": "Venn Diagram Method", "explanation": "Draw all possible Venn diagrams for the given statements. A conclusion is valid only if it holds true in ALL possible diagrams."}, {"name": "Key Rules", "explanation": "All A are B \u2192 Some A are B (true). All A are B \u2192 Some B are A (true). Some A are B \u2192 Some B are A (true). No A is B \u2192 No B is A (true)."}],
        "formulas": [],
        "solved_examples": [{"question": "All dogs are cats. All cats are birds. Conclusion: All dogs are birds?", "solution": "Draw: Dogs \u2282 Cats \u2282 Birds. If all dogs are cats and all cats are birds, then all dogs are birds. TRUE."}, {"question": "Some pens are pencils. All pencils are erasers. Conclusion: Some pens are erasers?", "solution": "The 'some pens' that are pencils must also be erasers (since all pencils are erasers). TRUE."}],
        "tips": ["Always draw Venn diagrams \u2014 never rely on intuition.", "A conclusion with 'All' requires stronger evidence than 'Some'.", "Check EVERY possible diagram before confirming/denying."],
    },
    17: {
        "title": "Number Series",
        "overview": "Find the pattern in a sequence of numbers and predict the next term or find the missing one.",
        "chapters": [
            {
                "title": "Arithmetic Progressions (AP)",
                "content": "This chapter covers arithmetic progressions (ap) as part of the Number Series topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of arithmetic progressions (ap) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Number Series concepts"],
                "examples": [{"question": "Sample placement question on Arithmetic Progressions (AP)", "solution": "Approach: Identify the concept from Arithmetic Progressions (AP), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Geometric Progressions (GP)",
                "content": "This chapter covers geometric progressions (gp) as part of the Number Series topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of geometric progressions (gp) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Number Series concepts"],
                "examples": [{"question": "Sample placement question on Geometric Progressions (GP)", "solution": "Approach: Identify the concept from Geometric Progressions (GP), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Mixed & Complex Series",
                "content": "This chapter covers mixed & complex series as part of the Number Series topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of mixed & complex series thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Number Series concepts"],
                "examples": [{"question": "Sample placement question on Mixed & Complex Series", "solution": "Approach: Identify the concept from Mixed & Complex Series, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Wrong Number Detection",
                "content": "This chapter covers wrong number detection as part of the Number Series topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of wrong number detection thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Number Series concepts"],
                "examples": [{"question": "Sample placement question on Wrong Number Detection", "solution": "Approach: Identify the concept from Wrong Number Detection, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Pattern Recognition",
                "content": "This chapter covers advanced pattern recognition as part of the Number Series topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced pattern recognition thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Number Series concepts"],
                "examples": [{"question": "Sample placement question on Advanced Pattern Recognition", "solution": "Approach: Identify the concept from Advanced Pattern Recognition, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Arithmetic Series", "explanation": "Constant difference: 2, 5, 8, 11... (d=3). Next = last + d."}, {"name": "Geometric Series", "explanation": "Constant ratio: 3, 6, 12, 24... (r=2). Next = last \u00d7 r."}, {"name": "Mixed/Complex Patterns", "explanation": "Differences of differences, alternating operations (+2,\u00d73,+2,\u00d73...), or prime number series."}, {"name": "Fibonacci-type", "explanation": "Each term = sum of two preceding: 1, 1, 2, 3, 5, 8, 13..."}],
        "formulas": ["AP: nth term = a + (n-1)d", "GP: nth term = a \u00d7 r^(n-1)", "Sum of AP = n/2 \u00d7 (first + last)"],
        "solved_examples": [{"question": "Find next: 2, 6, 18, 54, ?", "solution": "Ratio: 6/2=3, 18/6=3, 54/18=3. GP with r=3. Next = 54\u00d73 = 162."}, {"question": "Find next: 1, 4, 9, 16, 25, ?", "solution": "These are perfect squares: 1\u00b2, 2\u00b2, 3\u00b2, 4\u00b2, 5\u00b2. Next = 6\u00b2 = 36."}],
        "tips": ["First check differences. Then check ratio. Then check second differences.", "Look for squares, cubes, primes, and factorials.", "If the pattern isn't obvious, try differences of differences."],
    },
    18: {
        "title": "Analogies",
        "overview": "Analogies test the relationship between pairs. Given A:B, find C:D where the A-B relationship equals the C-D relationship.",
        "chapters": [
            {
                "title": "Word Analogies",
                "content": "This chapter covers word analogies as part of the Analogies topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of word analogies thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Analogies concepts"],
                "examples": [{"question": "Sample placement question on Word Analogies", "solution": "Approach: Identify the concept from Word Analogies, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Number Analogies",
                "content": "This chapter covers number analogies as part of the Analogies topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of number analogies thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Analogies concepts"],
                "examples": [{"question": "Sample placement question on Number Analogies", "solution": "Approach: Identify the concept from Number Analogies, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Letter & Symbol Analogies",
                "content": "This chapter covers letter & symbol analogies as part of the Analogies topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of letter & symbol analogies thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Analogies concepts"],
                "examples": [{"question": "Sample placement question on Letter & Symbol Analogies", "solution": "Approach: Identify the concept from Letter & Symbol Analogies, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Mixed Analogies",
                "content": "This chapter covers mixed analogies as part of the Analogies topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of mixed analogies thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Analogies concepts"],
                "examples": [{"question": "Sample placement question on Mixed Analogies", "solution": "Approach: Identify the concept from Mixed Analogies, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Complex Relationship Analogies",
                "content": "This chapter covers complex relationship analogies as part of the Analogies topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of complex relationship analogies thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Analogies concepts"],
                "examples": [{"question": "Sample placement question on Complex Relationship Analogies", "solution": "Approach: Identify the concept from Complex Relationship Analogies, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Types of Relationships", "explanation": "Synonym/Antonym, Part-Whole, Cause-Effect, Tool-Function, Worker-Product, Degree (warm:hot)."}, {"name": "Letter Analogies", "explanation": "Positional relationships: AB:CD (each +2), or mirror patterns."}, {"name": "Number Analogies", "explanation": "Mathematical relationships: 4:16 (square), 3:27 (cube), 6:36::8:64."}],
        "formulas": [],
        "solved_examples": [{"question": "Doctor : Hospital :: Teacher : ?", "solution": "A doctor works in a hospital. A teacher works in a school. Answer: School."}, {"question": "25 : 36 :: 49 : ?", "solution": "25=5\u00b2, 36=6\u00b2 (next perfect square). 49=7\u00b2, next = 8\u00b2 = 64. Answer: 64."}],
        "tips": ["Identify the exact relationship first, then apply.", "Be precise: Author:Book, not Author:Library.", "Watch for direction: Big:Small (antonym) vs Big:Bigger (degree)."],
    },
    19: {
        "title": "Logical Deduction",
        "overview": "Logical deduction involves deriving conclusions from a set of premises using formal logic rules. Covers statement-conclusion and assumption problems.",
        "chapters": [
            {
                "title": "Statements & Assumptions",
                "content": "This chapter covers statements & assumptions as part of the Logical Deduction topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of statements & assumptions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Logical Deduction concepts"],
                "examples": [{"question": "Sample placement question on Statements & Assumptions", "solution": "Approach: Identify the concept from Statements & Assumptions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Statements & Arguments",
                "content": "This chapter covers statements & arguments as part of the Logical Deduction topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of statements & arguments thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Logical Deduction concepts"],
                "examples": [{"question": "Sample placement question on Statements & Arguments", "solution": "Approach: Identify the concept from Statements & Arguments, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Course of Action",
                "content": "This chapter covers course of action as part of the Logical Deduction topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of course of action thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Logical Deduction concepts"],
                "examples": [{"question": "Sample placement question on Course of Action", "solution": "Approach: Identify the concept from Course of Action, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Cause & Effect",
                "content": "This chapter covers cause & effect as part of the Logical Deduction topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of cause & effect thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Logical Deduction concepts"],
                "examples": [{"question": "Sample placement question on Cause & Effect", "solution": "Approach: Identify the concept from Cause & Effect, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Critical Reasoning & Strengthening/Weakening",
                "content": "This chapter covers critical reasoning & strengthening/weakening as part of the Logical Deduction topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of critical reasoning & strengthening/weakening thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Logical Deduction concepts"],
                "examples": [{"question": "Sample placement question on Critical Reasoning & Strengthening/Weakening", "solution": "Approach: Identify the concept from Critical Reasoning & Strengthening/Weakening, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Statements & Conclusions", "explanation": "Evaluate whether conclusions logically follow from given statements. Don't use general knowledge \u2014 only use what's given."}, {"name": "Assumptions", "explanation": "An assumption is an unstated premise that must be true for the statement to be valid."}, {"name": "Course of Action", "explanation": "Given a problem statement, determine which suggested actions are appropriate responses."}, {"name": "Cause & Effect", "explanation": "Determine if two events share a cause-effect relationship, are independent, or one causes the other."}],
        "formulas": [],
        "solved_examples": [{"question": "Statement: 'All employees must attend the training.' Assumption: The training is mandatory.", "solution": "The word 'must' implies the training is not optional. The assumption is VALID."}],
        "tips": ["Only use information given in the premises.", "An assumption fills the gap between statement and conclusion.", "Common sense assumptions are often traps \u2014 stick to logic."],
    },
    20: {
        "title": "Synonyms",
        "overview": "Synonyms are words with similar meanings. Building vocabulary is essential for verbal ability in placement exams.",
        "chapters": [
            {
                "title": "Common Synonyms (A-M)",
                "content": "This chapter covers common synonyms (a-m) as part of the Synonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of common synonyms (a-m) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Synonyms concepts"],
                "examples": [{"question": "Sample placement question on Common Synonyms (A-M)", "solution": "Approach: Identify the concept from Common Synonyms (A-M), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Common Synonyms (N-Z)",
                "content": "This chapter covers common synonyms (n-z) as part of the Synonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of common synonyms (n-z) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Synonyms concepts"],
                "examples": [{"question": "Sample placement question on Common Synonyms (N-Z)", "solution": "Approach: Identify the concept from Common Synonyms (N-Z), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Context-based Synonym Selection",
                "content": "This chapter covers context-based synonym selection as part of the Synonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of context-based synonym selection thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Synonyms concepts"],
                "examples": [{"question": "Sample placement question on Context-based Synonym Selection", "solution": "Approach: Identify the concept from Context-based Synonym Selection, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Synonym Patterns in Exams",
                "content": "This chapter covers synonym patterns in exams as part of the Synonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of synonym patterns in exams thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Synonyms concepts"],
                "examples": [{"question": "Sample placement question on Synonym Patterns in Exams", "solution": "Approach: Identify the concept from Synonym Patterns in Exams, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Vocabulary Practice",
                "content": "This chapter covers advanced vocabulary practice as part of the Synonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced vocabulary practice thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Synonyms concepts"],
                "examples": [{"question": "Sample placement question on Advanced Vocabulary Practice", "solution": "Approach: Identify the concept from Advanced Vocabulary Practice, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Context Matters", "explanation": "A word can have different meanings in different contexts. 'Bank' (river bank vs financial bank). Choose synonym that matches context."}, {"name": "Word Roots", "explanation": "Latin/Greek roots help guess meanings. 'Bene' = good (benevolent, benefit). 'Mal' = bad (malice, malevolent). 'Aqua' = water."}, {"name": "Common Exam Words", "explanation": "Abate=reduce, Benevolent=kind, Candid=frank, Diligent=hardworking, Ephemeral=short-lived, Frugal=thrifty."}],
        "formulas": [],
        "solved_examples": [{"question": "Synonym of 'Arduous'", "solution": "Arduous means requiring great effort. Synonym: Strenuous, Difficult, Laborious."}, {"question": "Synonym of 'Benevolent'", "solution": "Benevolent means well-meaning and kindly. Synonym: Kind, Generous, Charitable."}],
        "tips": ["Read extensively to build vocabulary naturally.", "Learn word roots \u2014 they help with unfamiliar words.", "Practice 10 new words daily with usage in sentences."],
    },
    21: {
        "title": "Antonyms",
        "overview": "Antonyms are words with opposite meanings. Often paired with synonyms in verbal ability sections.",
        "chapters": [
            {
                "title": "Common Antonyms",
                "content": "This chapter covers common antonyms as part of the Antonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of common antonyms thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Antonyms concepts"],
                "examples": [{"question": "Sample placement question on Common Antonyms", "solution": "Approach: Identify the concept from Common Antonyms, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Prefix-based Antonyms (un-, in-, dis-)",
                "content": "This chapter covers prefix-based antonyms (un-, in-, dis-) as part of the Antonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of prefix-based antonyms (un-, in-, dis-) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Antonyms concepts"],
                "examples": [{"question": "Sample placement question on Prefix-based Antonyms (un-, in-, dis-)", "solution": "Approach: Identify the concept from Prefix-based Antonyms (un-, in-, dis-), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Context Antonyms",
                "content": "This chapter covers context antonyms as part of the Antonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of context antonyms thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Antonyms concepts"],
                "examples": [{"question": "Sample placement question on Context Antonyms", "solution": "Approach: Identify the concept from Context Antonyms, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Tricky Antonym Pairs",
                "content": "This chapter covers tricky antonym pairs as part of the Antonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of tricky antonym pairs thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Antonyms concepts"],
                "examples": [{"question": "Sample placement question on Tricky Antonym Pairs", "solution": "Approach: Identify the concept from Tricky Antonym Pairs, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Exam-oriented Antonym Practice",
                "content": "This chapter covers exam-oriented antonym practice as part of the Antonyms topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of exam-oriented antonym practice thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Antonyms concepts"],
                "examples": [{"question": "Sample placement question on Exam-oriented Antonym Practice", "solution": "Approach: Identify the concept from Exam-oriented Antonym Practice, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Gradable Antonyms", "explanation": "Opposites on a scale: hot-cold, big-small, fast-slow. There are degrees between them."}, {"name": "Complementary Antonyms", "explanation": "Either-or pairs: alive-dead, true-false, male-female. No middle ground."}, {"name": "Relational Antonyms", "explanation": "Pairs that exist in relation: teacher-student, buy-sell, parent-child."}],
        "formulas": [],
        "solved_examples": [{"question": "Antonym of 'Verbose'", "solution": "Verbose means using too many words. Antonym: Concise, Succinct, Brief."}, {"question": "Antonym of 'Affluent'", "solution": "Affluent means wealthy. Antonym: Poor, Impoverished, Destitute."}],
        "tips": ["Know both synonym AND antonym for common words.", "Prefix-based antonyms: happy/unhappy, possible/impossible.", "Context determines the correct antonym \u2014 'light' opposite could be 'heavy' or 'dark'."],
    },
    22: {
        "title": "Sentence Completion",
        "overview": "Fill in the blank(s) in a sentence with the most appropriate word. Tests vocabulary, grammar, and contextual understanding.",
        "chapters": [
            {
                "title": "Grammar-based Sentence Completion",
                "content": "This chapter covers grammar-based sentence completion as part of the Sentence Completion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of grammar-based sentence completion thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Sentence Completion concepts"],
                "examples": [{"question": "Sample placement question on Grammar-based Sentence Completion", "solution": "Approach: Identify the concept from Grammar-based Sentence Completion, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Vocabulary-based Fill-ins",
                "content": "This chapter covers vocabulary-based fill-ins as part of the Sentence Completion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of vocabulary-based fill-ins thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Sentence Completion concepts"],
                "examples": [{"question": "Sample placement question on Vocabulary-based Fill-ins", "solution": "Approach: Identify the concept from Vocabulary-based Fill-ins, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Idiom & Phrase Completion",
                "content": "This chapter covers idiom & phrase completion as part of the Sentence Completion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of idiom & phrase completion thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Sentence Completion concepts"],
                "examples": [{"question": "Sample placement question on Idiom & Phrase Completion", "solution": "Approach: Identify the concept from Idiom & Phrase Completion, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Dual Blank Sentences",
                "content": "This chapter covers dual blank sentences as part of the Sentence Completion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of dual blank sentences thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Sentence Completion concepts"],
                "examples": [{"question": "Sample placement question on Dual Blank Sentences", "solution": "Approach: Identify the concept from Dual Blank Sentences, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Paragraph-level Completion",
                "content": "This chapter covers paragraph-level completion as part of the Sentence Completion topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of paragraph-level completion thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Sentence Completion concepts"],
                "examples": [{"question": "Sample placement question on Paragraph-level Completion", "solution": "Approach: Identify the concept from Paragraph-level Completion, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Context Clues", "explanation": "Look for signal words: 'however/but' (contrast), 'moreover/and' (continuation), 'because/since' (cause-effect)."}, {"name": "Tone Matching", "explanation": "The answer must match the sentence's tone: positive, negative, neutral, formal, informal."}, {"name": "Elimination Strategy", "explanation": "Eliminate clearly wrong options first. Then test remaining options by reading the complete sentence aloud."}],
        "formulas": [],
        "solved_examples": [{"question": "Despite his _____, he failed the exam. (a) diligence (b) laziness (c) ignorance (d) absence", "solution": "'Despite' indicates contrast. He failed despite something positive. Answer: (a) diligence."}],
        "tips": ["'Despite/although' = contrast. 'Because/since' = cause. 'Moreover/furthermore' = addition.", "Read the complete sentence with your choice to verify it sounds natural.", "Two blanks: solve the easier blank first to eliminate options."],
    },
    23: {
        "title": "Reading Comprehension",
        "overview": "Read a passage carefully and answer questions about its content, tone, inference, and implications.",
        "chapters": [
            {
                "title": "Finding the Main Idea",
                "content": "This chapter covers finding the main idea as part of the Reading Comprehension topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of finding the main idea thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Reading Comprehension concepts"],
                "examples": [{"question": "Sample placement question on Finding the Main Idea", "solution": "Approach: Identify the concept from Finding the Main Idea, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Inference Questions",
                "content": "This chapter covers inference questions as part of the Reading Comprehension topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of inference questions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Reading Comprehension concepts"],
                "examples": [{"question": "Sample placement question on Inference Questions", "solution": "Approach: Identify the concept from Inference Questions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Vocabulary in Context",
                "content": "This chapter covers vocabulary in context as part of the Reading Comprehension topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of vocabulary in context thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Reading Comprehension concepts"],
                "examples": [{"question": "Sample placement question on Vocabulary in Context", "solution": "Approach: Identify the concept from Vocabulary in Context, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Author's Tone & Attitude",
                "content": "This chapter covers author's tone & attitude as part of the Reading Comprehension topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of author's tone & attitude thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Reading Comprehension concepts"],
                "examples": [{"question": "Sample placement question on Author's Tone & Attitude", "solution": "Approach: Identify the concept from Author's Tone & Attitude, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Different Passage Types & Strategies",
                "content": "This chapter covers different passage types & strategies as part of the Reading Comprehension topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of different passage types & strategies thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Reading Comprehension concepts"],
                "examples": [{"question": "Sample placement question on Different Passage Types & Strategies", "solution": "Approach: Identify the concept from Different Passage Types & Strategies, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Skimming vs Scanning", "explanation": "Skim: read quickly for general idea. Scan: look for specific information (names, dates, numbers)."}, {"name": "Question Types", "explanation": "Factual (directly stated), Inferential (implied but not stated), Vocabulary (word meaning in context), Main idea, Tone/attitude."}, {"name": "Strategy", "explanation": "1. Read questions first. 2. Skim the passage. 3. Read relevant parts carefully. 4. Answer based on passage, not outside knowledge."}],
        "formulas": [],
        "solved_examples": [{"question": "How to identify the main idea?", "solution": "The main idea is usually in the first or last paragraph. Ask: 'What is the passage mostly about?' Eliminate options that are too specific or too broad."}],
        "tips": ["Answer based on the passage ONLY \u2014 not your general knowledge.", "For 'tone' questions: is the author supportive, critical, neutral, sarcastic?", "Practice with a timer \u2014 aim for 2 minutes per passage in exams."],
    },
    24: {
        "title": "Para Jumbles",
        "overview": "Rearrange jumbled sentences into a coherent paragraph. Tests understanding of logical flow and connecting ideas.",
        "chapters": [
            {
                "title": "Identifying Opening & Closing Sentences",
                "content": "This chapter covers identifying opening & closing sentences as part of the Para Jumbles topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of identifying opening & closing sentences thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Para Jumbles concepts"],
                "examples": [{"question": "Sample placement question on Identifying Opening & Closing Sentences", "solution": "Approach: Identify the concept from Identifying Opening & Closing Sentences, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Using Linking Words & Transitions",
                "content": "This chapter covers using linking words & transitions as part of the Para Jumbles topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of using linking words & transitions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Para Jumbles concepts"],
                "examples": [{"question": "Sample placement question on Using Linking Words & Transitions", "solution": "Approach: Identify the concept from Using Linking Words & Transitions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Pronoun Reference Method",
                "content": "This chapter covers pronoun reference method as part of the Para Jumbles topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of pronoun reference method thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Para Jumbles concepts"],
                "examples": [{"question": "Sample placement question on Pronoun Reference Method", "solution": "Approach: Identify the concept from Pronoun Reference Method, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Chronological & Logical Ordering",
                "content": "This chapter covers chronological & logical ordering as part of the Para Jumbles topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of chronological & logical ordering thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Para Jumbles concepts"],
                "examples": [{"question": "Sample placement question on Chronological & Logical Ordering", "solution": "Approach: Identify the concept from Chronological & Logical Ordering, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Practice Strategies for Para Jumbles",
                "content": "This chapter covers practice strategies for para jumbles as part of the Para Jumbles topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of practice strategies for para jumbles thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Para Jumbles concepts"],
                "examples": [{"question": "Sample placement question on Practice Strategies for Para Jumbles", "solution": "Approach: Identify the concept from Practice Strategies for Para Jumbles, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Opening Sentence", "explanation": "Usually introduces the topic, contains no pronouns referring to previous context, and doesn't start with 'But/However/Moreover'."}, {"name": "Linking Words", "explanation": "'This/That/These' refer to something mentioned earlier. 'However/But' show contrast with previous sentence. 'Moreover/Furthermore' continue an idea."}, {"name": "Mandatory Pairs", "explanation": "Some sentences MUST be adjacent. Find these pairs first, then arrange the pairs."}],
        "formulas": [],
        "solved_examples": [{"question": "Strategy to solve", "solution": "1. Find the opening sentence (introduces topic). 2. Find mandatory pairs (pronouns, connectors). 3. Arrange pairs in logical order. 4. Verify flow."}],
        "tips": ["Find the opening sentence first \u2014 it introduces the topic.", "Look for pronoun references: 'He' must come after the person's name.", "Read the final arrangement to check it flows naturally."],
    },
    25: {
        "title": "Spotting Errors",
        "overview": "Identify the grammatical error in a given sentence. Tests knowledge of grammar rules: subject-verb agreement, tenses, prepositions, articles.",
        "chapters": [
            {
                "title": "Subject-Verb Agreement Errors",
                "content": "This chapter covers subject-verb agreement errors as part of the Spotting Errors topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of subject-verb agreement errors thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Spotting Errors concepts"],
                "examples": [{"question": "Sample placement question on Subject-Verb Agreement Errors", "solution": "Approach: Identify the concept from Subject-Verb Agreement Errors, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Tense Errors",
                "content": "This chapter covers tense errors as part of the Spotting Errors topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of tense errors thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Spotting Errors concepts"],
                "examples": [{"question": "Sample placement question on Tense Errors", "solution": "Approach: Identify the concept from Tense Errors, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Preposition Errors",
                "content": "This chapter covers preposition errors as part of the Spotting Errors topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of preposition errors thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Spotting Errors concepts"],
                "examples": [{"question": "Sample placement question on Preposition Errors", "solution": "Approach: Identify the concept from Preposition Errors, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Pronoun & Article Errors",
                "content": "This chapter covers pronoun & article errors as part of the Spotting Errors topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of pronoun & article errors thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Spotting Errors concepts"],
                "examples": [{"question": "Sample placement question on Pronoun & Article Errors", "solution": "Approach: Identify the concept from Pronoun & Article Errors, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Common Exam Error Patterns",
                "content": "This chapter covers common exam error patterns as part of the Spotting Errors topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of common exam error patterns thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Spotting Errors concepts"],
                "examples": [{"question": "Sample placement question on Common Exam Error Patterns", "solution": "Approach: Identify the concept from Common Exam Error Patterns, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Subject-Verb Agreement", "explanation": "Singular subject \u2192 singular verb. 'The list of items IS long' (not 'are'). Tricky: 'Neither A nor B' \u2192 verb agrees with B."}, {"name": "Tense Consistency", "explanation": "Don't mix tenses in one sentence without reason. 'He went to the store and buys milk' is wrong."}, {"name": "Common Errors", "explanation": "Articles (a/an/the), prepositions (on/in/at), pronoun agreement, misplaced modifiers, parallel structure."}],
        "formulas": [],
        "solved_examples": [{"question": "'Each of the boys have completed their task.' Find error.", "solution": "'Each' is singular \u2192 'has' not 'have'. Also 'their' should be 'his'. Correct: 'Each of the boys has completed his task.'"}],
        "tips": ["Check subject-verb agreement first \u2014 most common error.", "Watch for 'either/neither/each/every' \u2014 these are SINGULAR.", "Preposition errors: 'different from' (not 'than'), 'superior to' (not 'than')."],
    },
    26: {
        "title": "Idioms & Phrases",
        "overview": "Learn meanings of common English idioms and phrases frequently asked in placement exams.",
        "chapters": [
            {
                "title": "Common Idioms (A-L)",
                "content": "This chapter covers common idioms (a-l) as part of the Idioms & Phrases topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of common idioms (a-l) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Idioms & Phrases concepts"],
                "examples": [{"question": "Sample placement question on Common Idioms (A-L)", "solution": "Approach: Identify the concept from Common Idioms (A-L), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Common Idioms (M-Z)",
                "content": "This chapter covers common idioms (m-z) as part of the Idioms & Phrases topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of common idioms (m-z) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Idioms & Phrases concepts"],
                "examples": [{"question": "Sample placement question on Common Idioms (M-Z)", "solution": "Approach: Identify the concept from Common Idioms (M-Z), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Phrasal Verbs",
                "content": "This chapter covers phrasal verbs as part of the Idioms & Phrases topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of phrasal verbs thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Idioms & Phrases concepts"],
                "examples": [{"question": "Sample placement question on Phrasal Verbs", "solution": "Approach: Identify the concept from Phrasal Verbs, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Proverbs & Their Meanings",
                "content": "This chapter covers proverbs & their meanings as part of the Idioms & Phrases topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of proverbs & their meanings thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Idioms & Phrases concepts"],
                "examples": [{"question": "Sample placement question on Proverbs & Their Meanings", "solution": "Approach: Identify the concept from Proverbs & Their Meanings, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Exam-oriented Idiom Practice",
                "content": "This chapter covers exam-oriented idiom practice as part of the Idioms & Phrases topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of exam-oriented idiom practice thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Idioms & Phrases concepts"],
                "examples": [{"question": "Sample placement question on Exam-oriented Idiom Practice", "solution": "Approach: Identify the concept from Exam-oriented Idiom Practice, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Common Idioms", "explanation": "Break the ice = initiate conversation. Burn the midnight oil = study late. Hit the nail on the head = be exactly right. Once in a blue moon = very rarely."}, {"name": "Phrasal Verbs", "explanation": "Look up = search for information. Put off = postpone. Turn down = reject. Bring up = raise/mention. Come across = find unexpectedly."}, {"name": "Proverbs", "explanation": "A stitch in time saves nine = fix problems early. Don't count chickens before they hatch = don't be overconfident. Rome wasn't built in a day = be patient."}],
        "formulas": [],
        "solved_examples": [{"question": "'He let the cat out of the bag.' Meaning?", "solution": "To let the cat out of the bag = to reveal a secret accidentally."}, {"question": "'She's burning the candle at both ends.' Meaning?", "solution": "To exhaust oneself by overworking or being too busy."}],
        "tips": ["Learn 5 idioms per day \u2014 flashcards help.", "Use idioms in daily conversation to remember them.", "In exams, don't take idioms literally \u2014 they have figurative meanings."],
    },
    27: {
        "title": "Tables",
        "overview": "Interpret data presented in tabular form. Calculate percentages, ratios, averages, and comparisons from table data.",
        "chapters": [
            {
                "title": "Reading & Understanding Tables",
                "content": "This chapter covers reading & understanding tables as part of the Tables topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of reading & understanding tables thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Tables concepts"],
                "examples": [{"question": "Sample placement question on Reading & Understanding Tables", "solution": "Approach: Identify the concept from Reading & Understanding Tables, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Calculations from Table Data",
                "content": "This chapter covers calculations from table data as part of the Tables topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of calculations from table data thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Tables concepts"],
                "examples": [{"question": "Sample placement question on Calculations from Table Data", "solution": "Approach: Identify the concept from Calculations from Table Data, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Percentage-based Table Problems",
                "content": "This chapter covers percentage-based table problems as part of the Tables topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of percentage-based table problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Tables concepts"],
                "examples": [{"question": "Sample placement question on Percentage-based Table Problems", "solution": "Approach: Identify the concept from Percentage-based Table Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Ratio & Comparison from Tables",
                "content": "This chapter covers ratio & comparison from tables as part of the Tables topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of ratio & comparison from tables thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Tables concepts"],
                "examples": [{"question": "Sample placement question on Ratio & Comparison from Tables", "solution": "Approach: Identify the concept from Ratio & Comparison from Tables, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Multi-table Analysis",
                "content": "This chapter covers multi-table analysis as part of the Tables topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of multi-table analysis thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Tables concepts"],
                "examples": [{"question": "Sample placement question on Multi-table Analysis", "solution": "Approach: Identify the concept from Multi-table Analysis, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Reading Tables", "explanation": "Identify rows (usually categories) and columns (usually time periods or sub-categories). Note units and any footnotes."}, {"name": "Calculations", "explanation": "Common operations: % change = (new-old)/old \u00d7 100. Ratio between rows/columns. Average of a row or column."}, {"name": "Approximation", "explanation": "In competitive exams, approximate to save time. 19.8% \u2248 20%. 298/5 \u2248 300/5 = 60."}],
        "formulas": ["% change = ((New - Old) / Old) \u00d7 100", "Average = Sum / Count"],
        "solved_examples": [{"question": "If a table shows sales of 5 products over 3 years, find which product had highest growth.", "solution": "Calculate % growth for each product: (Year3 - Year1)/Year1 \u00d7 100. Compare all five."}],
        "tips": ["Don't read the entire table first \u2014 go to questions, then find relevant data.", "Approximation is your friend in DI \u2014 don't waste time on exact calculations.", "Check units carefully \u2014 lakhs vs crores makes a big difference."],
    },
    28: {
        "title": "Bar Graphs",
        "overview": "Analyze data represented as vertical or horizontal bars. Compare quantities, trends, and proportions visually.",
        "chapters": [
            {
                "title": "Reading Bar Graphs",
                "content": "This chapter covers reading bar graphs as part of the Bar Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of reading bar graphs thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Bar Graphs concepts"],
                "examples": [{"question": "Sample placement question on Reading Bar Graphs", "solution": "Approach: Identify the concept from Reading Bar Graphs, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Simple Calculations from Bars",
                "content": "This chapter covers simple calculations from bars as part of the Bar Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of simple calculations from bars thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Bar Graphs concepts"],
                "examples": [{"question": "Sample placement question on Simple Calculations from Bars", "solution": "Approach: Identify the concept from Simple Calculations from Bars, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Grouped & Clustered Bar Graphs",
                "content": "This chapter covers grouped & clustered bar graphs as part of the Bar Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of grouped & clustered bar graphs thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Bar Graphs concepts"],
                "examples": [{"question": "Sample placement question on Grouped & Clustered Bar Graphs", "solution": "Approach: Identify the concept from Grouped & Clustered Bar Graphs, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Stacked Bar Graphs",
                "content": "This chapter covers stacked bar graphs as part of the Bar Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of stacked bar graphs thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Bar Graphs concepts"],
                "examples": [{"question": "Sample placement question on Stacked Bar Graphs", "solution": "Approach: Identify the concept from Stacked Bar Graphs, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Comparative Bar Graph Analysis",
                "content": "This chapter covers comparative bar graph analysis as part of the Bar Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of comparative bar graph analysis thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Bar Graphs concepts"],
                "examples": [{"question": "Sample placement question on Comparative Bar Graph Analysis", "solution": "Approach: Identify the concept from Comparative Bar Graph Analysis, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Types", "explanation": "Simple bar (one series), Grouped bar (multiple series side by side), Stacked bar (components stacked on each other)."}, {"name": "Reading Values", "explanation": "Look at the scale on the axis. Estimate values by position relative to grid lines. Note if scale starts at 0 or is broken."}, {"name": "Comparisons", "explanation": "Height of bar = magnitude. Compare bars for trends (increasing/decreasing). Stacked bars: read component heights individually."}],
        "formulas": ["Height of bar segment = value of that component", "% share = (segment height / total bar height) \u00d7 100"],
        "solved_examples": [{"question": "Strategy for bar graph problems", "solution": "1. Read the title and axis labels. 2. Note the scale. 3. Read the question. 4. Find relevant bars. 5. Estimate values. 6. Calculate answer."}],
        "tips": ["For stacked bars, the component value = top edge - bottom edge of that segment.", "If bars are close in height, use the grid lines for more accurate reading.", "Double-check if the question asks for value or percentage."],
    },
    29: {
        "title": "Pie Charts",
        "overview": "Circular chart divided into sectors representing proportions. Each sector's angle is proportional to its value.",
        "chapters": [
            {
                "title": "Reading Pie Charts \u2014 Angles & Percentages",
                "content": "This chapter covers reading pie charts \u2014 angles & percentages as part of the Pie Charts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of reading pie charts \u2014 angles & percentages thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pie Charts concepts"],
                "examples": [{"question": "Sample placement question on Reading Pie Charts \u2014 Angles & Percentages", "solution": "Approach: Identify the concept from Reading Pie Charts \u2014 Angles & Percentages, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Calculations from Pie Charts",
                "content": "This chapter covers calculations from pie charts as part of the Pie Charts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of calculations from pie charts thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pie Charts concepts"],
                "examples": [{"question": "Sample placement question on Calculations from Pie Charts", "solution": "Approach: Identify the concept from Calculations from Pie Charts, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Comparative Pie Charts",
                "content": "This chapter covers comparative pie charts as part of the Pie Charts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of comparative pie charts thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pie Charts concepts"],
                "examples": [{"question": "Sample placement question on Comparative Pie Charts", "solution": "Approach: Identify the concept from Comparative Pie Charts, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Pie Charts Combined with Tables",
                "content": "This chapter covers pie charts combined with tables as part of the Pie Charts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of pie charts combined with tables thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pie Charts concepts"],
                "examples": [{"question": "Sample placement question on Pie Charts Combined with Tables", "solution": "Approach: Identify the concept from Pie Charts Combined with Tables, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Pie Chart Problems",
                "content": "This chapter covers advanced pie chart problems as part of the Pie Charts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced pie chart problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pie Charts concepts"],
                "examples": [{"question": "Sample placement question on Advanced Pie Chart Problems", "solution": "Approach: Identify the concept from Advanced Pie Chart Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Angle-Value Relationship", "explanation": "Total angle = 360\u00b0. If a sector is 25% of total, its angle = 0.25 \u00d7 360\u00b0 = 90\u00b0. Value = (angle/360) \u00d7 total."}, {"name": "Multiple Pie Charts", "explanation": "When comparing two pie charts, note the TOTAL values \u2014 percentages can be misleading if totals differ."}, {"name": "Calculations", "explanation": "% share = (sector value / total) \u00d7 100. Actual value = (% / 100) \u00d7 total amount."}],
        "formulas": ["Sector angle = (value / total) \u00d7 360\u00b0", "Value = (angle / 360\u00b0) \u00d7 total", "Percentage = (sector angle / 360\u00b0) \u00d7 100"],
        "solved_examples": [{"question": "A pie chart shows expenses. Food=120\u00b0, Rent=90\u00b0, Transport=60\u00b0, Others=90\u00b0. If total is \u20b936000, find food expense.", "solution": "Food = (120/360) \u00d7 36000 = \u20b912000."}],
        "tips": ["Convert angles to percentages for easier calculation: 36\u00b0 = 10%.", "When comparing two pies with different totals, convert to actual values first.", "Common angles: 90\u00b0=25%, 72\u00b0=20%, 60\u00b0=16.67%, 45\u00b0=12.5%, 36\u00b0=10%."],
    },
    30: {
        "title": "Line Graphs",
        "overview": "Data shown as points connected by lines, typically showing trends over time. Identify patterns, peaks, and rates of change.",
        "chapters": [
            {
                "title": "Reading Line Graphs",
                "content": "This chapter covers reading line graphs as part of the Line Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of reading line graphs thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Line Graphs concepts"],
                "examples": [{"question": "Sample placement question on Reading Line Graphs", "solution": "Approach: Identify the concept from Reading Line Graphs, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Trends, Slopes & Rate of Change",
                "content": "This chapter covers trends, slopes & rate of change as part of the Line Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of trends, slopes & rate of change thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Line Graphs concepts"],
                "examples": [{"question": "Sample placement question on Trends, Slopes & Rate of Change", "solution": "Approach: Identify the concept from Trends, Slopes & Rate of Change, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Multiple Line Comparison",
                "content": "This chapter covers multiple line comparison as part of the Line Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of multiple line comparison thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Line Graphs concepts"],
                "examples": [{"question": "Sample placement question on Multiple Line Comparison", "solution": "Approach: Identify the concept from Multiple Line Comparison, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Combined Chart Interpretation",
                "content": "This chapter covers combined chart interpretation as part of the Line Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of combined chart interpretation thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Line Graphs concepts"],
                "examples": [{"question": "Sample placement question on Combined Chart Interpretation", "solution": "Approach: Identify the concept from Combined Chart Interpretation, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Advanced Line Graph Problems",
                "content": "This chapter covers advanced line graph problems as part of the Line Graphs topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of advanced line graph problems thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Line Graphs concepts"],
                "examples": [{"question": "Sample placement question on Advanced Line Graph Problems", "solution": "Approach: Identify the concept from Advanced Line Graph Problems, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Trend Analysis", "explanation": "Upward slope = increasing trend. Downward = decreasing. Steeper slope = faster change. Flat = stable."}, {"name": "Rate of Change", "explanation": "Change between two points = y2 - y1. Rate = (y2-y1)/(x2-x1). Steepest segment has highest rate."}, {"name": "Multiple Lines", "explanation": "Compare multiple series on the same graph. Intersection = values are equal at that point. Gap between lines = difference."}],
        "formulas": ["Rate of change = (y\u2082 - y\u2081) / (x\u2082 - x\u2081)", "% change = ((y\u2082 - y\u2081) / y\u2081) \u00d7 100"],
        "solved_examples": [{"question": "How to find the year with maximum growth from a line graph?", "solution": "Look for the steepest upward segment. Calculate % change for each consecutive pair and compare."}],
        "tips": ["Steepness = rate of change. The steeper the line, the faster the change.", "Don't confuse 'highest value' with 'highest growth rate'.", "For 'approximately' questions, estimation is acceptable."],
    },
    31: {
        "title": "C Basics",
        "overview": "Fundamentals of C programming: syntax, data types, input/output, and basic program structure.",
        "chapters": [
            {
                "title": "Variables, Constants & Data Types in C",
                "content": "This chapter covers variables, constants & data types in c as part of the C Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of variables, constants & data types in c thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other C Basics concepts"],
                "examples": [{"question": "Sample placement question on Variables, Constants & Data Types in C", "solution": "Approach: Identify the concept from Variables, Constants & Data Types in C, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Operators & Expressions",
                "content": "This chapter covers operators & expressions as part of the C Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of operators & expressions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other C Basics concepts"],
                "examples": [{"question": "Sample placement question on Operators & Expressions", "solution": "Approach: Identify the concept from Operators & Expressions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Control Flow \u2014 if, else, switch",
                "content": "This chapter covers control flow \u2014 if, else, switch as part of the C Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of control flow \u2014 if, else, switch thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other C Basics concepts"],
                "examples": [{"question": "Sample placement question on Control Flow \u2014 if, else, switch", "solution": "Approach: Identify the concept from Control Flow \u2014 if, else, switch, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Functions & Scope",
                "content": "This chapter covers functions & scope as part of the C Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of functions & scope thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other C Basics concepts"],
                "examples": [{"question": "Sample placement question on Functions & Scope", "solution": "Approach: Identify the concept from Functions & Scope, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Arrays, Pointers & Memory",
                "content": "This chapter covers arrays, pointers & memory as part of the C Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of arrays, pointers & memory thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other C Basics concepts"],
                "examples": [{"question": "Sample placement question on Arrays, Pointers & Memory", "solution": "Approach: Identify the concept from Arrays, Pointers & Memory, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Program Structure", "explanation": "#include <stdio.h> for I/O. main() is the entry point. Statements end with semicolons. Blocks enclosed in {}."}, {"name": "Variables & Data Types", "explanation": "int (4 bytes), float (4 bytes), double (8 bytes), char (1 byte). Declare before use: int x = 5;"}, {"name": "Input/Output", "explanation": "printf() for output: printf(\"%d\", x); scanf() for input: scanf(\"%d\", &x); Format specifiers: %d (int), %f (float), %c (char), %s (string)."}, {"name": "Operators", "explanation": "Arithmetic: + - * / %. Relational: == != < > <= >=. Logical: && || !. Assignment: = += -= *= /=."}],
        "formulas": ["sizeof(int) = 4 bytes (typically)", "sizeof(char) = 1 byte (always)", "sizeof(float) = 4 bytes", "sizeof(double) = 8 bytes"],
        "solved_examples": [{"question": "What is output of: printf(\"%d\", 5/2);", "solution": "Integer division: 5/2 = 2 (truncated). Output: 2."}, {"question": "What is output of: int x=5; printf(\"%d\", x++);", "solution": "Post-increment: prints current value first, then increments. Output: 5 (x becomes 6 after)."}],
        "tips": ["Operator precedence: *, /, % before +, -.", "Integer division truncates: 7/2=3, not 3.5.", "& in scanf is required for non-array variables \u2014 forgetting it causes runtime errors."],
    },
    32: {
        "title": "Data Types & Operators",
        "overview": "Deep dive into data types, type conversion, bitwise operators, and operator precedence in C/C++.",
        "chapters": [
            {
                "title": "Primitive Data Types & Sizes",
                "content": "This chapter covers primitive data types & sizes as part of the Data Types & Operators topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of primitive data types & sizes thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Types & Operators concepts"],
                "examples": [{"question": "Sample placement question on Primitive Data Types & Sizes", "solution": "Approach: Identify the concept from Primitive Data Types & Sizes, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Type Casting \u2014 Implicit & Explicit",
                "content": "This chapter covers type casting \u2014 implicit & explicit as part of the Data Types & Operators topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of type casting \u2014 implicit & explicit thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Types & Operators concepts"],
                "examples": [{"question": "Sample placement question on Type Casting \u2014 Implicit & Explicit", "solution": "Approach: Identify the concept from Type Casting \u2014 Implicit & Explicit, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Arithmetic & Relational Operators",
                "content": "This chapter covers arithmetic & relational operators as part of the Data Types & Operators topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of arithmetic & relational operators thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Types & Operators concepts"],
                "examples": [{"question": "Sample placement question on Arithmetic & Relational Operators", "solution": "Approach: Identify the concept from Arithmetic & Relational Operators, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Logical & Bitwise Operators",
                "content": "This chapter covers logical & bitwise operators as part of the Data Types & Operators topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of logical & bitwise operators thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Types & Operators concepts"],
                "examples": [{"question": "Sample placement question on Logical & Bitwise Operators", "solution": "Approach: Identify the concept from Logical & Bitwise Operators, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Operator Precedence & Associativity",
                "content": "This chapter covers operator precedence & associativity as part of the Data Types & Operators topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of operator precedence & associativity thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Types & Operators concepts"],
                "examples": [{"question": "Sample placement question on Operator Precedence & Associativity", "solution": "Approach: Identify the concept from Operator Precedence & Associativity, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Type Conversion", "explanation": "Implicit: smaller type auto-converts to larger (int \u2192 float). Explicit: casting (int)3.7 = 3. Dangerous: large int \u2192 small type causes overflow."}, {"name": "Bitwise Operators", "explanation": "& (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift). Operate on binary representations."}, {"name": "Short-circuit Evaluation", "explanation": "In (A && B): if A is false, B is not evaluated. In (A || B): if A is true, B is not evaluated."}],
        "formulas": ["Left shift: a << n = a \u00d7 2^n", "Right shift: a >> n = a / 2^n (integer division)", "XOR: a ^ a = 0, a ^ 0 = a"],
        "solved_examples": [{"question": "What is 5 & 3?", "solution": "5 = 101, 3 = 011. AND: 001 = 1. Answer: 1."}, {"question": "What is 5 ^ 3?", "solution": "5 = 101, 3 = 011. XOR: 110 = 6. Answer: 6."}],
        "tips": ["XOR is useful: swap without temp (a^=b; b^=a; a^=b;).", "Left shift by 1 = multiply by 2. Right shift by 1 = divide by 2.", "Be careful with signed right shift \u2014 it preserves the sign bit."],
    },
    33: {
        "title": "Control Flow",
        "overview": "if-else, switch, for, while, do-while, break, continue \u2014 control the execution path of your program.",
        "chapters": [
            {
                "title": "if-else & Nested Conditions",
                "content": "This chapter covers if-else & nested conditions as part of the Control Flow topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of if-else & nested conditions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Control Flow concepts"],
                "examples": [{"question": "Sample placement question on if-else & Nested Conditions", "solution": "Approach: Identify the concept from if-else & Nested Conditions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "switch-case Statements",
                "content": "This chapter covers switch-case statements as part of the Control Flow topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of switch-case statements thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Control Flow concepts"],
                "examples": [{"question": "Sample placement question on switch-case Statements", "solution": "Approach: Identify the concept from switch-case Statements, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "for Loop & Variations",
                "content": "This chapter covers for loop & variations as part of the Control Flow topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of for loop & variations thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Control Flow concepts"],
                "examples": [{"question": "Sample placement question on for Loop & Variations", "solution": "Approach: Identify the concept from for Loop & Variations, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "while & do-while Loops",
                "content": "This chapter covers while & do-while loops as part of the Control Flow topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of while & do-while loops thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Control Flow concepts"],
                "examples": [{"question": "Sample placement question on while & do-while Loops", "solution": "Approach: Identify the concept from while & do-while Loops, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "break, continue & Nested Loops",
                "content": "This chapter covers break, continue & nested loops as part of the Control Flow topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of break, continue & nested loops thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Control Flow concepts"],
                "examples": [{"question": "Sample placement question on break, continue & Nested Loops", "solution": "Approach: Identify the concept from break, continue & Nested Loops, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Conditional Statements", "explanation": "if(condition){...} else{...}. Nested if-else for multiple conditions. switch-case for discrete values."}, {"name": "Loops", "explanation": "for(init; condition; update): known iterations. while(condition): unknown iterations, check first. do-while: executes at least once."}, {"name": "Break & Continue", "explanation": "break: exits the innermost loop. continue: skips remaining body, goes to next iteration. goto: jumps to label (avoid using)."}, {"name": "Nested Loops", "explanation": "Loop inside a loop. Inner loop completes all iterations for each iteration of outer loop. Total iterations = outer \u00d7 inner."}],
        "formulas": ["for loop runs: (end - start) / step times", "Nested loop iterations = outer_count \u00d7 inner_count"],
        "solved_examples": [{"question": "What is the output? for(int i=0; i<5; i++) { if(i==3) break; printf(\"%d \", i); }", "solution": "Output: 0 1 2 (loop breaks when i reaches 3)."}, {"question": "How many times does the inner loop run? for(int i=0;i<3;i++) for(int j=0;j<4;j++) ...", "solution": "Outer runs 3 times, inner runs 4 times each = 3 \u00d7 4 = 12 total iterations."}],
        "tips": ["Off-by-one errors: i<n runs n times, i<=n runs n+1 times.", "Infinite loop: while(1) or for(;;) \u2014 use break to exit.", "switch needs break after each case, otherwise it 'falls through'."],
    },
    34: {
        "title": "Arrays & Strings",
        "overview": "Arrays store multiple values of same type. Strings are character arrays terminated by '\\0'. Fundamental data structures.",
        "chapters": [
            {
                "title": "1D Arrays \u2014 Declaration & Traversal",
                "content": "This chapter covers 1d arrays \u2014 declaration & traversal as part of the Arrays & Strings topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of 1d arrays \u2014 declaration & traversal thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Arrays & Strings concepts"],
                "examples": [{"question": "Sample placement question on 1D Arrays \u2014 Declaration & Traversal", "solution": "Approach: Identify the concept from 1D Arrays \u2014 Declaration & Traversal, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "2D Arrays & Matrix Operations",
                "content": "This chapter covers 2d arrays & matrix operations as part of the Arrays & Strings topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of 2d arrays & matrix operations thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Arrays & Strings concepts"],
                "examples": [{"question": "Sample placement question on 2D Arrays & Matrix Operations", "solution": "Approach: Identify the concept from 2D Arrays & Matrix Operations, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "String Basics & Operations",
                "content": "This chapter covers string basics & operations as part of the Arrays & Strings topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of string basics & operations thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Arrays & Strings concepts"],
                "examples": [{"question": "Sample placement question on String Basics & Operations", "solution": "Approach: Identify the concept from String Basics & Operations, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "String Library Functions",
                "content": "This chapter covers string library functions as part of the Arrays & Strings topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of string library functions thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Arrays & Strings concepts"],
                "examples": [{"question": "Sample placement question on String Library Functions", "solution": "Approach: Identify the concept from String Library Functions, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Array & String Problem Solving",
                "content": "This chapter covers array & string problem solving as part of the Arrays & Strings topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of array & string problem solving thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Arrays & Strings concepts"],
                "examples": [{"question": "Sample placement question on Array & String Problem Solving", "solution": "Approach: Identify the concept from Array & String Problem Solving, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Arrays", "explanation": "Declaration: int arr[5]; Indexing starts at 0. arr[0] is first element, arr[4] is last. Size = sizeof(arr)/sizeof(arr[0])."}, {"name": "2D Arrays", "explanation": "int matrix[3][4]; Rows \u00d7 Columns. Access: matrix[i][j]. Stored in row-major order in C."}, {"name": "Strings in C", "explanation": "char str[] = \"hello\"; Ends with \\0 (null terminator). strlen() gives length (excludes \\0). strcmp() compares strings."}, {"name": "String Functions", "explanation": "strlen(s), strcpy(dest,src), strcat(dest,src), strcmp(s1,s2) returns 0 if equal. Include <string.h>."}],
        "formulas": ["Array size in bytes = number_of_elements \u00d7 sizeof(element_type)", "String length = number of characters before \\0", "2D array element address = base + (i \u00d7 cols + j) \u00d7 sizeof(type)"],
        "solved_examples": [{"question": "What is sizeof(\"Hello\")?", "solution": "5 characters + 1 null terminator = 6 bytes."}, {"question": "int a[5] = {1,2,3}; What is a[3]?", "solution": "Uninitialized remaining elements default to 0. a[3] = 0."}],
        "tips": ["Arrays don't check bounds in C \u2014 accessing out of bounds is undefined behavior.", "Strings must have space for \\0: char s[6] for 5-char string.", "Use strncpy instead of strcpy to prevent buffer overflow."],
    },
    35: {
        "title": "Pointers & References",
        "overview": "Pointers store memory addresses. They're powerful but tricky \u2014 essential for understanding dynamic memory and data structures.",
        "chapters": [
            {
                "title": "Pointer Basics \u2014 Declaration & Dereferencing",
                "content": "This chapter covers pointer basics \u2014 declaration & dereferencing as part of the Pointers & References topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of pointer basics \u2014 declaration & dereferencing thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pointers & References concepts"],
                "examples": [{"question": "Sample placement question on Pointer Basics \u2014 Declaration & Dereferencing", "solution": "Approach: Identify the concept from Pointer Basics \u2014 Declaration & Dereferencing, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Pointer Arithmetic",
                "content": "This chapter covers pointer arithmetic as part of the Pointers & References topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of pointer arithmetic thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pointers & References concepts"],
                "examples": [{"question": "Sample placement question on Pointer Arithmetic", "solution": "Approach: Identify the concept from Pointer Arithmetic, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Pointers & Arrays Relationship",
                "content": "This chapter covers pointers & arrays relationship as part of the Pointers & References topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of pointers & arrays relationship thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pointers & References concepts"],
                "examples": [{"question": "Sample placement question on Pointers & Arrays Relationship", "solution": "Approach: Identify the concept from Pointers & Arrays Relationship, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Dynamic Memory \u2014 malloc, calloc, free",
                "content": "This chapter covers dynamic memory \u2014 malloc, calloc, free as part of the Pointers & References topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of dynamic memory \u2014 malloc, calloc, free thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pointers & References concepts"],
                "examples": [{"question": "Sample placement question on Dynamic Memory \u2014 malloc, calloc, free", "solution": "Approach: Identify the concept from Dynamic Memory \u2014 malloc, calloc, free, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Common Pointer Pitfalls",
                "content": "This chapter covers common pointer pitfalls as part of the Pointers & References topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of common pointer pitfalls thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Pointers & References concepts"],
                "examples": [{"question": "Sample placement question on Common Pointer Pitfalls", "solution": "Approach: Identify the concept from Common Pointer Pitfalls, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Pointer Basics", "explanation": "int *p; declares pointer to int. p = &x; stores address of x. *p dereferences (accesses value at address). & is address-of operator."}, {"name": "Pointer Arithmetic", "explanation": "p++ moves to next element (adds sizeof(type) bytes). p+n moves n elements forward. Array name is a pointer to first element."}, {"name": "Pointers & Arrays", "explanation": "arr[i] = *(arr+i). Array name is a constant pointer. &arr[0] == arr."}, {"name": "Double Pointers", "explanation": "int **pp; Pointer to a pointer. Used for 2D dynamic arrays and modifying pointers in functions."}],
        "formulas": ["ptr + n advances by n \u00d7 sizeof(*ptr) bytes", "arr[i] is equivalent to *(arr + i)", "&arr[i] is equivalent to (arr + i)"],
        "solved_examples": [{"question": "int x=10, *p=&x; What is *p?", "solution": "*p dereferences p \u2192 gives value at address of x \u2192 10."}, {"question": "int a[]={10,20,30}; int *p=a; What is *(p+2)?", "solution": "p points to a[0]. p+2 points to a[2]. *(p+2) = 30."}],
        "tips": ["NULL pointer: always initialize pointers (int *p = NULL;).", "Dangling pointer: don't use pointer after freeing memory.", "Pointer to pointer (**pp) is needed when a function must modify the pointer itself."],
    },
    36: {
        "title": "OOP Concepts",
        "overview": "Object-Oriented Programming: classes, objects, inheritance, polymorphism, encapsulation, and abstraction.",
        "chapters": [
            {
                "title": "Classes, Objects & Constructors",
                "content": "This chapter covers classes, objects & constructors as part of the OOP Concepts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of classes, objects & constructors thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other OOP Concepts concepts"],
                "examples": [{"question": "Sample placement question on Classes, Objects & Constructors", "solution": "Approach: Identify the concept from Classes, Objects & Constructors, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Inheritance \u2014 Types & Usage",
                "content": "This chapter covers inheritance \u2014 types & usage as part of the OOP Concepts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of inheritance \u2014 types & usage thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other OOP Concepts concepts"],
                "examples": [{"question": "Sample placement question on Inheritance \u2014 Types & Usage", "solution": "Approach: Identify the concept from Inheritance \u2014 Types & Usage, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Polymorphism \u2014 Overloading & Overriding",
                "content": "This chapter covers polymorphism \u2014 overloading & overriding as part of the OOP Concepts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of polymorphism \u2014 overloading & overriding thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other OOP Concepts concepts"],
                "examples": [{"question": "Sample placement question on Polymorphism \u2014 Overloading & Overriding", "solution": "Approach: Identify the concept from Polymorphism \u2014 Overloading & Overriding, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Encapsulation & Abstraction",
                "content": "This chapter covers encapsulation & abstraction as part of the OOP Concepts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of encapsulation & abstraction thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other OOP Concepts concepts"],
                "examples": [{"question": "Sample placement question on Encapsulation & Abstraction", "solution": "Approach: Identify the concept from Encapsulation & Abstraction, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "SOLID Principles & Design Patterns Intro",
                "content": "This chapter covers solid principles & design patterns intro as part of the OOP Concepts topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of solid principles & design patterns intro thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other OOP Concepts concepts"],
                "examples": [{"question": "Sample placement question on SOLID Principles & Design Patterns Intro", "solution": "Approach: Identify the concept from SOLID Principles & Design Patterns Intro, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Classes & Objects", "explanation": "Class is a blueprint. Object is an instance. Class has data members (attributes) and member functions (methods)."}, {"name": "Encapsulation", "explanation": "Bundling data and methods together. Access modifiers: private (class only), protected (class + derived), public (everyone)."}, {"name": "Inheritance", "explanation": "Derived class inherits from base class. Types: single, multiple, multilevel, hierarchical, hybrid. 'is-a' relationship."}, {"name": "Polymorphism", "explanation": "Same interface, different behavior. Compile-time: function overloading, operator overloading. Runtime: virtual functions, function overriding."}],
        "formulas": [],
        "solved_examples": [{"question": "What is the difference between overloading and overriding?", "solution": "Overloading: same name, different parameters (compile-time). Overriding: same name & parameters in derived class (runtime). Overriding requires inheritance."}, {"question": "What is an abstract class?", "solution": "A class with at least one pure virtual function (=0). Cannot be instantiated. Must be inherited and the pure virtual function must be implemented."}],
        "tips": ["Remember: Encapsulation=data hiding, Abstraction=complexity hiding.", "Virtual functions enable runtime polymorphism via vtable.", "Multiple inheritance can cause the diamond problem \u2014 use virtual inheritance."],
    },
    37: {
        "title": "Data Structures",
        "overview": "Organize and store data efficiently. Stacks, queues, linked lists, trees, and hash tables \u2014 each with different trade-offs.",
        "chapters": [
            {
                "title": "Stacks & Queues",
                "content": "This chapter covers stacks & queues as part of the Data Structures topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of stacks & queues thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Structures concepts"],
                "examples": [{"question": "Sample placement question on Stacks & Queues", "solution": "Approach: Identify the concept from Stacks & Queues, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Linked Lists \u2014 Singly, Doubly, Circular",
                "content": "This chapter covers linked lists \u2014 singly, doubly, circular as part of the Data Structures topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of linked lists \u2014 singly, doubly, circular thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Structures concepts"],
                "examples": [{"question": "Sample placement question on Linked Lists \u2014 Singly, Doubly, Circular", "solution": "Approach: Identify the concept from Linked Lists \u2014 Singly, Doubly, Circular, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Trees \u2014 Binary, BST, Traversals",
                "content": "This chapter covers trees \u2014 binary, bst, traversals as part of the Data Structures topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of trees \u2014 binary, bst, traversals thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Structures concepts"],
                "examples": [{"question": "Sample placement question on Trees \u2014 Binary, BST, Traversals", "solution": "Approach: Identify the concept from Trees \u2014 Binary, BST, Traversals, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Graphs \u2014 BFS, DFS, Representation",
                "content": "This chapter covers graphs \u2014 bfs, dfs, representation as part of the Data Structures topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of graphs \u2014 bfs, dfs, representation thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Structures concepts"],
                "examples": [{"question": "Sample placement question on Graphs \u2014 BFS, DFS, Representation", "solution": "Approach: Identify the concept from Graphs \u2014 BFS, DFS, Representation, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Hashing & Hash Tables",
                "content": "This chapter covers hashing & hash tables as part of the Data Structures topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of hashing & hash tables thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Data Structures concepts"],
                "examples": [{"question": "Sample placement question on Hashing & Hash Tables", "solution": "Approach: Identify the concept from Hashing & Hash Tables, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Stack", "explanation": "LIFO (Last In First Out). Operations: push, pop, peek. Applications: function calls, undo, expression evaluation. O(1) for all operations."}, {"name": "Queue", "explanation": "FIFO (First In First Out). Operations: enqueue, dequeue, front. Applications: BFS, scheduling, buffers. O(1) for all operations."}, {"name": "Linked List", "explanation": "Nodes connected by pointers. Singly (next), Doubly (prev+next), Circular. Insertion/deletion O(1) at known position, search O(n)."}, {"name": "Trees", "explanation": "Hierarchical structure. Binary tree: max 2 children. BST: left < parent < right. Operations: insert, search, delete \u2014 O(log n) average for BST."}],
        "formulas": ["Array access: O(1)", "Linked list search: O(n)", "BST operations: O(log n) average, O(n) worst", "Hash table: O(1) average for insert/search/delete"],
        "solved_examples": [{"question": "Evaluate postfix: 2 3 + 4 *", "solution": "Stack: push 2, push 3. '+': pop 3,2 \u2192 push 5. Push 4. '*': pop 4,5 \u2192 push 20. Answer: 20."}, {"question": "Inorder traversal of BST gives?", "solution": "Sorted order! Inorder (Left-Root-Right) of BST always gives ascending order."}],
        "tips": ["Choose data structure based on most frequent operation.", "Stack for LIFO, Queue for FIFO \u2014 don't mix them up.", "BST degenerates to linked list if insertions are sorted \u2014 use balanced BST."],
    },
    38: {
        "title": "Algorithms Basics",
        "overview": "Fundamental algorithms: searching, sorting, and time complexity analysis. The foundation of efficient programming.",
        "chapters": [
            {
                "title": "Sorting \u2014 Bubble, Selection, Insertion, Merge, Quick",
                "content": "This chapter covers sorting \u2014 bubble, selection, insertion, merge, quick as part of the Algorithms Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of sorting \u2014 bubble, selection, insertion, merge, quick thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Algorithms Basics concepts"],
                "examples": [{"question": "Sample placement question on Sorting \u2014 Bubble, Selection, Insertion, Merge, Quick", "solution": "Approach: Identify the concept from Sorting \u2014 Bubble, Selection, Insertion, Merge, Quick, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Searching \u2014 Linear, Binary & Variants",
                "content": "This chapter covers searching \u2014 linear, binary & variants as part of the Algorithms Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of searching \u2014 linear, binary & variants thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Algorithms Basics concepts"],
                "examples": [{"question": "Sample placement question on Searching \u2014 Linear, Binary & Variants", "solution": "Approach: Identify the concept from Searching \u2014 Linear, Binary & Variants, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Recursion & Backtracking",
                "content": "This chapter covers recursion & backtracking as part of the Algorithms Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of recursion & backtracking thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Algorithms Basics concepts"],
                "examples": [{"question": "Sample placement question on Recursion & Backtracking", "solution": "Approach: Identify the concept from Recursion & Backtracking, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Time & Space Complexity (Big-O)",
                "content": "This chapter covers time & space complexity (big-o) as part of the Algorithms Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of time & space complexity (big-o) thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Algorithms Basics concepts"],
                "examples": [{"question": "Sample placement question on Time & Space Complexity (Big-O)", "solution": "Approach: Identify the concept from Time & Space Complexity (Big-O), apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Greedy Algorithms & Dynamic Programming Intro",
                "content": "This chapter covers greedy algorithms & dynamic programming intro as part of the Algorithms Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of greedy algorithms & dynamic programming intro thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other Algorithms Basics concepts"],
                "examples": [{"question": "Sample placement question on Greedy Algorithms & Dynamic Programming Intro", "solution": "Approach: Identify the concept from Greedy Algorithms & Dynamic Programming Intro, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Time Complexity", "explanation": "Big-O notation: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n\u00b2) quadratic, O(2^n) exponential."}, {"name": "Sorting Algorithms", "explanation": "Bubble sort: O(n\u00b2). Selection sort: O(n\u00b2). Merge sort: O(n log n). Quick sort: O(n log n) avg, O(n\u00b2) worst. Heap sort: O(n log n)."}, {"name": "Searching", "explanation": "Linear search: O(n), works on unsorted. Binary search: O(log n), requires sorted array. Divide and conquer approach."}, {"name": "Recursion", "explanation": "Function calls itself. Must have base case (stops recursion) and recursive case (reduces problem). Stack overflow if no base case."}],
        "formulas": ["Binary search: O(log\u2082 n)", "Merge sort: O(n log n) always", "Quick sort: O(n log n) average, O(n\u00b2) worst", "Fibonacci naive recursion: O(2^n)"],
        "solved_examples": [{"question": "Binary search for 7 in [1,3,5,7,9,11]: trace steps.", "solution": "Step 1: mid=5, 7>5 \u2192 search right [7,9,11]. Step 2: mid=9, 7<9 \u2192 search left [7]. Step 3: mid=7, found! 3 comparisons."}, {"question": "What is time complexity of: for(i=1; i<=n; i*=2) ...?", "solution": "i goes: 1, 2, 4, 8... 2^k = n \u2192 k = log\u2082n. Time: O(log n)."}],
        "tips": ["Know the complexities of all major sorting algorithms.", "Binary search only works on sorted data.", "For recursion: always identify the base case first, then the recursive relation."],
    },
    39: {
        "title": "SQL Basics",
        "overview": "Structured Query Language for database operations. SELECT, INSERT, UPDATE, DELETE, JOINs, and aggregate functions.",
        "chapters": [
            {
                "title": "SELECT, WHERE & Basic Queries",
                "content": "This chapter covers select, where & basic queries as part of the SQL Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of select, where & basic queries thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other SQL Basics concepts"],
                "examples": [{"question": "Sample placement question on SELECT, WHERE & Basic Queries", "solution": "Approach: Identify the concept from SELECT, WHERE & Basic Queries, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "JOINs \u2014 INNER, LEFT, RIGHT, FULL",
                "content": "This chapter covers joins \u2014 inner, left, right, full as part of the SQL Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of joins \u2014 inner, left, right, full thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other SQL Basics concepts"],
                "examples": [{"question": "Sample placement question on JOINs \u2014 INNER, LEFT, RIGHT, FULL", "solution": "Approach: Identify the concept from JOINs \u2014 INNER, LEFT, RIGHT, FULL, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "GROUP BY, HAVING & Aggregation",
                "content": "This chapter covers group by, having & aggregation as part of the SQL Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of group by, having & aggregation thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other SQL Basics concepts"],
                "examples": [{"question": "Sample placement question on GROUP BY, HAVING & Aggregation", "solution": "Approach: Identify the concept from GROUP BY, HAVING & Aggregation, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "Subqueries & Nested Queries",
                "content": "This chapter covers subqueries & nested queries as part of the SQL Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of subqueries & nested queries thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other SQL Basics concepts"],
                "examples": [{"question": "Sample placement question on Subqueries & Nested Queries", "solution": "Approach: Identify the concept from Subqueries & Nested Queries, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
            {
                "title": "DDL, DML & Database Design Basics",
                "content": "This chapter covers ddl, dml & database design basics as part of the SQL Basics topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
                "key_points": ["Understand the fundamentals of ddl, dml & database design basics thoroughly", "Practice with placement-style MCQs from IndiaBix and GFG", "Time yourself \u2014 most exams give 1-2 minutes per question", "Review solved examples to understand the approach", "Connect this with other SQL Basics concepts"],
                "examples": [{"question": "Sample placement question on DDL, DML & Database Design Basics", "solution": "Approach: Identify the concept from DDL, DML & Database Design Basics, apply the relevant formula or logic, and verify your answer by substitution."}],
            },
        ],
        "key_concepts": [{"name": "Basic Queries", "explanation": "SELECT columns FROM table WHERE condition ORDER BY column. Use * for all columns. WHERE filters rows."}, {"name": "Aggregate Functions", "explanation": "COUNT(), SUM(), AVG(), MIN(), MAX(). Used with GROUP BY. HAVING filters groups (like WHERE for groups)."}, {"name": "JOINs", "explanation": "INNER JOIN: matching rows from both tables. LEFT JOIN: all from left + matching from right. RIGHT JOIN: all from right + matching from left. CROSS JOIN: cartesian product."}, {"name": "Subqueries", "explanation": "Query within a query. Can be in SELECT, FROM, or WHERE clause. Correlated subquery: references outer query."}],
        "formulas": ["SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ...", "INSERT INTO table (cols) VALUES (vals)", "UPDATE table SET col=val WHERE condition", "DELETE FROM table WHERE condition"],
        "solved_examples": [{"question": "Find employees with salary above average.", "solution": "SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);"}, {"question": "Count employees per department.", "solution": "SELECT department, COUNT(*) as count FROM employees GROUP BY department ORDER BY count DESC;"}],
        "tips": ["WHERE filters before GROUP BY. HAVING filters after GROUP BY.", "Always use WHERE with UPDATE/DELETE \u2014 without it, you affect ALL rows.", "NULL comparisons use IS NULL / IS NOT NULL, not = or !=."],
    },
    # === DSA DEEP DIVE (Topics 40-51) ===
    40: {
        "title": "Arrays & Matrices",
        "overview": "Arrays are the most fundamental data structure and appear in nearly every coding round. This topic covers array traversal, prefix sums, Kadane's algorithm, matrix operations, rotation techniques, and subarray problems that are staples of Amazon, Microsoft, and TCS NQT exams.",
        "chapters": [
            {
                "title": "Array Fundamentals & Traversal Techniques",
                "content": "An array is a contiguous block of memory storing elements of the same type, accessed by index in O(1) time.\n\nDeclaration and Initialization:\n  int arr[5] = {10, 20, 30, 40, 50};\n  # Python: arr = [10, 20, 30, 40, 50]\n\nTraversal Patterns:\n1) Linear scan: Visit each element once. O(n).\n2) Two-pointer technique: Use left and right pointers moving toward each other. Useful for sorted arrays, pair-sum problems.\n3) Sliding window: Maintain a window of size k, slide it across the array to compute running sums or maximums.\n\nTwo-Pointer Example (pair with given sum S in sorted array):\n  left, right = 0, n-1\n  while left < right:\n      curr = arr[left] + arr[right]\n      if curr == S: return (left, right)\n      elif curr < S: left += 1\n      else: right -= 1\n\nSliding Window Example (max sum subarray of size k):\n  window_sum = sum(arr[:k])\n  max_sum = window_sum\n  for i in range(k, n):\n      window_sum += arr[i] - arr[i-k]\n      max_sum = max(max_sum, window_sum)\n\nTime Complexity: O(n) for single traversal, O(n log n) if sorting is needed first.\nSpace Complexity: O(1) extra for in-place techniques.",
                "key_points": [
                    "Array access is O(1) but insertion/deletion at arbitrary index is O(n)",
                    "Two-pointer works only on sorted arrays for pair-sum; sort first if unsorted",
                    "Sliding window converts O(n*k) brute force to O(n)",
                    "Always consider edge cases: empty array, single element, all same elements",
                    "TCS NQT frequently tests basic traversal and two-pointer patterns"
                ],
                "examples": [
                    {"question": "Find two numbers in a sorted array that sum to 15: [1, 3, 5, 7, 8, 10, 12]", "solution": "Use two pointers: left=0 (val 1), right=6 (val 12). 1+12=13<15, move left. 3+12=15. Found pair (3,12) at indices 1 and 6."},
                    {"question": "Find maximum sum of any 3 consecutive elements in [2, 1, 5, 1, 3, 2]", "solution": "Sliding window of size 3: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6. Maximum = 9."},
                    {"question": "Reverse an array in-place: [1, 2, 3, 4, 5]", "solution": "Two pointers: swap arr[0] and arr[4] -> [5,2,3,4,1], swap arr[1] and arr[3] -> [5,4,3,2,1]. O(n) time, O(1) space."}
                ],
            },
            {
                "title": "Prefix Sum & Difference Array",
                "content": "Prefix sum is a preprocessing technique that allows range-sum queries in O(1) after O(n) preprocessing.\n\nBuilding prefix sum array:\n  prefix[0] = arr[0]\n  for i in range(1, n):\n      prefix[i] = prefix[i-1] + arr[i]\n\nRange sum query: sum(arr[l..r]) = prefix[r] - prefix[l-1]  (handle l=0 edge case)\n\nExample: arr = [3, 1, 4, 1, 5, 9]\nprefix = [3, 4, 8, 9, 14, 23]\nSum of arr[2..4] = prefix[4] - prefix[1] = 14 - 4 = 10\nVerify: 4 + 1 + 5 = 10. Correct.\n\nDifference Array Technique (for range update queries):\nTo add val to all elements from index l to r:\n  diff[l] += val\n  diff[r+1] -= val  (if r+1 < n)\nThen reconstruct: arr[i] = sum(diff[0..i])\n\nThis converts O(n) per update to O(1) per update, with one O(n) reconstruction pass.\n\n2D Prefix Sum for Matrices:\n  prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]\nSubmatrix sum from (r1,c1) to (r2,c2):\n  = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]",
                "key_points": [
                    "Prefix sum converts O(n) range queries to O(1) after O(n) preprocessing",
                    "Difference array is the inverse: optimizes range updates",
                    "2D prefix sums are asked in Amazon and Microsoft interviews",
                    "Watch for integer overflow in prefix sums of large arrays",
                    "Prefix XOR works similarly for XOR range queries"
                ],
                "examples": [
                    {"question": "Given arr = [1, 2, 3, 4, 5], find sum of elements from index 1 to 3.", "solution": "Build prefix = [1, 3, 6, 10, 15]. Sum(1..3) = prefix[3] - prefix[0] = 10 - 1 = 9. Verify: 2+3+4 = 9."},
                    {"question": "Apply +5 to indices 1-3 and +3 to indices 2-4 in arr = [0,0,0,0,0]. Use difference array.", "solution": "diff = [0,0,0,0,0]. After +5 to [1,3]: diff = [0,5,0,0,-5]. After +3 to [2,4]: diff = [0,5,3,0,-5]. Reconstruct: [0,5,8,8,3]."},
                    {"question": "Count subarrays with sum equal to k=3 in [1,1,1,2,3].", "solution": "Use prefix sum + hashmap. Track prefix sums and count how many times (prefix[i]-k) appeared before. prefix=[1,2,3,5,8]. At index 2, prefix=3, 3-3=0 found once. Total count = 3 subarrays: [1,1,1], [1,2], [3]."}
                ],
            },
            {
                "title": "Kadane's Algorithm & Subarray Problems",
                "content": "Kadane's Algorithm finds the maximum sum contiguous subarray in O(n) time.\n\nAlgorithm:\n  max_ending_here = max_so_far = arr[0]\n  for i in range(1, n):\n      max_ending_here = max(arr[i], max_ending_here + arr[i])\n      max_so_far = max(max_so_far, max_ending_here)\n  return max_so_far\n\nIntuition: At each position, decide whether to extend the current subarray or start fresh. If the running sum becomes negative, starting fresh is better.\n\nExample: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\nStep through: max_ending_here progresses as: -2, 1, -2, 4, 3, 5, 6, 1, 5\nmax_so_far = 6 (subarray [4, -1, 2, 1])\n\nVariations:\n1) Minimum sum subarray: Negate all elements, apply Kadane's, negate result.\n2) Maximum circular subarray sum: max(kadane(arr), total_sum - min_subarray_sum). Handle edge case where all elements are negative.\n3) Maximum product subarray: Track both max_product and min_product (since negative * negative = positive).\n\nProduct subarray:\n  max_prod = min_prod = result = arr[0]\n  for i in range(1, n):\n      if arr[i] < 0: swap(max_prod, min_prod)\n      max_prod = max(arr[i], max_prod * arr[i])\n      min_prod = min(arr[i], min_prod * arr[i])\n      result = max(result, max_prod)",
                "key_points": [
                    "Kadane's is THE most frequently asked array algorithm in placements",
                    "Time: O(n), Space: O(1) - memorize this complexity",
                    "For circular variant, answer = max(normal_kadane, total_sum - min_subarray)",
                    "Product subarray needs tracking both max and min due to negative numbers",
                    "Amazon, Flipkart, and Microsoft commonly ask Kadane's variations"
                ],
                "examples": [
                    {"question": "Find max subarray sum in [-2, -3, 4, -1, -2, 1, 5, -3]", "solution": "Kadane's: start max_here=-2, then -3, then 4 (restart), 3, 1, 2, 7, 4. max_so_far = 7, subarray [4,-1,-2,1,5]."},
                    {"question": "Find max product subarray in [2, 3, -2, 4]", "solution": "Track max_prod and min_prod. [2]: max=2,min=2. [3]: max=6,min=3. [-2]: swap then max=max(-2,6*-2)= -2, min=min(-2, 3*-2)=-12. Wait, swap first: max=3*-2=-6 vs -2 -> -2, min=6*-2=-12 vs -2 -> -12. [4]: max=max(4,-2*4)=4, min=min(4,-12*4)=-48. Result = max(2,6,-2,4) = 6."},
                    {"question": "Find max circular subarray sum in [8, -1, 3, 4]", "solution": "Normal kadane = 14 (entire array). Total = 14. Min subarray = -1. Circular = 14 - (-1) = 15. But wait - max(14, 15) = 15. The circular subarray is [3, 4, 8] wrapping around."}
                ],
            },
            {
                "title": "Matrix Operations & 2D Array Techniques",
                "content": "A matrix is a 2D array of size m x n. Key operations include traversal, rotation, transposition, and spiral order.\n\nMatrix Transpose:\n  for i in range(n):\n      for j in range(i+1, n):\n          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n\nRotate Matrix 90 degrees clockwise (in-place):\n  Step 1: Transpose the matrix\n  Step 2: Reverse each row\n  # For counter-clockwise: Transpose then reverse each column\n\nSpiral Order Traversal:\n  Use four boundaries: top, bottom, left, right.\n  while top <= bottom and left <= right:\n      Traverse right along top row, top += 1\n      Traverse down along right col, right -= 1\n      Traverse left along bottom row (if top <= bottom), bottom -= 1\n      Traverse up along left col (if left <= right), left += 1\n\nMatrix Multiplication (m x n) * (n x p) = (m x p):\n  for i in range(m):\n      for j in range(p):\n          result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))\n  Time: O(m * n * p)\n\nSearch in Row-wise and Column-wise Sorted Matrix:\n  Start from top-right corner (or bottom-left).\n  If element == target: found\n  If element > target: move left\n  If element < target: move down\n  Time: O(m + n)",
                "key_points": [
                    "Rotate 90 CW = Transpose + Reverse rows. This is a classic interview question.",
                    "Spiral traversal uses four boundary variables - practice until automatic",
                    "Staircase search in sorted matrix is O(m+n), not O(m*n)",
                    "Matrix multiplication: (m x n) * (n x p) requires inner dimensions to match",
                    "Infosys and Wipro frequently ask matrix rotation and spiral traversal"
                ],
                "examples": [
                    {"question": "Rotate [[1,2,3],[4,5,6],[7,8,9]] by 90 degrees clockwise", "solution": "Step 1 Transpose: [[1,4,7],[2,5,8],[3,6,9]]. Step 2 Reverse each row: [[7,4,1],[8,5,2],[9,6,3]]."},
                    {"question": "Print spiral order of [[1,2,3],[4,5,6],[7,8,9]]", "solution": "top=0,bottom=2,left=0,right=2. Right: 1,2,3. Down: 6,9. Left: 8,7. Up: 4. Right: 5. Output: [1,2,3,6,9,8,7,4,5]."},
                    {"question": "Search 14 in row-col sorted matrix [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]", "solution": "Start top-right: 11>14? No. 11<14, go down: 12<14, go down: 16>14, go left: 9<14, go down: 13<14, go right: 14==14. Found at (3,2). Steps: 5."}
                ],
            },
            {
                "title": "Array Rotation & Rearrangement",
                "content": "Array rotation shifts elements cyclically. Rearrangement problems involve reordering elements under constraints.\n\nLeft Rotate by d positions:\nMethod 1 - Reversal Algorithm (O(n) time, O(1) space):\n  reverse(arr, 0, d-1)\n  reverse(arr, d, n-1)\n  reverse(arr, 0, n-1)\nExample: arr = [1,2,3,4,5,6,7], d=2\n  Reverse first 2: [2,1,3,4,5,6,7]\n  Reverse remaining: [2,1,7,6,5,4,3]\n  Reverse all: [3,4,5,6,7,1,2]\n\nMethod 2 - Juggling Algorithm: GCD-based cyclic replacement. O(n) time, O(1) space.\n\nDutch National Flag (3-way partition):\nSort array of 0s, 1s, 2s in single pass:\n  low = mid = 0; high = n-1\n  while mid <= high:\n      if arr[mid] == 0: swap(arr[low], arr[mid]); low++; mid++\n      elif arr[mid] == 1: mid++\n      else: swap(arr[mid], arr[high]); high--\n\nNext Permutation:\n  1. Find largest i such that arr[i] < arr[i+1] (from right)\n  2. Find largest j such that arr[j] > arr[i]\n  3. Swap arr[i] and arr[j]\n  4. Reverse arr[i+1:]\n  If no such i exists, reverse entire array (it was the last permutation).\n\nMove Zeros to End (maintain order):\n  pos = 0\n  for i in range(n):\n      if arr[i] != 0:\n          arr[pos] = arr[i]; pos += 1\n  while pos < n: arr[pos] = 0; pos += 1",
                "key_points": [
                    "Reversal algorithm for rotation is the most elegant O(n)/O(1) solution",
                    "Dutch National Flag is asked by Amazon, Google - know it by heart",
                    "Next permutation is a classic that tests your attention to detail",
                    "Move zeros to end: single pass with write pointer is optimal",
                    "These are common TCS CodeVita and HackerRank screening problems"
                ],
                "examples": [
                    {"question": "Right rotate [1,2,3,4,5] by 2 positions", "solution": "Right rotate by 2 = Left rotate by n-2 = 3. Using reversal: Reverse first 3: [3,2,1,4,5]. Reverse last 2: [3,2,1,5,4]. Reverse all: [4,5,1,2,3]."},
                    {"question": "Sort [0,1,2,0,1,2,0] using Dutch National Flag", "solution": "low=mid=0, high=6. mid=0(val 0): swap, low=1,mid=1. mid=1(val 1): mid=2. mid=2(val 2): swap with high=6(val 0), high=5. Now arr[2]=0: swap, low=2,mid=3. mid=3(val 1): mid=4. mid=4(val 2): swap with high=5(val 2), high=4. mid>high, stop. Result: [0,0,0,1,1,2,2]."},
                    {"question": "Find next permutation of [1,3,5,4,2]", "solution": "Step 1: From right, find i where arr[i]<arr[i+1]: arr[1]=3 < arr[2]=5, so i=1. Step 2: Find j>i where arr[j]>arr[i]: arr[3]=4>3, so j=3. Step 3: Swap: [1,4,5,3,2]. Step 4: Reverse arr[2:]: [1,4,2,3,5]."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Two Pointer Technique", "explanation": "Use two indices moving toward each other (or same direction) to solve pair/subarray problems in O(n). Works best on sorted arrays."},
            {"name": "Sliding Window", "explanation": "Maintain a window of fixed or variable size. Slide it across the array to compute aggregates. Converts O(n*k) to O(n)."},
            {"name": "Prefix Sum", "explanation": "Precompute cumulative sums so any range sum query is O(1). prefix[i] = sum(arr[0..i])."},
            {"name": "Kadane's Algorithm", "explanation": "DP approach to find max sum contiguous subarray in O(n). At each index, decide: extend current subarray or start new one."},
            {"name": "Reversal Algorithm", "explanation": "Rotate array by d positions using three reversals. O(n) time, O(1) space. Reverse first d, reverse rest, reverse all."}
        ],
        "formulas": [
            "Prefix Sum: prefix[i] = prefix[i-1] + arr[i]; range_sum(l,r) = prefix[r] - prefix[l-1]",
            "2D Prefix: prefix[i][j] = mat[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]",
            "Kadane: max_ending_here = max(arr[i], max_ending_here + arr[i])",
            "Circular Max Subarray = max(kadane_max, total_sum - kadane_min)",
            "Left rotate by d = reverse(0,d-1) + reverse(d,n-1) + reverse(0,n-1)"
        ],
        "solved_examples": [
            {"question": "Find the subarray with maximum sum in [-2, 1, -3, 4, -1, 2, 1, -5, 4].", "solution": "Apply Kadane's algorithm. Track max_ending_here: -2->1->-2->4->3->5->6->1->5. Maximum is 6 for subarray [4,-1,2,1]."},
            {"question": "Rotate matrix [[1,2],[3,4]] by 90 degrees clockwise.", "solution": "Transpose: [[1,3],[2,4]]. Reverse each row: [[3,1],[4,2]]. Verify: top-right 1 moves to bottom-right. Correct."},
            {"question": "Find equilibrium index in [-7, 1, 5, 2, -4, 3, 0].", "solution": "Total sum = 0. Left sum at index 0: 0, right sum: 7. Index 3: left=(-7+1+5)=-1, right=(-4+3+0)=-1. Equal! Equilibrium index = 3."}
        ],
        "tips": [
            "When you see 'subarray' think Kadane's or prefix sum; when you see 'subsequence' think DP.",
            "For matrix problems, always clarify if rotation is clockwise or counter-clockwise.",
            "Two-pointer on unsorted array? Sort first, but note if original indices are needed.",
            "Prefix sum + hashmap is a powerful combo for 'subarray with sum k' problems.",
            "In TCS NQT, array questions are typically easier - solve them first to save time for harder sections."
        ],
    },
    41: {
        "title": "Linked Lists",
        "overview": "Linked lists are fundamental pointer-based data structures heavily tested in coding interviews. This topic covers singly and doubly linked lists, reversal techniques, cycle detection with Floyd's algorithm, merging sorted lists, and advanced problems like copying lists with random pointers.",
        "chapters": [
            {
                "title": "Singly Linked List Fundamentals",
                "content": "A singly linked list consists of nodes where each node contains data and a pointer to the next node.\n\nNode Structure:\n  class Node:\n      def __init__(self, data):\n          self.data = data\n          self.next = None\n\nBasic Operations:\n1) Insertion at head - O(1):\n  new_node.next = head\n  head = new_node\n\n2) Insertion at tail - O(n) without tail pointer, O(1) with:\n  tail.next = new_node\n  tail = new_node\n\n3) Insertion at position k - O(k):\n  Traverse to node k-1, adjust pointers.\n\n4) Deletion: Find the node before target, set prev.next = target.next.\n\n5) Search: Linear scan O(n).\n\nFinding Middle Element (Two pointers):\n  slow = fast = head\n  while fast and fast.next:\n      slow = slow.next\n      fast = fast.next.next\n  # slow is at middle\n\nFinding Nth Node from End:\n  Move first pointer n steps ahead.\n  Then move both first and second together.\n  When first reaches end, second is at nth from end.\n\nLength calculation:\n  count = 0; curr = head\n  while curr: count += 1; curr = curr.next",
                "key_points": [
                    "Linked list access is O(n) - no random access like arrays",
                    "Always handle edge cases: empty list, single node, operation on head",
                    "Two-pointer (slow/fast) finds middle in one pass - O(n) time O(1) space",
                    "Nth from end uses the gap technique with two pointers",
                    "Draw pointer diagrams when solving - this prevents bugs"
                ],
                "examples": [
                    {"question": "Find the middle of linked list 1->2->3->4->5", "solution": "slow=1, fast=1. Step 1: slow=2, fast=3. Step 2: slow=3, fast=5. fast.next is None, stop. Middle = 3."},
                    {"question": "Find 2nd node from end in 10->20->30->40->50", "solution": "Move first pointer 2 steps: first=30. Now move both: first=40,second=20; first=50,second=30; first=None,second=40. Answer: 40."},
                    {"question": "Delete node with value 30 from 10->20->30->40", "solution": "Traverse to node with value 20 (prev of 30). Set prev.next = prev.next.next. Result: 10->20->40."}
                ],
            },
            {
                "title": "Linked List Reversal Techniques",
                "content": "Reversing a linked list is one of the most commonly asked interview questions.\n\nIterative Reversal - O(n) time, O(1) space:\n  prev = None\n  curr = head\n  while curr:\n      next_node = curr.next\n      curr.next = prev\n      prev = curr\n      curr = next_node\n  head = prev\n\nRecursive Reversal - O(n) time, O(n) space (call stack):\n  def reverse(head):\n      if not head or not head.next:\n          return head\n      new_head = reverse(head.next)\n      head.next.next = head\n      head.next = None\n      return new_head\n\nReverse in Groups of K:\n  def reverseKGroup(head, k):\n      curr = head; count = 0\n      while curr and count < k:\n          curr = curr.next; count += 1\n      if count == k:\n          reversed_head = reverse_first_k(head, k)\n          head.next = reverseKGroup(curr, k)\n          return reversed_head\n      return head\n\nReverse a Sublist (from position m to n):\n  Navigate to position m-1 (connection point).\n  Reverse nodes from m to n.\n  Reconnect: prev_of_m.next = new_head; old_m.next = node_after_n.\n\nCheck Palindrome using Reversal:\n  Find middle, reverse second half, compare with first half, restore (optional).",
                "key_points": [
                    "Iterative reversal uses 3 pointers (prev, curr, next) - draw it out",
                    "Recursive reversal is elegant but uses O(n) stack space",
                    "Reverse in groups of K is asked by Amazon, Microsoft, Google",
                    "Palindrome check = find middle + reverse second half + compare",
                    "Always return the new head after reversal - common mistake is forgetting this"
                ],
                "examples": [
                    {"question": "Reverse 1->2->3->4->5 iteratively", "solution": "prev=None, curr=1. Step: next=2, 1.next=None, prev=1, curr=2. Step: next=3, 2.next=1, prev=2, curr=3. Step: next=4, 3.next=2, prev=3, curr=4. Step: next=5, 4.next=3, prev=4, curr=5. Step: next=None, 5.next=4, prev=5, curr=None. Head=5. Result: 5->4->3->2->1."},
                    {"question": "Check if 1->2->2->1 is a palindrome", "solution": "Find middle: slow=2(first), fast=end. Reverse second half: 1->2->2<-1 becomes 1->2 and 1->2. Compare: 1==1, 2==2. Palindrome = True."},
                    {"question": "Reverse in groups of 3: 1->2->3->4->5->6->7->8", "solution": "Reverse first 3: 3->2->1. Reverse next 3: 6->5->4. Remaining 7->8 (less than 3, keep as is). Result: 3->2->1->6->5->4->7->8."}
                ],
            },
            {
                "title": "Cycle Detection & Floyd's Algorithm",
                "content": "Floyd's Cycle Detection (Tortoise and Hare) determines if a linked list has a cycle and finds the cycle start.\n\nDetecting a Cycle - O(n) time, O(1) space:\n  slow = fast = head\n  while fast and fast.next:\n      slow = slow.next\n      fast = fast.next.next\n      if slow == fast:\n          return True  # Cycle exists\n  return False  # No cycle\n\nFinding the Start of the Cycle:\n  After slow and fast meet inside the cycle:\n  slow = head  # Reset slow to head\n  while slow != fast:\n      slow = slow.next\n      fast = fast.next  # Both move one step\n  return slow  # This is the start of the cycle\n\nMathematical Proof:\n  Let distance from head to cycle start = a\n  Let distance from cycle start to meeting point = b\n  Let cycle length = c\n  slow travels: a + b\n  fast travels: a + b + n*c (for some n)\n  Since fast = 2 * slow: a + b + n*c = 2(a + b)\n  Therefore: a = n*c - b = (n-1)*c + (c-b)\n  This means moving a steps from head reaches cycle start,\n  and moving a steps from meeting point also reaches cycle start.\n\nFinding Cycle Length:\n  After detecting cycle (slow == fast):\n  count = 1; temp = slow.next\n  while temp != slow:\n      count += 1; temp = temp.next\n\nRemoving the Cycle:\n  Find cycle start. Traverse cycle to find node pointing to cycle start. Set its next to None.",
                "key_points": [
                    "Floyd's algorithm is O(n) time, O(1) space - no extra data structures needed",
                    "After meeting point, reset one pointer to head, move both at same speed to find cycle start",
                    "This is asked by Amazon, Microsoft, Goldman Sachs in interviews",
                    "Alternative: use a HashSet to store visited nodes - O(n) space but simpler to code",
                    "Always handle the case where there is no cycle (fast reaches None)"
                ],
                "examples": [
                    {"question": "Detect cycle in: 1->2->3->4->5->3 (5 points back to 3)", "solution": "slow=1,fast=1. Step 1: s=2,f=3. Step 2: s=3,f=5. Step 3: s=4,f=4(back to 3, then 4). Wait - f goes 5->3, then 3->4. So step 3: s=4,f=4. They meet! Cycle exists."},
                    {"question": "Find cycle start in above example", "solution": "After meeting at 4: reset slow=1(head). Move both by 1: slow=2,fast=5; slow=3,fast=3. They meet at 3. Cycle starts at node 3."},
                    {"question": "Find cycle length in 1->2->3->4->5->3", "solution": "After detecting cycle at meeting point (say node 4): start counting from 4. temp=5->3->4, count=3. Cycle length = 3 (nodes 3,4,5)."}
                ],
            },
            {
                "title": "Merge & Intersection of Linked Lists",
                "content": "Merge Two Sorted Linked Lists - O(n+m) time, O(1) space:\n  def mergeTwoLists(l1, l2):\n      dummy = Node(0)\n      tail = dummy\n      while l1 and l2:\n          if l1.data <= l2.data:\n              tail.next = l1; l1 = l1.next\n          else:\n              tail.next = l2; l2 = l2.next\n          tail = tail.next\n      tail.next = l1 if l1 else l2\n      return dummy.next\n\nMerge K Sorted Lists:\n  Approach 1: Use min-heap. Push first node of each list. Pop min, push its next. O(N log k) where N=total nodes, k=number of lists.\n  Approach 2: Divide and conquer - merge pairs, then merge results. O(N log k).\n\nIntersection Point of Two Lists:\n  Method 1 - Length Difference:\n    Find lengths of both lists.\n    Advance the longer list by (lenA - lenB) nodes.\n    Move both together until they meet.\n\n  Method 2 - Two Pointer Elegant:\n    pA = headA; pB = headB\n    while pA != pB:\n        pA = pA.next if pA else headB\n        pB = pB.next if pB else headA\n    return pA  # Intersection point or None\n\n  Why Method 2 works: Both pointers traverse exactly lenA + lenB nodes.\n  If there is an intersection, they will meet at it.\n  If no intersection, both become None simultaneously.\n\nAdd Two Numbers Represented as Linked Lists:\n  Traverse both lists, add digits + carry.\n  Create new node for each digit. Handle remaining carry.",
                "key_points": [
                    "Dummy node technique simplifies merge operations enormously",
                    "Two-pointer intersection method is O(n+m) time, O(1) space - very elegant",
                    "Merge K sorted lists with heap is a common Amazon interview question",
                    "For add two numbers: remember to handle the final carry (e.g., 999 + 1 = 1000)",
                    "Practice both iterative and recursive merge - interviewers may ask for either"
                ],
                "examples": [
                    {"question": "Merge sorted lists 1->3->5 and 2->4->6", "solution": "Compare 1,2: pick 1. Compare 3,2: pick 2. Compare 3,4: pick 3. Compare 5,4: pick 4. Compare 5,6: pick 5. Remaining: 6. Result: 1->2->3->4->5->6."},
                    {"question": "Find intersection of A: 1->2->3->6->7 and B: 4->5->6->7", "solution": "lenA=5, lenB=4, diff=1. Advance A by 1: start at 2. Now move together: (2,4), (3,5), (6,6) - match! Intersection at node 6."},
                    {"question": "Add 2->4->3 (342) and 5->6->4 (465)", "solution": "2+5=7, carry=0. 4+6=10, digit=0, carry=1. 3+4+1=8, carry=0. Result: 7->0->8 (807). Verify: 342+465=807."}
                ],
            },
            {
                "title": "Doubly Linked List & Advanced Problems",
                "content": "Doubly Linked List (DLL) has both next and prev pointers.\n\nNode Structure:\n  class DLLNode:\n      def __init__(self, data):\n          self.data = data\n          self.next = None\n          self.prev = None\n\nAdvantages over Singly LL: O(1) deletion given the node (no need to find prev), bidirectional traversal.\nDisadvantage: Extra memory for prev pointer.\n\nInsert at head:\n  new_node.next = head\n  if head: head.prev = new_node\n  head = new_node\n\nDelete a given node:\n  if node.prev: node.prev.next = node.next\n  if node.next: node.next.prev = node.prev\n  if node == head: head = node.next\n\nCopy List with Random Pointer:\n  Each node has next and a random pointer to any node in the list.\n  Approach 1 - HashMap: O(n) time, O(n) space.\n    Create mapping old_node -> new_node.\n    Set next and random using the map.\n  Approach 2 - Interleaving (O(1) space):\n    Step 1: Insert cloned nodes between original nodes.\n      A -> A' -> B -> B' -> C -> C'\n    Step 2: Set random pointers of cloned nodes.\n      clone.random = original.random.next\n    Step 3: Separate the two lists.\n\nLRU Cache (uses DLL + HashMap):\n  DLL maintains access order (most recent at head).\n  HashMap provides O(1) lookup.\n  On access: move node to head.\n  On capacity full: remove tail node.\n  All operations are O(1).",
                "key_points": [
                    "DLL enables O(1) deletion given a node pointer - key advantage",
                    "Copy with random pointer interleaving method saves space - Amazon favorite",
                    "LRU Cache = DLL + HashMap - asked by virtually every top company",
                    "Flatten a multilevel DLL is a Microsoft interview classic",
                    "Always handle prev pointer updates in DLL - most bugs come from forgetting this"
                ],
                "examples": [
                    {"question": "Implement LRU Cache with capacity 2: put(1,1), put(2,2), get(1), put(3,3), get(2)", "solution": "put(1,1): cache={1:1}, order=[1]. put(2,2): cache={1:1,2:2}, order=[2,1]. get(1): return 1, order=[1,2]. put(3,3): evict LRU=2, cache={1:1,3:3}, order=[3,1]. get(2): return -1 (not found)."},
                    {"question": "Copy list with random pointer: A(random->C)->B(random->A)->C(random->B)", "solution": "Interleave: A->A'->B->B'->C->C'. Set randoms: A'.random = A.random.next = C'. B'.random = B.random.next = A'. C'.random = C.random.next = B'. Separate: A->B->C and A'->B'->C'."},
                    {"question": "Delete node 3 from DLL: 1<->2<->3<->4<->5", "solution": "node=3. node.prev(2).next = node.next(4). node.next(4).prev = node.prev(2). Result: 1<->2<->4<->5."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Linked List", "explanation": "Linear data structure where elements are stored in nodes connected by pointers. No contiguous memory needed. O(1) insertion/deletion at known position, O(n) access."},
            {"name": "Floyd's Cycle Detection", "explanation": "Use slow (1 step) and fast (2 step) pointers. If they meet, cycle exists. Reset one to head and move both at 1 step to find cycle start."},
            {"name": "Dummy Node Technique", "explanation": "Create a dummy node before head to simplify edge cases in operations like merge, insert at head, etc. Return dummy.next as the result."},
            {"name": "Two-Pointer for Middle", "explanation": "Slow moves 1 step, fast moves 2 steps. When fast reaches end, slow is at middle. Works for both odd and even length lists."},
            {"name": "LRU Cache", "explanation": "Doubly linked list (order) + HashMap (O(1) lookup). Most recently used at head, least recently used at tail. All operations O(1)."}
        ],
        "formulas": [
            "Middle element: slow-fast pointer technique, O(n) time O(1) space",
            "Cycle detection: Floyd's algorithm, O(n) time O(1) space",
            "Merge two sorted lists: O(n+m) time, O(1) space with dummy node",
            "Intersection point: traverse lenA+lenB nodes with pointer switching",
            "Reverse: 3 pointers (prev, curr, next), O(n) time O(1) space"
        ],
        "solved_examples": [
            {"question": "Reverse a linked list 1->2->3->4->5.", "solution": "Iterative: prev=None. Process each node, point it back. After all steps: 5->4->3->2->1->None. New head = 5."},
            {"question": "Detect if 1->2->3->4->2 has a cycle.", "solution": "Floyd's: slow=1,fast=1. Moves: (2,3),(3,2),(4,4). Meet at 4. Cycle exists. Reset slow=1. Move both by 1: (2,2). Cycle starts at 2."},
            {"question": "Merge 1->4->7 and 2->3->8 into sorted list.", "solution": "Using dummy node. Compare: 1<2 pick 1. 4>2 pick 2. 4>3 pick 3. 4<8 pick 4. 7<8 pick 7. Pick 8. Result: 1->2->3->4->7->8."}
        ],
        "tips": [
            "Always draw the pointer diagram before coding linked list problems.",
            "Use dummy/sentinel nodes to avoid special-casing head operations.",
            "For interviews, mention time and space complexity of your linked list approach.",
            "Practice both iterative and recursive versions - companies like Amazon ask for both.",
            "Common bug: losing reference to next node before reassigning pointers. Save it first!"
        ],
    },
    42: {
        "title": "Stacks & Queues",
        "overview": "Stacks and queues are linear data structures with restricted access patterns. Stacks follow LIFO (Last In First Out) and queues follow FIFO (First In First Out). This topic covers their implementations, monotonic stack, priority queues, and classic problems like balanced parentheses and next greater element that appear in Amazon, Microsoft, and TCS coding rounds.",
        "chapters": [
            {
                "title": "Stack Fundamentals & Applications",
                "content": "A stack is a LIFO data structure supporting push, pop, peek, and isEmpty in O(1).\n\nImplementation using Array:\n  class Stack:\n      def __init__(self):\n          self.items = []\n      def push(self, val): self.items.append(val)\n      def pop(self): return self.items.pop() if self.items else None\n      def peek(self): return self.items[-1] if self.items else None\n      def is_empty(self): return len(self.items) == 0\n\nImplementation using Linked List:\n  Push: Insert at head (O(1)). Pop: Remove head (O(1)).\n\nBalanced Parentheses:\n  def isValid(s):\n      stack = []\n      mapping = {')':'(', '}':'{', ']':'['}\n      for ch in s:\n          if ch in '({[':\n              stack.append(ch)\n          elif ch in ')}]':\n              if not stack or stack[-1] != mapping[ch]:\n                  return False\n              stack.pop()\n      return len(stack) == 0\n\nEvaluate Postfix Expression:\n  For each token: if operand, push. If operator, pop two operands, compute, push result.\n  Example: '2 3 + 4 *' -> push 2, push 3, '+': pop 3,2 -> 5, push 5, push 4, '*': pop 4,5 -> 20.\n\nInfix to Postfix (Shunting Yard):\n  Use operator stack. Push operands to output. For operators: pop higher/equal precedence operators to output, then push current.",
                "key_points": [
                    "All stack operations are O(1) - this is key for interview discussions",
                    "Balanced parentheses is the most common stack problem in placements",
                    "Postfix evaluation and infix-to-postfix conversion are TCS/Infosys favorites",
                    "Stack overflow occurs when stack exceeds memory limit (recursion depth)",
                    "Use Python list as stack (append/pop) - do not use insert(0,x) which is O(n)"
                ],
                "examples": [
                    {"question": "Check if '{[()]}' is balanced", "solution": "Push '{', push '[', push '('. See ')': top is '(' match, pop. See ']': top is '[' match, pop. See '}': top is '{' match, pop. Stack empty. Valid!"},
                    {"question": "Evaluate postfix: 5 1 2 + 4 * + 3 -", "solution": "Push 5,1,2. '+': 1+2=3, push. Push 4. '*': 3*4=12, push. '+': 5+12=17, push. Push 3. '-': 17-3=14. Answer: 14."},
                    {"question": "Convert infix A*(B+C)-D to postfix", "solution": "A -> output:A. * -> stack:*. ( -> stack:*(. B -> output:AB. + -> stack:*(+. C -> output:ABC. ) -> pop + to output: ABC+, pop (. Stack:*. - -> pop * to output: ABC+*. Push -. D -> output:ABC+*D. Pop all: ABC+*D-. Answer: ABC+*D-."}
                ],
            },
            {
                "title": "Monotonic Stack",
                "content": "A monotonic stack maintains elements in either increasing or decreasing order. It is used to find next greater/smaller elements efficiently.\n\nNext Greater Element (NGE):\n  For each element, find the first greater element to its right.\n  def nextGreater(arr):\n      n = len(arr)\n      result = [-1] * n\n      stack = []  # stores indices\n      for i in range(n):\n          while stack and arr[i] > arr[stack[-1]]:\n              result[stack.pop()] = arr[i]\n          stack.append(i)\n      return result\n  Time: O(n) - each element pushed and popped at most once.\n\nNext Smaller Element: Same logic but use < instead of >.\n\nPrevious Greater Element: Traverse from left to right, maintain decreasing stack.\n\nLargest Rectangle in Histogram:\n  Use monotonic increasing stack of indices.\n  For each bar, while stack top is taller, pop and calculate area:\n    width = i - stack[-1] - 1 (or i if stack empty)\n    area = height[popped] * width\n  Push sentinel -1 initially, and process remaining stack at end.\n  Time: O(n), Space: O(n)\n\nTrapping Rain Water:\n  Method 1: For each index, water = min(max_left, max_right) - height[i]. Precompute max_left[] and max_right[].\n  Method 2: Two pointer approach. O(n) time, O(1) space.\n  Method 3: Stack-based approach using monotonic stack.",
                "key_points": [
                    "Monotonic stack gives O(n) solution for next greater/smaller element problems",
                    "Each element is pushed and popped at most once, ensuring O(n) total",
                    "Largest rectangle in histogram is a classic hard problem - Amazon, Google favorite",
                    "Trapping rain water has 3 approaches: precompute, two-pointer, stack",
                    "Stock span problem is a direct application of previous greater element"
                ],
                "examples": [
                    {"question": "Find NGE for [4, 5, 2, 25]", "solution": "i=0: push 0. i=1: 5>4, pop 0, result[0]=5. push 1. i=2: 2<5, push 2. i=3: 25>2, pop 2, result[2]=25. 25>5, pop 1, result[1]=25. push 3. Remaining: result[3]=-1. Answer: [5, 25, 25, -1]."},
                    {"question": "Largest rectangle in histogram [2,1,5,6,2,3]", "solution": "Process: push -1. i=0 push 0. i=1: 1<2, pop 0, area=2*1=2. push 1. i=2 push 2. i=3 push 3. i=4: 2<6, pop 3 area=6*1=6. 2<5, pop 2 area=5*2=10. push 4. i=5 push 5. End: pop 5 area=3*1=3. pop 4 area=2*4=8. Max=10."},
                    {"question": "Trapping rain water: [0,1,0,2,1,0,1,3,2,1,2,1]", "solution": "max_left=[0,1,1,2,2,2,2,3,3,3,3,3]. max_right=[3,3,3,3,3,3,3,3,2,2,2,1]. Water at each: min(L,R)-h = [0,0,1,0,1,2,1,0,0,1,0,0]. Total = 6."}
                ],
            },
            {
                "title": "Queue Implementations & Variants",
                "content": "A queue is a FIFO data structure: enqueue at rear, dequeue from front.\n\nImplementation using Array (Circular Queue):\n  class CircularQueue:\n      def __init__(self, k):\n          self.queue = [None] * k\n          self.front = self.rear = -1\n          self.size = k\n      def enqueue(self, val):\n          if (self.rear + 1) % self.size == self.front:\n              return 'Full'\n          if self.front == -1: self.front = 0\n          self.rear = (self.rear + 1) % self.size\n          self.queue[self.rear] = val\n      def dequeue(self):\n          if self.front == -1: return 'Empty'\n          val = self.queue[self.front]\n          if self.front == self.rear:\n              self.front = self.rear = -1\n          else:\n              self.front = (self.front + 1) % self.size\n          return val\n\nDeque (Double-Ended Queue):\n  Supports insertion and deletion at both ends in O(1).\n  Python: from collections import deque\n  Operations: append(), appendleft(), pop(), popleft()\n\nQueue using Two Stacks:\n  Push-efficient: push to stack1. Pop: transfer all to stack2, pop.\n  Amortized O(1) per operation.\n  def enqueue(val): stack1.push(val)\n  def dequeue():\n      if stack2 is empty:\n          while stack1: stack2.push(stack1.pop())\n      return stack2.pop()\n\nStack using Two Queues:\n  Push-expensive: enqueue to q2, transfer all from q1 to q2, swap q1 and q2.\n  Pop: dequeue from q1.",
                "key_points": [
                    "Circular queue solves the problem of wasted space in linear array implementation",
                    "Queue using two stacks is a very common interview question (Amazon, Google)",
                    "Deque is versatile - can act as both stack and queue",
                    "BFS uses a queue - this connection is critical for graph problems",
                    "Python collections.deque is O(1) for both ends; list.pop(0) is O(n) - never use it as queue"
                ],
                "examples": [
                    {"question": "Implement queue using two stacks. Enqueue 1,2,3 then dequeue twice.", "solution": "Enqueue: stack1=[1,2,3]. Dequeue: stack2 empty, transfer: stack2=[3,2,1]. Pop stack2: return 1. Dequeue: Pop stack2: return 2. stack2=[3]."},
                    {"question": "Circular queue of size 3: enqueue(1), enqueue(2), enqueue(3), dequeue(), enqueue(4)", "solution": "front=0,rear=0: [1,_,_]. rear=1: [1,2,_]. rear=2: [1,2,3]. Dequeue: front=1, return 1. rear=(2+1)%3=0: [4,2,3]. front=1, rear=0."},
                    {"question": "Implement stack using two queues. Push 1,2,3 then pop.", "solution": "Push 1: q1=[1]. Push 2: q2=[2], move q1 to q2: q2=[2,1], swap: q1=[2,1]. Push 3: q2=[3], move q1: q2=[3,2,1], swap: q1=[3,2,1]. Pop: dequeue q1: return 3."}
                ],
            },
            {
                "title": "Priority Queue & Heap",
                "content": "A priority queue serves the highest (or lowest) priority element first. It is typically implemented using a binary heap.\n\nBinary Heap Properties:\n  Min-Heap: parent <= children. Root is minimum.\n  Max-Heap: parent >= children. Root is maximum.\n  Complete binary tree stored as array:\n    Parent of i: (i-1)//2\n    Left child of i: 2*i + 1\n    Right child of i: 2*i + 2\n\nHeap Operations:\n  Insert (push): Add at end, bubble up. O(log n).\n  Extract min/max (pop): Replace root with last, bubble down. O(log n).\n  Peek: Return root. O(1).\n  Build heap from array: O(n) using bottom-up heapify.\n\nPython heapq (min-heap):\n  import heapq\n  heapq.heappush(heap, val)\n  heapq.heappop(heap)  # returns smallest\n  heapq.heapify(arr)   # in-place, O(n)\n  # For max-heap: negate values\n\nKth Largest Element:\n  Method 1: Min-heap of size k. Push elements; if size > k, pop. Root is kth largest. O(n log k).\n  Method 2: Max-heap, pop k times. O(n + k log n).\n  Method 3: QuickSelect (average O(n)).\n\nMerge K Sorted Arrays:\n  Push first element of each array into min-heap with (value, array_index, element_index).\n  Pop min, push next element from same array.\n  O(N log k) where N = total elements, k = number of arrays.\n\nTop K Frequent Elements:\n  Count frequencies with HashMap, then use min-heap of size k. O(n log k).",
                "key_points": [
                    "Heap insert and extract are O(log n), peek is O(1)",
                    "Build heap is O(n), not O(n log n) - know the proof for interviews",
                    "Python heapq is min-heap only - negate values for max-heap behavior",
                    "Kth largest/smallest element is an extremely common interview question",
                    "Priority queue questions appear in Amazon SDE, Microsoft, and Flipkart interviews"
                ],
                "examples": [
                    {"question": "Find 3rd largest in [3,2,1,5,6,4] using min-heap of size 3", "solution": "Push 3: [3]. Push 2: [2,3]. Push 1: [1,2,3]. Push 5: heap size 4>3, pop min 1: [2,3,5]. Push 6: pop 2: [3,5,6]. Push 4: pop 3: [4,5,6]. Root = 4 = 3rd largest."},
                    {"question": "Merge sorted arrays [1,4,7] and [2,5,8] and [3,6,9] using heap", "solution": "Heap: [(1,0,0),(2,1,0),(3,2,0)]. Pop 1, push (4,0,1). Pop 2, push (5,1,1). Pop 3, push (6,2,1). Pop 4, push (7,0,2). Pop 5, push (8,1,2). Pop 6, push (9,2,2). Pop 7,8,9. Result: [1,2,3,4,5,6,7,8,9]."},
                    {"question": "Top 2 frequent elements in [1,1,1,2,2,3]", "solution": "Frequency: {1:3, 2:2, 3:1}. Min-heap of size 2: push (3,1), push (2,2), push (1,3) -> pop min (1,3). Wait: push (1,3), size=3>2, pop smallest freq (1,3). Heap: [(2,2),(3,1)]. Answer: [1,2]."}
                ],
            },
            {
                "title": "Classic Stack & Queue Problems",
                "content": "Min Stack (stack that returns minimum in O(1)):\n  Approach 1: Use auxiliary stack storing minimums.\n    push(val): push to main. If val <= min_stack top, push to min_stack.\n    pop(): pop from main. If popped == min_stack top, pop min_stack.\n    getMin(): return min_stack top.\n  Approach 2: Store (val, current_min) pairs.\n\nSliding Window Maximum (Deque approach):\n  Maintain deque of indices in decreasing order of values.\n  For each element:\n    Remove indices outside window from front.\n    Remove smaller elements from back.\n    Add current index to back.\n    Front of deque is maximum of current window.\n  Time: O(n), Space: O(k)\n\n  def maxSlidingWindow(nums, k):\n      dq = deque()  # stores indices\n      result = []\n      for i in range(len(nums)):\n          while dq and dq[0] < i - k + 1: dq.popleft()\n          while dq and nums[dq[-1]] < nums[i]: dq.pop()\n          dq.append(i)\n          if i >= k - 1: result.append(nums[dq[0]])\n      return result\n\nCelebrity Problem:\n  A celebrity is known by everyone but knows nobody.\n  Use stack: push all people. Pop two, the one who knows the other is not celebrity.\n  Push survivor back. Verify the final candidate. O(n).\n\nSort a Stack using recursion:\n  Pop top, recursively sort remaining, insert popped element in sorted order.",
                "key_points": [
                    "Min Stack uses O(n) extra space but gives O(1) getMin - worth the tradeoff",
                    "Sliding window maximum with deque is O(n) - much better than O(nk) brute force",
                    "Celebrity problem with stack reduces comparisons from O(n^2) to O(n)",
                    "These are frequently asked in Amazon onsite and Microsoft coding rounds",
                    "Always mention the time-space tradeoff when discussing min stack in interviews"
                ],
                "examples": [
                    {"question": "Min Stack: push(5), push(3), push(7), getMin(), pop(), getMin()", "solution": "push(5): main=[5], min=[5]. push(3): main=[5,3], min=[5,3]. push(7): main=[5,3,7], min=[5,3] (7>3). getMin()=3. pop()=7: main=[5,3]. getMin()=3."},
                    {"question": "Sliding window max for [1,3,-1,-3,5,3,6,7], k=3", "solution": "Window [1,3,-1]: deque=[1(3)], max=3. [-1,-3]: deque=[1(3),2(-1)], remove 0, max=3. [3,-1,-3]: deque has 1(3), max=3. [-3,5,3]: deque=[4(5)], max=5. [5,3,6]: deque=[6(6)], max=6. [3,6,7]: deque=[7(7)], max=7. Output: [3,3,3,5,6,7]. Wait, let me redo properly. Windows: [1,3,-1]->3, [3,-1,-3]->3, [-1,-3,5]->5, [-3,5,3]->5, [5,3,6]->6, [3,6,7]->7. Answer: [3,3,5,5,6,7]."},
                    {"question": "Sort stack [3,1,4,2] using recursion", "solution": "Pop 2, sort [3,1,4]. Pop 4, sort [3,1]. Pop 1, sort [3]. Base case. Insert 1 into [3]: 1<3, pop 3, push 1, push 3: [1,3]. Insert 4: 4>3, push 4: [1,3,4]. Insert 2: 2<4, pop 4; 2<3, pop 3; 2>1, push 2, push 3, push 4: [1,2,3,4]."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Stack (LIFO)", "explanation": "Last In First Out. Push/Pop/Peek all O(1). Used for expression evaluation, backtracking, DFS, undo operations."},
            {"name": "Queue (FIFO)", "explanation": "First In First Out. Enqueue/Dequeue O(1). Used for BFS, scheduling, buffering. Circular queue avoids wasted space."},
            {"name": "Monotonic Stack", "explanation": "Stack maintaining increasing or decreasing order. Solves next greater/smaller element in O(n). Each element pushed and popped at most once."},
            {"name": "Priority Queue / Heap", "explanation": "Serves highest priority first. Binary heap: insert O(log n), extract O(log n), peek O(1). Used for Kth element, merge K lists, scheduling."},
            {"name": "Deque", "explanation": "Double-ended queue allowing O(1) operations at both ends. Used for sliding window maximum. Python collections.deque."}
        ],
        "formulas": [
            "Heap parent index: (i-1)//2; left child: 2i+1; right child: 2i+2",
            "Build heap: O(n); Insert/Extract: O(log n); Peek: O(1)",
            "Stack operations (push/pop/peek): O(1) time",
            "Sliding window max with deque: O(n) time, O(k) space",
            "Kth largest with min-heap of size k: O(n log k)"
        ],
        "solved_examples": [
            {"question": "Evaluate postfix expression: 2 3 1 * + 9 -", "solution": "Push 2,3,1. '*': 3*1=3, push. '+': 2+3=5, push. Push 9. '-': 5-9=-4. Answer: -4."},
            {"question": "Find next greater element for each in [13, 7, 6, 12].", "solution": "Monotonic stack (right to left): 12->stack[12], NGE=-1. 6->stack[6,12], NGE=12. 7->pop 6, stack[7,12], NGE=12. 13->pop all, stack[13], NGE=-1. Answer: [-1, 12, 12, -1]."},
            {"question": "Is '({[]})' balanced?", "solution": "Push '(', '{', '['. See ']': top='[' match. See '}': top='{' match. See ')': top='(' match. Stack empty. YES."}
        ],
        "tips": [
            "When you see 'next greater' or 'next smaller', immediately think monotonic stack.",
            "For sliding window problems, deque is almost always the optimal approach.",
            "Stack problems often have elegant recursive solutions - but mention stack overflow risk.",
            "In placement MCQs, stack/queue output-prediction questions are common - trace carefully.",
            "Know how to implement stack using queue and vice versa - asked in TCS, Infosys interviews."
        ],
    },
    43: {
        "title": "Trees & BST",
        "overview": "Trees are hierarchical data structures fundamental to CS. Binary trees and Binary Search Trees (BST) are the most tested tree types in placements. This topic covers traversals (inorder, preorder, postorder, level-order), BST operations, balanced trees (AVL), LCA, tree diameter, and serialization - all staples of Amazon, Microsoft, and Google interviews.",
        "chapters": [
            {
                "title": "Binary Tree Fundamentals & Traversals",
                "content": "A binary tree is a tree where each node has at most two children (left and right).\n\nNode Structure:\n  class TreeNode:\n      def __init__(self, val):\n          self.val = val\n          self.left = None\n          self.right = None\n\nTraversal Orders:\n1) Inorder (Left, Root, Right) - gives sorted order for BST:\n  def inorder(root):\n      if root:\n          inorder(root.left)\n          print(root.val)\n          inorder(root.right)\n\n2) Preorder (Root, Left, Right) - used for serialization:\n  def preorder(root):\n      if root:\n          print(root.val)\n          preorder(root.left)\n          preorder(root.right)\n\n3) Postorder (Left, Right, Root) - used for deletion:\n  def postorder(root):\n      if root:\n          postorder(root.left)\n          postorder(root.right)\n          print(root.val)\n\n4) Level Order (BFS) using queue:\n  def levelOrder(root):\n      if not root: return []\n      queue = [root]; result = []\n      while queue:\n          level = []\n          for _ in range(len(queue)):\n              node = queue.pop(0)\n              level.append(node.val)\n              if node.left: queue.append(node.left)\n              if node.right: queue.append(node.right)\n          result.append(level)\n      return result\n\nIterative Inorder using Stack:\n  stack = []; curr = root\n  while curr or stack:\n      while curr:\n          stack.append(curr); curr = curr.left\n      curr = stack.pop()\n      print(curr.val)\n      curr = curr.right",
                "key_points": [
                    "Inorder of BST gives sorted sequence - this property is tested extensively",
                    "Know all three DFS traversals both recursively and iteratively",
                    "Level order traversal uses a queue (BFS) - used to find level-wise information",
                    "Time complexity of all traversals is O(n), space is O(h) where h is height",
                    "Construct tree from inorder+preorder or inorder+postorder is a classic interview question"
                ],
                "examples": [
                    {"question": "Given tree: 1(2(4,5),3(6,7)). Find inorder, preorder, postorder.", "solution": "Inorder (L,Root,R): 4,2,5,1,6,3,7. Preorder (Root,L,R): 1,2,4,5,3,6,7. Postorder (L,R,Root): 4,5,2,6,7,3,1."},
                    {"question": "Level order of tree: 3(9,20(15,7))", "solution": "Level 0: [3]. Level 1: [9,20]. Level 2: [15,7]. Result: [[3],[9,20],[15,7]]."},
                    {"question": "Construct tree from inorder=[9,3,15,20,7] and preorder=[3,9,20,15,7]", "solution": "Root=3 (first of preorder). In inorder, 3 splits: left=[9], right=[15,20,7]. Left subtree root=9. Right subtree root=20, left=15, right=7. Tree: 3(9, 20(15,7))."}
                ],
            },
            {
                "title": "BST Operations & Properties",
                "content": "A Binary Search Tree satisfies: left subtree values < root < right subtree values.\n\nSearch - O(h):\n  def search(root, key):\n      if not root or root.val == key: return root\n      if key < root.val: return search(root.left, key)\n      return search(root.right, key)\n\nInsert - O(h):\n  def insert(root, val):\n      if not root: return TreeNode(val)\n      if val < root.val: root.left = insert(root.left, val)\n      elif val > root.val: root.right = insert(root.right, val)\n      return root\n\nDelete - O(h):\n  Case 1: Leaf node - simply remove.\n  Case 2: One child - replace with child.\n  Case 3: Two children - replace with inorder successor (smallest in right subtree) or inorder predecessor (largest in left subtree), then delete that node.\n\n  def delete(root, key):\n      if not root: return root\n      if key < root.val: root.left = delete(root.left, key)\n      elif key > root.val: root.right = delete(root.right, key)\n      else:\n          if not root.left: return root.right\n          if not root.right: return root.left\n          succ = findMin(root.right)\n          root.val = succ.val\n          root.right = delete(root.right, succ.val)\n      return root\n\nValidate BST:\n  def isValidBST(root, low=float('-inf'), high=float('inf')):\n      if not root: return True\n      if root.val <= low or root.val >= high: return False\n      return isValidBST(root.left, low, root.val) and isValidBST(root.right, root.val, high)\n\nKth Smallest: Do inorder traversal, count to k. Or augment BST with subtree sizes.",
                "key_points": [
                    "BST search/insert/delete are O(h) - O(log n) if balanced, O(n) if skewed",
                    "Inorder traversal of BST gives sorted output - use this to validate BST",
                    "Delete with two children: replace with inorder successor then delete successor",
                    "Validate BST using min/max range, NOT by just checking left < root < right locally",
                    "BST questions are asked by Amazon, Microsoft, Flipkart in every hiring cycle"
                ],
                "examples": [
                    {"question": "Insert 5 into BST: 4(2(1,3),6(null,8))", "solution": "5>4, go right. 5<6, go left. 6.left is null, insert 5 there. Result: 4(2(1,3),6(5,8))."},
                    {"question": "Delete 4 from BST: 4(2(1,3),6(5,8))", "solution": "Node 4 has two children. Inorder successor = smallest in right subtree = 5. Replace 4 with 5. Delete 5 from right subtree. Result: 5(2(1,3),6(null,8))."},
                    {"question": "Find kth smallest (k=3) in BST: 5(3(2,4),7(6,8))", "solution": "Inorder: 2,3,4,5,6,7,8. 3rd element = 4. Alternatively, use iterative inorder with counter."}
                ],
            },
            {
                "title": "Tree Height, Depth, Diameter & LCA",
                "content": "Height of a tree: Longest path from root to any leaf.\n  def height(root):\n      if not root: return 0  # or -1 depending on convention\n      return 1 + max(height(root.left), height(root.right))\n\nDepth of a node: Distance from root to that node.\n\nDiameter: Longest path between any two nodes (may not pass through root).\n  def diameter(root):\n      self.ans = 0\n      def depth(node):\n          if not node: return 0\n          L = depth(node.left)\n          R = depth(node.right)\n          self.ans = max(self.ans, L + R)  # path through this node\n          return 1 + max(L, R)\n      depth(root)\n      return self.ans\n\nLowest Common Ancestor (LCA) of nodes p and q:\n  For Binary Tree:\n  def lca(root, p, q):\n      if not root or root == p or root == q: return root\n      left = lca(root.left, p, q)\n      right = lca(root.right, p, q)\n      if left and right: return root  # p and q on different sides\n      return left if left else right\n\n  For BST (more efficient):\n  def lcaBST(root, p, q):\n      if p.val < root.val and q.val < root.val:\n          return lcaBST(root.left, p, q)\n      if p.val > root.val and q.val > root.val:\n          return lcaBST(root.right, p, q)\n      return root  # split point\n\nBalanced Tree Check:\n  A tree is balanced if for every node, |height(left) - height(right)| <= 1.\n  Optimize by returning -1 for unbalanced subtrees to avoid redundant computation.",
                "key_points": [
                    "Diameter may not pass through the root - a common misconception",
                    "LCA in BST is O(h) by exploiting BST property; in general tree it is O(n)",
                    "Height vs Depth: height is from node to leaf, depth is from root to node",
                    "Check balanced in O(n) by combining height computation with balance check",
                    "Amazon and Microsoft frequently ask diameter, LCA, and balanced tree problems"
                ],
                "examples": [
                    {"question": "Find diameter of tree: 1(2(4,5),3)", "solution": "depth(4)=1, depth(5)=1. At node 2: L=1, R=1, diameter candidate=2. depth(2)=2. depth(3)=1. At node 1: L=2, R=1, diameter candidate=3. Return max diameter = 3 (path: 4->2->1->3 or 5->2->1->3)."},
                    {"question": "Find LCA of 4 and 5 in tree: 3(5(6,2(7,4)),1(0,8))", "solution": "At 3: left=lca(5,4,5)=5, right=lca(1,4,5)=None. lca(5): root==p(5), return 5. Since only left found, LCA=5."},
                    {"question": "Is tree 1(2(3,null),4) balanced?", "solution": "height(3)=1. height(null)=0. Node 2: |1-0|=1, ok, height=2. height(4)=1. Node 1: |2-1|=1, ok. Balanced = True."}
                ],
            },
            {
                "title": "Mirror Tree, Symmetric & Tree Views",
                "content": "Mirror (Invert) a Binary Tree:\n  def mirror(root):\n      if not root: return None\n      root.left, root.right = root.right, root.left\n      mirror(root.left)\n      mirror(root.right)\n      return root\n\nCheck if Two Trees are Mirror Images:\n  def isMirror(t1, t2):\n      if not t1 and not t2: return True\n      if not t1 or not t2: return False\n      return (t1.val == t2.val and\n              isMirror(t1.left, t2.right) and\n              isMirror(t1.right, t2.left))\n\nSymmetric Tree: isMirror(root.left, root.right)\n\nLeft View (first node of each level):\n  Level order; append first element of each level.\n\nRight View (last node of each level):\n  Level order; append last element of each level.\n  Or recursive: go right first, track max level seen.\n\nTop View:\n  BFS with horizontal distance (HD). Root HD=0, left child HD-1, right child HD+1.\n  For each HD, store first node encountered. Print in HD order.\n\nBottom View:\n  Same as top view, but store last node encountered for each HD.\n\nVertical Order Traversal:\n  BFS with HD. Group nodes by HD. Within same HD, order by level then value.\n\nBoundary Traversal:\n  Left boundary (top to bottom) + Leaves (left to right) + Right boundary (bottom to top).",
                "key_points": [
                    "Mirror/invert tree is a simple recursion but tests understanding of tree structure",
                    "Symmetric tree = the tree is a mirror of itself",
                    "Views use BFS with horizontal distance (HD) concept",
                    "Top view: first node at each HD; Bottom view: last node at each HD",
                    "Boundary traversal combines three sub-problems - common in Amazon interviews"
                ],
                "examples": [
                    {"question": "Invert tree: 4(2(1,3),7(6,9))", "solution": "Swap children at each node. At 4: swap 2,7. At 7(now left): swap 6,9. At 2(now right): swap 1,3. Result: 4(7(9,6),2(3,1))."},
                    {"question": "Find left view of: 1(2(4,5),3(null,6))", "solution": "Level 0: [1] -> first = 1. Level 1: [2,3] -> first = 2. Level 2: [4,5,6] -> first = 4. Left view: [1, 2, 4]."},
                    {"question": "Top view of: 1(2(4,5),3(null,6)). HD: 1=0, 2=-1, 3=1, 4=-2, 5=0, 6=2", "solution": "HD -2: 4. HD -1: 2. HD 0: 1 (first encountered, not 5). HD 1: 3. HD 2: 6. Top view: [4, 2, 1, 3, 6]."}
                ],
            },
            {
                "title": "AVL Trees & Serialization",
                "content": "AVL Tree: Self-balancing BST where for every node, |height(left) - height(right)| <= 1.\n\nBalance Factor: BF(node) = height(left) - height(right). Valid: -1, 0, 1.\n\nRotations:\n1) Left Rotation (RR case): When right subtree is heavy.\n   y = x.right; x.right = y.left; y.left = x; return y\n2) Right Rotation (LL case): When left subtree is heavy.\n   y = x.left; x.left = y.right; y.right = x; return y\n3) Left-Right (LR case): Left rotate left child, then right rotate root.\n4) Right-Left (RL case): Right rotate right child, then left rotate root.\n\nInsertion: Insert like BST, then check BF bottom-up. If |BF| > 1, apply rotation.\n\nDeletion: Delete like BST, check BF bottom-up, apply rotations as needed.\n\nSerialization (convert tree to string) and Deserialization (string to tree):\n  Preorder with null markers:\n  def serialize(root):\n      if not root: return 'null,'\n      return str(root.val) + ',' + serialize(root.left) + serialize(root.right)\n\n  def deserialize(data):\n      vals = iter(data.split(','))\n      def build():\n          val = next(vals)\n          if val == 'null': return None\n          node = TreeNode(int(val))\n          node.left = build()\n          node.right = build()\n          return node\n      return build()\n\nBFS Serialization: Level order with null for missing children. Useful for LeetCode-style input.",
                "key_points": [
                    "AVL guarantees O(log n) for search/insert/delete by maintaining balance",
                    "Four rotation cases: LL, RR, LR, RL - know when each applies",
                    "Serialization with preorder + null markers is the simplest approach",
                    "AVL vs Red-Black: AVL is more strictly balanced, faster search; RB has fewer rotations on insert",
                    "Infosys and TCS ask theoretical AVL questions; Amazon/Microsoft ask serialization coding"
                ],
                "examples": [
                    {"question": "Insert 3,2,1 into AVL tree. Show rotations.", "solution": "Insert 3: root=3. Insert 2: 3(2,null). Insert 1: 3(2(1,null),null). BF(3)=2, LL case. Right rotate at 3: root=2(1,3). Balanced."},
                    {"question": "Serialize tree: 1(2,3(4,5))", "solution": "Preorder with nulls: 1,2,null,null,3,4,null,null,5,null,null"},
                    {"question": "Deserialize: '1,2,null,null,3,null,null'", "solution": "Read 1: root. Read 2: left of 1. Read null: left of 2 = null. Read null: right of 2 = null. Read 3: right of 1. Read null: left of 3 = null. Read null: right of 3 = null. Tree: 1(2,3)."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Binary Search Tree", "explanation": "Tree where left < root < right for all nodes. Inorder gives sorted sequence. Search/Insert/Delete are O(h)."},
            {"name": "Tree Traversals", "explanation": "Inorder (L,Root,R), Preorder (Root,L,R), Postorder (L,R,Root), Level-order (BFS). All are O(n) time."},
            {"name": "Lowest Common Ancestor", "explanation": "Deepest node that is ancestor of both p and q. For BST: use split point. For general tree: recursive check both subtrees."},
            {"name": "AVL Tree", "explanation": "Self-balancing BST. Balance factor = height(left) - height(right). If |BF| > 1, apply rotations (LL, RR, LR, RL)."},
            {"name": "Tree Diameter", "explanation": "Longest path between any two nodes. Computed as max(left_depth + right_depth) over all nodes. May not pass through root."}
        ],
        "formulas": [
            "Height of tree: h = 1 + max(h_left, h_right). O(n) time.",
            "Max nodes at level L = 2^L. Total nodes in complete tree of height h = 2^(h+1) - 1.",
            "Min height of tree with n nodes = floor(log2(n)). Max height = n-1 (skewed).",
            "BST search/insert/delete: O(h) where h = O(log n) balanced, O(n) skewed.",
            "AVL rotation: LL->Right rotate, RR->Left rotate, LR->Left then Right, RL->Right then Left."
        ],
        "solved_examples": [
            {"question": "Find if tree 1(2(3,4),2(4,3)) is symmetric.", "solution": "Check isMirror(left, right). left=2(3,4), right=2(4,3). 2==2, check isMirror(3,3) and isMirror(4,4). 3==3 (both leaves), 4==4 (both leaves). Symmetric = True."},
            {"question": "Find LCA of 5 and 1 in BST: 6(2(0,4(3,5)),8(7,9)).", "solution": "At 6: 5<6 and 1<6, go left. At 2: 5>2 and 1<2, split! LCA = 2."},
            {"question": "Build BST from preorder [8,5,1,7,10,12].", "solution": "8 is root. Elements < 8 go left: [5,1,7]. Elements > 8 go right: [10,12]. Recurse: 5(1,7) and 10(null,12). Tree: 8(5(1,7),10(null,12))."}
        ],
        "tips": [
            "For tree problems, always consider: What if the tree is empty? What if it has one node?",
            "Inorder + Preorder uniquely defines a binary tree. Inorder + Postorder also works. Preorder + Postorder does NOT (for general trees).",
            "Practice drawing trees from traversals - this is a common MCQ type in TCS and Infosys.",
            "For BST problems, think about the sorted property - inorder traversal is your friend.",
            "In interviews, always clarify if the tree is a BST or general binary tree - solutions differ significantly."
        ],
    },
    44: {
        "title": "Graphs",
        "overview": "Graphs are versatile data structures modeling relationships between objects. This topic covers representations (adjacency list/matrix), BFS, DFS, topological sort, shortest path algorithms (Dijkstra, Bellman-Ford), minimum spanning trees (Prim, Kruskal), and cycle detection. Graph problems are among the most popular in Amazon, Google, and Microsoft interviews.",
        "chapters": [
            {
                "title": "Graph Representation & BFS",
                "content": "Graph G = (V, E) consists of vertices V and edges E. Edges can be directed or undirected, weighted or unweighted.\n\nRepresentations:\n1) Adjacency Matrix: 2D array where matrix[i][j] = 1 (or weight) if edge exists.\n   Space: O(V^2). Good for dense graphs. Edge lookup: O(1).\n2) Adjacency List: Array of lists. adj[i] = list of neighbors of i.\n   Space: O(V+E). Good for sparse graphs. Edge lookup: O(degree).\n\nAdjacency List in Python:\n  graph = defaultdict(list)\n  graph[u].append(v)  # directed\n  graph[u].append(v); graph[v].append(u)  # undirected\n\nBFS (Breadth-First Search):\n  Uses queue. Visits all nodes at distance d before d+1.\n  def bfs(graph, start):\n      visited = set([start])\n      queue = deque([start])\n      while queue:\n          node = queue.popleft()\n          process(node)\n          for neighbor in graph[node]:\n              if neighbor not in visited:\n                  visited.add(neighbor)\n                  queue.append(neighbor)\n\nBFS Applications:\n- Shortest path in unweighted graph\n- Level order traversal\n- Connected components\n- Bipartite check (color nodes alternately)\n\nShortest Path (unweighted): BFS from source. dist[neighbor] = dist[node] + 1.\n\nBipartite Check: Try 2-coloring with BFS. If any neighbor has same color, not bipartite.",
                "key_points": [
                    "Adjacency list is preferred for sparse graphs (most real-world graphs)",
                    "BFS gives shortest path in unweighted graphs - Dijkstra is for weighted",
                    "BFS time: O(V+E), space: O(V) for visited set and queue",
                    "Bipartite check = 2-colorability = no odd-length cycle",
                    "Amazon and Google frequently ask BFS shortest-path and bipartite problems"
                ],
                "examples": [
                    {"question": "BFS traversal from node 0 in graph: 0-1, 0-2, 1-3, 2-3, 3-4", "solution": "Start 0, queue=[0]. Visit 0, add 1,2. Queue=[1,2]. Visit 1, add 3. Queue=[2,3]. Visit 2, 3 already queued. Queue=[3]. Visit 3, add 4. Queue=[4]. Visit 4. BFS order: 0,1,2,3,4."},
                    {"question": "Find shortest path from 0 to 4 in above graph", "solution": "BFS from 0: dist[0]=0. dist[1]=1, dist[2]=1. dist[3]=2 (from 1 or 2). dist[4]=3. Shortest path length = 3. Path: 0->1->3->4 or 0->2->3->4."},
                    {"question": "Is graph bipartite? Edges: 0-1, 1-2, 2-3, 3-0", "solution": "Color 0=Red. 1=Blue. 2=Red. 3=Blue. Check 3-0: Blue-Red, ok. Yes, bipartite."}
                ],
            },
            {
                "title": "DFS & Cycle Detection",
                "content": "DFS (Depth-First Search):\n  Uses recursion (implicit stack) or explicit stack. Goes as deep as possible before backtracking.\n\n  def dfs(graph, node, visited):\n      visited.add(node)\n      process(node)\n      for neighbor in graph[node]:\n          if neighbor not in visited:\n              dfs(graph, neighbor, visited)\n\nDFS Applications:\n- Cycle detection\n- Topological sort\n- Connected components / Strongly connected components\n- Path finding\n- Detecting back edges\n\nCycle Detection in Undirected Graph:\n  During DFS, if we encounter a visited node that is not the parent, cycle exists.\n  def hasCycle(graph, node, visited, parent):\n      visited.add(node)\n      for neighbor in graph[node]:\n          if neighbor not in visited:\n              if hasCycle(graph, neighbor, visited, node):\n                  return True\n          elif neighbor != parent:\n              return True  # Back edge = cycle\n      return False\n\nCycle Detection in Directed Graph:\n  Use three colors: White (unvisited), Gray (in current DFS path), Black (fully processed).\n  If we encounter a Gray node, cycle exists (back edge in DFS tree).\n  def hasCycleDG(graph, node, white, gray, black):\n      white.discard(node); gray.add(node)\n      for neighbor in graph[node]:\n          if neighbor in black: continue\n          if neighbor in gray: return True  # Cycle!\n          if hasCycleDG(graph, neighbor, white, gray, black):\n              return True\n      gray.discard(node); black.add(node)\n      return False\n\nConnected Components: Run DFS/BFS from each unvisited node. Count number of DFS calls.",
                "key_points": [
                    "DFS uses O(V) space for recursion stack in worst case",
                    "Cycle in undirected: visited neighbor != parent. Cycle in directed: Gray node revisited.",
                    "Three-color method is critical for directed graph cycle detection",
                    "DFS time complexity: O(V+E) same as BFS",
                    "TCS NQT and Infosys ask cycle detection frequently in MCQ format"
                ],
                "examples": [
                    {"question": "DFS traversal from 0: edges 0-1, 0-2, 1-3, 2-4, 3-4", "solution": "Start 0, visit 0. Go to 1, visit 1. Go to 3, visit 3. Go to 4, visit 4. Backtrack to 3, 1, 0. Go to 2, visit 2. 4 already visited. DFS: 0,1,3,4,2."},
                    {"question": "Detect cycle in undirected graph: edges 0-1, 1-2, 2-0", "solution": "DFS from 0 (parent=-1). Visit 1 (parent=0). Visit 2 (parent=1). Neighbor 0 is visited and 0 != parent(1). Cycle detected! Cycle: 0-1-2-0."},
                    {"question": "Detect cycle in directed graph: edges 0->1, 1->2, 2->0", "solution": "DFS from 0: color 0 Gray. Visit 1: color 1 Gray. Visit 2: color 2 Gray. Neighbor 0 is Gray (still in path). Cycle detected! 0->1->2->0."}
                ],
            },
            {
                "title": "Topological Sort",
                "content": "Topological sort is a linear ordering of vertices in a DAG (Directed Acyclic Graph) such that for every edge u->v, u comes before v.\n\nMethod 1: DFS-based (Kahn's reverse):\n  def topologicalSort(graph, V):\n      visited = set()\n      stack = []\n      def dfs(node):\n          visited.add(node)\n          for neighbor in graph[node]:\n              if neighbor not in visited:\n                  dfs(neighbor)\n          stack.append(node)  # add after all descendants\n      for v in range(V):\n          if v not in visited: dfs(v)\n      return stack[::-1]  # reverse\n\nMethod 2: Kahn's Algorithm (BFS-based, uses in-degree):\n  def kahnSort(graph, V):\n      in_degree = [0] * V\n      for u in graph:\n          for v in graph[u]: in_degree[v] += 1\n      queue = deque([v for v in range(V) if in_degree[v] == 0])\n      result = []\n      while queue:\n          node = queue.popleft()\n          result.append(node)\n          for neighbor in graph[node]:\n              in_degree[neighbor] -= 1\n              if in_degree[neighbor] == 0:\n                  queue.append(neighbor)\n      if len(result) != V: return 'Cycle exists'  # not a DAG\n      return result\n\nApplications:\n- Course scheduling (prerequisites)\n- Build system dependency resolution\n- Task ordering\n\nCycle detection in directed graph: If Kahn's algorithm processes fewer than V nodes, cycle exists.",
                "key_points": [
                    "Topological sort only works on DAGs (Directed Acyclic Graphs)",
                    "Kahn's algorithm also detects cycles - if result has fewer than V nodes, cycle exists",
                    "DFS-based: add to stack AFTER processing all neighbors, then reverse",
                    "Multiple valid topological orderings may exist for same graph",
                    "Course scheduling is the classic topological sort interview question (LeetCode 207, 210)"
                ],
                "examples": [
                    {"question": "Topological sort of: 5->0, 5->2, 4->0, 4->1, 2->3, 3->1", "solution": "Kahn's: in-degree: 0:2, 1:2, 2:1, 3:1, 4:0, 5:0. Start with [4,5]. Process 4: reduce 0,1. Process 5: reduce 0,2. Now 0 and 2 have in-degree 0. Process 0: nothing. Process 2: reduce 3. Process 3: reduce 1. Process 1. Order: [4,5,0,2,3,1] or [5,4,2,0,3,1]."},
                    {"question": "Can you take all courses? n=4, prereqs=[[1,0],[2,0],[3,1],[3,2]]", "solution": "Graph: 0->1, 0->2, 1->3, 2->3. Kahn's: in-degree 0:0, 1:1, 2:1, 3:2. Start [0]. Process 0: 1 and 2 become 0. Process 1: 3 becomes 1. Process 2: 3 becomes 0. Process 3. All 4 processed. Yes, all courses possible. Order: 0,1,2,3."},
                    {"question": "Detect cycle: edges 0->1, 1->2, 2->0", "solution": "Kahn's: in-degree all = 1. No node with in-degree 0. Queue starts empty. Result = []. len(result)=0 != V=3. Cycle exists!"}
                ],
            },
            {
                "title": "Shortest Path: Dijkstra & Bellman-Ford",
                "content": "Dijkstra's Algorithm (non-negative weights):\n  Finds shortest path from source to all vertices. Uses min-heap (priority queue).\n  def dijkstra(graph, src, V):\n      dist = [float('inf')] * V\n      dist[src] = 0\n      pq = [(0, src)]  # (distance, node)\n      while pq:\n          d, u = heapq.heappop(pq)\n          if d > dist[u]: continue  # skip outdated entry\n          for v, w in graph[u]:  # (neighbor, weight)\n              if dist[u] + w < dist[v]:\n                  dist[v] = dist[u] + w\n                  heapq.heappush(pq, (dist[v], v))\n      return dist\n  Time: O((V+E) log V) with min-heap.\n\nBellman-Ford Algorithm (handles negative weights):\n  Relax all edges V-1 times. Detects negative cycles on Vth pass.\n  def bellmanFord(edges, V, src):\n      dist = [float('inf')] * V\n      dist[src] = 0\n      for _ in range(V - 1):\n          for u, v, w in edges:\n              if dist[u] != float('inf') and dist[u] + w < dist[v]:\n                  dist[v] = dist[u] + w\n      # Check for negative cycle\n      for u, v, w in edges:\n          if dist[u] != float('inf') and dist[u] + w < dist[v]:\n              return 'Negative cycle'\n      return dist\n  Time: O(V * E).\n\nWhen to use which:\n- All non-negative weights: Dijkstra (faster)\n- Negative weights possible: Bellman-Ford\n- Unweighted graph: BFS (simplest)\n- All-pairs shortest path: Floyd-Warshall O(V^3)",
                "key_points": [
                    "Dijkstra FAILS with negative edge weights - use Bellman-Ford instead",
                    "Dijkstra with min-heap: O((V+E)log V). Bellman-Ford: O(VE)",
                    "Bellman-Ford detects negative weight cycles on the Vth iteration",
                    "Floyd-Warshall finds all-pairs shortest paths in O(V^3)",
                    "Dijkstra is extremely common in Amazon and Google interviews"
                ],
                "examples": [
                    {"question": "Dijkstra from node 0: edges 0->1(4), 0->2(1), 2->1(2), 1->3(1), 2->3(5)", "solution": "dist=[0,inf,inf,inf]. PQ=[(0,0)]. Pop (0,0): update 1=4, 2=1. PQ=[(1,2),(4,1)]. Pop (1,2): update 1=min(4,1+2)=3. PQ=[(3,1),(4,1),(6,3)]. Pop (3,1): update 3=min(inf,3+1)=4. Pop (4,1) skip. Pop (6,3) skip (4<6). Final: [0,3,1,4]."},
                    {"question": "Bellman-Ford from 0: edges 0->1(1), 1->2(-1), 0->2(4)", "solution": "Init dist=[0,inf,inf]. Pass 1: Edge 0->1: dist[1]=1. Edge 1->2: dist[2]=0. Edge 0->2: dist[2]=min(0,4)=0. Pass 2: No changes. Final: [0,1,0]. No negative cycle."},
                    {"question": "Detect negative cycle: edges 0->1(1), 1->2(-1), 2->0(-1)", "solution": "dist=[0,inf,inf]. Pass 1: dist=[0,1,0]. Pass 2: Edge 2->0: 0+(-1)=-1 < 0, dist[0]=-1. dist=[-1,0,-1]. After V-1=2 passes, check: edge 2->0: -1+(-1)=-2 < -1. Negative cycle detected!"}
                ],
            },
            {
                "title": "Minimum Spanning Tree & Advanced Topics",
                "content": "Minimum Spanning Tree (MST): A spanning tree with minimum total edge weight. A tree with V-1 edges connecting all V vertices.\n\nKruskal's Algorithm:\n  Sort all edges by weight. Add edges greedily if they don't form a cycle (use Union-Find).\n  def kruskal(edges, V):\n      edges.sort(key=lambda x: x[2])  # sort by weight\n      parent = list(range(V))\n      rank = [0] * V\n      mst = []; cost = 0\n      for u, v, w in edges:\n          if find(parent, u) != find(parent, v):\n              union(parent, rank, u, v)\n              mst.append((u, v, w))\n              cost += w\n      return cost, mst\n  Time: O(E log E) for sorting.\n\nPrim's Algorithm:\n  Start from any vertex. Greedily add cheapest edge connecting MST to non-MST vertex.\n  def prim(graph, V):\n      visited = set(); cost = 0\n      pq = [(0, 0)]  # (weight, node)\n      while pq and len(visited) < V:\n          w, u = heapq.heappop(pq)\n          if u in visited: continue\n          visited.add(u); cost += w\n          for v, wt in graph[u]:\n              if v not in visited:\n                  heapq.heappush(pq, (wt, v))\n      return cost\n  Time: O((V+E) log V) with min-heap.\n\nUnion-Find (Disjoint Set Union):\n  find(x): Follow parent pointers to root. Path compression: point all to root.\n  union(x, y): Merge sets. Union by rank for efficiency.\n  def find(parent, x):\n      if parent[x] != x: parent[x] = find(parent, parent[x])\n      return parent[x]",
                "key_points": [
                    "Kruskal's sorts edges and uses Union-Find; Prim's uses priority queue from a vertex",
                    "MST has exactly V-1 edges for V vertices",
                    "Union-Find with path compression and union by rank: nearly O(1) per operation",
                    "Kruskal's is better for sparse graphs; Prim's for dense graphs",
                    "MST and Union-Find are asked in Amazon, Microsoft, and Google interviews"
                ],
                "examples": [
                    {"question": "Find MST using Kruskal's: edges (0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)", "solution": "Sort: (2,3,4),(0,3,5),(0,2,6),(0,1,10),(1,3,15). Add (2,3,4): no cycle. Add (0,3,5): no cycle. Add (0,2,6): 0 and 2 already connected via 3, skip. Add (0,1,10): no cycle. MST edges: (2,3,4),(0,3,5),(0,1,10). Cost = 19."},
                    {"question": "Prim's from node 0: same graph", "solution": "Start 0. Edges from 0: (1,10),(2,6),(3,5). Pick min (3,5). From {0,3}: edges (1,15),(2,4). Pick (2,4). From {0,2,3}: edge (1,10). Pick (1,10). MST cost = 5+4+10 = 19."},
                    {"question": "Union-Find: union(0,1), union(2,3), union(1,3). Find connected components.", "solution": "Initially: parent=[0,1,2,3]. union(0,1): parent[1]=0. union(2,3): parent[3]=2. union(1,3): find(1)=0, find(3)=2, parent[2]=0. All in one component. Components = 1."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "BFS", "explanation": "Level-by-level exploration using queue. Gives shortest path in unweighted graphs. Time: O(V+E)."},
            {"name": "DFS", "explanation": "Depth-first exploration using stack/recursion. Used for cycle detection, topological sort, connected components. Time: O(V+E)."},
            {"name": "Dijkstra's Algorithm", "explanation": "Greedy shortest path for non-negative weights. Uses min-heap. Time: O((V+E)log V). Fails with negative weights."},
            {"name": "Topological Sort", "explanation": "Linear ordering of DAG vertices. Kahn's (BFS with in-degree) or DFS-based. Used for dependency resolution."},
            {"name": "MST (Kruskal/Prim)", "explanation": "Minimum weight tree connecting all vertices. Kruskal's: sort edges + Union-Find. Prim's: grow tree greedily with min-heap."}
        ],
        "formulas": [
            "BFS/DFS time: O(V+E); space: O(V)",
            "Dijkstra: O((V+E) log V) with binary heap",
            "Bellman-Ford: O(V*E); detects negative cycles",
            "Kruskal: O(E log E); Prim with heap: O((V+E) log V)",
            "MST has exactly V-1 edges for a connected graph with V vertices"
        ],
        "solved_examples": [
            {"question": "Find number of connected components in graph with 5 nodes, edges: 0-1, 2-3.", "solution": "BFS/DFS from 0: visits {0,1}. From 2: visits {2,3}. Node 4 alone. Components = 3."},
            {"question": "Topological sort of: A->B, A->C, B->D, C->D.", "solution": "In-degree: A=0, B=1, C=1, D=2. Start with A. Process A: B,C become 0. Process B: D becomes 1. Process C: D becomes 0. Process D. Order: A,B,C,D or A,C,B,D."},
            {"question": "Shortest path from S to all in weighted graph: S->A(1), S->B(4), A->B(2), A->C(6), B->C(3).", "solution": "Dijkstra: dist=[S:0, A:inf, B:inf, C:inf]. Process S: A=1, B=4. Process A: B=min(4,3)=3, C=7. Process B: C=min(7,6)=6. Final: S=0, A=1, B=3, C=6."}
        ],
        "tips": [
            "BFS for shortest path in unweighted, Dijkstra for weighted (non-negative), Bellman-Ford for negative weights.",
            "Always check if graph is directed or undirected - cycle detection logic differs.",
            "For MST problems, know both Kruskal's and Prim's - interviews may ask for a specific one.",
            "Union-Find is also useful standalone for dynamic connectivity problems.",
            "Graph problems are the hardest category in interviews - practice at least 30 problems on LeetCode."
        ],
    },
    45: {
        "title": "Hashing",
        "overview": "Hashing provides O(1) average-case lookup, insertion, and deletion. It is the backbone of hash maps, hash sets, and frequency counting. This topic covers hash functions, collision handling, and classic problems like two sum, anagram grouping, and frequency-based questions that are staples in every placement exam from TCS to Amazon.",
        "chapters": [
            {
                "title": "Hash Table Fundamentals",
                "content": "A hash table maps keys to values using a hash function that converts keys to array indices.\n\nHash Function: h(key) = key % table_size\nGood hash function properties: Deterministic, uniform distribution, fast to compute.\n\nCollision: When two keys hash to the same index.\n\nCollision Handling:\n1) Chaining (Open Hashing):\n   Each bucket stores a linked list of entries.\n   Insert: O(1). Search/Delete: O(1) avg, O(n) worst (all in one chain).\n   Load factor alpha = n/m (n entries, m buckets).\n   Average chain length = alpha.\n\n2) Open Addressing (Closed Hashing):\n   All entries stored in the table itself. On collision, probe for next empty slot.\n   a) Linear Probing: h(k,i) = (h(k) + i) % m\n      Problem: Primary clustering.\n   b) Quadratic Probing: h(k,i) = (h(k) + i^2) % m\n      Problem: Secondary clustering.\n   c) Double Hashing: h(k,i) = (h1(k) + i*h2(k)) % m\n      Best distribution, no clustering.\n\nPython dict is a hash map. set is a hash set.\n  d = {}; d['key'] = value  # O(1) avg\n  s = set(); s.add(val)     # O(1) avg\n  val in d  # O(1) avg lookup\n\nLoad Factor and Rehashing:\n  When load factor > threshold (e.g., 0.75), resize table (usually double) and rehash all entries.",
                "key_points": [
                    "Hash table operations are O(1) average, O(n) worst case",
                    "Chaining is simpler; open addressing has better cache performance",
                    "Load factor = n/m. Rehash when it exceeds threshold (typically 0.75)",
                    "Double hashing avoids both primary and secondary clustering",
                    "TCS and Infosys frequently ask theoretical hashing questions in MCQ format"
                ],
                "examples": [
                    {"question": "Insert keys 5, 28, 19, 15, 20, 33, 12 into hash table of size 7 using h(k)=k%7 with chaining.", "solution": "5%7=5, 28%7=0, 19%7=5, 15%7=1, 20%7=6, 33%7=5, 12%7=5. Buckets: 0:[28], 1:[15], 5:[5,19,33,12], 6:[20]. Others empty."},
                    {"question": "Insert 10, 22, 31, 4, 15 into table size 11 using linear probing, h(k)=k%11", "solution": "10%11=10: slot 10. 22%11=0: slot 0. 31%11=9: slot 9. 4%11=4: slot 4. 15%11=4: collision! Probe 5: empty, slot 5. Table: [22,_,_,_,4,15,_,_,_,31,10]."},
                    {"question": "Calculate load factor: 8 entries in table of size 10.", "solution": "Load factor = 8/10 = 0.8. This exceeds typical threshold of 0.75, so rehashing would be triggered."}
                ],
            },
            {
                "title": "HashMap Patterns: Two Sum & Frequency Counting",
                "content": "Two Sum (find pair with given sum):\n  def twoSum(nums, target):\n      seen = {}  # value -> index\n      for i, num in enumerate(nums):\n          complement = target - num\n          if complement in seen:\n              return [seen[complement], i]\n          seen[num] = i\n  Time: O(n), Space: O(n)\n\nFrequency Counting:\n  from collections import Counter\n  freq = Counter(arr)  # {element: count}\n  # Or manually:\n  freq = {}\n  for x in arr:\n      freq[x] = freq.get(x, 0) + 1\n\nFirst Non-Repeating Character:\n  freq = Counter(s)\n  for ch in s:\n      if freq[ch] == 1: return ch\n\nSubarray Sum Equals K (using prefix sum + hashmap):\n  def subarraySum(nums, k):\n      count = 0; prefix = 0\n      prefix_count = {0: 1}\n      for num in nums:\n          prefix += num\n          if prefix - k in prefix_count:\n              count += prefix_count[prefix - k]\n          prefix_count[prefix] = prefix_count.get(prefix, 0) + 1\n      return count\n\nLongest Subarray with Sum K:\n  Store first occurrence of each prefix sum. If prefix[j] - prefix[i] = k, subarray i+1..j has sum k.\n  Length = j - first_occurrence_of(prefix - k).",
                "key_points": [
                    "Two Sum with HashMap is THE most asked coding question across all companies",
                    "Prefix sum + HashMap solves many subarray-sum problems in O(n)",
                    "Counter/frequency map is the go-to tool for counting problems",
                    "Store first occurrence for longest subarray, count occurrences for count of subarrays",
                    "These patterns appear in Amazon, Google, Flipkart, and TCS NQT"
                ],
                "examples": [
                    {"question": "Two Sum: nums=[2,7,11,15], target=9", "solution": "i=0: complement=9-2=7, not in seen. seen={2:0}. i=1: complement=9-7=2, 2 in seen! Return [0,1]."},
                    {"question": "Count subarrays with sum=3 in [1,2,3,-1,1,3]", "solution": "prefix_count={0:1}. prefix: 1->{1:1}. 3->{3:1}, 3-0=3 in map, count=1. 6->{6:1}, 6-3=3 in map, count=2. 5->{5:1}. 6->{6:2}, 6-3=3 in map (once), count=3. 9->{9:1}, 9-3=6 in map (twice), count=5. Answer: 5."},
                    {"question": "First non-repeating character in 'aabbcdde'", "solution": "freq: a=2, b=2, c=1, d=2, e=1. Scan string: a(2,skip), a(skip), b(skip), b(skip), c(1, found!). Answer: 'c'."}
                ],
            },
            {
                "title": "Anagram & Grouping Problems",
                "content": "Anagram: Two strings are anagrams if they contain same characters with same frequency.\n\nCheck Anagram:\n  Method 1: Sort both strings, compare. O(n log n).\n  Method 2: Frequency count comparison. O(n).\n  def isAnagram(s, t):\n      return Counter(s) == Counter(t)\n\nGroup Anagrams:\n  Key insight: All anagrams have the same sorted form.\n  def groupAnagrams(strs):\n      groups = defaultdict(list)\n      for s in strs:\n          key = tuple(sorted(s))\n          groups[key].append(s)\n      return list(groups.values())\n  Time: O(n * k log k) where k is max string length.\n  Alternative key: tuple of character counts (26 elements for lowercase).\n\nValid Anagram with Unicode:\n  Use Counter for arbitrary characters, not just a-z.\n\nContains Duplicate within Distance K:\n  Use HashMap storing value -> last index. If same value found within k distance, return True.\n  def containsNearbyDuplicate(nums, k):\n      seen = {}  # value -> index\n      for i, num in enumerate(nums):\n          if num in seen and i - seen[num] <= k:\n              return True\n          seen[num] = i\n      return False\n\nIntersection of Two Arrays:\n  Use set intersection: set(nums1) & set(nums2)\n  For maintaining count: use Counter and take min of counts.",
                "key_points": [
                    "Sorted string is the canonical key for anagram grouping",
                    "Counter comparison for anagram check is O(n) - faster than sorting",
                    "Group anagrams uses HashMap with sorted-string keys",
                    "Set operations (union, intersection, difference) are O(min(len(s1), len(s2)))",
                    "Anagram questions are common in TCS, Infosys, Wipro placement exams"
                ],
                "examples": [
                    {"question": "Group anagrams: ['eat','tea','tan','ate','nat','bat']", "solution": "Sort keys: eat->'aet', tea->'aet', tan->'ant', ate->'aet', nat->'ant', bat->'abt'. Groups: {aet:[eat,tea,ate], ant:[tan,nat], abt:[bat]}."},
                    {"question": "Check if 'listen' and 'silent' are anagrams", "solution": "Counter('listen')={l:1,i:1,s:1,t:1,e:1,n:1}. Counter('silent')={s:1,i:1,l:1,e:1,n:1,t:1}. Equal? Yes. Anagram!"},
                    {"question": "Find duplicates within distance 2 in [1,2,3,1,2,3]", "solution": "i=0: seen={1:0}. i=1: seen={1:0,2:1}. i=2: seen={1:0,2:1,3:2}. i=3: 1 in seen, 3-0=3 > 2, update seen={1:3,...}. i=4: 2 in seen, 4-1=3 > 2, update. i=5: 3 in seen, 5-2=3 > 2, update. No duplicate within distance 2. Return False."}
                ],
            },
            {
                "title": "Advanced Hashing: Longest Consecutive Sequence & 4Sum",
                "content": "Longest Consecutive Sequence:\n  Given unsorted array, find length of longest consecutive elements sequence in O(n).\n  def longestConsecutive(nums):\n      num_set = set(nums)\n      best = 0\n      for num in num_set:\n          if num - 1 not in num_set:  # start of a sequence\n              curr = num; length = 1\n              while curr + 1 in num_set:\n                  curr += 1; length += 1\n              best = max(best, length)\n      return best\n  Key insight: Only start counting from sequence beginnings (num-1 not in set).\n  Time: O(n) - each number visited at most twice.\n\n4Sum Pattern (generalized k-sum):\n  Two Sum: O(n) with HashMap.\n  Three Sum: Sort + Two Pointer. O(n^2).\n  Four Sum: Sort + fix one + Three Sum. O(n^3).\n\n  def threeSum(nums, target):\n      nums.sort(); result = []\n      for i in range(len(nums) - 2):\n          if i > 0 and nums[i] == nums[i-1]: continue\n          left, right = i+1, len(nums)-1\n          while left < right:\n              s = nums[i] + nums[left] + nums[right]\n              if s == target: result.append([nums[i],nums[left],nums[right]])\n                  # skip duplicates\n              if s <= target: left += 1\n              if s >= target: right -= 1\n      return result\n\nSubstring with Concatenation of All Words:\n  Use HashMap of word frequencies. Sliding window of total_length. Check each window.",
                "key_points": [
                    "Longest consecutive sequence: start only from sequence beginnings for O(n)",
                    "Three Sum = sort + two pointer. Four Sum adds one more loop.",
                    "Skip duplicates in k-sum problems to avoid duplicate triplets/quadruplets",
                    "Set lookup is O(1) average - converting array to set enables fast membership tests",
                    "These are frequently asked in Amazon, Google, and Microsoft coding interviews"
                ],
                "examples": [
                    {"question": "Longest consecutive in [100,4,200,1,3,2]", "solution": "Set: {100,4,200,1,3,2}. Start at 1 (0 not in set): 1,2,3,4 -> length 4. Start at 100: length 1. Start at 200: length 1. Answer: 4."},
                    {"question": "Three Sum = 0 in [-1,0,1,2,-1,-4]", "solution": "Sort: [-4,-1,-1,0,1,2]. i=0(-4): left=-1,right=2, sum=-3<0. left=-1,right=2, sum=-3. left=0,right=2, sum=-2. No triplet. i=1(-1): left=-1,right=2, sum=0! Found [-1,-1,2]. left=0,right=1, sum=0! Found [-1,0,1]. i=2(-1): skip duplicate. Answer: [[-1,-1,2],[-1,0,1]]."},
                    {"question": "Find if array has two elements summing to 0: [3,-3,5,1,-1]", "solution": "HashMap approach: see 3, store {3:0}. See -3, complement=0-(-3)=3. But we need sum=0: complement=0-(-3)=3, 3 in seen! Return True. Pair: (3,-3)."}
                ],
            },
            {
                "title": "Hashing in Strings & Design Problems",
                "content": "Rabin-Karp String Matching uses rolling hash:\n  Hash a window of text, compare with pattern hash. On match, verify character by character.\n  Rolling hash: h(s[i+1..i+m]) = (h(s[i..i+m-1]) - s[i]*d^(m-1)) * d + s[i+m]\n  Average: O(n+m), Worst: O(nm) due to hash collisions.\n\nDesign a HashMap from scratch:\n  class MyHashMap:\n      def __init__(self):\n          self.size = 1000\n          self.buckets = [[] for _ in range(self.size)]\n      def _hash(self, key): return key % self.size\n      def put(self, key, val):\n          bucket = self.buckets[self._hash(key)]\n          for i, (k, v) in enumerate(bucket):\n              if k == key: bucket[i] = (key, val); return\n          bucket.append((key, val))\n      def get(self, key):\n          for k, v in self.buckets[self._hash(key)]:\n              if k == key: return v\n          return -1\n      def remove(self, key):\n          bucket = self.buckets[self._hash(key)]\n          for i, (k, v) in enumerate(bucket):\n              if k == key: del bucket[i]; return\n\nConsistent Hashing (distributed systems):\n  Used in load balancing and distributed caches.\n  Nodes placed on a virtual ring. Keys hashed to ring, served by next clockwise node.\n  Adding/removing a node only affects neighbors.\n\nBloom Filter: Probabilistic set membership. No false negatives, possible false positives. Uses multiple hash functions.",
                "key_points": [
                    "Rabin-Karp uses rolling hash for efficient string matching",
                    "Designing a HashMap is a common system design / OOP interview question",
                    "Consistent hashing is important for system design interviews at Amazon, Google",
                    "Bloom filters trade accuracy for space efficiency - know the concept",
                    "Hash collisions are a favorite MCQ topic in GATE and placement exams"
                ],
                "examples": [
                    {"question": "Rabin-Karp: Find 'abc' in 'xabcabcy' using hash = sum of ASCII values", "solution": "Pattern hash = a+b+c = 97+98+99 = 294. Window 'xab' = 120+97+98 = 315. Slide: 'abc' = 97+98+99 = 294. Match! Verify chars: a==a, b==b, c==c. Found at index 1."},
                    {"question": "Design: MyHashMap put(1,1), put(2,2), get(1), get(3), put(2,1), get(2)", "solution": "put(1,1): bucket[1]=[(1,1)]. put(2,2): bucket[2]=[(2,2)]. get(1): hash=1, find key 1, return 1. get(3): hash=3, empty, return -1. put(2,1): hash=2, key 2 exists, update to (2,1). get(2): return 1."},
                    {"question": "Linear probing: Insert 10, 22, 31, 4, 15, 28, 17 into table size 11, h(k)=k%11. How many collisions?", "solution": "10->10(0). 22->0(0). 31->9(0). 4->4(0). 15->4 collision! Probe 5(1). 28->6(0). 17->6 collision! Probe 7(1). Total collisions: 2."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Hash Function", "explanation": "Maps keys to array indices. Good function: deterministic, uniform distribution, fast. Common: h(k) = k % m."},
            {"name": "Collision Handling", "explanation": "Chaining: linked lists at buckets. Open addressing: linear probing, quadratic probing, double hashing. Chaining is simpler, open addressing has better cache."},
            {"name": "Two Sum Pattern", "explanation": "Store complement in HashMap. For each element, check if target-element exists. O(n) time, O(n) space."},
            {"name": "Frequency Counting", "explanation": "Use HashMap/Counter to count occurrences. Foundation for anagram, mode, majority element problems."},
            {"name": "Prefix Sum + HashMap", "explanation": "Count/find subarrays with given sum. Store prefix sum frequencies. Check if (current_prefix - target) exists."}
        ],
        "formulas": [
            "Hash function: h(k) = k % m (m = table size, ideally prime)",
            "Load factor: alpha = n/m. Rehash when alpha > 0.75",
            "Linear probing: h(k,i) = (h(k) + i) % m",
            "Double hashing: h(k,i) = (h1(k) + i*h2(k)) % m",
            "Average search in chaining: O(1 + alpha). In open addressing: O(1/(1-alpha))"
        ],
        "solved_examples": [
            {"question": "Two Sum: Find indices of two numbers summing to 6 in [3, 2, 4].", "solution": "i=0(3): complement=3, seen={}. Not found. seen={3:0}. i=1(2): complement=4, not in seen. seen={3:0,2:1}. i=2(4): complement=2, found at index 1! Return [1,2]."},
            {"question": "Group anagrams: ['abc','bca','xyz','zyx','cab'].", "solution": "Sort keys: abc->abc, bca->abc, xyz->xyz, zyx->xyz, cab->abc. Groups: {abc:[abc,bca,cab], xyz:[xyz,zyx]}."},
            {"question": "Longest consecutive sequence in [0,3,7,2,5,8,4,6,0,1].", "solution": "Set: {0,1,2,3,4,5,6,7,8}. Start at 0 (no -1): count 0,1,2,3,4,5,6,7,8 = length 9. Answer: 9."}
        ],
        "tips": [
            "Two Sum is the gateway problem - master it and its variations (3Sum, 4Sum, subarray sum).",
            "In placement MCQs, hashing collision questions use specific probing sequences - trace carefully.",
            "Python dict and set are hash-based: O(1) average operations. Use them freely.",
            "For interview coding, always mention the time-space tradeoff of hashing: O(1) time at cost of O(n) space.",
            "Know the difference between HashMap and HashSet: map stores key-value pairs, set stores only keys."
        ],
    },
    46: {
        "title": "Dynamic Programming",
        "overview": "Dynamic Programming (DP) solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation. This topic covers memoization vs tabulation, 1D and 2D DP, knapsack variants, LCS, LIS, coin change, and matrix chain multiplication. DP is the most feared yet most rewarding topic in coding interviews at Amazon, Google, and Microsoft.",
        "chapters": [
            {
                "title": "DP Fundamentals: Memoization vs Tabulation",
                "content": "Dynamic Programming applies when a problem has:\n1) Optimal Substructure: Optimal solution contains optimal solutions of subproblems.\n2) Overlapping Subproblems: Same subproblems solved repeatedly.\n\nTwo Approaches:\n\nTop-Down (Memoization): Recursive + cache.\n  def fib(n, memo={}):\n      if n <= 1: return n\n      if n in memo: return memo[n]\n      memo[n] = fib(n-1, memo) + fib(n-2, memo)\n      return memo[n]\n  Time: O(n), Space: O(n)\n\nBottom-Up (Tabulation): Iterative, fill table.\n  def fib(n):\n      if n <= 1: return n\n      dp = [0] * (n+1)\n      dp[1] = 1\n      for i in range(2, n+1):\n          dp[i] = dp[i-1] + dp[i-2]\n      return dp[n]\n  Space-optimized (O(1)): Only keep last two values.\n  def fib(n):\n      a, b = 0, 1\n      for _ in range(2, n+1):\n          a, b = b, a+b\n      return b\n\nClimbing Stairs (ways to reach nth stair, 1 or 2 steps):\n  Exactly Fibonacci! dp[i] = dp[i-1] + dp[i-2].\n\nHouse Robber (max loot, cannot rob adjacent houses):\n  dp[i] = max(dp[i-1], dp[i-2] + nums[i])\n  At each house: skip it (dp[i-1]) or rob it (dp[i-2] + nums[i]).\n\nRecurrence Identification Steps:\n  1. Define state: What does dp[i] represent?\n  2. Find transition: How does dp[i] relate to smaller subproblems?\n  3. Base cases: What are dp[0], dp[1]?\n  4. Answer: Which dp entry is the final answer?",
                "key_points": [
                    "Memoization = top-down (recursive), Tabulation = bottom-up (iterative)",
                    "Tabulation is generally preferred: no recursion overhead, easier to optimize space",
                    "Always try to reduce space: if dp[i] depends only on dp[i-1] and dp[i-2], use two variables",
                    "Climbing stairs = Fibonacci is the simplest DP problem - start here",
                    "House Robber pattern (take or skip) appears in many variations"
                ],
                "examples": [
                    {"question": "Climbing stairs: How many ways to reach step 5?", "solution": "dp[1]=1, dp[2]=2, dp[3]=3, dp[4]=5, dp[5]=8. Answer: 8 ways."},
                    {"question": "House Robber: nums=[2,7,9,3,1]", "solution": "dp[0]=2, dp[1]=max(2,7)=7, dp[2]=max(7,2+9)=11, dp[3]=max(11,7+3)=11, dp[4]=max(11,11+1)=12. Answer: 12 (rob houses 0,2,4: 2+9+1=12)."},
                    {"question": "Min cost climbing stairs: cost=[10,15,20]", "solution": "dp[0]=10, dp[1]=15, dp[2]=min(dp[0],dp[1])+20=min(10,15)+20=30. Can start from step 0 or 1. Answer: min(dp[1],dp[2])=min(15,30)=15. Wait - we want to reach top (beyond last step). dp[3]=min(dp[1],dp[2])=min(15,30)=15. Answer: 15."}
                ],
            },
            {
                "title": "0/1 Knapsack & Variants",
                "content": "0/1 Knapsack: Given n items with weights and values, maximize value within capacity W. Each item used at most once.\n\n  def knapsack(W, wt, val, n):\n      dp = [[0]*(W+1) for _ in range(n+1)]\n      for i in range(1, n+1):\n          for w in range(1, W+1):\n              if wt[i-1] <= w:\n                  dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])\n              else:\n                  dp[i][w] = dp[i-1][w]\n      return dp[n][W]\n  Time: O(nW), Space: O(nW) -> can optimize to O(W) with 1D array.\n\n1D optimization (traverse W right to left):\n  dp = [0] * (W+1)\n  for i in range(n):\n      for w in range(W, wt[i]-1, -1):\n          dp[w] = max(dp[w], dp[w-wt[i]] + val[i])\n\nSubset Sum: Is there a subset summing to target?\n  dp[i][s] = dp[i-1][s] OR dp[i-1][s-nums[i]]\n  (Skip item i or include it.)\n\nEqual Partition: Can array be split into two equal-sum subsets?\n  If total sum is odd, impossible. Else, find subset with sum = total/2.\n\nCount of Subset Sum: How many subsets sum to target?\n  dp[i][s] = dp[i-1][s] + dp[i-1][s-nums[i]]\n\nMinimum Subset Sum Difference:\n  Find subset sum closest to total/2. Answer = total - 2*closest.",
                "key_points": [
                    "0/1 Knapsack is the foundation - learn it thoroughly, all variants derive from it",
                    "For 0/1 knapsack 1D optimization, iterate capacity RIGHT TO LEFT",
                    "For unbounded knapsack, iterate LEFT TO RIGHT (item can be reused)",
                    "Subset sum, equal partition, count subsets are all knapsack variants",
                    "Knapsack is extremely common in Amazon, Google, and Microsoft interviews"
                ],
                "examples": [
                    {"question": "0/1 Knapsack: W=7, items: (wt=1,val=1),(wt=3,val=4),(wt=4,val=5),(wt=5,val=7)", "solution": "Optimal: take items 2(wt3,val4) and 3(wt4,val5). Total weight=7, value=9. dp table build: dp[4][7]=9."},
                    {"question": "Subset Sum: nums=[3,34,4,12,5,2], target=9", "solution": "Subsets summing to 9: {4,5}, {3,4,2}. dp[6][9]=True. Answer: Yes."},
                    {"question": "Equal partition: [1,5,11,5]", "solution": "Total=22, target=11. Find subset sum 11: {1,5,5} or {11}. dp[4][11]=True. Can partition into {1,5,5} and {11}. Answer: Yes."}
                ],
            },
            {
                "title": "LCS, LIS & String DP",
                "content": "Longest Common Subsequence (LCS):\n  def lcs(s1, s2):\n      m, n = len(s1), len(s2)\n      dp = [[0]*(n+1) for _ in range(m+1)]\n      for i in range(1, m+1):\n          for j in range(1, n+1):\n              if s1[i-1] == s2[j-1]:\n                  dp[i][j] = dp[i-1][j-1] + 1\n              else:\n                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n      return dp[m][n]\n  Time: O(mn), Space: O(mn) -> O(n) with rolling array.\n\nLCS Variants:\n- Longest Common Substring: dp[i][j] = dp[i-1][j-1]+1 if match, else 0. Answer = max of table.\n- Shortest Common Supersequence: len = m + n - LCS(s1,s2)\n- Edit Distance: dp[i][j] = min(insert, delete, replace) operations.\n  if s1[i-1]==s2[j-1]: dp[i][j]=dp[i-1][j-1]\n  else: dp[i][j]=1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])\n\nLongest Increasing Subsequence (LIS):\n  O(n^2) approach:\n  dp = [1] * n\n  for i in range(1, n):\n      for j in range(i):\n          if arr[j] < arr[i]: dp[i] = max(dp[i], dp[j]+1)\n  answer = max(dp)\n\n  O(n log n) approach using patience sorting:\n  tails = []\n  for num in arr:\n      pos = bisect_left(tails, num)\n      if pos == len(tails): tails.append(num)\n      else: tails[pos] = num\n  return len(tails)\n\nPalindrome Problems:\n- Longest Palindromic Subsequence = LCS(s, reverse(s))\n- Longest Palindromic Substring: Expand around center O(n^2) or Manacher's O(n).",
                "key_points": [
                    "LCS recurrence: match -> diagonal+1, no match -> max(up, left)",
                    "LIS O(n log n) with binary search is much faster than O(n^2) DP",
                    "Edit distance is asked by Google, Amazon - know insert/delete/replace cases",
                    "Longest palindromic subsequence = LCS(s, reverse(s)) - elegant reduction",
                    "String DP problems require careful index management - off-by-one errors are common"
                ],
                "examples": [
                    {"question": "LCS of 'ABCBDAB' and 'BDCAB'", "solution": "Build dp table. LCS = 'BCAB' (length 4). Trace back: B matches at end, then C, then A, then B."},
                    {"question": "LIS of [10, 9, 2, 5, 3, 7, 101, 18]", "solution": "dp approach: dp=[1,1,1,2,2,3,4,4]. Max=4. LIS: [2,3,7,101] or [2,5,7,18]. O(n log n): tails evolves as [10],[9],[2],[2,5],[2,3],[2,3,7],[2,3,7,101],[2,3,7,18]. Length=4."},
                    {"question": "Edit distance: 'horse' to 'ros'", "solution": "dp table (5x3): horse->rorse(replace h->r), rorse->rose(remove r), rose->ros(remove e). Distance = 3."}
                ],
            },
            {
                "title": "Coin Change & Grid DP",
                "content": "Coin Change (minimum coins):\n  def coinChange(coins, amount):\n      dp = [float('inf')] * (amount+1)\n      dp[0] = 0\n      for coin in coins:\n          for a in range(coin, amount+1):\n              dp[a] = min(dp[a], dp[a-coin] + 1)\n      return dp[amount] if dp[amount] != float('inf') else -1\n  Time: O(n*amount), unbounded knapsack variant (left to right).\n\nCoin Change 2 (count ways):\n  dp = [0] * (amount+1); dp[0] = 1\n  for coin in coins:\n      for a in range(coin, amount+1):\n          dp[a] += dp[a-coin]\n  Note: Coin loop outside amount loop to avoid counting permutations.\n\nUnique Paths in Grid:\n  dp[i][j] = dp[i-1][j] + dp[i][j-1]  (from top + from left)\n  With obstacles: dp[i][j] = 0 if obstacle.\n\nMinimum Path Sum:\n  dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])\n\nMatrix Chain Multiplication:\n  Minimize scalar multiplications to compute A1*A2*...*An.\n  dp[i][j] = min over k of (dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j])\n  for all i <= k < j.\n  Time: O(n^3), Space: O(n^2).\n  Fill table diagonally (gap = j-i from 1 to n-1).\n\nRod Cutting: Maximize revenue by cutting rod into pieces.\n  dp[i] = max(price[j] + dp[i-j]) for j in 1..i.\n  Unbounded knapsack variant.",
                "key_points": [
                    "Coin change (min coins): unbounded knapsack. Iterate coins then amounts.",
                    "Coin change (count ways): order of loops matters! Coins outside, amounts inside.",
                    "Grid DP: dp[i][j] combines dp[i-1][j] and dp[i][j-1]. Handle boundaries.",
                    "Matrix chain multiplication uses interval DP - fill diagonally.",
                    "These are among the top 10 most-asked DP problems in interviews."
                ],
                "examples": [
                    {"question": "Coin change: coins=[1,5,10], amount=12", "solution": "dp[0]=0. Build up: dp[1]=1, dp[2]=2, ..., dp[5]=1(one 5-coin), ..., dp[10]=1(one 10-coin), dp[11]=2(10+1), dp[12]=2(10+1+1)? Wait: dp[12]=min(dp[11]+1, dp[7]+1, dp[2]+1)=min(3,3,3)=3. Actually dp[12]=min(dp[11]+1(1-coin)=3, dp[7]+1(5-coin)=4, dp[2]+1(10-coin)=3)=3. Hmm, dp[10]=1, dp[11]=2, dp[12]=3. But 10+1+1=12, that is 3 coins. Or 5+5+1+1=4 coins. Min is 3."},
                    {"question": "Unique paths in 3x3 grid (no obstacles)", "solution": "dp: [[1,1,1],[1,2,3],[1,3,6]]. Answer = dp[2][2] = 6 paths."},
                    {"question": "Matrix chain: dimensions [10,30,5,60]. Matrices A1(10x30), A2(30x5), A3(5x60).", "solution": "dp[1][2]=10*30*5=1500. dp[2][3]=30*5*60=9000. dp[1][3]=min(dp[1][1]+dp[2][3]+10*30*60 , dp[1][2]+dp[3][3]+10*5*60)=min(0+9000+18000, 1500+0+3000)=min(27000,4500)=4500. Optimal: (A1*A2)*A3."}
                ],
            },
            {
                "title": "Advanced DP Patterns",
                "content": "DP on Trees:\n  Example: Maximum path sum in binary tree.\n  At each node, choose: extend from left, extend from right, or start new path.\n  Track max path that can be extended (single path) and overall max (any path).\n\nBitmask DP:\n  Used when state includes a subset of n elements (n <= 20).\n  dp[mask] represents state for subset encoded by bitmask.\n  Example: Traveling Salesman Problem (TSP).\n  dp[mask][i] = min cost to visit all cities in mask, ending at i.\n  dp[mask | (1<<j)][j] = min(dp[mask][i] + dist[i][j])\n  Time: O(2^n * n^2)\n\nDigit DP:\n  Count numbers up to N with certain properties.\n  State: (position, tight_constraint, other_properties).\n  Used for counting numbers with digit sum = k, etc.\n\nInterval DP (Range DP):\n  dp[i][j] for subarray/substring from i to j.\n  Fill by increasing gap length.\n  Examples: Matrix chain multiplication, palindrome partitioning, burst balloons.\n\nDP Optimization Techniques:\n- Space optimization: Rolling array, two-variable.\n- Monotone queue optimization: O(n) instead of O(nk).\n- Divide and conquer optimization: When dp[i][j] transition point is monotone.\n\nCommon DP Patterns Summary:\n1. Take or skip -> knapsack\n2. String matching -> LCS/Edit distance\n3. Counting paths -> grid DP / coin change 2\n4. Optimization -> min/max over subproblems\n5. Interval -> matrix chain / palindrome partition",
                "key_points": [
                    "Bitmask DP handles subset problems when n <= 20 (2^20 = ~10^6 states)",
                    "Interval DP fills table diagonally by gap length",
                    "DP on trees uses post-order traversal (solve children first)",
                    "Always look for space optimization: 2D -> 1D -> constant space",
                    "DP is the most asked topic at Amazon, Google, Microsoft - practice 50+ problems"
                ],
                "examples": [
                    {"question": "Palindrome partitioning: minimum cuts for 'aab'", "solution": "Substrings: 'a' palindrome, 'aa' palindrome, 'aab' not, 'a' palindrome, 'ab' not, 'b' palindrome. dp[0]=0, dp[1]=0 (aa is palindrome), dp[2]=1 (aa|b). Minimum 1 cut."},
                    {"question": "TSP with 3 cities, dist=[[0,10,15],[10,0,20],[15,20,0]]. Start from 0.", "solution": "dp[{0},0]=0. dp[{0,1},1]=10. dp[{0,2},2]=15. dp[{0,1,2},2]=min(dp[{0,1},1]+20)=30. dp[{0,1,2},1]=min(dp[{0,2},2]+20)=35. Return to 0: min(30+15, 35+10)=min(45,45)=45. Optimal tour: 0->1->2->0, cost 45."},
                    {"question": "Count numbers from 1 to 25 with digit sum = 5", "solution": "Numbers: 5, 14, 23. That is 3 numbers. Digit DP would enumerate: ones digit + tens digit = 5, with constraint <= 25."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Memoization", "explanation": "Top-down DP. Solve recursively, cache results. Natural for tree-shaped subproblem graphs. Uses recursion stack."},
            {"name": "Tabulation", "explanation": "Bottom-up DP. Fill table iteratively from base cases. No recursion overhead. Easier to optimize space."},
            {"name": "0/1 Knapsack", "explanation": "Select items to maximize value within weight limit. dp[i][w] = max(skip, take). 1D: iterate weight right-to-left."},
            {"name": "LCS", "explanation": "Longest Common Subsequence. Match: dp[i][j]=dp[i-1][j-1]+1. No match: max(dp[i-1][j], dp[i][j-1]). O(mn)."},
            {"name": "LIS", "explanation": "Longest Increasing Subsequence. O(n^2) DP or O(n log n) with binary search + patience sorting."}
        ],
        "formulas": [
            "Fibonacci: dp[i] = dp[i-1] + dp[i-2]",
            "Knapsack: dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])",
            "LCS: match -> dp[i-1][j-1]+1, else -> max(dp[i-1][j], dp[i][j-1])",
            "Coin change: dp[a] = min(dp[a], dp[a-coin]+1) for each coin",
            "Edit distance: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])"
        ],
        "solved_examples": [
            {"question": "Minimum coins for amount 11 using coins [1,5,6].", "solution": "dp: [0,1,2,3,4,1,1,2,3,4,2,2]. dp[11]=min(dp[10]+1, dp[6]+1, dp[5]+1)=min(3,2,2)=2. Coins: 5+6=11. Answer: 2 coins."},
            {"question": "LCS of 'AGGTAB' and 'GXTXAYB'.", "solution": "Build 6x7 table. LCS = 'GTAB', length = 4."},
            {"question": "Edit distance from 'kitten' to 'sitting'.", "solution": "k->s (replace), e->i (replace), n->g (replace), +g (insert). Wait, let us trace: kitten -> sitten (replace k->s) -> sittin (replace e->i) -> sitting (insert g). Distance = 3."}
        ],
        "tips": [
            "Start with the recurrence relation. Once you have it, coding is straightforward.",
            "If you cannot see the DP, try brute force recursion first, then add memoization.",
            "For 2D DP, draw the table on paper before coding. It helps catch errors.",
            "In interviews, explain your state definition clearly: 'dp[i] represents...'",
            "DP problems become easier with practice. Solve LeetCode DP tagged problems (Easy->Medium->Hard)."
        ],
    },
    47: {
        "title": "Searching & Sorting",
        "overview": "Searching and sorting are fundamental algorithmic techniques. Binary search and its variations are critical for efficient searching. Sorting algorithms like merge sort and quick sort are interview staples. This topic covers binary search variations, comparison-based and non-comparison sorting, and advanced problems like searching in rotated arrays.",
        "chapters": [
            {
                "title": "Binary Search & Variations",
                "content": "Binary search finds a target in a sorted array in O(log n) time.\n\nStandard Binary Search:\n  def binarySearch(arr, target):\n      lo, hi = 0, len(arr) - 1\n      while lo <= hi:\n          mid = lo + (hi - lo) // 2  # avoid overflow\n          if arr[mid] == target: return mid\n          elif arr[mid] < target: lo = mid + 1\n          else: hi = mid - 1\n      return -1\n\nLower Bound (first occurrence of target):\n  def lowerBound(arr, target):\n      lo, hi = 0, len(arr) - 1; result = -1\n      while lo <= hi:\n          mid = lo + (hi - lo) // 2\n          if arr[mid] == target: result = mid; hi = mid - 1\n          elif arr[mid] < target: lo = mid + 1\n          else: hi = mid - 1\n      return result\n\nUpper Bound (last occurrence): Same but lo = mid + 1 on match.\n\nCount occurrences = upperBound - lowerBound + 1.\n\nSearch in Rotated Sorted Array:\n  def search(nums, target):\n      lo, hi = 0, len(nums)-1\n      while lo <= hi:\n          mid = (lo + hi) // 2\n          if nums[mid] == target: return mid\n          if nums[lo] <= nums[mid]:  # left half sorted\n              if nums[lo] <= target < nums[mid]: hi = mid - 1\n              else: lo = mid + 1\n          else:  # right half sorted\n              if nums[mid] < target <= nums[hi]: lo = mid + 1\n              else: hi = mid - 1\n      return -1\n\nSearch answer space: Binary search on answer (e.g., min capacity to ship packages in d days).\n  lo, hi = max(weights), sum(weights)\n  while lo < hi:\n      mid = (lo + hi) // 2\n      if canShip(mid, d): hi = mid\n      else: lo = mid + 1",
                "key_points": [
                    "Always use lo + (hi-lo)//2 instead of (lo+hi)//2 to prevent integer overflow",
                    "Binary search works on any monotonic function, not just sorted arrays",
                    "Search in rotated array: determine which half is sorted, then decide",
                    "Binary search on answer is a powerful technique for optimization problems",
                    "Amazon and Google ask binary search variations very frequently"
                ],
                "examples": [
                    {"question": "Find first and last occurrence of 5 in [1,2,5,5,5,6,8]", "solution": "Lower bound: lo=0,hi=6. mid=3(5): result=3, hi=2. mid=1(2): lo=2. mid=2(5): result=2, hi=1. lo>hi. First=2. Upper bound: similarly, last=4. Count = 4-2+1 = 3."},
                    {"question": "Search 3 in rotated array [4,5,6,7,0,1,2,3]", "solution": "lo=0,hi=7. mid=3(7). Left [4,5,6,7] sorted. 3<4, not in left half. lo=4. mid=5(1). Right [1,2,3] sorted. 1<3<=3, lo=6. mid=6(2). 2<3, lo=7. mid=7(3). Found at index 7."},
                    {"question": "Find square root of 10 (integer part) using binary search", "solution": "lo=1, hi=10. mid=5: 25>10, hi=4. mid=2: 4<10, lo=3. mid=3: 9<10, lo=4. mid=4: 16>10, hi=3. lo>hi. Answer = 3."}
                ],
            },
            {
                "title": "Merge Sort & Quick Sort",
                "content": "Merge Sort: Divide array in half, sort each half, merge.\n  def mergeSort(arr):\n      if len(arr) <= 1: return arr\n      mid = len(arr) // 2\n      left = mergeSort(arr[:mid])\n      right = mergeSort(arr[mid:])\n      return merge(left, right)\n\n  def merge(left, right):\n      result = []; i = j = 0\n      while i < len(left) and j < len(right):\n          if left[i] <= right[j]: result.append(left[i]); i += 1\n          else: result.append(right[j]); j += 1\n      result.extend(left[i:]); result.extend(right[j:])\n      return result\n  Time: O(n log n) always. Space: O(n). Stable.\n\nQuick Sort: Pick pivot, partition, recurse on halves.\n  def quickSort(arr, lo, hi):\n      if lo < hi:\n          p = partition(arr, lo, hi)\n          quickSort(arr, lo, p-1)\n          quickSort(arr, p+1, hi)\n\n  def partition(arr, lo, hi):\n      pivot = arr[hi]; i = lo - 1\n      for j in range(lo, hi):\n          if arr[j] < pivot:\n              i += 1; arr[i], arr[j] = arr[j], arr[i]\n      arr[i+1], arr[hi] = arr[hi], arr[i+1]\n      return i + 1\n  Time: O(n log n) avg, O(n^2) worst. Space: O(log n) avg. Not stable.\n  Worst case: already sorted array with last element as pivot. Fix: random pivot.\n\nCount Inversions using Merge Sort:\n  During merge, if right element is picked before left, inversions += len(left) - i.\n  Total inversions = inversions from left + right + merge step.",
                "key_points": [
                    "Merge sort: O(n log n) guaranteed, stable, O(n) extra space",
                    "Quick sort: O(n log n) average, in-place, not stable. Random pivot avoids O(n^2).",
                    "Merge sort is preferred when stability matters or for linked lists",
                    "Quick sort is preferred in practice: better cache performance, in-place",
                    "Count inversions with merge sort is a classic Amazon/Microsoft interview question"
                ],
                "examples": [
                    {"question": "Merge sort [38,27,43,3,9,82,10]", "solution": "Split: [38,27,43] and [3,9,82,10]. Further split and sort: [27,38,43] and [3,9,10,82]. Merge: [3,9,10,27,38,43,82]."},
                    {"question": "Partition [10,80,30,90,40,50,70] with pivot=70 (last element)", "solution": "i=-1. j=0(10<70): i=0, swap. j=1(80>70): skip. j=2(30<70): i=1, swap 80,30. j=3(90>70): skip. j=4(40<70): i=2, swap 80,40. j=5(50<70): i=3, swap 90,50. Place pivot at i+1=4: swap arr[4]=80 with 70. Result: [10,30,40,50,70,90,80]."},
                    {"question": "Count inversions in [2,4,1,3,5]", "solution": "Merge sort approach. Split: [2,4] and [1,3,5]. [2,4] sorted: 0 inv. [1,3,5] sorted: 0 inv. Merge: 1<2, pick 1 (inv += 2, remaining in left=[2,4]). 2<3, pick 2. 3<4, pick 3 (inv += 1). 4<5, pick 4. Pick 5. Total inversions = 3."}
                ],
            },
            {
                "title": "Non-Comparison Sorts & Special Sorting",
                "content": "Counting Sort (O(n+k) where k = range of values):\n  def countingSort(arr):\n      max_val = max(arr)\n      count = [0] * (max_val + 1)\n      for x in arr: count[x] += 1\n      i = 0\n      for val in range(max_val + 1):\n          while count[val] > 0:\n              arr[i] = val; i += 1; count[val] -= 1\n  Best when range k is small relative to n.\n\nRadix Sort (O(d*(n+k)) where d = number of digits):\n  Sort by each digit from least significant to most significant using a stable sort (counting sort).\n  Works for integers and strings of fixed length.\n\nBucket Sort (O(n+k) average):\n  Distribute elements into buckets, sort each bucket, concatenate.\n  Best when input is uniformly distributed.\n\nComparator-Based Sorting:\n  Python: sorted(arr, key=lambda x: (-x[1], x[0]))  # sort by second desc, then first asc\n  Custom comparator for largest number:\n  from functools import cmp_to_key\n  def compare(a, b):\n      if a+b > b+a: return -1\n      return 1\n  sorted(nums_str, key=cmp_to_key(compare))\n\nSort Colors (Dutch National Flag):\n  Three-way partition: 0s, 1s, 2s in single pass. O(n) time, O(1) space.\n  (Covered in Arrays topic.)\n\nStability: Merge sort, counting sort, radix sort are stable. Quick sort, heap sort are not.",
                "key_points": [
                    "Counting sort beats O(n log n) when range is small: O(n+k)",
                    "Radix sort: sort by each digit using stable sub-sort. O(d(n+k))",
                    "Know which sorts are stable: merge, counting, insertion, bubble, radix",
                    "Custom comparators are essential for problems like 'largest number'",
                    "Sorting stability questions are common in GATE and placement MCQs"
                ],
                "examples": [
                    {"question": "Counting sort: [4,2,2,8,3,3,1]", "solution": "count: [0,1,2,2,1,0,0,0,1]. Reconstruct: 1,2,2,3,3,4,8. Sorted in O(n+k) where k=8."},
                    {"question": "Form largest number from [3, 30, 34, 5, 9]", "solution": "Compare pairs as strings: '9'+'5'='95' vs '5'+'9'='59', 9 first. '9'+'34'='934' vs '34'+'9'='349', 9 first. '5'+'34'='534' vs '34'+'5'='345', 5 first. '34'+'3'='343' vs '3'+'34'='334', 34 first. '34'+'30'='3430' vs '30'+'34'='3034', 34 first. Order: 9,5,34,3,30. Largest: '9534330'."},
                    {"question": "Sort [(1,'b'),(2,'a'),(1,'a')] stably by first element", "solution": "Stable sort preserves relative order of equal keys. Result: [(1,'b'),(1,'a'),(2,'a')]. Note (1,'b') stays before (1,'a') as in original."}
                ],
            },
            {
                "title": "Binary Search Advanced Applications",
                "content": "Find Peak Element: arr[i] > arr[i-1] and arr[i] > arr[i+1].\n  def findPeak(arr):\n      lo, hi = 0, len(arr)-1\n      while lo < hi:\n          mid = (lo + hi) // 2\n          if arr[mid] < arr[mid+1]: lo = mid + 1\n          else: hi = mid\n      return lo\n\nSearch in 2D Sorted Matrix:\n  Treat m*n matrix as 1D array. index -> (index//n, index%n).\n  Standard binary search on virtual 1D array. O(log(mn)).\n\nMinimum in Rotated Sorted Array:\n  def findMin(nums):\n      lo, hi = 0, len(nums)-1\n      while lo < hi:\n          mid = (lo + hi) // 2\n          if nums[mid] > nums[hi]: lo = mid + 1\n          else: hi = mid\n      return nums[lo]\n\nKoko Eating Bananas (binary search on answer):\n  Find minimum speed k such that Koko can eat all bananas in h hours.\n  lo=1, hi=max(piles). Binary search: for each mid, check if sum(ceil(p/mid)) <= h.\n\nMedian of Two Sorted Arrays (O(log(min(m,n)))):\n  Binary search on partition of smaller array.\n  Ensure left partition max <= right partition min for both arrays.\n  Partition i in arr1, j=(m+n+1)/2-i in arr2.\n  If arr1[i-1] <= arr2[j] and arr2[j-1] <= arr1[i]: found median.\n\nAggressive Cows / Magnetic Balls:\n  Binary search on answer (minimum distance). Check if we can place k cows with at least mid distance apart.",
                "key_points": [
                    "Binary search on answer: define search space, write feasibility check function",
                    "Peak element: always go toward the larger neighbor",
                    "Median of two sorted arrays is the hardest binary search problem - O(log(min(m,n)))",
                    "Koko eating bananas pattern applies to many 'minimum speed/capacity' problems",
                    "These problems appear in Amazon, Google, Microsoft SDE interviews"
                ],
                "examples": [
                    {"question": "Find peak in [1,2,3,1]", "solution": "lo=0,hi=3. mid=1: arr[1]=2 < arr[2]=3, lo=2. mid=2: arr[2]=3 > arr[3]=1, hi=2. lo==hi==2. Peak at index 2, value 3."},
                    {"question": "Min in rotated array [3,4,5,1,2]", "solution": "lo=0,hi=4. mid=2: arr[2]=5 > arr[4]=2, lo=3. mid=3: arr[3]=1 < arr[4]=2, hi=3. lo==hi==3. Min = arr[3] = 1."},
                    {"question": "Koko has piles [3,6,7,11], h=8 hours. Min eating speed?", "solution": "lo=1, hi=11. mid=6: hours=1+1+2+2=6<=8, hi=6. mid=3: hours=1+2+3+4=10>8, lo=4. mid=5: hours=1+2+2+3=8<=8, hi=5. mid=4: hours=1+2+2+3=8<=8, hi=4. lo==hi==4. Answer: 4 bananas/hour."}
                ],
            },
            {
                "title": "Sorting Algorithm Comparison & Selection",
                "content": "Algorithm Comparison Table:\n  Algorithm      | Best    | Average | Worst   | Space  | Stable\n  Bubble Sort    | O(n)    | O(n^2)  | O(n^2)  | O(1)   | Yes\n  Selection Sort | O(n^2)  | O(n^2)  | O(n^2)  | O(1)   | No\n  Insertion Sort | O(n)    | O(n^2)  | O(n^2)  | O(1)   | Yes\n  Merge Sort     | O(nlogn)| O(nlogn)| O(nlogn)| O(n)   | Yes\n  Quick Sort     | O(nlogn)| O(nlogn)| O(n^2)  | O(logn)| No\n  Heap Sort      | O(nlogn)| O(nlogn)| O(nlogn)| O(1)   | No\n  Counting Sort  | O(n+k)  | O(n+k)  | O(n+k)  | O(k)   | Yes\n  Radix Sort     | O(d(n+k))|O(d(n+k))|O(d(n+k))| O(n+k)| Yes\n\nWhen to use which:\n- Small arrays (n < 20): Insertion sort (fast due to low overhead).\n- Nearly sorted: Insertion sort O(n) or TimSort.\n- General purpose: Merge sort (stable) or Quick sort (in-place).\n- Known small range: Counting sort.\n- Memory constrained: Quick sort or Heap sort.\n- Linked lists: Merge sort (no random access needed).\n- Stable required: Merge sort, Counting sort.\n\nPython's sort: TimSort = hybrid of merge sort and insertion sort. O(n log n), stable.\n\nSelection Algorithm (QuickSelect for kth element):\n  Average O(n), worst O(n^2). Based on quicksort partition.\n  Partition, if pivot at position k, done. Else recurse on correct half.",
                "key_points": [
                    "Memorize the comparison table - it appears in every placement exam",
                    "Quick sort is O(n^2) worst case but O(n log n) average with random pivot",
                    "Merge sort is the only O(n log n) stable comparison sort",
                    "Lower bound for comparison-based sorting is Omega(n log n)",
                    "TCS NQT, Infosys, and GATE heavily test sorting algorithm properties"
                ],
                "examples": [
                    {"question": "Which sort is best for nearly sorted array of 1 million elements?", "solution": "Insertion sort: O(n) for nearly sorted data. Each element is at most a few positions from its correct place, so very few swaps needed. TimSort (Python default) also excels here."},
                    {"question": "Sort [5,3,8,1,2] using selection sort. Count comparisons.", "solution": "Pass 1: find min in [5,3,8,1,2]=1 (4 comparisons), swap with pos 0: [1,3,8,5,2]. Pass 2: min in [3,8,5,2]=2 (3 comp), swap: [1,2,8,5,3]. Pass 3: min in [8,5,3]=3 (2 comp): [1,2,3,5,8]. Pass 4: min in [5,8]=5 (1 comp): no swap. Total: 10 comparisons = n(n-1)/2."},
                    {"question": "Is heap sort stable? Prove with example.", "solution": "No. Example: [(4,'a'),(4,'b'),(1,'c')]. After heapify and extract: we get 1, then 4, then 4. But which 4 comes first depends on heap structure, not original order. So (4,'b') might come before (4,'a'). Not stable."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Binary Search", "explanation": "Search sorted array in O(log n). lo, hi pointers; compare mid. Works on any monotonic predicate, not just sorted arrays."},
            {"name": "Merge Sort", "explanation": "Divide and conquer. Split, sort halves, merge. O(n log n) always, stable, O(n) space. Best for linked lists."},
            {"name": "Quick Sort", "explanation": "Partition around pivot, recurse. O(n log n) average, O(n^2) worst. In-place, not stable. Random pivot fixes worst case."},
            {"name": "Counting Sort", "explanation": "Non-comparison sort. Count occurrences, reconstruct. O(n+k) where k=range. Stable. Best when k is small."},
            {"name": "Binary Search on Answer", "explanation": "When answer has monotonic feasibility, binary search the answer space. Define lo/hi bounds, check mid feasibility."}
        ],
        "formulas": [
            "Binary search: O(log n) time, O(1) space",
            "Merge sort: O(n log n) time, O(n) space, stable",
            "Quick sort: O(n log n) avg, O(n^2) worst, O(log n) space",
            "Counting sort: O(n+k) time, O(k) space",
            "Lower bound for comparison sorting: Omega(n log n)"
        ],
        "solved_examples": [
            {"question": "Find target 7 in rotated array [4,5,6,7,0,1,2].", "solution": "lo=0,hi=6. mid=3(7)==target. Found at index 3."},
            {"question": "Sort [10,7,8,9,1,5] using quick sort (pivot=last).", "solution": "Partition with pivot 5: [1,5,8,9,10,7]. Recurse left [1] done. Recurse right [8,9,10,7], pivot 7: [7,9,10,8]... Continue until sorted: [1,5,7,8,9,10]."},
            {"question": "Count inversions in [5,4,3,2,1].", "solution": "Fully reversed array. Inversions = n(n-1)/2 = 10. Using merge sort: each merge step counts inversions across halves."}
        ],
        "tips": [
            "Binary search bugs: use lo + (hi-lo)//2, be careful with lo<=hi vs lo<hi.",
            "For placement MCQs, memorize time/space/stability of all sorting algorithms.",
            "Quick sort with random pivot is almost always O(n log n) in practice.",
            "When problem says 'find minimum X such that condition holds', think binary search on answer.",
            "Python's sorted() uses TimSort: O(n log n), stable. Mention this in interviews when relevant."
        ],
    },
    48: {
        "title": "Recursion & Backtracking",
        "overview": "Recursion is a method where a function calls itself to solve smaller subproblems. Backtracking extends recursion by exploring all possibilities and pruning invalid paths. This topic covers recursion fundamentals, the call stack, and classic backtracking problems like N-Queens, Sudoku solver, permutations, subsets, and rat-in-a-maze that are staples of Amazon, Google, and Microsoft coding interviews.",
        "chapters": [
            {
                "title": "Recursion Fundamentals & Call Stack",
                "content": "A recursive function has two parts:\n1) Base case: Condition to stop recursion.\n2) Recursive case: Function calls itself with a smaller problem.\n\nExample - Factorial:\n  def factorial(n):\n      if n <= 1: return 1  # base case\n      return n * factorial(n-1)  # recursive case\n\nCall Stack for factorial(4):\n  factorial(4) -> 4 * factorial(3)\n    factorial(3) -> 3 * factorial(2)\n      factorial(2) -> 2 * factorial(1)\n        factorial(1) -> returns 1\n      returns 2*1 = 2\n    returns 3*2 = 6\n  returns 4*6 = 24\n\nRecursion vs Iteration:\n  Every recursive solution can be converted to iterative (using explicit stack).\n  Recursion is elegant but uses O(call depth) stack space.\n\nTail Recursion: Recursive call is the last operation. Can be optimized by compiler.\n  def factorial_tail(n, acc=1):\n      if n <= 1: return acc\n      return factorial_tail(n-1, n*acc)  # tail call\n\nCommon Recursive Patterns:\n- Linear recursion: f(n) calls f(n-1) once. Example: factorial, sum of array.\n- Binary recursion: f(n) calls f(n-1) and f(n-2). Example: Fibonacci.\n- Multiple recursion: f(n) calls f for multiple subproblems. Example: tree traversals.\n\nPower Function (fast exponentiation):\n  def power(x, n):\n      if n == 0: return 1\n      half = power(x, n//2)\n      if n % 2 == 0: return half * half\n      else: return x * half * half\n  Time: O(log n)",
                "key_points": [
                    "Always define a base case - missing it causes infinite recursion / stack overflow",
                    "Each recursive call adds a frame to the call stack - space is O(depth)",
                    "Python default recursion limit is 1000 - increase with sys.setrecursionlimit()",
                    "Tail recursion can be optimized but Python does NOT optimize tail calls",
                    "Draw the recursion tree to understand time complexity"
                ],
                "examples": [
                    {"question": "Compute sum of digits of 1234 recursively", "solution": "def digitSum(n): if n==0: return 0; return n%10 + digitSum(n//10). digitSum(1234) = 4 + digitSum(123) = 4 + 3 + digitSum(12) = 4+3+2+digitSum(1) = 4+3+2+1 = 10."},
                    {"question": "Reverse a string recursively: 'hello'", "solution": "def rev(s): if len(s)<=1: return s; return rev(s[1:]) + s[0]. rev('hello') = rev('ello')+'h' = rev('llo')+'e'+'h' = ... = 'olleh'."},
                    {"question": "Tower of Hanoi for 3 disks", "solution": "def hanoi(n, src, dest, aux): if n==1: print(src,'->',dest); return; hanoi(n-1,src,aux,dest); print(src,'->',dest); hanoi(n-1,aux,dest,src). Moves: A->C, A->B, C->B, A->C, B->A, B->C, A->C. Total = 2^3-1 = 7 moves."}
                ],
            },
            {
                "title": "Backtracking Framework",
                "content": "Backtracking = recursion + pruning. Explore all candidates, abandon (backtrack) as soon as a candidate is invalid.\n\nGeneral Template:\n  def backtrack(state, choices):\n      if is_solution(state):\n          record(state)\n          return\n      for choice in choices:\n          if is_valid(choice, state):\n              make_choice(choice, state)\n              backtrack(state, remaining_choices)\n              undo_choice(choice, state)  # BACKTRACK\n\nSubsets (Power Set):\n  def subsets(nums):\n      result = []\n      def backtrack(start, current):\n          result.append(current[:])\n          for i in range(start, len(nums)):\n              current.append(nums[i])\n              backtrack(i+1, current)\n              current.pop()  # backtrack\n      backtrack(0, [])\n      return result\n  For [1,2,3]: [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]. Total: 2^n = 8.\n\nPermutations:\n  def permutations(nums):\n      result = []\n      def backtrack(current, remaining):\n          if not remaining:\n              result.append(current[:])\n              return\n          for i in range(len(remaining)):\n              current.append(remaining[i])\n              backtrack(current, remaining[:i]+remaining[i+1:])\n              current.pop()\n      backtrack([], nums)\n      return result\n  For [1,2,3]: 3! = 6 permutations.\n\nCombinations (choose k from n):\n  def combine(n, k):\n      result = []\n      def backtrack(start, current):\n          if len(current) == k:\n              result.append(current[:]); return\n          for i in range(start, n+1):\n              current.append(i)\n              backtrack(i+1, current)\n              current.pop()\n      backtrack(1, [])\n      return result",
                "key_points": [
                    "Backtracking template: choose, explore, unchoose. Master this pattern.",
                    "Subsets: 2^n results. Permutations: n! results. Combinations: C(n,k) results.",
                    "Always make a copy (current[:]) when recording solutions, not a reference",
                    "Pruning (is_valid check) is what makes backtracking efficient",
                    "These are the most common backtracking questions in every coding interview"
                ],
                "examples": [
                    {"question": "Generate all subsets of [1,2]", "solution": "backtrack(0,[]): add []. i=0: add 1, backtrack(1,[1]): add [1]. i=1: add 2, backtrack(2,[1,2]): add [1,2]. pop 2. pop 1. i=1: add 2, backtrack(2,[2]): add [2]. pop 2. Result: [[],[1],[1,2],[2]]."},
                    {"question": "All permutations of [1,2]", "solution": "backtrack([],[1,2]): pick 1: backtrack([1],[2]): pick 2: backtrack([1,2],[]): add [1,2]. pop 2. pop 1. Pick 2: backtrack([2],[1]): pick 1: add [2,1]. Result: [[1,2],[2,1]]."},
                    {"question": "Combinations C(4,2)", "solution": "backtrack(1,[]): i=1:[1], i=2:[1,2] add. i=3:[1,3] add. i=4:[1,4] add. i=2:[2], i=3:[2,3] add. i=4:[2,4] add. i=3:[3], i=4:[3,4] add. Result: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]. Count = C(4,2) = 6."}
                ],
            },
            {
                "title": "N-Queens Problem",
                "content": "Place N queens on an NxN chessboard such that no two queens attack each other (same row, column, or diagonal).\n\nApproach: Place queens one row at a time. For each row, try each column. Check if placement is safe.\n\n  def solveNQueens(n):\n      result = []\n      board = [['.'] * n for _ in range(n)]\n      cols = set(); diag1 = set(); diag2 = set()\n\n      def backtrack(row):\n          if row == n:\n              result.append([''.join(r) for r in board])\n              return\n          for col in range(n):\n              if col in cols or (row-col) in diag1 or (row+col) in diag2:\n                  continue  # prune\n              board[row][col] = 'Q'\n              cols.add(col); diag1.add(row-col); diag2.add(row+col)\n              backtrack(row + 1)\n              board[row][col] = '.'  # backtrack\n              cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)\n\n      backtrack(0)\n      return result\n\nDiagonal tracking:\n  Same diagonal (\\): row - col is constant.\n  Same anti-diagonal (/): row + col is constant.\n  Using sets for cols, diag1, diag2 gives O(1) conflict check.\n\nNumber of solutions:\n  N=1: 1, N=2: 0, N=3: 0, N=4: 2, N=5: 10, N=6: 4, N=7: 40, N=8: 92.\n\nTime Complexity: O(N!) in the worst case (but pruning makes it much faster).\n\nVariant - N Queens II: Just count solutions, no need to store boards.",
                "key_points": [
                    "Use sets for column and diagonal tracking - O(1) per check",
                    "Diagonal key: row-col for \\ diagonal, row+col for / diagonal",
                    "N-Queens is the classic backtracking problem - know it thoroughly",
                    "For N=4, the two solutions are: (1,3,0,2) and (2,0,3,1) column positions",
                    "Amazon, Microsoft, and Google ask N-Queens or its variants in interviews"
                ],
                "examples": [
                    {"question": "Solve 4-Queens", "solution": "Row 0, col 1: Q at (0,1). Row 1: col 3 safe. Q at (1,3). Row 2: col 0 safe. Q at (2,0). Row 3: col 2 safe. Q at (3,2). Solution 1: [.Q.., ...Q, Q..., ..Q.]. Solution 2: [..Q., Q..., ...Q, .Q..]."},
                    {"question": "Why can't we place 3 queens on 3x3 board?", "solution": "Try (0,0): blocks row 0, col 0, diag 0,0. (1,2): blocks row 1, col 2, diag -1,3. Row 2: col 0 blocked (diag), col 1 blocked (anti-diag 3? No. col 1: diag=2-1=1 ok, anti-diag=2+1=3 blocked). Col 2 blocked. No valid placement. All attempts fail."},
                    {"question": "How many solutions for 8-Queens?", "solution": "92 distinct solutions. With rotational symmetry, 12 fundamental solutions. The problem can be solved efficiently with backtracking in milliseconds."}
                ],
            },
            {
                "title": "Sudoku Solver & Constraint Satisfaction",
                "content": "Sudoku: Fill 9x9 grid with digits 1-9. Each row, column, and 3x3 box must contain all digits 1-9 exactly once.\n\n  def solveSudoku(board):\n      def isValid(board, row, col, num):\n          for i in range(9):\n              if board[row][i] == num: return False\n              if board[i][col] == num: return False\n          box_r, box_c = 3*(row//3), 3*(col//3)\n          for i in range(box_r, box_r+3):\n              for j in range(box_c, box_c+3):\n                  if board[i][j] == num: return False\n          return True\n\n      def solve(board):\n          for i in range(9):\n              for j in range(9):\n                  if board[i][j] == '.':\n                      for num in '123456789':\n                          if isValid(board, i, j, num):\n                              board[i][j] = num\n                              if solve(board): return True\n                              board[i][j] = '.'  # backtrack\n                      return False  # no valid number\n          return True  # all filled\n\n      solve(board)\n\nOptimization: Use sets for rows, cols, boxes to check validity in O(1).\n  rows = [set() for _ in range(9)]\n  cols = [set() for _ in range(9)]\n  boxes = [set() for _ in range(9)]  # box index = (row//3)*3 + col//3\n\nWord Search (find word in grid):\n  For each cell matching first letter, DFS in 4 directions.\n  Mark visited cells to avoid reuse. Backtrack by unmarking.\n\nCrossword Puzzle: Similar to Sudoku. Try each word in each position, backtrack on conflict.",
                "key_points": [
                    "Sudoku solver demonstrates constraint propagation + backtracking",
                    "Use sets for row/col/box tracking for O(1) validation",
                    "Word search in grid is another common backtracking problem",
                    "Sudoku has unique solution - backtracking finds it by trying all valid options",
                    "Microsoft and Amazon ask Sudoku solver and word search in coding rounds"
                ],
                "examples": [
                    {"question": "Validate placing 5 at position (0,0) in Sudoku where row 0 has [.,3,.,.,.,.,.,.,.]", "solution": "Check row 0: 3 present, 5 not present. OK. Check col 0: check all 9 cells. Check box (0,0)-(2,2). If 5 not in any: valid. Place 5 and continue."},
                    {"question": "Word Search: Find 'ABC' in grid [['A','B','C'],['D','E','F']]", "solution": "Start at (0,0)='A'. Right to (0,1)='B'. Right to (0,2)='C'. Found! Path: (0,0)->(0,1)->(0,2)."},
                    {"question": "How many recursive calls does Sudoku solver make in worst case?", "solution": "Each empty cell tries 9 digits. If k cells empty, worst case is 9^k. But pruning drastically reduces this. Typical Sudoku (17 givens): ~10^6 calls with pruning, vs ~9^64 without."}
                ],
            },
            {
                "title": "Rat in a Maze & Path Finding",
                "content": "Rat in a Maze: Find all paths from (0,0) to (n-1,n-1) in a maze. 1=open, 0=blocked. Can move Down, Right, Up, Left.\n\n  def ratInMaze(maze, n):\n      result = []\n      visited = [[False]*n for _ in range(n)]\n\n      def solve(x, y, path):\n          if x == n-1 and y == n-1:\n              result.append(path)\n              return\n          # Try all 4 directions: D, L, R, U (lexicographic)\n          directions = [(1,0,'D'), (0,-1,'L'), (0,1,'R'), (-1,0,'U')]\n          for dx, dy, d in directions:\n              nx, ny = x+dx, y+dy\n              if 0<=nx<n and 0<=ny<n and maze[nx][ny]==1 and not visited[nx][ny]:\n                  visited[nx][ny] = True\n                  solve(nx, ny, path + d)\n                  visited[nx][ny] = False  # backtrack\n\n      if maze[0][0] == 1:\n          visited[0][0] = True\n          solve(0, 0, '')\n      return result\n\nKnight's Tour: Visit all squares on chessboard exactly once.\n  Knight moves: 8 possible L-shaped moves.\n  Warnsdorff's rule heuristic: Move to square with fewest onward moves.\n\nGenerate Parentheses: Generate all valid combinations of n pairs.\n  def generateParenthesis(n):\n      result = []\n      def backtrack(s, open_count, close_count):\n          if len(s) == 2*n:\n              result.append(s); return\n          if open_count < n:\n              backtrack(s+'(', open_count+1, close_count)\n          if close_count < open_count:\n              backtrack(s+')', open_count, close_count+1)\n      backtrack('', 0, 0)\n      return result\n\nLetter Combinations of Phone Number:\n  Map digits to letters. Backtrack through each digit, try each letter.\n  Time: O(4^n) where n = number of digits (worst case: 7 and 9 have 4 letters).",
                "key_points": [
                    "Rat in maze: mark visited, explore, unmark (backtrack). Classic pattern.",
                    "Generate parentheses: open_count < n to add '(', close_count < open_count to add ')'",
                    "Phone number letter combinations is a common easy backtracking problem",
                    "Path finding backtracking explores all paths - BFS/DFS finds one shortest/any path",
                    "These problems are asked by TCS, Infosys, Amazon in various difficulty levels"
                ],
                "examples": [
                    {"question": "Rat in maze: [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]", "solution": "Paths from (0,0) to (3,3): DDRDRR? Let us trace: (0,0)->D(1,0)->D(2,0)->R(2,1)->D(3,1)->R(3,2)->R(3,3). Path: DDDRR. Another: (0,0)->D(1,0)->R(1,1)->D(2,1)->D(3,1)->R(3,2)->R(3,3). Path: DRDDRR."},
                    {"question": "Generate parentheses for n=2", "solution": "backtrack('',0,0): add '(': ('(',1,0). add '(': ('((',2,0). add ')': ('(()',2,1). add ')': ('(())',2,2). Record. Back. add ')': ('()',1,1). add '(': ('()(', 2,1). add ')': ('()()',2,2). Record. Result: ['(())', '()()']."},
                    {"question": "Letter combinations of '23'", "solution": "2->abc, 3->def. Combine: a+d=ad, a+e=ae, a+f=af, b+d=bd, b+e=be, b+f=bf, c+d=cd, c+e=ce, c+f=cf. Total: 3*3 = 9 combinations."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Recursion", "explanation": "Function calling itself with smaller input. Needs base case (termination) and recursive case (reduction). Uses call stack."},
            {"name": "Backtracking", "explanation": "Recursion + pruning. Explore all valid candidates, abandon invalid paths early. Template: choose, explore, unchoose."},
            {"name": "N-Queens", "explanation": "Place N queens on NxN board with no conflicts. Track columns and diagonals using sets. O(N!) worst case with pruning."},
            {"name": "Subsets/Permutations", "explanation": "Subsets: include or exclude each element (2^n). Permutations: arrange all elements (n!). Both use backtracking."},
            {"name": "Constraint Satisfaction", "explanation": "Problems like Sudoku where variables must satisfy constraints. Backtracking tries values, prunes invalid assignments."}
        ],
        "formulas": [
            "Subsets: 2^n total subsets for n elements",
            "Permutations: n! for n elements; P(n,r) = n!/(n-r)!",
            "Combinations: C(n,r) = n! / (r! * (n-r)!)",
            "Tower of Hanoi: 2^n - 1 moves for n disks",
            "N-Queens solutions: 1, 0, 0, 2, 10, 4, 40, 92 for N=1..8"
        ],
        "solved_examples": [
            {"question": "Find all subsets of [1,2,3] that sum to 3.", "solution": "All subsets: [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]. Sum=3: [3], [1,2]. Answer: [[1,2], [3]]."},
            {"question": "Solve Tower of Hanoi for 2 disks.", "solution": "Move disk 1 from A to B. Move disk 2 from A to C. Move disk 1 from B to C. Total: 3 = 2^2-1 moves."},
            {"question": "Generate all permutations of 'AB'.", "solution": "Fix A first: AB. Fix B first: BA. Result: ['AB', 'BA']."}
        ],
        "tips": [
            "Always identify the base case first when writing recursive solutions.",
            "Draw the recursion tree for the first few levels to verify correctness.",
            "For backtracking, the 'undo' step is crucial - forgetting it causes bugs.",
            "If recursion depth is too deep, convert to iterative with explicit stack.",
            "In interviews, explain your pruning strategy clearly - it shows algorithmic thinking."
        ],
    },
    49: {
        "title": "Greedy Algorithms",
        "overview": "Greedy algorithms make locally optimal choices at each step hoping to find a global optimum. This topic covers activity selection, fractional knapsack, Huffman coding, job scheduling, and minimum platforms - problems that frequently appear in TCS, Amazon, and Microsoft placement exams.",
        "chapters": [
            {
                "title": "Greedy Strategy & Activity Selection",
                "content": "Greedy Approach: Make the best choice at each step without reconsidering.\nGreedy works when:\n1) Greedy choice property: Local optimal leads to global optimal.\n2) Optimal substructure: Optimal solution contains optimal sub-solutions.\n\nActivity Selection: Given n activities with start and end times, find maximum non-overlapping activities.\n  def activitySelection(start, end):\n      # Sort by end time\n      activities = sorted(zip(start, end), key=lambda x: x[1])\n      result = [activities[0]]\n      last_end = activities[0][1]\n      for s, e in activities[1:]:\n          if s >= last_end:\n              result.append((s, e))\n              last_end = e\n      return result\n  Time: O(n log n) for sorting.\n\nWhy sort by end time? Finishing earliest leaves maximum room for remaining activities.\n\nExample: Activities (start, end): (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)\nSorted by end: (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)\nSelect (1,4). Next compatible: (5,7). Next: (8,11). Next: (12,16). Total: 4 activities.\n\nGreedy vs DP:\n- Greedy: faster, simpler, but only works when greedy property holds.\n- DP: always works for optimal substructure, but slower.\n- If greedy doesn't work, fall back to DP.",
                "key_points": [
                    "Activity selection: sort by end time, greedily pick compatible activities",
                    "Greedy works for activity selection - provably optimal",
                    "Always verify that greedy choice property holds before using greedy",
                    "Greedy is O(n log n) typically, much faster than DP alternatives",
                    "Activity selection variants appear in TCS, Amazon, and Google interviews"
                ],
                "examples": [
                    {"question": "Activity selection: starts=[1,3,0,5,8,5], ends=[2,4,6,7,9,9]", "solution": "Sort by end: (1,2),(3,4),(0,6),(5,7),(8,9),(5,9). Pick (1,2). Next: 3>=2, pick (3,4). Next: 0<4 skip. 5>=4, pick (5,7). 8>=7, pick (8,9). 5<9 skip. Total: 4 activities."},
                    {"question": "Can greedy solve 0/1 knapsack?", "solution": "No. Example: capacity=50, items: (wt=10,val=60),(wt=20,val=100),(wt=30,val=120). Greedy by value/weight: take item 1(6.0), item 2(5.0), item 3(4.0). Items 1+2 = wt 30, val 160. But optimal: items 2+3 = wt 50, val 220. Greedy fails!"},
                    {"question": "Maximum meetings in one room: [(0,5),(1,2),(3,4),(5,7),(6,8)]", "solution": "Sort by end: (1,2),(3,4),(0,5),(5,7),(6,8). Pick (1,2), (3,4), (5,7). Total = 3."}
                ],
            },
            {
                "title": "Fractional Knapsack & Huffman Coding",
                "content": "Fractional Knapsack: Unlike 0/1, can take fractions of items.\n  def fractionalKnapsack(W, items):\n      # Sort by value/weight ratio (descending)\n      items.sort(key=lambda x: x[1]/x[0], reverse=True)\n      total_value = 0\n      for weight, value in items:\n          if W >= weight:\n              total_value += value\n              W -= weight\n          else:\n              total_value += value * (W / weight)\n              break\n      return total_value\n  Time: O(n log n). Greedy works here because fractions are allowed.\n\nHuffman Coding: Lossless data compression. Build optimal prefix-free binary codes based on character frequencies.\n  Algorithm:\n  1. Create leaf node for each character with its frequency.\n  2. Build a min-heap of nodes.\n  3. While heap has more than one node:\n     a. Extract two minimum frequency nodes.\n     b. Create internal node with frequency = sum.\n     c. Left child = first extracted, right child = second.\n     d. Insert new node back into heap.\n  4. Root of final tree = Huffman tree.\n  5. Traverse tree: left = 0, right = 1. Path = code.\n\nExample: Chars a:5, b:9, c:12, d:13, e:16, f:45\n  Merge a(5)+b(9)=14. Merge c(12)+d(13)=25. Merge 14+e(16)=30. Merge 25+30=55. Merge 45+55=100.\n  Codes: f=0, c=100, d=101, a=1100, b=1101, e=111.\n  Weighted path length = 5*4+9*4+12*3+13*3+16*3+45*1 = 224 bits.\n\nHuffman is optimal for prefix-free codes. Greedy works because merging smallest frequencies first minimizes total weighted path.",
                "key_points": [
                    "Fractional knapsack: sort by value/weight ratio, take greedily. O(n log n).",
                    "0/1 knapsack needs DP; fractional knapsack works with greedy.",
                    "Huffman coding: min-heap, always merge two smallest. O(n log n).",
                    "Huffman codes are prefix-free: no code is a prefix of another.",
                    "Huffman coding is a common GATE and placement theory question."
                ],
                "examples": [
                    {"question": "Fractional knapsack: W=50, items (wt,val): (10,60),(20,100),(30,120)", "solution": "Ratios: 6.0, 5.0, 4.0. Sort desc: item1, item2, item3. Take item1 fully: W=40, val=60. Take item2 fully: W=20, val=160. Take 20/30 of item3: val=160+80=240. Answer: 240."},
                    {"question": "Build Huffman tree for: a:3, b:5, c:8, d:10", "solution": "Heap: [3,5,8,10]. Merge a(3)+b(5)=8. Heap: [8,8,10]. Merge 8+c(8)=16. Heap: [10,16]. Merge 10+16=26. Codes: d=0, a=110, b=111, c=10. Verify: 3*3+5*3+8*2+10*1 = 9+15+16+10 = 50 bits."},
                    {"question": "Why is Huffman coding greedy?", "solution": "At each step, we merge the two nodes with lowest frequency. This greedy choice minimizes the total cost because low-frequency characters get longer codes and high-frequency characters get shorter codes. The greedy choice property is provable by exchange argument."}
                ],
            },
            {
                "title": "Job Scheduling & Deadline Problems",
                "content": "Job Sequencing with Deadlines: Given n jobs with deadlines and profits, find max profit schedule. Each job takes 1 unit of time.\n\n  def jobScheduling(jobs):\n      # Sort by profit (descending)\n      jobs.sort(key=lambda x: x[2], reverse=True)  # (id, deadline, profit)\n      max_deadline = max(j[1] for j in jobs)\n      slots = [-1] * (max_deadline + 1)  # slot[i] = job at time i\n      total_profit = 0; count = 0\n      for job_id, deadline, profit in jobs:\n          for t in range(deadline, 0, -1):  # find latest free slot\n              if slots[t] == -1:\n                  slots[t] = job_id\n                  total_profit += profit\n                  count += 1\n                  break\n      return count, total_profit\n  Time: O(n^2) simple, O(n log n) with disjoint set.\n\nMinimum Platforms at Railway Station:\n  Given arrival and departure times, find minimum platforms needed.\n  def minPlatforms(arr, dep):\n      arr.sort(); dep.sort()\n      platforms = max_platforms = 0\n      i = j = 0\n      while i < len(arr):\n          if arr[i] <= dep[j]:\n              platforms += 1\n              max_platforms = max(max_platforms, platforms)\n              i += 1\n          else:\n              platforms -= 1\n              j += 1\n      return max_platforms\n  Time: O(n log n) for sorting.\n\nMeeting Rooms II: Same as minimum platforms. Count maximum overlapping intervals.\n\nWeighted Job Scheduling (non-greedy, needs DP):\n  When jobs have different durations, greedy fails. Use DP + binary search.\n  Sort by end time. For each job, binary search for last non-overlapping job.\n  dp[i] = max(dp[i-1], profit[i] + dp[last_non_overlapping]).",
                "key_points": [
                    "Job scheduling: sort by profit descending, assign to latest available slot",
                    "Minimum platforms: sort arrivals and departures separately, sweep",
                    "This sweep technique also solves meeting rooms, interval overlap problems",
                    "Weighted job scheduling needs DP, not pure greedy",
                    "Job scheduling is a top question in TCS NQT and Infosys placement exams"
                ],
                "examples": [
                    {"question": "Jobs (id,deadline,profit): (1,4,20),(2,1,10),(3,1,40),(4,1,30). Max profit?", "solution": "Sort by profit: job3(40), job4(30), job1(20), job2(10). Job3 dl=1: slot 1=job3. Job4 dl=1: slot 1 taken, no free slot. Job1 dl=4: slot 4=job1. Job2 dl=1: slot 1 taken. Total: 40+20=60, 2 jobs."},
                    {"question": "Min platforms: arrivals=[900,940,950,1100,1500,1800], departures=[910,1200,1120,1130,1900,2000]", "solution": "Sort arr=[900,940,950,1100,1500,1800], dep=[910,1120,1130,1200,1900,2000]. i=0(900<=910): plat=1,max=1. i=1(940<=910? No): 940>910, plat=0, j=1. 940<=1120: plat=1,max=1. i=2(950<=1120): plat=2,max=2. i=3(1100<=1120): plat=3,max=3. i=4(1500>1120): plat=2. 1500>1130: plat=1. 1500>1200: plat=0. 1500<=1900: plat=1. i=5(1800<=1900): plat=2. Max=3 platforms."},
                    {"question": "Weighted job scheduling: (1,3,50),(2,5,20),(4,6,30),(6,7,60). Max profit?", "solution": "Sort by end: (1,3,50),(2,5,20),(4,6,30),(6,7,60). dp[1]=50. dp[2]=max(50,20+0)=50. dp[3]=max(50,30+50)=80. dp[4]=max(80,60+80)=140. Answer: 140 (jobs 1,3,4)."}
                ],
            },
            {
                "title": "Interval Greedy & Coin Problems",
                "content": "Interval Scheduling Maximization (same as activity selection):\n  Sort by end time, pick non-overlapping.\n\nInterval Partitioning (min resources for all intervals):\n  Sort by start time. Use min-heap of end times.\n  For each interval: if it starts after heap min, reuse that resource (pop and push).\n  Otherwise, allocate new resource (push).\n  Answer = max heap size.\n\nMerge Overlapping Intervals:\n  def merge(intervals):\n      intervals.sort()\n      merged = [intervals[0]]\n      for start, end in intervals[1:]:\n          if start <= merged[-1][1]:\n              merged[-1] = (merged[-1][0], max(merged[-1][1], end))\n          else:\n              merged.append((start, end))\n      return merged\n\nMinimum Coins for Change (Greedy - only works for certain coin systems):\n  For standard denominations (1, 5, 10, 25): greedy works.\n  Pick largest coin that fits, repeat.\n  For arbitrary coin systems: greedy may fail. Use DP.\n  Example: coins=[1,3,4], amount=6. Greedy: 4+1+1=3 coins. Optimal: 3+3=2 coins.\n\nAssign Cookies (easy greedy):\n  Sort children greed and cookie sizes. Match smallest cookie to smallest satisfiable child.\n\nJump Game: Can you reach the last index?\n  Track maxReach. For each index, if i > maxReach, stuck. Else update maxReach = max(maxReach, i+nums[i]).",
                "key_points": [
                    "Merge intervals: sort by start, extend end. O(n log n).",
                    "Jump game: greedy with maxReach is O(n) - elegant and simple",
                    "Coin change greedy only works for canonical coin systems",
                    "Interval partitioning = minimum meeting rooms = minimum platforms",
                    "These problems appear across all placement exams and coding rounds"
                ],
                "examples": [
                    {"question": "Merge intervals: [(1,3),(2,6),(8,10),(15,18)]", "solution": "Sort (already sorted). Start with (1,3). (2,6): 2<=3, merge to (1,6). (8,10): 8>6, new interval. (15,18): 15>10, new. Result: [(1,6),(8,10),(15,18)]."},
                    {"question": "Jump Game: [2,3,1,1,4]. Can reach end?", "solution": "maxReach=0. i=0: maxReach=max(0,0+2)=2. i=1: 1<=2, maxReach=max(2,1+3)=4. 4>=4(last index). Yes!"},
                    {"question": "Jump Game: [3,2,1,0,4]. Can reach end?", "solution": "maxReach=0. i=0: maxReach=3. i=1: maxReach=3. i=2: maxReach=3. i=3: maxReach=3. i=4: but wait, 4>3? i=3: 3<=3, maxReach=max(3,3+0)=3. After loop, maxReach=3<4. No, cannot reach end."}
                ],
            },
            {
                "title": "Greedy on Strings & Miscellaneous",
                "content": "Minimum Characters to Make String Palindrome:\n  Insert characters at front. Use KMP failure function on s + '#' + reverse(s).\n  Characters needed = n - failure_function_last_value.\n\nSmallest String with Removals:\n  Remove k characters from string to get lexicographically smallest. Use stack (greedy).\n  def removeKDigits(num, k):\n      stack = []\n      for d in num:\n          while k and stack and stack[-1] > d:\n              stack.pop(); k -= 1\n          stack.append(d)\n      stack = stack[:len(stack)-k] if k else stack\n      return ''.join(stack).lstrip('0') or '0'\n\nGas Station:\n  def canCompleteCircuit(gas, cost):\n      total = start = tank = 0\n      for i in range(len(gas)):\n          diff = gas[i] - cost[i]\n          total += diff; tank += diff\n          if tank < 0:\n              start = i + 1; tank = 0\n      return start if total >= 0 else -1\n  Greedy insight: If total gas >= total cost, solution exists. Start from the point where running tank goes negative.\n\nCandy Distribution:\n  Each child gets at least 1 candy. Higher-rated child gets more than neighbor.\n  Two passes: left-to-right (compare with left neighbor), right-to-left (compare with right).\n  Candies[i] = max of both passes.\n\nTask Scheduler:\n  Schedule tasks with cooldown n between same tasks.\n  Count most frequent task. Answer = max(len(tasks), (maxFreq-1)*(n+1)+countOfMax).",
                "key_points": [
                    "Remove K digits is a classic monotonic stack + greedy problem",
                    "Gas station uses the 'if total >= 0, solution exists' insight",
                    "Candy distribution needs two-pass greedy (left and right)",
                    "Task scheduler uses frequency analysis to determine minimum time",
                    "These advanced greedy problems appear in Amazon and Microsoft SDE rounds"
                ],
                "examples": [
                    {"question": "Remove 3 digits from '1432219' to get smallest", "solution": "Stack: [1]. '4'>1, push [1,4]. '3'<4, pop 4, k=2. [1,3]. '2'<3, pop 3, k=1. [1,2]. '2'>=2, push [1,2,2]. '1'<2, pop 2, k=0. [1,2,1]. '9': push [1,2,1,9]. Result: '1219'."},
                    {"question": "Gas station: gas=[1,2,3,4,5], cost=[3,4,5,1,2]", "solution": "total=0, tank=0, start=0. i=0: diff=-2, total=-2, tank=-2<0, start=1, tank=0. i=1: diff=-2, total=-4, tank=-2<0, start=2, tank=0. i=2: diff=-2, total=-6, tank=-2<0, start=3, tank=0. i=3: diff=3, total=-3, tank=3. i=4: diff=3, total=0, tank=6. total>=0, return start=3."},
                    {"question": "Candy: ratings=[1,0,2]", "solution": "Left pass: [1,1,2] (0<1 so keep 1, 2>0 so increment). Right pass: [2,1,2] (0<2 ok, 1>0 so left[1] should be at least 2). Take max: [2,1,2]. Total = 5."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Greedy Choice Property", "explanation": "A locally optimal choice leads to globally optimal solution. Must be proven (often by exchange argument)."},
            {"name": "Activity Selection", "explanation": "Sort by end time, greedily pick non-overlapping activities. O(n log n). Maximizes count of activities."},
            {"name": "Fractional Knapsack", "explanation": "Sort by value/weight ratio. Take items greedily. Unlike 0/1 knapsack, fractions allowed, so greedy works."},
            {"name": "Huffman Coding", "explanation": "Greedy compression. Always merge two lowest-frequency nodes. Produces optimal prefix-free binary codes."},
            {"name": "Interval Merging", "explanation": "Sort by start time. If current overlaps with last merged, extend. Otherwise add new interval."}
        ],
        "formulas": [
            "Activity selection: O(n log n) sort + O(n) scan",
            "Fractional knapsack: sort by val/wt ratio, O(n log n)",
            "Huffman: O(n log n) using min-heap",
            "Minimum platforms: O(n log n) sort + O(n) sweep",
            "Job sequencing: O(n^2) simple, O(n log n) with DSU"
        ],
        "solved_examples": [
            {"question": "Fractional knapsack: W=15, items (wt,val): (1,5),(3,10),(5,15),(7,7),(9,8).", "solution": "Ratios: 5.0, 3.33, 3.0, 1.0, 0.89. Sort: item1(5.0), item2(3.33), item3(3.0). Take item1: W=14, val=5. Take item2: W=11, val=15. Take item3: W=6, val=30. Take item4: W=-1, take 6/7: val=30+6=36. Answer: 36."},
            {"question": "Merge intervals: [(1,4),(2,5),(7,9)].", "solution": "Sort by start. (1,4) and (2,5): overlap, merge to (1,5). (7,9): no overlap. Result: [(1,5),(7,9)]."},
            {"question": "Jump Game II: minimum jumps for [2,3,1,1,4].", "solution": "Greedy: current end=0, farthest=0, jumps=0. i=0: farthest=2, i==end=0, jump=1, end=2. i=1: farthest=4, i=1<2. i=2: i==end=2, jump=2, end=4. Reached. Answer: 2 jumps."}
        ],
        "tips": [
            "Not all problems that look greedy are greedy. Verify the greedy choice property.",
            "If greedy doesn't work, consider DP. Many problems have both greedy and DP solutions.",
            "For interval problems, always clarify if intervals are open or closed.",
            "Sorting is the first step in almost every greedy algorithm - choose the right sort key.",
            "In TCS NQT and Infosys, greedy MCQs test whether you know WHEN greedy works vs fails."
        ],
    },
    50: {
        "title": "Bit Manipulation",
        "overview": "Bit manipulation operates directly on binary representations of numbers, enabling extremely efficient solutions. This topic covers AND, OR, XOR operations, bit masking, counting set bits, power-of-2 checks, single-number problems, and subset generation using bitmasks. These problems appear in Amazon, Microsoft, and TCS NQT exams.",
        "chapters": [
            {
                "title": "Bitwise Operators & Basics",
                "content": "Bitwise Operators:\n  AND (&): 1 & 1 = 1, else 0. Useful for masking/clearing bits.\n  OR  (|): 0 | 0 = 0, else 1. Useful for setting bits.\n  XOR (^): Same = 0, different = 1. Useful for toggling and finding unique elements.\n  NOT (~): Flips all bits. ~x = -(x+1) in two's complement.\n  Left Shift (<<): x << k = x * 2^k. Shifts bits left, fills 0s.\n  Right Shift (>>): x >> k = x // 2^k. Shifts bits right.\n\nCommon Bit Tricks:\n  Check if ith bit is set: (n >> i) & 1 == 1\n  Set ith bit: n | (1 << i)\n  Clear ith bit: n & ~(1 << i)\n  Toggle ith bit: n ^ (1 << i)\n  Clear lowest set bit: n & (n-1)\n  Isolate lowest set bit: n & (-n)\n  Check power of 2: n > 0 and (n & (n-1)) == 0\n\nTwo's Complement: -n is represented as ~n + 1.\n  -5 in 8-bit: 5 = 00000101, ~5 = 11111010, +1 = 11111011.\n\nSwap without temp variable:\n  a ^= b; b ^= a; a ^= b\n  Works because XOR is its own inverse: a ^ b ^ b = a.",
                "key_points": [
                    "XOR is the most versatile bit operator: a^a=0, a^0=a",
                    "n & (n-1) clears the lowest set bit - key trick for many problems",
                    "Power of 2 check: n & (n-1) == 0 (and n > 0)",
                    "Left shift by k = multiply by 2^k. Right shift by k = divide by 2^k.",
                    "Bit manipulation questions are common in TCS NQT, Amazon, and Google interviews"
                ],
                "examples": [
                    {"question": "Check if 3rd bit (0-indexed) of 13 is set. 13 = 1101.", "solution": "(13 >> 3) & 1 = (1) & 1 = 1. Yes, 3rd bit is set."},
                    {"question": "Set the 2nd bit of 9. 9 = 1001.", "solution": "9 | (1 << 2) = 1001 | 0100 = 1101 = 13."},
                    {"question": "Is 16 a power of 2?", "solution": "16 = 10000. 16 & 15 = 10000 & 01111 = 00000 = 0. And 16 > 0. Yes, power of 2."}
                ],
            },
            {
                "title": "Counting Set Bits & Bit Tricks",
                "content": "Count Set Bits (Hamming Weight):\n  Method 1 - Brian Kernighan's Algorithm:\n  def countBits(n):\n      count = 0\n      while n:\n          n &= (n-1)  # clear lowest set bit\n          count += 1\n      return count\n  Time: O(number of set bits).\n\n  Method 2 - Lookup table / popcount: O(1) with hardware support.\n  Python: bin(n).count('1')\n\nCount total set bits from 1 to n:\n  Pattern: For bit position k, bits alternate in groups of 2^k.\n  Total set bits = sum over each bit position.\n  Or use: f(n) = f(n//2)*2 + n//2 + (n%2==1 ? f(n%2) : 0). O(log n).\n\nHamming Distance: Number of positions where bits differ.\n  hamming(a, b) = countBits(a ^ b)\n\nReverse Bits of a 32-bit integer:\n  def reverseBits(n):\n      result = 0\n      for i in range(32):\n          result = (result << 1) | (n & 1)\n          n >>= 1\n      return result\n\nCheck if number is a palindrome in binary:\n  Compare reversed bits with original (for significant bits only).\n\nNext Power of 2:\n  def nextPowerOf2(n):\n      n -= 1\n      n |= n >> 1; n |= n >> 2; n |= n >> 4\n      n |= n >> 8; n |= n >> 16\n      return n + 1",
                "key_points": [
                    "Brian Kernighan's algorithm counts set bits in O(set bits) time",
                    "Hamming distance = popcount(a XOR b)",
                    "Reverse bits: shift result left, append LSB of n, shift n right",
                    "Next power of 2: fill all bits right of MSB, then add 1",
                    "Set bit counting is asked in Amazon, Microsoft, and GATE exams"
                ],
                "examples": [
                    {"question": "Count set bits of 23. 23 = 10111.", "solution": "Brian Kernighan: 23&22=10111&10110=10110(22), count=1. 22&21=10110&10101=10100(20), count=2. 20&19=10100&10011=10000(16), count=3. 16&15=0, count=4. Answer: 4 set bits."},
                    {"question": "Hamming distance between 1 (001) and 4 (100)", "solution": "1 XOR 4 = 001 XOR 100 = 101 = 5. countBits(5) = 2. Hamming distance = 2."},
                    {"question": "Reverse bits of 13 (8-bit: 00001101)", "solution": "Process: take LSB, shift left: result builds as 10110000. Reversed 8-bit: 10110000 = 176."}
                ],
            },
            {
                "title": "Single Number Problems",
                "content": "Single Number I: Every element appears twice except one. Find it.\n  def singleNumber(nums):\n      result = 0\n      for num in nums: result ^= num\n      return result\n  Why: a ^ a = 0, and 0 ^ b = b. All pairs cancel out.\n\nSingle Number II: Every element appears three times except one.\n  Use bit counting: For each bit position, count set bits. If count % 3 != 0, that bit belongs to the single number.\n  def singleNumber2(nums):\n      result = 0\n      for i in range(32):\n          bit_sum = sum((num >> i) & 1 for num in nums)\n          if bit_sum % 3:\n              result |= (1 << i)\n      return result\n\nSingle Number III: Two elements appear once, rest appear twice.\n  XOR all elements. Result = a ^ b (the two unique numbers).\n  Find any set bit in result (the differentiating bit).\n  Partition array into two groups based on that bit.\n  XOR each group separately to get a and b.\n  def singleNumber3(nums):\n      xor_all = 0\n      for num in nums: xor_all ^= num\n      diff_bit = xor_all & (-xor_all)  # lowest set bit\n      a = b = 0\n      for num in nums:\n          if num & diff_bit: a ^= num\n          else: b ^= num\n      return [a, b]\n\nFind Missing Number (0 to n, one missing):\n  XOR all numbers 0..n, XOR with all array elements. Result = missing number.\n  Or use sum formula: n*(n+1)/2 - sum(array).",
                "key_points": [
                    "XOR of all elements cancels pairs: the classic single number trick",
                    "For elements appearing 3 times: count bits modulo 3",
                    "For two unique numbers: XOR gives difference, split by any differing bit",
                    "Missing number: XOR or sum formula - both O(n) time O(1) space",
                    "Single number problems are very common in Amazon, Google, and TCS interviews"
                ],
                "examples": [
                    {"question": "Single number in [4,1,2,1,2]", "solution": "XOR all: 4^1^2^1^2 = 4^(1^1)^(2^2) = 4^0^0 = 4. Answer: 4."},
                    {"question": "Single number (appears once, others thrice) in [2,2,3,2]", "solution": "Bit 0: 0+0+1+0=1, 1%3=1 -> set. Bit 1: 1+1+1+1=4, 4%3=1 -> set. Result = 11 binary = 3. Answer: 3."},
                    {"question": "Find missing number in [3,0,1] (range 0-3)", "solution": "XOR: (0^1^2^3) ^ (3^0^1) = (0^0)^(1^1)^(3^3)^2 = 2. Or sum: 6-4=2. Missing: 2."}
                ],
            },
            {
                "title": "Subset Generation & Bitmask Techniques",
                "content": "Subset Generation using Bitmask:\n  For n elements, iterate through all 2^n bitmasks (0 to 2^n - 1).\n  Each bit position represents whether to include that element.\n\n  def subsets(nums):\n      n = len(nums)\n      result = []\n      for mask in range(1 << n):  # 0 to 2^n - 1\n          subset = []\n          for i in range(n):\n              if mask & (1 << i):\n                  subset.append(nums[i])\n          result.append(subset)\n      return result\n\n  Example: nums = [a, b, c]\n  mask=000 -> []\n  mask=001 -> [a]\n  mask=010 -> [b]\n  mask=011 -> [a,b]\n  mask=100 -> [c]\n  mask=101 -> [a,c]\n  mask=110 -> [b,c]\n  mask=111 -> [a,b,c]\n\nIterating over submasks of a given mask:\n  sub = mask\n  while sub > 0:\n      process(sub)\n      sub = (sub - 1) & mask\n\nBitmask DP:\n  State includes a set of elements, encoded as bitmask.\n  dp[mask] = optimal value for subset represented by mask.\n  Transition: try adding one element to the subset.\n  Time: O(2^n * n), feasible for n <= 20.\n\nMaximum AND of pair:\n  For each bit from MSB to LSB, check if enough numbers have that bit set.\n  Greedily include bits that at least 2 numbers have.\n\nMinimum XOR pair:\n  Sort the array. Minimum XOR must be between adjacent elements in sorted order.",
                "key_points": [
                    "Bitmask subset generation: iterate 0 to 2^n-1, check each bit",
                    "Bitmask DP is powerful for set-based problems when n <= 20",
                    "Iterating submasks of a mask: sub = (sub-1) & mask",
                    "Minimum XOR pair is always between adjacent elements in sorted array",
                    "These techniques appear in competitive programming and advanced interviews"
                ],
                "examples": [
                    {"question": "Generate all subsets of [1,2,3] using bitmask", "solution": "n=3, iterate 0-7. 0(000):[], 1(001):[1], 2(010):[2], 3(011):[1,2], 4(100):[3], 5(101):[1,3], 6(110):[2,3], 7(111):[1,2,3]. Total: 8 subsets."},
                    {"question": "Find minimum XOR pair in [5,3,1,4,2]", "solution": "Sort: [1,2,3,4,5]. Adjacent XORs: 1^2=3, 2^3=1, 3^4=7, 4^5=1. Minimum XOR = 1 (between 2,3 or 4,5)."},
                    {"question": "Count submasks of mask 5 (101 binary)", "solution": "sub=5(101): process. sub=(4)&5=4(100): process. sub=(3)&5=1(001): process. sub=(0)&5=0: stop. Submasks: {5, 4, 1} plus empty set. Total non-empty: 3."}
                ],
            },
            {
                "title": "XOR Properties & Advanced Problems",
                "content": "Key XOR Properties:\n  a ^ a = 0 (self-inverse)\n  a ^ 0 = a (identity)\n  a ^ b = b ^ a (commutative)\n  (a ^ b) ^ c = a ^ (b ^ c) (associative)\n  a ^ b = c implies a = b ^ c (invertible)\n\nXOR of numbers 0 to n:\n  def xorUpToN(n):\n      if n % 4 == 0: return n\n      if n % 4 == 1: return 1\n      if n % 4 == 2: return n + 1\n      if n % 4 == 3: return 0\n  Pattern: n, 1, n+1, 0 repeating every 4.\n\nXOR queries on array range [L, R]:\n  prefix_xor[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]\n  xor(L, R) = prefix_xor[R] ^ prefix_xor[L-1]\n\nFind two non-repeating elements:\n  XOR all gives a^b. Use lowest set bit to partition.\n  (Same as Single Number III above.)\n\nMaximum XOR of two numbers in array:\n  Use Trie. Insert all numbers bit by bit (MSB first).\n  For each number, greedily try opposite bit to maximize XOR.\n  Time: O(n * 32) = O(n).\n\nGray Code: Generate n-bit Gray code sequence.\n  def grayCode(n):\n      return [i ^ (i >> 1) for i in range(1 << n)]\n  Adjacent codes differ by exactly one bit.\n\nDivide two integers without * / %:\n  Use bit shifting. Repeatedly subtract largest power-of-2 multiple of divisor.",
                "key_points": [
                    "XOR of 0 to n follows a pattern with period 4: memorize it",
                    "Prefix XOR enables O(1) range XOR queries after O(n) preprocessing",
                    "Maximum XOR pair uses Trie - important for competitive programming",
                    "Gray code: i ^ (i >> 1) - each adjacent pair differs by 1 bit",
                    "XOR properties make many problems solvable in O(1) space"
                ],
                "examples": [
                    {"question": "XOR of all numbers from 1 to 7", "solution": "7 % 4 = 3, so answer = 0. Verify: 1^2=3, 3^3=0, 0^4=4, 4^5=1, 1^6=7, 7^7=0. Correct!"},
                    {"question": "XOR of subarray [2..4] in arr=[3,1,5,2,4]. Prefix XOR: [3,2,7,5,1].", "solution": "xor(2,4) = prefix[4] ^ prefix[1] = 1 ^ 2 = 3. Verify: 5^2^4 = 3. Correct!"},
                    {"question": "Generate 3-bit Gray code", "solution": "i^(i>>1) for i=0..7: 0^0=0, 1^0=1, 2^1=3, 3^1=2, 4^2=6, 5^2=7, 6^3=5, 7^3=4. Sequence: [0,1,3,2,6,7,5,4] = [000,001,011,010,110,111,101,100]."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "XOR Properties", "explanation": "a^a=0, a^0=a, commutative, associative. Foundation of single number, missing number, and pair problems."},
            {"name": "Brian Kernighan's Algorithm", "explanation": "Count set bits by repeatedly clearing lowest set bit: n &= (n-1). Runs in O(set bits) time."},
            {"name": "Bitmask Subset Generation", "explanation": "Iterate 0 to 2^n-1. Each integer represents a subset. Bit i set means element i included."},
            {"name": "Bit Manipulation Tricks", "explanation": "Check bit: (n>>i)&1. Set bit: n|(1<<i). Clear bit: n&~(1<<i). Clear lowest set: n&(n-1). Isolate lowest: n&(-n)."},
            {"name": "Power of 2 Check", "explanation": "n > 0 and (n & (n-1)) == 0. Works because powers of 2 have exactly one set bit."}
        ],
        "formulas": [
            "XOR 0 to n: n%4==0:n, n%4==1:1, n%4==2:n+1, n%4==3:0",
            "Count set bits (Brian Kernighan): O(number of set bits)",
            "Subsets using bitmask: 2^n subsets for n elements",
            "Hamming distance(a,b) = popcount(a XOR b)",
            "n & (n-1) clears lowest set bit; n & (-n) isolates lowest set bit"
        ],
        "solved_examples": [
            {"question": "Find the two numbers appearing once in [1,2,1,3,2,5].", "solution": "XOR all: 1^2^1^3^2^5 = 3^5 = 6 (110). Lowest set bit: 6&(-6) = 2 (010). Group by bit 1: {2,2,3} and {1,1,5}. XOR each: 3 and 5. Answer: [3, 5]."},
            {"question": "Check if 12 is a power of 2.", "solution": "12 & 11 = 1100 & 1011 = 1000 = 8 != 0. Not a power of 2."},
            {"question": "Swap 3 and 7 using XOR.", "solution": "a=3(011), b=7(111). a^=b: a=100(4). b^=a: b=011(3). a^=b: a=111(7). Now a=7, b=3. Swapped!"}
        ],
        "tips": [
            "XOR is your best friend for 'find the unique element' problems.",
            "Memorize the XOR 0-to-n pattern (period 4) - saves time in MCQs.",
            "n & (n-1) trick appears everywhere: power of 2, count bits, etc.",
            "For placement MCQs, practice converting between decimal and binary quickly.",
            "Bit manipulation gives O(1) or O(log n) solutions where brute force is O(n) - mention this in interviews."
        ],
    },
    51: {
        "title": "String Algorithms",
        "overview": "String algorithms handle pattern matching, searching, and manipulation efficiently. This topic covers KMP, Rabin-Karp, Z-algorithm for pattern matching, palindrome detection, anagram problems, and trie data structures. String problems are extremely common in Amazon, Microsoft, Google, and TCS placement exams.",
        "chapters": [
            {
                "title": "KMP Pattern Matching",
                "content": "KMP (Knuth-Morris-Pratt) algorithm matches a pattern in text in O(n+m) time by preprocessing the pattern to build a failure/prefix function.\n\nFailure Function (LPS Array):\n  LPS[i] = length of longest proper prefix of pattern[0..i] that is also a suffix.\n  def buildLPS(pattern):\n      m = len(pattern)\n      lps = [0] * m\n      length = 0; i = 1\n      while i < m:\n          if pattern[i] == pattern[length]:\n              length += 1; lps[i] = length; i += 1\n          else:\n              if length != 0: length = lps[length-1]\n              else: lps[i] = 0; i += 1\n      return lps\n\nKMP Search:\n  def kmpSearch(text, pattern):\n      n, m = len(text), len(pattern)\n      lps = buildLPS(pattern)\n      i = j = 0  # i for text, j for pattern\n      matches = []\n      while i < n:\n          if text[i] == pattern[j]:\n              i += 1; j += 1\n          if j == m:\n              matches.append(i - j)\n              j = lps[j-1]\n          elif i < n and text[i] != pattern[j]:\n              if j != 0: j = lps[j-1]\n              else: i += 1\n      return matches\n\nExample: text='ABABDABACDABABCABAB', pattern='ABABCABAB'\nLPS for 'ABABCABAB': [0,0,1,2,0,1,2,3,4]\nKMP finds match at index 10.\n\nWhy KMP is O(n+m): Both i and j never decrease after incrementing. Total advances bounded by n + m.",
                "key_points": [
                    "KMP avoids redundant comparisons using the LPS (failure) array",
                    "LPS[i] = length of longest proper prefix-suffix of pattern[0..i]",
                    "Time: O(n+m) for search + O(m) for LPS preprocessing",
                    "KMP is the standard algorithm for exact string matching",
                    "GATE and placement exams frequently ask to compute the LPS array"
                ],
                "examples": [
                    {"question": "Build LPS for 'AAACAAAA'", "solution": "i=1: A==A, lps[1]=1. i=2: A==A, lps[2]=2. i=3: C!=A, length=lps[1]=1, C!=A, length=lps[0]=0, lps[3]=0. i=4: A==A, lps[4]=1. i=5: A==A, lps[5]=2. i=6: A==A, lps[6]=3. i=7: A==A, lps[7]=3? Wait: length=3, pattern[7]='A'==pattern[3]='C'? No. length=lps[2]=2, A==A? pattern[7]='A'==pattern[2]='A'. lps[7]=3. Actually let me recompute carefully. LPS = [0,1,2,0,1,2,3,3]."},
                    {"question": "Find 'ABA' in 'AABABAABA' using KMP", "solution": "LPS for ABA: [0,0,1]. Search: i=0,j=0 A==A j=1. i=1 A!=B j=lps[0]=0. A==A j=1. i=2 B==B j=2. i=3 A==A j=3=m, match at 1! j=lps[2]=1. i=4 B==B j=2. i=5 A==A j=3=m, match at 3! j=1. Continue. Matches at positions: 1, 3, 6."},
                    {"question": "Why is naive string matching O(nm) but KMP is O(n+m)?", "solution": "Naive: for each position in text (n), compare up to m characters. Total: O(nm). KMP: LPS tells us how far to skip on mismatch. The text pointer never goes back, and pattern pointer advances or jumps to LPS value. Total comparisons: at most 2n."}
                ],
            },
            {
                "title": "Rabin-Karp & Z-Algorithm",
                "content": "Rabin-Karp Algorithm: Uses rolling hash for pattern matching.\n  Hash function: h(s) = (s[0]*d^(m-1) + s[1]*d^(m-2) + ... + s[m-1]) mod q\n  Rolling hash: h(s[i+1..i+m]) = (d*(h(s[i..i+m-1]) - s[i]*d^(m-1)) + s[i+m]) mod q\n\n  def rabinKarp(text, pattern):\n      n, m = len(text), len(pattern)\n      d = 256; q = 101  # prime\n      h = pow(d, m-1, q)\n      p_hash = t_hash = 0\n      for i in range(m):\n          p_hash = (d * p_hash + ord(pattern[i])) % q\n          t_hash = (d * t_hash + ord(text[i])) % q\n      for i in range(n - m + 1):\n          if p_hash == t_hash:\n              if text[i:i+m] == pattern: print(f'Found at {i}')\n          if i < n - m:\n              t_hash = (d*(t_hash - ord(text[i])*h) + ord(text[i+m])) % q\n              if t_hash < 0: t_hash += q\n\n  Average: O(n+m). Worst: O(nm) due to hash collisions.\n  Best for: multiple pattern matching.\n\nZ-Algorithm: Z[i] = length of longest substring starting at i that matches prefix of string.\n  def zFunction(s):\n      n = len(s)\n      z = [0] * n; z[0] = n\n      l = r = 0\n      for i in range(1, n):\n          if i < r: z[i] = min(r - i, z[i - l])\n          while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1\n          if i + z[i] > r: l, r = i, i + z[i]\n      return z\n\nPattern matching with Z: Concatenate pattern + '$' + text. Where Z[i] == m, pattern found.\n  Time: O(n+m).",
                "key_points": [
                    "Rabin-Karp: O(n+m) average using rolling hash. Spurious hits possible.",
                    "Use a large prime q to reduce hash collisions",
                    "Z-algorithm: Z[i] = longest match with prefix starting at position i",
                    "Z-algorithm is simpler to implement than KMP for many applications",
                    "Rabin-Karp excels at multi-pattern search (e.g., plagiarism detection)"
                ],
                "examples": [
                    {"question": "Z-array for 'aabxaab'", "solution": "z[0]=7(full). i=1: s[1]='a'==s[0]='a', z[1]=1. s[2]='b'!=s[1]='a'. z[1]=1. i=2: s[2]='b'!=s[0]='a'. z[2]=0. i=3: z[3]=0. i=4: s[4]='a'==s[0], s[5]='a'==s[1], s[6]='b'==s[2], end. z[4]=3. i=5: within [4,7), z[5]=min(2,z[1])=1. z[5]=1. i=6: z[6]=0. Z=[7,1,0,0,3,1,0]."},
                    {"question": "Find 'ab' in 'ababab' using Z-algorithm", "solution": "Concat: 'ab$ababab'. Z-array: [9,0,0,2,0,2,0,2,0]. Positions where Z[i]==2 (length of pattern): i=3,5,7. Matches at text positions: 3-3=0, 5-3=2, 7-3=4. Found at 0, 2, 4."},
                    {"question": "Rabin-Karp: find 'cat' in 'the cat sat'. d=26, q=101.", "solution": "Hash 'cat' = (2*676+0*26+19)%101 = (1352+19)%101 = 1371%101 = 57. Roll hash through text. When hash matches 57, verify characters. Match at position 4."}
                ],
            },
            {
                "title": "Palindrome Detection & Problems",
                "content": "Palindrome Check: O(n) two-pointer.\n  def isPalindrome(s):\n      l, r = 0, len(s)-1\n      while l < r:\n          if s[l] != s[r]: return False\n          l += 1; r -= 1\n      return True\n\nLongest Palindromic Substring:\n  Method 1 - Expand Around Center: O(n^2) time, O(1) space.\n  For each center (2n-1 centers: n single, n-1 between pairs):\n    Expand while characters match.\n  def longestPalindrome(s):\n      def expand(l, r):\n          while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1\n          return s[l+1:r]\n      result = ''\n      for i in range(len(s)):\n          odd = expand(i, i)\n          even = expand(i, i+1)\n          result = max(result, odd, even, key=len)\n      return result\n\n  Method 2 - Manacher's Algorithm: O(n) time.\n  Transform string (insert # between chars). Use symmetry to avoid redundant expansion.\n\nPalindromic Substrings Count:\n  Use expand around center for each of 2n-1 centers. Count expansions.\n\nLongest Palindromic Subsequence:\n  DP: LPS(s) = LCS(s, reverse(s)). O(n^2).\n\nMinimum insertions to make palindrome:\n  = n - LPS(s). (Characters not in longest palindromic subsequence need matching.)\n\nValid Palindrome II (can delete at most one character):\n  Two pointers. On mismatch, try skipping left or right. Check if remaining is palindrome.",
                "key_points": [
                    "Expand around center is the most practical palindrome substring algorithm",
                    "There are 2n-1 centers (n odd-length, n-1 even-length)",
                    "Longest palindromic subsequence = LCS with reversed string",
                    "Manacher's algorithm is O(n) but rarely asked to implement in interviews",
                    "Palindrome problems are extremely common in Amazon, Google, and TCS exams"
                ],
                "examples": [
                    {"question": "Longest palindromic substring of 'babad'", "solution": "Centers: b(b), a(bab), b(aba), a(a), d(d). Between: ba, ab, ba, ad. Longest: 'bab' or 'aba' (length 3)."},
                    {"question": "Count palindromic substrings in 'aaa'", "solution": "Single: a,a,a (3). Double: aa,aa (2). Triple: aaa (1). Total: 6."},
                    {"question": "Min insertions to make 'abcd' a palindrome", "solution": "LPS of 'abcd': LCS('abcd','dcba') = 1 (just 'd' or 'a' etc). Min insertions = 4-1 = 3. E.g., abcd -> dcbabcd (or abcdcba)."}
                ],
            },
            {
                "title": "Trie Data Structure",
                "content": "A Trie (prefix tree) stores strings character by character. Each node has children for each possible character.\n\nTrie Node:\n  class TrieNode:\n      def __init__(self):\n          self.children = {}  # char -> TrieNode\n          self.is_end = False  # marks end of word\n\nOperations:\n  class Trie:\n      def __init__(self): self.root = TrieNode()\n\n      def insert(self, word):  # O(m)\n          node = self.root\n          for ch in word:\n              if ch not in node.children:\n                  node.children[ch] = TrieNode()\n              node = node.children[ch]\n          node.is_end = True\n\n      def search(self, word):  # O(m)\n          node = self.root\n          for ch in word:\n              if ch not in node.children: return False\n              node = node.children[ch]\n          return node.is_end\n\n      def startsWith(self, prefix):  # O(m)\n          node = self.root\n          for ch in prefix:\n              if ch not in node.children: return False\n              node = node.children[ch]\n          return True\n\nApplications:\n- Autocomplete / search suggestions\n- Spell checker\n- Word search in grid (DFS + Trie)\n- Longest common prefix\n- Maximum XOR pair (binary Trie)\n\nLongest Common Prefix using Trie:\n  Insert all strings. Traverse from root while node has exactly one child and is not end. Path = LCP.\n\nWord Break Problem:\n  Use Trie + DP. dp[i] = True if s[0..i-1] can be segmented into dictionary words.\n  For each position, check Trie for matching prefix.",
                "key_points": [
                    "Trie insert/search/prefix are all O(word_length) - very efficient",
                    "Trie space: O(total characters across all words * alphabet size)",
                    "Trie is the go-to for prefix-based problems (autocomplete, prefix search)",
                    "Binary Trie (0/1) is used for maximum XOR problems",
                    "Trie questions appear in Amazon, Google, Microsoft SDE interviews"
                ],
                "examples": [
                    {"question": "Insert 'apple', 'app' into Trie. Search 'app' and 'apple'.", "solution": "Insert 'apple': root->a->p->p->l->e(end). Insert 'app': root->a->p->p(end, reuse existing path). Search 'app': traverse a->p->p, is_end=True. Found! Search 'apple': traverse a->p->p->l->e, is_end=True. Found!"},
                    {"question": "Longest common prefix of ['flower','flow','flight'] using Trie", "solution": "Insert all. From root: 'f' (only child, not end). 'l' (only child). 'o'/'i' (two children) - stop! LCP = 'fl'."},
                    {"question": "Word break: s='leetcode', dict=['leet','code']", "solution": "dp[0]=True. i=4: s[0:4]='leet' in dict and dp[0]=True, so dp[4]=True. i=8: s[4:8]='code' in dict and dp[4]=True, so dp[8]=True. Answer: True."}
                ],
            },
            {
                "title": "String Manipulation & Common Problems",
                "content": "String Rotation Check:\n  s2 is a rotation of s1 if len(s1)==len(s2) and s2 in (s1+s1).\n  Example: 'waterbottle' rotation of 'erbottlewat'? 'erbottlewat'+'erbottlewat' contains 'waterbottle'? Yes!\n\nLongest Substring Without Repeating Characters:\n  Sliding window + HashSet.\n  def lengthOfLongestSubstring(s):\n      seen = {}; start = max_len = 0\n      for i, ch in enumerate(s):\n          if ch in seen and seen[ch] >= start:\n              start = seen[ch] + 1\n          seen[ch] = i\n          max_len = max(max_len, i - start + 1)\n      return max_len\n  Time: O(n)\n\nMinimum Window Substring:\n  Find smallest substring of s containing all characters of t.\n  Use two HashMaps (need, have) with sliding window. Expand right, shrink left.\n  Time: O(n)\n\nString Compression: 'aabcccccaaa' -> 'a2b1c5a3'. Compare lengths.\n\nAtoi (string to integer):\n  Handle: whitespace, +/- sign, digits, overflow, non-digit characters.\n\nLongest Repeating Character Replacement:\n  Sliding window. Window is valid if (window_size - max_freq_in_window) <= k.\n  Expand right, track max frequency. If invalid, shrink left.\n\nGroup Shifted Strings:\n  Key = tuple of differences between consecutive characters (mod 26).\n  'abc' -> (1,1), 'bcd' -> (1,1). Same group!",
                "key_points": [
                    "Sliding window + HashMap solves most substring problems in O(n)",
                    "String rotation: check if s2 is substring of s1+s1",
                    "Minimum window substring is a hard problem - know the two-pointer approach",
                    "String compression / run-length encoding is a common easy problem",
                    "These problems are top interview questions at Amazon, Google, Facebook"
                ],
                "examples": [
                    {"question": "Longest substring without repeating in 'abcabcbb'", "solution": "Window: a(1), ab(2), abc(3), move start past a: bca(3), move past b: cab(3), move past c: abc(3), move: bc(2), b(1). Max length = 3."},
                    {"question": "Is 'rotation' a rotation of 'tationro'?", "solution": "len match: 8==8. 'tationro'+'tationro' = 'tationrotationro'. Contains 'rotation'? Yes at index 6. It is a rotation!"},
                    {"question": "Minimum window in s='ADOBECODEBANC' containing t='ABC'", "solution": "Expand until all ABC found: window 'ADOBEC' (0-5, len 6). Shrink: 'DOBEC' missing A. Expand: 'DOBECODEBA' has ABC. Shrink to 'CODEBA' has ABC (len 6). Shrink: 'ODEBA' missing C. Expand: 'ODEBANC' has ABC. Shrink: 'BANC' has ABC (len 4). Answer: 'BANC'."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "KMP Algorithm", "explanation": "Pattern matching in O(n+m). Uses LPS (failure) array to skip redundant comparisons. Text pointer never goes back."},
            {"name": "Rabin-Karp", "explanation": "Rolling hash pattern matching. Average O(n+m), worst O(nm). Good for multiple pattern search."},
            {"name": "Z-Algorithm", "explanation": "Z[i] = length of longest match with prefix starting at i. Pattern matching by concatenation. O(n+m)."},
            {"name": "Trie", "explanation": "Prefix tree for efficient string operations. Insert/Search/Prefix in O(word_length). Used for autocomplete, spell check."},
            {"name": "Sliding Window", "explanation": "Maintain a window with two pointers. Expand/shrink to find optimal substring. O(n) for most substring problems."}
        ],
        "formulas": [
            "KMP: O(n+m) time, O(m) space for LPS array",
            "Rabin-Karp rolling hash: h_new = (d*(h_old - s[i]*d^(m-1)) + s[i+m]) mod q",
            "Z-algorithm: O(n) time and space",
            "Trie operations: O(word_length) per operation",
            "Longest palindromic subsequence = LCS(s, reverse(s))"
        ],
        "solved_examples": [
            {"question": "Find pattern 'aab' in text 'aabaacaadaabaaba' using KMP.", "solution": "LPS for 'aab': [0,1,0]. KMP finds matches at positions 0, 9, 12."},
            {"question": "Longest substring without repeating in 'pwwkew'.", "solution": "Sliding window: p(1), pw(2), w repeat move start: wk(2), wke(3), w repeat: kew(3). Answer: 3."},
            {"question": "Count palindromic substrings in 'abc'.", "solution": "Single chars: a, b, c (3). Doubles: ab(no), bc(no). Triple: abc(no). Total: 3."}
        ],
        "tips": [
            "For pattern matching: KMP for single pattern, Rabin-Karp for multiple patterns, Trie for prefix queries.",
            "Sliding window technique solves 90% of substring problems - master it.",
            "In interviews, string problems often have O(n) solutions - avoid O(n^2) unless necessary.",
            "Practice building the LPS array by hand - GATE and placement exams test this directly.",
            "When asked about autocomplete or dictionary problems, immediately mention Trie."
        ],
    },
    # === CORE CS SUBJECTS (Topics 52-59) ===
    52: {
        "title": "OS: Processes & Threads",
        "overview": "Operating system process management is a core CS topic tested in placements. This covers the process lifecycle, PCB, threads vs processes, multi-threading, inter-process communication (IPC), context switching, and the fork() system call. These concepts are frequently tested in TCS NQT, Infosys, Wipro, and Amazon interviews.",
        "chapters": [
            {
                "title": "Process Fundamentals & Lifecycle",
                "content": "A process is a program in execution. It has its own memory space, program counter, registers, and stack.\n\nProcess States:\n  New -> Ready -> Running -> Waiting/Blocked -> Terminated\n  New: Process is being created.\n  Ready: Waiting for CPU allocation.\n  Running: Instructions being executed.\n  Waiting: Waiting for I/O or event.\n  Terminated: Process finished execution.\n\nState Transitions:\n  New -> Ready: Admitted to ready queue.\n  Ready -> Running: Scheduler dispatches process.\n  Running -> Ready: Preempted (time quantum expired).\n  Running -> Waiting: I/O request or wait for event.\n  Waiting -> Ready: I/O complete or event occurred.\n  Running -> Terminated: Process exits.\n\nProcess Control Block (PCB):\n  Contains: Process ID (PID), Process state, Program counter,\n  CPU registers, Memory management info (page tables),\n  I/O status, Accounting info (CPU time used).\n  PCB is created when process is created, updated on context switch.\n\nProcess Creation:\n  Parent creates child processes. Forms a process tree.\n  fork() in Unix: Creates child as copy of parent.\n  exec(): Replaces process memory with new program.\n  wait(): Parent waits for child to terminate.\n\nProcess Termination:\n  Normal exit, error exit, killed by another process (kill signal).\n  Zombie process: Terminated but parent hasn't called wait().\n  Orphan process: Parent terminated before child.",
                "key_points": [
                    "5 process states: New, Ready, Running, Waiting, Terminated",
                    "PCB stores all information needed to resume a process after context switch",
                    "Zombie process: child terminated but parent hasn't collected exit status",
                    "Orphan process: parent dies first; init/systemd adopts the child",
                    "Process lifecycle questions are very common in TCS NQT and GATE"
                ],
                "examples": [
                    {"question": "A process is currently Running and makes a read() system call. What state transition occurs?", "solution": "Running -> Waiting (Blocked). The process is waiting for the I/O operation to complete. Once the disk read finishes, the process moves from Waiting -> Ready."},
                    {"question": "How many processes are created by: fork(); fork(); fork();", "solution": "First fork: 2 processes. Second fork: each forks, 4 processes. Third fork: each forks, 8 processes. Total processes = 2^3 = 8 (including the original parent)."},
                    {"question": "What information is stored in PCB?", "solution": "PID, process state, program counter, CPU registers, memory management info (page table base), list of open files, I/O status, scheduling info (priority, time quantum used), accounting info (CPU time)."}
                ],
            },
            {
                "title": "Threads vs Processes",
                "content": "A thread is the smallest unit of execution within a process. A process can have multiple threads sharing the same address space.\n\nProcess vs Thread:\n  Process: Own memory space, heavyweight, isolated, IPC needed for communication.\n  Thread: Shared memory within process, lightweight, direct communication via shared data.\n\nWhat threads share: Code section, data section, heap, open files, signals.\nWhat threads have own: Thread ID, program counter, register set, stack.\n\nTypes of Threads:\n1) User-Level Threads (ULT): Managed by user library. OS unaware.\n   Fast to create/switch. But if one thread blocks, all block.\n2) Kernel-Level Threads (KLT): Managed by OS kernel.\n   Slower to create/switch. But blocking one doesn't block others.\n3) Hybrid: Many-to-Many mapping.\n\nMultithreading Models:\n  Many-to-One: Many ULTs map to one KLT. Problem: one block = all block.\n  One-to-One: Each ULT maps to one KLT. More concurrency but overhead.\n  Many-to-Many: Many ULTs map to many KLTs. Best of both worlds.\n\nBenefits of Threads:\n  Responsiveness (UI thread + worker threads).\n  Resource sharing (threads share process memory).\n  Economy (thread creation ~100x faster than process).\n  Scalability (utilize multi-core CPUs).\n\nThread Safety: When multiple threads access shared data, use synchronization (mutex, semaphore) to prevent race conditions.",
                "key_points": [
                    "Threads share memory within a process; processes have separate memory",
                    "Thread creation is ~100x faster than process creation",
                    "User-level threads are faster but one blocking thread blocks all",
                    "Kernel-level threads allow true parallelism on multi-core systems",
                    "TCS, Infosys, and Wipro frequently ask thread vs process differences"
                ],
                "examples": [
                    {"question": "A web browser uses threads for: tab rendering, download manager, spell checker. What do they share?", "solution": "They share: the browser's code, global data/settings, heap memory (bookmarks, history), open file descriptors (cookies file). Each thread has its own: stack (local variables), program counter (where in code it is executing), registers."},
                    {"question": "In Many-to-One model, what happens when one thread makes a blocking system call?", "solution": "All threads in that process block. Since the OS sees only one kernel thread for the process, blocking it means no thread can run. This is the main disadvantage of Many-to-One model."},
                    {"question": "Why use threads instead of multiple processes for a web server?", "solution": "Threads share memory so they can access the same connection pool, cache, and configuration without IPC. Thread creation/switching is faster. Memory efficient (shared address space vs separate for each process)."}
                ],
            },
            {
                "title": "Inter-Process Communication (IPC)",
                "content": "Processes need to communicate and synchronize. Since they don't share memory, special IPC mechanisms are needed.\n\nIPC Methods:\n\n1) Pipes: Unidirectional data channel.\n   Unnamed pipe: Between parent-child. int fd[2]; pipe(fd); fd[0]=read, fd[1]=write.\n   Named pipe (FIFO): Between unrelated processes. mkfifo('myfifo').\n\n2) Message Queues: Processes send/receive structured messages.\n   Asynchronous communication. Messages stored in kernel until read.\n\n3) Shared Memory: Fastest IPC. Processes map same physical memory.\n   shmget() to create, shmat() to attach, shmdt() to detach.\n   Needs synchronization (semaphores) to avoid race conditions.\n\n4) Semaphores: Signaling mechanism for synchronization.\n   Binary semaphore (0 or 1) = mutex.\n   Counting semaphore (0 to n) for resource counting.\n   wait(S): if S > 0, decrement; else block.\n   signal(S): increment S; wake up blocked process.\n\n5) Sockets: Communication across network. TCP/UDP.\n   Client-server model. Used for distributed systems.\n\n6) Signals: Asynchronous notification. kill(pid, SIGTERM).\n   Common: SIGKILL (force terminate), SIGTERM (graceful), SIGINT (Ctrl+C).\n\nProducer-Consumer Problem:\n  Shared buffer. Producer adds items, consumer removes.\n  Use semaphores: empty(buffer_size), full(0), mutex(1).\n  Producer: wait(empty), wait(mutex), produce, signal(mutex), signal(full).\n  Consumer: wait(full), wait(mutex), consume, signal(mutex), signal(empty).",
                "key_points": [
                    "Shared memory is fastest IPC but needs explicit synchronization",
                    "Pipes are simplest but unidirectional and typically parent-child only",
                    "Semaphores solve synchronization: binary for mutual exclusion, counting for resources",
                    "Producer-consumer is the classic IPC problem - memorize the semaphore solution",
                    "IPC questions are common in GATE, TCS, and OS interview rounds"
                ],
                "examples": [
                    {"question": "Producer-Consumer with buffer size 5. Show semaphore operations for producing 2 items.", "solution": "Initial: empty=5, full=0, mutex=1. Produce item 1: wait(empty)=4, wait(mutex)=0, add item, signal(mutex)=1, signal(full)=1. Produce item 2: wait(empty)=3, wait(mutex)=0, add item, signal(mutex)=1, signal(full)=2. Buffer: 2 items, empty=3, full=2."},
                    {"question": "Why can't we just use a shared variable (flag) instead of semaphores?", "solution": "Race condition! Two processes checking and setting the flag simultaneously can both see it as 'free' and enter the critical section. Semaphore operations (wait/signal) are atomic - guaranteed by the OS/hardware."},
                    {"question": "Pipe: Parent writes 'hello', child reads. Show pseudocode.", "solution": "pipe(fd); pid = fork(); if pid == 0: close(fd[1]); read(fd[0], buf, 5); // child reads 'hello'. else: close(fd[0]); write(fd[1], 'hello', 5); wait(NULL); // parent writes."}
                ],
            },
            {
                "title": "Context Switching & fork()",
                "content": "Context Switch: Saving state of current process and loading state of next process.\n\nSteps:\n  1. Save current process state (PC, registers, etc.) in its PCB.\n  2. Update process state (Running -> Ready or Waiting).\n  3. Move PCB to appropriate queue.\n  4. Select next process (scheduling decision).\n  5. Load new process state from its PCB.\n  6. Update memory management (page table base register).\n  7. Resume new process.\n\nContext switch time: Typically 1-10 microseconds. Pure overhead (no useful work done).\nMore context switches = more overhead = less CPU utilization for actual work.\n\nfork() System Call:\n  Creates a new child process as a copy of the parent.\n  Returns: PID of child (to parent), 0 (to child), -1 (on error).\n\n  pid = fork();\n  if (pid == 0) {\n      // Child process\n      printf('I am child, PID=%d', getpid());\n  } else if (pid > 0) {\n      // Parent process\n      printf('I am parent, child PID=%d', pid);\n      wait(NULL);  // wait for child\n  }\n\nfork() Counting:\n  n fork() calls create 2^n processes total (including original).\n  fork(); fork(); -> 4 processes.\n  But with conditionals, count carefully!\n\nCopy-on-Write (COW):\n  After fork(), parent and child share same physical pages.\n  Pages are copied only when one process writes to them.\n  Optimization: avoids unnecessary copying if child calls exec() immediately.\n\nexec() Family:\n  Replaces current process image with new program.\n  execvp(), execl(), execlp(), etc.\n  fork() + exec() = standard way to run a new program.",
                "key_points": [
                    "Context switch is pure overhead - minimize by reducing unnecessary switches",
                    "fork() returns 0 to child, child PID to parent",
                    "n consecutive fork() calls create 2^n total processes",
                    "Copy-on-Write avoids copying memory until actual write occurs",
                    "fork()/exec()/wait() trio is fundamental to Unix process management"
                ],
                "examples": [
                    {"question": "How many times is 'hello' printed? fork(); printf('hello');", "solution": "fork() creates 2 processes. Both execute printf. 'hello' printed 2 times."},
                    {"question": "Output of: fork(); fork(); printf('A'); ?", "solution": "First fork: 2 processes. Each does second fork: 4 processes. Each prints 'A'. Output: 'A' printed 4 times."},
                    {"question": "What is output? pid=fork(); if(pid==0) printf('C'); else printf('P');", "solution": "Parent gets pid>0: prints 'P'. Child gets pid=0: prints 'C'. Output: 'P' and 'C' (order depends on scheduling). Could be 'PC' or 'CP'."}
                ],
            },
            {
                "title": "Multi-threading & Synchronization Basics",
                "content": "Race Condition: When multiple threads access shared data concurrently, and the outcome depends on the order of execution.\n\nExample:\n  shared x = 0\n  Thread 1: x = x + 1  (read 0, compute 1, write 1)\n  Thread 2: x = x + 1  (read 0, compute 1, write 1)\n  Expected: x = 2. Actual: x = 1 (if both read before either writes).\n\nCritical Section: Code segment accessing shared resources.\n  Requirements for solution:\n  1. Mutual Exclusion: Only one thread in critical section at a time.\n  2. Progress: If no thread is in CS, a waiting thread can enter.\n  3. Bounded Waiting: Limit on how long a thread waits.\n\nMutex (Mutual Exclusion):\n  lock(): Acquire mutex. If locked, block until available.\n  unlock(): Release mutex.\n  Only the thread that locked can unlock.\n\nSemaphore (Dijkstra):\n  wait(S) / P(S): Decrement. If S < 0, block.\n  signal(S) / V(S): Increment. If S <= 0, wake a blocked process.\n  Any thread can signal (unlike mutex).\n\nDeadlock with Semaphores:\n  Thread 1: wait(A), wait(B)\n  Thread 2: wait(B), wait(A)\n  If T1 gets A and T2 gets B, both block forever.\n\nClassic Problems:\n  1. Producer-Consumer (Bounded Buffer)\n  2. Readers-Writers Problem\n  3. Dining Philosophers Problem\n\nReaders-Writers:\n  Multiple readers can read simultaneously.\n  Only one writer at a time, no readers during write.\n  Use: mutex (for reader_count), rw_mutex (for write access), reader_count variable.",
                "key_points": [
                    "Race condition: outcome depends on non-deterministic thread scheduling",
                    "Critical section needs: mutual exclusion, progress, bounded waiting",
                    "Mutex: only owner can unlock. Semaphore: any thread can signal.",
                    "Producer-Consumer, Readers-Writers, Dining Philosophers are the 3 classic problems",
                    "Synchronization is heavily tested in GATE, Amazon, Microsoft OS rounds"
                ],
                "examples": [
                    {"question": "Dining Philosophers: 5 philosophers, 5 forks. How to avoid deadlock?", "solution": "Solution 1: Allow at most 4 philosophers to sit simultaneously. Solution 2: Odd philosophers pick left first, even pick right first. Solution 3: Use a single mutex (but reduces concurrency). The problem illustrates circular wait deadlock condition."},
                    {"question": "Readers-Writers: 3 readers and 1 writer. Can all 3 readers read simultaneously?", "solution": "Yes! Multiple readers can access data concurrently since reading doesn't modify data. First reader locks rw_mutex (blocks writers), subsequent readers just increment reader_count. Last reader to leave unlocks rw_mutex."},
                    {"question": "What's wrong with: Thread1: lock(A); lock(B); Thread2: lock(B); lock(A);", "solution": "Potential deadlock! If Thread1 acquires A and Thread2 acquires B, both are waiting for the other's lock. Fix: both threads lock in same order (A then B), or use trylock with timeout."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Process", "explanation": "Program in execution with own memory space, PC, registers, stack. States: New, Ready, Running, Waiting, Terminated."},
            {"name": "Thread", "explanation": "Lightweight unit of execution within a process. Shares code, data, heap with sibling threads. Has own stack, PC, registers."},
            {"name": "Context Switch", "explanation": "Saving state of current process/thread and loading another. Pure overhead. Involves saving/loading PCB data."},
            {"name": "fork()", "explanation": "Unix system call creating child process. Returns 0 to child, child PID to parent. Copy-on-Write for efficiency."},
            {"name": "Semaphore", "explanation": "Synchronization primitive. wait() decrements and may block. signal() increments and may wake. Solves critical section problems."}
        ],
        "formulas": [
            "n consecutive fork() calls = 2^n total processes",
            "Context switch time: typically 1-10 microseconds",
            "Producer-Consumer: wait(empty)->wait(mutex)->produce->signal(mutex)->signal(full)",
            "Degree of multiprogramming = number of processes in memory",
            "Thread creation time << Process creation time (typically 10-100x faster)"
        ],
        "solved_examples": [
            {"question": "How many processes created by: for(i=0;i<3;i++) fork();", "solution": "Iteration 0: 1->2 processes. Iteration 1: 2->4 processes. Iteration 2: 4->8 processes. Total: 8 processes (2^3). The original is one of the 8."},
            {"question": "Producer-Consumer: buffer size 3, initially empty. Producer produces 4 items. What happens?", "solution": "P produces item 1: empty=2, full=1. P produces item 2: empty=1, full=2. P produces item 3: empty=0, full=3. P tries to produce item 4: wait(empty) blocks since empty=0. P blocked until consumer consumes."},
            {"question": "After fork(), parent and child have same PID?", "solution": "No. Each process has a unique PID. fork() returns child's PID to parent (non-zero) and 0 to child. getpid() returns different values in parent and child."}
        ],
        "tips": [
            "Draw the process state diagram from memory - it appears in every OS exam.",
            "For fork() questions, draw a tree of processes. Each fork doubles the count.",
            "Remember: threads share heap but NOT stack. Each thread has its own stack.",
            "Classic synchronization problems (Producer-Consumer, etc.) are must-know for GATE and placements.",
            "In TCS NQT, OS questions focus on theory: process states, thread vs process, scheduling."
        ],
    },
    53: {
        "title": "OS: Memory Management",
        "overview": "Memory management is how the OS allocates, tracks, and reclaims memory for processes. This topic covers paging, segmentation, virtual memory, page replacement algorithms (FIFO, LRU, Optimal), thrashing, and memory allocation strategies. These concepts are heavily tested in GATE, TCS NQT, Infosys, and Amazon OS interview rounds.",
        "chapters": [
            {
                "title": "Paging & Address Translation",
                "content": "Paging divides physical memory into fixed-size frames and logical memory into same-size pages.\n\nPage size = Frame size (typically 4KB).\n\nLogical Address = Page Number + Page Offset\n  Page number = logical_address / page_size\n  Offset = logical_address % page_size\n\nPage Table: Maps page numbers to frame numbers.\n  Logical address -> Page table lookup -> Frame number + Offset -> Physical address.\n\nAddress Translation:\n  Given: logical address, page size, page table.\n  Physical address = frame_number * page_size + offset\n\nExample:\n  Page size = 4 bytes. Logical address = 13.\n  Page number = 13 / 4 = 3. Offset = 13 % 4 = 1.\n  If page 3 maps to frame 6: Physical address = 6 * 4 + 1 = 25.\n\nPage Table Entry (PTE):\n  Frame number, valid/invalid bit, dirty bit, reference bit, protection bits.\n  Valid bit: 1 if page is in memory, 0 if on disk (page fault if accessed).\n\nInternal Fragmentation:\n  Last page of a process may not fully fill a frame.\n  Average waste = page_size / 2 per process.\n\nMulti-level Page Table:\n  Single page table may be too large. Split into levels.\n  Two-level: Outer page table + Inner page tables.\n  Reduces memory for page tables of sparse address spaces.",
                "key_points": [
                    "Logical address = page number + offset. Physical = frame number + offset.",
                    "Page size = frame size. Typically 4KB in modern systems.",
                    "Page table maps page number to frame number. Stored in main memory.",
                    "Internal fragmentation: avg half-page wasted per process.",
                    "Paging address translation is the #1 tested OS concept in GATE and placements."
                ],
                "examples": [
                    {"question": "Page size=1KB, logical address space=64KB, physical=32KB. How many pages? Frames? Page table entries?", "solution": "Pages = 64KB/1KB = 64. Frames = 32KB/1KB = 32. Page table entries = 64 (one per page). Bits for page number = log2(64) = 6. Bits for frame number = log2(32) = 5."},
                    {"question": "Logical address 0x3A5F with page size 4KB. Find page number and offset.", "solution": "4KB = 2^12, so offset is lower 12 bits. 0x3A5F = 0011 1010 0101 1111. Page = 0x3A5F >> 12 = 0x3 = 3. Offset = 0xA5F = 2655. Page 3, offset 2655."},
                    {"question": "Page table: [5, 3, 7, 2]. Translate logical address 9 with page size 4.", "solution": "Page = 9/4 = 2. Offset = 9%4 = 1. Frame = page_table[2] = 7. Physical = 7*4 + 1 = 29."}
                ],
            },
            {
                "title": "Segmentation & Virtual Memory",
                "content": "Segmentation divides memory into variable-size segments based on logical divisions (code, data, stack, heap).\n\nSegment Table: segment_number -> (base_address, limit)\n  Physical address = base + offset (if offset < limit, else segmentation fault).\n\nPaging vs Segmentation:\n  Paging: Fixed size, no external fragmentation, internal fragmentation.\n  Segmentation: Variable size, external fragmentation, no internal fragmentation.\n  Modern systems: Segmented paging (combine both).\n\nVirtual Memory:\n  Allows processes to use more memory than physically available.\n  Only needed pages kept in memory; rest on disk (swap space).\n  Uses demand paging: pages loaded only when accessed.\n\nDemand Paging:\n  Initially no pages in memory. On access: page fault -> load from disk.\n  Page Fault Handling:\n  1. Check page table: valid/invalid bit.\n  2. If invalid: trap to OS (page fault).\n  3. Find free frame (or use page replacement).\n  4. Load page from disk to frame.\n  5. Update page table (set valid bit, frame number).\n  6. Restart the instruction.\n\nEffective Access Time (EAT):\n  EAT = (1-p) * memory_access_time + p * page_fault_time\n  where p = page fault rate.\n  page_fault_time includes: trap + page read from disk + restart.\n  Typically: memory access ~100ns, page fault ~10ms.\n\nTLB (Translation Lookaside Buffer):\n  Cache for page table entries. Small (64-1024 entries), fast (1-2 ns).\n  EAT with TLB = hit_ratio * (TLB_time + mem_time) + (1-hit_ratio) * (TLB_time + 2*mem_time)",
                "key_points": [
                    "Virtual memory allows processes to exceed physical memory using disk swap",
                    "Demand paging loads pages only when needed - lazy loading",
                    "Page fault is expensive: ~10ms (disk access) vs ~100ns (memory access)",
                    "TLB caches page table entries for fast address translation",
                    "EAT calculations are very common in GATE and placement exams"
                ],
                "examples": [
                    {"question": "Memory access = 100ns, page fault rate = 0.001, page fault time = 10ms. Find EAT.", "solution": "EAT = (1-0.001)*100 + 0.001*10,000,000 = 99.9 + 10,000 = 10,099.9 ns. Even 0.1% page faults slow down system 100x!"},
                    {"question": "TLB hit ratio = 90%, TLB access = 10ns, memory access = 100ns. Find EAT.", "solution": "Hit: 10(TLB) + 100(mem) = 110ns. Miss: 10(TLB) + 100(page table in mem) + 100(actual access) = 210ns. EAT = 0.9*110 + 0.1*210 = 99 + 21 = 120ns."},
                    {"question": "Segment table: seg 0=(400,100), seg 1=(800,200). Translate (1, 150).", "solution": "Segment 1: base=800, limit=200. Offset=150 < 200, valid. Physical = 800+150 = 950."}
                ],
            },
            {
                "title": "Page Replacement Algorithms",
                "content": "When a page fault occurs and all frames are full, choose a victim page to evict.\n\nFIFO (First In First Out):\n  Replace the oldest page in memory.\n  Simple but may suffer from Belady's Anomaly (more frames can cause more faults!).\n\nOptimal (OPT):\n  Replace page that won't be used for the longest time in future.\n  Best possible (fewest faults). Used as benchmark. Not implementable (needs future knowledge).\n\nLRU (Least Recently Used):\n  Replace page that hasn't been used for the longest time.\n  Good approximation of OPT. No Belady's anomaly.\n  Implementation: counter-based, stack-based, or clock algorithm approximation.\n\nExample: Reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1\nFrames = 3:\n\nFIFO: Faults at 7,0,1,2,3,4,0,1,7. Wait, let me trace:\n  7: [7] fault. 0: [7,0] fault. 1: [7,0,1] fault.\n  2: [2,0,1] fault (replace 7). 0: hit. 3: [2,3,1] fault (replace 0).\n  0: [2,3,0] fault (replace 1). 4: [4,3,0] fault (replace 2).\n  2: [4,2,0] fault (replace 3). 3: [4,2,3] fault (replace 0).\n  0: [0,2,3] fault (replace 4). 3: hit. 2: hit.\n  1: [0,1,3] fault (replace 2). 2: [0,1,2] fault (replace 3).\n  0: hit. 1: hit. 7: [7,1,2] fault. 0: [7,0,2] fault. 1: [7,0,1] fault.\n  FIFO faults = 15.\n\nLRU with same string and 3 frames: 12 faults.\nOPT with same string and 3 frames: 9 faults.\n\nBelady's Anomaly: FIFO with reference string 1,2,3,4,1,2,5,1,2,3,4,5:\n  3 frames: 9 faults. 4 frames: 10 faults! More frames, more faults.",
                "key_points": [
                    "FIFO is simplest but suffers from Belady's anomaly",
                    "Optimal is best but needs future knowledge - used only as benchmark",
                    "LRU is the practical best choice - no Belady's anomaly",
                    "Stack-based algorithms (LRU, OPT) never suffer Belady's anomaly",
                    "Page replacement tracing is extremely common in GATE, TCS, and Infosys exams"
                ],
                "examples": [
                    {"question": "FIFO with 3 frames, reference string: 1,2,3,4,1,2. Count faults.", "solution": "[1] fault. [1,2] fault. [1,2,3] fault. Replace 1: [4,2,3] fault. Replace 2: [4,1,3] fault. Replace 3: [4,1,2] fault. Total: 6 faults."},
                    {"question": "LRU with 3 frames, reference string: 1,2,3,4,1,2. Count faults.", "solution": "[1] fault. [1,2] fault. [1,2,3] fault. Replace LRU(1): [4,2,3] fault. Replace LRU(2): [4,1,3] fault. Replace LRU(3): [4,1,2] fault. Total: 6 faults. (Same as FIFO here.)"},
                    {"question": "Optimal with 3 frames, reference string: 1,2,3,4,1,2. Count faults.", "solution": "[1] fault. [1,2] fault. [1,2,3] fault. Replace page not used furthest: 3 not needed again, replace 3: [1,2,4] fault. 1: hit. 2: hit. Total: 4 faults. Optimal is best!"}
                ],
            },
            {
                "title": "Thrashing & Memory Allocation",
                "content": "Thrashing: When a process spends more time paging (handling page faults) than executing.\n\nCauses:\n  Too many processes in memory (high degree of multiprogramming).\n  Each process gets too few frames.\n  Constant page faults -> constant disk I/O -> CPU utilization drops -> OS admits more processes -> worse thrashing.\n\nWorking Set Model:\n  Working set W(t, delta) = set of pages referenced in the last delta time units.\n  If sum of all working sets > available frames, thrashing occurs.\n  Solution: Suspend processes until working sets fit in memory.\n\nPage Fault Frequency (PFF):\n  Monitor page fault rate per process.\n  If rate too high: allocate more frames.\n  If rate too low: deallocate frames.\n  Keep fault rate in acceptable band.\n\nMemory Allocation Strategies (contiguous allocation):\n  First Fit: Allocate first hole that's big enough. Fast.\n  Best Fit: Allocate smallest hole that's big enough. Least waste but slow.\n  Worst Fit: Allocate largest hole. Leaves biggest remainder. Usually worst performance.\n  Next Fit: Like first fit but starts from last allocation point.\n\nExternal Fragmentation: Free memory is available but not contiguous.\n  Solution: Compaction (move processes to create contiguous free space). Expensive.\n  Paging eliminates external fragmentation.\n\nInternal Fragmentation: Allocated memory is larger than needed.\n  Last page of a process may waste up to (page_size - 1) bytes.\n\nBuddy System: Split memory into powers of 2. Allocate smallest power-of-2 block that fits.\n  Easy to merge (buddies) when freed.",
                "key_points": [
                    "Thrashing = excessive paging due to insufficient frames per process",
                    "Working set model prevents thrashing by tracking active page sets",
                    "First fit is generally fastest and good enough for most cases",
                    "External fragmentation: enough total free memory but not contiguous",
                    "Memory allocation and fragmentation are staple GATE and placement topics"
                ],
                "examples": [
                    {"question": "Memory holes: 100K, 500K, 200K, 300K, 600K. Allocate 212K, 417K, 112K, 426K using First Fit.", "solution": "212K: first fit in 500K hole -> 288K remaining. 417K: first fit in 600K hole -> 183K remaining. 112K: first fit in 288K hole -> 176K remaining. 426K: no hole big enough. Cannot allocate."},
                    {"question": "Same holes, Best Fit for 212K?", "solution": "Holes: 100K, 500K, 200K, 300K, 600K. Best fit for 212K = smallest hole >= 212K = 300K. Remaining: 100K, 500K, 200K, 88K, 600K."},
                    {"question": "Why does high degree of multiprogramming cause thrashing?", "solution": "More processes -> each gets fewer frames -> more page faults -> more disk I/O -> CPU idle waiting for I/O -> OS thinks CPU is idle and admits MORE processes -> even fewer frames per process -> even more faults. Vicious cycle = thrashing."}
                ],
            },
            {
                "title": "Advanced Memory Concepts",
                "content": "Page Table Size Optimization:\n  Problem: Large address space = huge page table.\n  Solutions:\n  1. Multi-level page tables: Only allocate PTEs for used pages.\n  2. Inverted page table: One entry per physical frame (not per page).\n     Entry: (pid, page_number). Search: hash for fast lookup.\n     Saves space but search is slower.\n  3. Hashed page tables: Hash function maps page number to chain of entries.\n\nCopy-on-Write (COW):\n  After fork(), parent and child share same pages.\n  When either writes, that page is copied.\n  Saves memory and time when child calls exec() immediately.\n\nMemory-Mapped Files:\n  Map file contents to virtual memory. Access file like array.\n  mmap() system call. Efficient for large file I/O.\n  Multiple processes can share a mapped file (shared memory IPC).\n\nNUMA (Non-Uniform Memory Access):\n  In multi-processor systems, memory access time depends on memory location.\n  Local memory: fast. Remote memory: slow.\n  OS tries to allocate memory close to the CPU that uses it.\n\nSwap Space:\n  Disk area for storing evicted pages.\n  Swap-in: Load page from swap to memory.\n  Swap-out: Write page from memory to swap.\n  Linux: swap partition or swap file. Windows: pagefile.sys.\n\nFrame Allocation:\n  Equal allocation: n frames / p processes. Simple but ignores size differences.\n  Proportional: Allocate based on process size. s_i / S_total * n frames.\n  Priority-based: Higher priority gets more frames.",
                "key_points": [
                    "Multi-level page tables save space by not allocating unused entries",
                    "Inverted page table: one entry per frame, saves space, needs hashing",
                    "COW is critical for efficient fork() - copy only on write",
                    "Proportional frame allocation is fairer than equal allocation",
                    "These advanced concepts appear in GATE and senior-level interviews"
                ],
                "examples": [
                    {"question": "32-bit address, 4KB pages. Size of single-level page table?", "solution": "Pages = 2^32 / 2^12 = 2^20 = 1M entries. If each PTE is 4 bytes: table size = 4MB. Too large to keep in contiguous memory! Hence multi-level paging."},
                    {"question": "Two-level page table: 32-bit address, 4KB pages, 4B PTE. Page table fits in one page.", "solution": "Entries per page = 4KB/4B = 1024 = 2^10. Inner page table: 10 bits. Remaining address bits: 32-12(offset)-10 = 10 bits for outer table. Outer table: 2^10 * 4B = 4KB (one page). Inner tables: up to 2^10, each 4KB, allocated on demand."},
                    {"question": "Proportional allocation: Process A size 10MB, B size 30MB, C size 60MB, total frames=100.", "solution": "A: 10/100 * 100 = 10 frames. B: 30/100 * 100 = 30 frames. C: 60/100 * 100 = 60 frames."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Paging", "explanation": "Divide logical memory into pages, physical into frames. Page table maps pages to frames. Eliminates external fragmentation."},
            {"name": "Virtual Memory", "explanation": "Process can use more memory than physically available. Uses demand paging: load pages from disk on access. Enables multiprogramming."},
            {"name": "Page Replacement", "explanation": "When memory full, choose victim page to evict. FIFO (simple), LRU (practical best), Optimal (theoretical best)."},
            {"name": "Thrashing", "explanation": "Excessive paging where process spends more time on page faults than execution. Caused by insufficient frames per process."},
            {"name": "TLB", "explanation": "Translation Lookaside Buffer. Cache for page table entries. Makes address translation fast (~1ns vs 100ns memory access)."}
        ],
        "formulas": [
            "Physical address = frame_number * page_size + offset",
            "Page number = logical_address / page_size; Offset = logical_address % page_size",
            "EAT = (1-p) * memory_time + p * page_fault_time",
            "EAT with TLB = h*(TLB+mem) + (1-h)*(TLB+2*mem) where h = hit ratio",
            "Number of pages = logical_address_space / page_size"
        ],
        "solved_examples": [
            {"question": "Logical address 1024, page size 256. Page table: [3,7,1,5,...]. Find physical address.", "solution": "Page = 1024/256 = 4. Offset = 1024%256 = 0. Frame = page_table[4]. Assuming page_table[4]=5: physical = 5*256 + 0 = 1280."},
            {"question": "LRU, 4 frames, reference string: 1,2,3,4,5,1,2,3. Count page faults.", "solution": "1:[1] F. 2:[1,2] F. 3:[1,2,3] F. 4:[1,2,3,4] F. 5: replace LRU=1: [5,2,3,4] F. 1: replace LRU=2: [5,1,3,4] F. 2: replace LRU=3: [5,1,2,4] F. 3: replace LRU=4: [5,1,2,3] F. Total: 8 faults."},
            {"question": "First Fit: holes 150, 350, 200, 750. Allocate 350.", "solution": "First hole >= 350: 350K hole (exact fit). Allocated. Remaining holes: 150, 0, 200, 750."}
        ],
        "tips": [
            "Page replacement tracing is the most common OS numerical question. Practice at least 10 examples.",
            "Memorize: FIFO has Belady's anomaly, LRU and Optimal do not.",
            "For EAT calculations, watch units: page fault time is usually in milliseconds, memory access in nanoseconds.",
            "Draw page tables when solving address translation problems - it prevents silly errors.",
            "In TCS NQT, memory management questions are typically formula-based. Know the formulas cold."
        ],
    },
    54: {
        "title": "OS: Scheduling & Deadlocks",
        "overview": "CPU scheduling determines which process runs on the CPU and when. Deadlocks occur when processes wait circularly for resources. This topic covers FCFS, SJF, Round Robin, Priority scheduling, deadlock conditions, prevention, avoidance (Banker's algorithm), and synchronization primitives. These are among the most tested OS topics in GATE, TCS, Infosys, and Amazon interviews.",
        "chapters": [
            {
                "title": "CPU Scheduling: FCFS & SJF",
                "content": "CPU Scheduler selects a process from the ready queue and allocates the CPU.\n\nScheduling Criteria:\n  CPU Utilization: Keep CPU busy (maximize).\n  Throughput: Processes completed per time unit (maximize).\n  Turnaround Time: Total time from arrival to completion (minimize).\n  Waiting Time: Time spent in ready queue (minimize).\n  Response Time: Time from submission to first response (minimize).\n\nFormulas:\n  Turnaround Time (TAT) = Completion Time - Arrival Time\n  Waiting Time (WT) = TAT - Burst Time\n  Response Time = First CPU access - Arrival Time\n\nFCFS (First Come First Served):\n  Non-preemptive. Process that arrives first gets CPU first.\n  Simple but convoy effect: short processes wait behind long ones.\n\nExample: P1(BT=24), P2(BT=3), P3(BT=3). All arrive at 0.\n  Gantt: |P1(0-24)|P2(24-27)|P3(27-30)|\n  Avg WT = (0+24+27)/3 = 17. Avg TAT = (24+27+30)/3 = 27.\n\nSJF (Shortest Job First):\n  Non-preemptive: Pick shortest burst time. Optimal for avg WT.\n  Same example: |P2(0-3)|P3(3-6)|P1(6-30)|\n  Avg WT = (6+0+3)/3 = 3. Much better!\n\nSRTF (Shortest Remaining Time First):\n  Preemptive version of SJF. If new process arrives with shorter remaining time, preempt current.\n  Optimal for avg WT among preemptive algorithms.\n  Problem: starvation of long processes.",
                "key_points": [
                    "TAT = Completion - Arrival. WT = TAT - Burst. Know these formulas cold.",
                    "FCFS: simple but convoy effect. Non-preemptive.",
                    "SJF (non-preemptive): optimal avg waiting time among non-preemptive",
                    "SRTF (preemptive SJF): optimal avg waiting time overall",
                    "Scheduling problems with calculations are the #1 OS question type in placements"
                ],
                "examples": [
                    {"question": "FCFS: P1(AT=0,BT=5), P2(AT=1,BT=3), P3(AT=2,BT=8), P4(AT=3,BT=6). Find avg WT.", "solution": "Gantt: P1(0-5), P2(5-8), P3(8-16), P4(16-22). WT: P1=0, P2=5-1=4, P3=8-2=6, P4=16-3=13. Wait: that is CT-AT-BT. P2: 8-1-3=4. P3: 16-2-8=6. P4: 22-3-6=13. Avg WT = (0+4+6+13)/4 = 5.75."},
                    {"question": "SJF (non-preemptive): same processes. Find avg WT.", "solution": "At t=0: only P1, run P1(0-5). At t=5: P2(BT=3), P3(BT=8), P4(BT=6). Shortest=P2, run P2(5-8). At t=8: P3(8), P4(6). Shortest=P4, run P4(8-14). Then P3(14-22). WT: P1=0, P2=5-1=4, P4=8-3-6=5? No: WT=CT-AT-BT. P2:8-1-3=4. P4:14-3-6=5. P3:22-2-8=12. Avg=(0+4+5+12)/4=5.25."},
                    {"question": "SRTF: P1(AT=0,BT=7), P2(AT=2,BT=4), P3(AT=4,BT=1), P4(AT=5,BT=4).", "solution": "t=0: P1 runs. t=2: P2 arrives, remaining P1=5, P2=4. P2 shorter, preempt. t=4: P3 arrives, P2 remaining=2, P3=1. P3 shorter, preempt. t=5: P3 done. P4 arrives, P2 rem=2, P4=4, P1 rem=5. P2 runs. t=7: P2 done. P4=4 < P1=5. P4 runs. t=11: P4 done. P1 runs. t=16: P1 done. Avg WT: P1=16-0-7=9, P2=7-2-4=1, P3=5-4-1=0, P4=11-5-4=2. Avg=3."}
                ],
            },
            {
                "title": "Round Robin & Priority Scheduling",
                "content": "Round Robin (RR):\n  Preemptive. Each process gets a time quantum (q). After q, preempted and moved to end of ready queue.\n  If burst < q, process finishes early and releases CPU.\n  Fair but context switch overhead.\n\nTime Quantum Selection:\n  Too small: too many context switches (overhead).\n  Too large: degenerates to FCFS.\n  Rule of thumb: 80% of bursts should be shorter than quantum.\n\nExample: P1(BT=24), P2(BT=3), P3(BT=3). q=4. All arrive at 0.\n  Gantt: P1(0-4)|P2(4-7)|P3(7-10)|P1(10-14)|P1(14-18)|P1(18-22)|P1(22-26)|P1(26-30)\n  WT: P1=30-24=6, P2=4, P3=7. Avg=(6+4+7)/3=5.67.\n\nPriority Scheduling:\n  Each process has a priority. Highest priority runs first.\n  Can be preemptive or non-preemptive.\n  Problem: Starvation (low priority processes never run).\n  Solution: Aging - increase priority of waiting processes over time.\n\nMulti-Level Queue Scheduling:\n  Multiple ready queues with different priorities.\n  Example: System processes > Interactive > Batch.\n  Each queue can have its own scheduling algorithm.\n\nMulti-Level Feedback Queue:\n  Processes can move between queues based on behavior.\n  CPU-bound processes move to lower priority.\n  I/O-bound processes move to higher priority.\n  Most flexible and used in modern OS (Linux CFS is similar concept).",
                "key_points": [
                    "RR: fair, preemptive, good response time. Performance depends on quantum.",
                    "Priority scheduling may cause starvation - aging is the solution.",
                    "Multi-level feedback queue is used in real operating systems.",
                    "Context switch overhead is proportional to 1/quantum in RR.",
                    "RR Gantt chart problems are extremely common in GATE and TCS NQT."
                ],
                "examples": [
                    {"question": "RR with q=2: P1(AT=0,BT=5), P2(AT=1,BT=4), P3(AT=2,BT=2), P4(AT=3,BT=1). Find avg TAT.", "solution": "t0-2: P1(rem 3). t2-4: P2(rem 2). t4-6: P3(rem 0, done CT=6). t6-7: P4(rem 0, done CT=7). t7-9: P1(rem 1). t9-11: P2(rem 0, done CT=11). t11-12: P1(rem 0, done CT=12). TAT: P1=12, P2=10, P3=4, P4=4. Avg=(12+10+4+4)/4=7.5."},
                    {"question": "Priority (non-preemptive): P1(BT=10,Pr=3), P2(BT=1,Pr=1), P3(BT=2,Pr=4), P4(BT=1,Pr=5), P5(BT=5,Pr=2). Lower number=higher priority. All arrive at 0.", "solution": "Order: P2(1), P5(2), P1(3), P3(4), P4(5). Gantt: P2(0-1), P5(1-6), P1(6-16), P3(16-18), P4(18-19). Avg WT = (6+0+16+18+1)/5 = 8.2."},
                    {"question": "What is aging? Why is it needed?", "solution": "Aging gradually increases the priority of waiting processes. Without it, low-priority processes may starve indefinitely if high-priority processes keep arriving. Example: increase priority by 1 every 15 minutes of waiting."}
                ],
            },
            {
                "title": "Deadlock: Conditions & Prevention",
                "content": "Deadlock: A set of processes where each is waiting for a resource held by another in the set. Circular wait.\n\nNecessary Conditions (ALL four must hold simultaneously):\n  1. Mutual Exclusion: Resource used by one process at a time.\n  2. Hold and Wait: Process holds resources while waiting for more.\n  3. No Preemption: Resources cannot be forcibly taken.\n  4. Circular Wait: P1->P2->...->Pn->P1 waiting cycle.\n\nResource Allocation Graph (RAG):\n  Processes = circles, Resources = rectangles.\n  Request edge: Pi -> Rj (process requests resource).\n  Assignment edge: Rj -> Pi (resource assigned to process).\n  Cycle in RAG with single-instance resources -> deadlock.\n  Cycle with multi-instance resources -> may or may not be deadlock.\n\nDeadlock Prevention (break one of the four conditions):\n  1. Break Mutual Exclusion: Not practical for non-shareable resources.\n  2. Break Hold and Wait: Request all resources at once. Or release all before requesting new.\n  3. Break No Preemption: If process can't get a resource, release all and restart.\n  4. Break Circular Wait: Order resources numerically. Request in increasing order only.\n\nDeadlock Avoidance: Check before allocation if it leads to safe state.\n  Safe state: There exists a sequence where all processes can finish.\n  Unsafe state: No such sequence exists. May lead to deadlock.\n  Use Banker's algorithm to check safety.",
                "key_points": [
                    "All four conditions (ME, H&W, NP, CW) must hold for deadlock to occur",
                    "Breaking any one condition prevents deadlock",
                    "Circular wait prevention (resource ordering) is most practical",
                    "Cycle in single-instance RAG = deadlock. Multi-instance: need Banker's.",
                    "Deadlock conditions are asked in every placement exam - memorize them"
                ],
                "examples": [
                    {"question": "Two processes: P1 holds R1, requests R2. P2 holds R2, requests R1. Is this deadlock?", "solution": "Check conditions: 1) ME: R1, R2 used exclusively. 2) Hold&Wait: Both hold and wait. 3) No preemption: Can't take resources. 4) Circular wait: P1->R2->P2->R1->P1. All 4 conditions met. YES, deadlock."},
                    {"question": "How does resource ordering prevent deadlock?", "solution": "Assign numbers: R1=1, R2=2. Rule: request in increasing order. P1 requests R1(1) then R2(2) - ok. P2 must also request R1(1) first, then R2(2). But P2 needs R2 for its task, so it requests R1 first (even if not needed yet). This prevents circular wait."},
                    {"question": "Is the system in deadlock? RAG: P1->R1->P2->R2->P3->R3->P1. Single instances.", "solution": "Cycle exists: P1->R1->P2->R2->P3->R3->P1. With single instances per resource, cycle = deadlock. Yes, system is deadlocked."}
                ],
            },
            {
                "title": "Banker's Algorithm",
                "content": "Banker's Algorithm: Deadlock avoidance. Checks if granting a request leaves system in safe state.\n\nData Structures (n processes, m resource types):\n  Available[m]: Available instances of each resource.\n  Max[n][m]: Maximum demand of each process.\n  Allocation[n][m]: Currently allocated to each process.\n  Need[n][m] = Max - Allocation: Remaining need.\n\nSafety Algorithm:\n  1. Work = Available (copy). Finish[i] = False for all.\n  2. Find process i where Finish[i]=False and Need[i] <= Work.\n  3. If found: Work += Allocation[i]. Finish[i] = True. Go to step 2.\n  4. If no such process found: If all Finish[i]=True, SAFE. Else UNSAFE.\n\nResource Request Algorithm:\n  When Pi requests Request[i]:\n  1. If Request[i] > Need[i]: Error (exceeds max claim).\n  2. If Request[i] > Available: Wait.\n  3. Tentatively allocate: Available -= Request. Allocation[i] += Request. Need[i] -= Request.\n  4. Run safety algorithm. If safe: grant. If unsafe: rollback and wait.\n\nExample:\n  5 processes, 3 resource types. Available = [3,3,2].\n  Allocation:     Max:          Need (Max-Alloc):\n  P0: [0,1,0]    [7,5,3]       [7,4,3]\n  P1: [2,0,0]    [3,2,2]       [1,2,2]\n  P2: [3,0,2]    [9,0,2]       [6,0,0]\n  P3: [2,1,1]    [2,2,2]       [0,1,1]\n  P4: [0,0,2]    [4,3,3]       [4,3,1]\n\nSafety check: Work=[3,3,2]. P1 need [1,2,2]<=[3,3,2]. Run P1: Work=[5,3,2]. P3 need [0,1,1]<=[5,3,2]. Run P3: Work=[7,4,3]. P4 need [4,3,1]<=[7,4,3]. Run P4: Work=[7,4,5]. P0 need [7,4,3]<=[7,4,5]. Run P0: Work=[7,5,5]. P2 need [6,0,0]<=[7,5,5]. Run P2: Work=[10,5,7].\nSafe sequence: <P1, P3, P4, P0, P2>. System is safe.",
                "key_points": [
                    "Banker's checks if granting request keeps system in safe state",
                    "Need = Max - Allocation. Available changes as processes finish.",
                    "Safe state: exists at least one sequence where all can finish",
                    "Banker's algorithm is O(n^2 * m) per request",
                    "Banker's algorithm problems are extremely common in GATE and placement exams"
                ],
                "examples": [
                    {"question": "Available=[1,1,2]. P0: Alloc=[1,0,0], Need=[0,0,1]. P1: Alloc=[0,1,0], Need=[1,1,0]. P2: Alloc=[0,0,1], Need=[0,0,1]. Is it safe?", "solution": "Work=[1,1,2]. P0 need [0,0,1]<=[1,1,2]: YES. Work=[2,1,2]. P1 need [1,1,0]<=[2,1,2]: YES. Work=[2,2,2]. P2 need [0,0,1]<=[2,2,2]: YES. Work=[2,2,3]. Safe sequence: <P0,P1,P2>."},
                    {"question": "Can P1 request [1,0,0]? Available=[1,1,2], P1 Need=[1,1,0], P1 Alloc=[0,1,0].", "solution": "Request [1,0,0] <= Need [1,1,0]: OK. Request [1,0,0] <= Available [1,1,2]: OK. Tentative: Available=[0,1,2], P1 Alloc=[1,1,0], P1 Need=[0,1,0]. Run safety check with new values. If safe, grant request."},
                    {"question": "What is the difference between safe state and deadlock-free state?", "solution": "Safe state guarantees no deadlock will occur regardless of future requests. Unsafe state means deadlock MIGHT occur but is not guaranteed. All safe states are deadlock-free, but some unsafe states may also be deadlock-free (by luck)."}
                ],
            },
            {
                "title": "Deadlock Detection & Recovery",
                "content": "Deadlock Detection (when prevention/avoidance not used):\n\nSingle Instance per Resource Type:\n  Use wait-for graph (simplified RAG). Cycle = deadlock.\n  Maintain graph, periodically check for cycles. O(V+E).\n\nMultiple Instances:\n  Use algorithm similar to Banker's safety algorithm.\n  Data: Available, Allocation, Request (current pending requests).\n  Find process whose Request <= Available. 'Run' it (free its resources).\n  If all can finish: no deadlock. Otherwise: remaining processes are deadlocked.\n\nHow Often to Run Detection:\n  Every request: expensive but detects immediately.\n  Periodically (e.g., every 5 minutes): less overhead but delayed detection.\n  When CPU utilization drops below threshold: likely deadlock.\n\nDeadlock Recovery:\n  1. Process Termination:\n     a. Abort all deadlocked processes: drastic, loses all work.\n     b. Abort one at a time: check if deadlock resolved after each.\n        Choose victim: lowest priority, least work done, most resources held.\n  2. Resource Preemption:\n     Select victim, rollback to safe state, preempt resources.\n     Problem: starvation if same process always chosen as victim.\n     Solution: Include rollback count in victim selection.\n\nOstrich Algorithm:\n  Ignore deadlocks! Used when deadlocks are rare and cost of prevention/detection is high.\n  Unix/Linux/Windows use this for some resources.\n  Practical approach: let user kill stuck processes.\n\nLivelock: Processes keep changing state in response to each other but make no progress.\n  Example: Two people in a corridor both stepping aside to the same side repeatedly.",
                "key_points": [
                    "Detection for single instance: cycle in wait-for graph",
                    "Detection for multiple instances: algorithm similar to Banker's",
                    "Recovery: terminate processes or preempt resources",
                    "Ostrich algorithm: ignore deadlocks when they are rare (used in practice!)",
                    "Livelock is different from deadlock: processes are active but make no progress"
                ],
                "examples": [
                    {"question": "Wait-for graph: P1->P2, P2->P3, P3->P1. Is there deadlock?", "solution": "Cycle exists: P1->P2->P3->P1. With single-instance resources implied, this means deadlock. All three processes are deadlocked."},
                    {"question": "3 processes deadlocked. Which to terminate? P1(priority=5, runtime=2hr), P2(priority=10, runtime=5min), P3(priority=3, runtime=1hr).", "solution": "Terminate P2: highest priority number (lowest priority), least work done (5 min). This causes minimum loss. Then check if remaining P1, P3 are still deadlocked."},
                    {"question": "Why do real operating systems use the ostrich algorithm?", "solution": "Deadlock prevention and avoidance are expensive (restrict resource usage, run Banker's on every request). For most desktop/server workloads, deadlocks are rare. The cost of handling them exceeds the cost of occasional manual restart. Users can simply kill stuck processes."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "CPU Scheduling", "explanation": "FCFS (simple, convoy effect), SJF (optimal avg WT), SRTF (preemptive SJF), RR (fair, time quantum), Priority (may starve)."},
            {"name": "Deadlock Conditions", "explanation": "All four must hold: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait. Break any one to prevent."},
            {"name": "Banker's Algorithm", "explanation": "Deadlock avoidance. Check if request leaves system in safe state. Uses Available, Max, Allocation, Need matrices."},
            {"name": "Scheduling Metrics", "explanation": "TAT = Completion - Arrival. WT = TAT - Burst. Response = First_CPU - Arrival. Minimize WT and TAT."},
            {"name": "Starvation vs Deadlock", "explanation": "Starvation: process waits indefinitely but system progresses. Deadlock: circular wait, no process progresses. Fix starvation with aging."}
        ],
        "formulas": [
            "Turnaround Time = Completion Time - Arrival Time",
            "Waiting Time = Turnaround Time - Burst Time",
            "Response Time = First CPU Access - Arrival Time",
            "Need[i] = Max[i] - Allocation[i]",
            "Safe state: exists sequence <P1,...,Pn> where each Pi's Need <= Available + sum of allocated by finished processes"
        ],
        "solved_examples": [
            {"question": "RR (q=3): P1(AT=0,BT=4), P2(AT=0,BT=3). Gantt and avg WT.", "solution": "P1(0-3, rem 1), P2(3-6, rem 0), P1(6-7, rem 0). WT: P1 = 7-0-4 = 3. P2 = 6-0-3 = 3. Avg WT = 3."},
            {"question": "FCFS vs SJF: P1(BT=6), P2(BT=8), P3(BT=7), P4(BT=3). All arrive at 0.", "solution": "FCFS: 0+6+14+21 = WT sum = 41, avg = 10.25. SJF order: P4,P1,P3,P2. WT: 0+3+9+16=28, avg=7. SJF is better by 3.25."},
            {"question": "Banker's: Available=[2,1]. P0: Alloc=[1,0], Max=[3,2]. P1: Alloc=[1,1], Max=[2,1]. Safe?", "solution": "Need: P0=[2,2], P1=[1,0]. Work=[2,1]. P1 need [1,0]<=[2,1]. Run P1: Work=[3,2]. P0 need [2,2]<=[3,2]. Run P0: Work=[4,2]. Safe! Sequence: <P1,P0>."}
        ],
        "tips": [
            "For scheduling problems, ALWAYS draw the Gantt chart first. Then calculate CT, TAT, WT.",
            "SJF is optimal but needs burst time prediction. SRTF is preemptive SJF.",
            "In RR, if BT < quantum, process finishes early. Track remaining burst times carefully.",
            "For Banker's algorithm, calculate Need matrix first. Then find safe sequence greedily.",
            "Deadlock conditions mnemonic: 'My Horse Needs Corn' (Mutual exclusion, Hold&wait, No preemption, Circular wait)."
        ],
    },
    55: {
        "title": "DBMS: Normalization & SQL",
        "overview": "Database Management Systems organize data efficiently. Normalization eliminates redundancy through normal forms. SQL is the language for querying relational databases. This topic covers 1NF through BCNF, functional dependencies, SQL queries including joins and subqueries, ER diagrams, and relational algebra. These are core topics in TCS, Infosys, Wipro, and Amazon placement exams.",
        "chapters": [
            {
                "title": "Normalization: 1NF to 3NF",
                "content": "Normalization reduces data redundancy and prevents anomalies (insertion, update, deletion).\n\nFunctional Dependency (FD):\n  X -> Y means X uniquely determines Y.\n  If two tuples have same X, they must have same Y.\n  Example: StudentID -> Name (each ID has one name).\n\nCandidate Key: Minimal set of attributes that uniquely identifies a tuple.\nPrimary Key: Chosen candidate key.\nPrime Attribute: Part of some candidate key.\nNon-Prime: Not part of any candidate key.\n\n1NF (First Normal Form):\n  All attributes are atomic (no multi-valued or composite attributes).\n  Each cell has a single value. No repeating groups.\n  Violation: Student(ID, Name, Phones) where Phones has multiple values.\n  Fix: Create separate row for each phone, or separate Phones table.\n\n2NF (Second Normal Form):\n  In 1NF + No partial dependency (no non-prime attribute depends on part of a candidate key).\n  Only relevant when candidate key is composite.\n  Violation: (StudentID, CourseID) -> Grade, StudentID -> Name.\n  Name depends on only part of the key (StudentID). Partial dependency.\n  Fix: Separate into Students(StudentID, Name) and Enrollment(StudentID, CourseID, Grade).\n\n3NF (Third Normal Form):\n  In 2NF + No transitive dependency (no non-prime depends on another non-prime).\n  Violation: StudentID -> DeptID -> DeptName.\n  DeptName transitively depends on StudentID through DeptID.\n  Fix: Students(StudentID, DeptID) and Departments(DeptID, DeptName).",
                "key_points": [
                    "1NF: atomic values. 2NF: no partial dependency. 3NF: no transitive dependency.",
                    "Partial dependency: non-prime depends on PART of candidate key (only for composite keys)",
                    "Transitive dependency: non-prime depends on another non-prime",
                    "Normalization reduces redundancy but may require more joins",
                    "Normalization levels are tested in every GATE, TCS, and Infosys exam"
                ],
                "examples": [
                    {"question": "Is R(A,B,C,D) with FDs A->B, B->C in 3NF? Key is A.", "solution": "2NF: Key is A (not composite), so no partial dependencies possible. OK. 3NF: A->B->C. C depends on A through B (transitive, B is non-prime). NOT in 3NF. Fix: R1(A,B,D) and R2(B,C)."},
                    {"question": "R(StudentID, CourseID, CourseName, Grade). FDs: (StudentID,CourseID)->Grade, CourseID->CourseName. Key=(StudentID,CourseID). Normal form?", "solution": "1NF: yes (atomic). 2NF: CourseID->CourseName. CourseName depends on PART of key. Partial dependency! NOT in 2NF. Fix: R1(StudentID,CourseID,Grade), R2(CourseID,CourseName)."},
                    {"question": "Identify the highest normal form: R(A,B,C) with A->B, A->C. Key=A.", "solution": "1NF: yes. 2NF: key is single attribute, no partial deps. Yes. 3NF: A->B, A->C. Both B and C depend directly on key, no transitive. YES 3NF. Also BCNF since A is a superkey."}
                ],
            },
            {
                "title": "BCNF & Functional Dependency Theory",
                "content": "BCNF (Boyce-Codd Normal Form):\n  For every FD X -> Y, X must be a superkey.\n  Stronger than 3NF. 3NF allows: if Y is a prime attribute, the FD is OK even if X is not a superkey.\n  BCNF does NOT allow this exception.\n\nExample violating 3NF but not BCNF:\n  R(Student, Subject, Professor). FDs:\n  (Student, Subject) -> Professor\n  Professor -> Subject\n  Keys: (Student, Subject) and (Student, Professor).\n  Professor -> Subject: Professor is not a superkey, but Subject is prime. OK for 3NF.\n  NOT BCNF (Professor is not a superkey). Decompose: R1(Professor, Subject), R2(Student, Professor).\n\nArmstrong's Axioms:\n  1. Reflexivity: If Y subset of X, then X -> Y.\n  2. Augmentation: If X -> Y, then XZ -> YZ.\n  3. Transitivity: If X -> Y and Y -> Z, then X -> Z.\n  Derived rules:\n  Union: X -> Y and X -> Z implies X -> YZ.\n  Decomposition: X -> YZ implies X -> Y and X -> Z.\n  Pseudo-transitivity: X -> Y and WY -> Z implies WX -> Z.\n\nClosure of Attribute Set X (X+):\n  All attributes determined by X.\n  Algorithm: Start with X. Repeatedly add Y for each FD A -> Y where A is subset of current set.\n  X is a candidate key if X+ = all attributes AND no proper subset of X has this property.\n\nCanonical Cover (Minimal Cover):\n  1. Decompose right side (single attribute on right).\n  2. Remove redundant FDs.\n  3. Remove extraneous attributes from left side.",
                "key_points": [
                    "BCNF: every FD has a superkey on the left. Stricter than 3NF.",
                    "3NF allows non-superkey determinant if dependent is prime. BCNF does not.",
                    "Armstrong's axioms derive all possible FDs from given set",
                    "Attribute closure X+ finds all attributes determined by X",
                    "BCNF and closure computation are frequent GATE and placement questions"
                ],
                "examples": [
                    {"question": "FDs: A->B, B->C, C->D. Find A+.", "solution": "Start: {A}. A->B: {A,B}. B->C: {A,B,C}. C->D: {A,B,C,D}. A+ = {A,B,C,D}. A is a candidate key (determines all attributes)."},
                    {"question": "R(A,B,C,D). FDs: AB->C, C->D, D->A. Find all candidate keys.", "solution": "AB+: AB->C, C->D, D->A -> {A,B,C,D}. AB is key. BC+: C->D, D->A -> {A,B,C,D}. BC is key. BD+: D->A, AB->C -> {A,B,C,D}. BD is key. CD+: C->D, D->A, AB->C? Need B. {C,D,A} -> can't get B. Not key. Is there key without B? A+={A}. C+={C,D,A}. No way to get B without B. So B must be in every key. Keys: AB, BC, BD."},
                    {"question": "Is R(A,B,C) with FDs A->B, B->C in BCNF?", "solution": "Key: A (A+=ABC). FD A->B: A is superkey. OK. FD B->C: B is NOT superkey (B+={B,C}). Violates BCNF. Decompose: R1(B,C), R2(A,B)."}
                ],
            },
            {
                "title": "SQL: Queries, Joins & Aggregation",
                "content": "SQL Query Structure:\n  SELECT columns\n  FROM tables\n  [JOIN table ON condition]\n  [WHERE condition]\n  [GROUP BY columns]\n  [HAVING condition]\n  [ORDER BY columns]\n  [LIMIT n]\n\nExecution Order: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT\n\nJOIN Types:\n  INNER JOIN: Only matching rows from both tables.\n  LEFT JOIN: All from left + matching from right (NULL if no match).\n  RIGHT JOIN: All from right + matching from left.\n  FULL OUTER JOIN: All from both (NULL where no match).\n  CROSS JOIN: Cartesian product (every row paired with every other).\n  SELF JOIN: Table joined with itself.\n\nExamples:\n  -- Employees with department names\n  SELECT e.name, d.dept_name\n  FROM employees e\n  INNER JOIN departments d ON e.dept_id = d.dept_id;\n\n  -- All employees, even without department\n  SELECT e.name, d.dept_name\n  FROM employees e\n  LEFT JOIN departments d ON e.dept_id = d.dept_id;\n\nAggregate Functions:\n  COUNT(*), COUNT(col), SUM(col), AVG(col), MIN(col), MAX(col)\n  Used with GROUP BY to aggregate per group.\n\n  -- Average salary per department\n  SELECT dept_id, AVG(salary) as avg_sal\n  FROM employees\n  GROUP BY dept_id\n  HAVING AVG(salary) > 50000;\n\nWHERE vs HAVING:\n  WHERE: Filters rows BEFORE grouping.\n  HAVING: Filters groups AFTER grouping.\n  WHERE cannot use aggregate functions; HAVING can.",
                "key_points": [
                    "SQL execution order: FROM->WHERE->GROUP BY->HAVING->SELECT->ORDER BY",
                    "INNER JOIN returns only matching rows; LEFT JOIN includes all from left table",
                    "WHERE filters rows before GROUP BY; HAVING filters groups after",
                    "COUNT(*) counts all rows; COUNT(col) counts non-NULL values",
                    "SQL joins and aggregation are tested in every placement exam"
                ],
                "examples": [
                    {"question": "Find employees with salary above average.", "solution": "SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);"},
                    {"question": "Find departments with more than 5 employees.", "solution": "SELECT dept_id, COUNT(*) as cnt FROM employees GROUP BY dept_id HAVING COUNT(*) > 5;"},
                    {"question": "Find employees who don't belong to any department.", "solution": "SELECT e.name FROM employees e LEFT JOIN departments d ON e.dept_id = d.dept_id WHERE d.dept_id IS NULL; -- Or: SELECT name FROM employees WHERE dept_id NOT IN (SELECT dept_id FROM departments);"}
                ],
            },
            {
                "title": "Subqueries & Advanced SQL",
                "content": "Subqueries: Queries nested inside other queries.\n\nTypes:\n  Scalar subquery: Returns single value.\n    SELECT name FROM emp WHERE salary = (SELECT MAX(salary) FROM emp);\n\n  Row subquery: Returns single row.\n  Table subquery: Returns multiple rows/columns. Used with IN, EXISTS, ANY, ALL.\n\nCorrelated Subquery: References outer query. Re-executed for each outer row.\n  -- Employees earning more than their department average\n  SELECT e.name, e.salary\n  FROM employees e\n  WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);\n\nEXISTS vs IN:\n  EXISTS: Returns true if subquery returns any rows. Efficient for large subqueries.\n  IN: Checks if value is in subquery result. Simpler syntax.\n\nWindow Functions:\n  ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE(), LAG(), LEAD()\n  OVER (PARTITION BY ... ORDER BY ...)\n\n  -- Rank employees by salary within each department\n  SELECT name, dept_id, salary,\n         RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rank\n  FROM employees;\n\n  RANK: Gaps after ties (1,2,2,4). DENSE_RANK: No gaps (1,2,2,3). ROW_NUMBER: No ties (1,2,3,4).\n\nCommon SQL Patterns:\n  Nth highest salary:\n  SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET N-1;\n  Or: SELECT MIN(salary) FROM (SELECT DISTINCT salary FROM emp ORDER BY salary DESC LIMIT N) t;\n\n  Duplicate detection:\n  SELECT col, COUNT(*) FROM table GROUP BY col HAVING COUNT(*) > 1;\n\n  Self Join (employees and their managers):\n  SELECT e.name, m.name as manager FROM emp e JOIN emp m ON e.manager_id = m.emp_id;",
                "key_points": [
                    "Correlated subqueries reference the outer query - re-executed per row",
                    "EXISTS is more efficient than IN for large datasets",
                    "RANK vs DENSE_RANK vs ROW_NUMBER: understand the difference for interviews",
                    "Nth highest salary is the most asked SQL interview question",
                    "Window functions are increasingly asked in Amazon and Microsoft SQL rounds"
                ],
                "examples": [
                    {"question": "Find the 3rd highest salary.", "solution": "SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2; -- Or using subquery: SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees));"},
                    {"question": "Find employees who earn more than all employees in department 10.", "solution": "SELECT name FROM employees WHERE salary > ALL (SELECT salary FROM employees WHERE dept_id = 10);"},
                    {"question": "Find duplicate emails in a Users table.", "solution": "SELECT email, COUNT(*) as cnt FROM Users GROUP BY email HAVING COUNT(*) > 1;"}
                ],
            },
            {
                "title": "ER Diagrams & Relational Algebra",
                "content": "ER (Entity-Relationship) Model:\n  Entity: Object with attributes (rectangle).\n  Attribute: Property (oval). Types: simple, composite, multi-valued, derived.\n  Relationship: Association between entities (diamond).\n  Cardinality: 1:1, 1:N, M:N.\n\nER to Relational Mapping:\n  Strong entity -> Table with all attributes. PK = entity key.\n  Weak entity -> Table with own attributes + owner's PK. PK = owner PK + partial key.\n  1:1 relationship -> FK in either table (prefer total participation side).\n  1:N relationship -> FK in the N-side table.\n  M:N relationship -> New junction table with PKs from both entities.\n\nRelational Algebra:\n  Selection (sigma): sigma_condition(R) - filter rows.\n  Projection (pi): pi_columns(R) - select columns.\n  Union (R U S): All tuples in R or S (compatible schemas).\n  Intersection (R intersect S): Tuples in both R and S.\n  Difference (R - S): Tuples in R but not S.\n  Cartesian Product (R x S): All pairs.\n  Natural Join (R |><| S): Join on common attributes.\n  Theta Join: Join on condition.\n  Division (R / S): Tuples in R associated with ALL tuples in S.\n\nEquivalences:\n  sigma_c1 AND c2(R) = sigma_c1(sigma_c2(R))\n  pi_a(sigma_c(R)) = sigma_c(pi_a(R)) if c uses only attributes in a\n  sigma_c(R x S) = R |><|_c S (theta join)\n\nRelational Calculus:\n  Tuple Relational Calculus: {t | condition(t)}\n  Domain Relational Calculus: {<a,b,...> | condition}\n  Equivalent in expressive power to relational algebra.",
                "key_points": [
                    "ER diagram cardinality: 1:1, 1:N, M:N determines FK placement",
                    "M:N relationships need a junction (bridge) table",
                    "Weak entity depends on strong entity; its PK includes owner's PK",
                    "Relational algebra: selection (rows), projection (columns), join, division",
                    "ER diagrams and relational algebra are staple GATE and placement topics"
                ],
                "examples": [
                    {"question": "Convert M:N relationship between Students and Courses to tables.", "solution": "Students(student_id PK, name). Courses(course_id PK, title). Enrollment(student_id FK, course_id FK, grade). PK of Enrollment = (student_id, course_id)."},
                    {"question": "Relational algebra: Find names of employees in department 'CS'.", "solution": "pi_name(sigma_{dept='CS'}(Employees)). First select rows where dept='CS', then project the name column."},
                    {"question": "Division: R has (Student, Course) and S has (Course). R/S gives students enrolled in ALL courses in S.", "solution": "If S = {Math, CS} and R has (Alice,Math), (Alice,CS), (Bob,Math). R/S = {Alice} because only Alice has both courses."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Normal Forms", "explanation": "1NF: atomic values. 2NF: no partial dependency. 3NF: no transitive dependency. BCNF: every determinant is a superkey."},
            {"name": "Functional Dependency", "explanation": "X->Y means X uniquely determines Y. Used to derive keys, normal forms, and decomposition."},
            {"name": "SQL Joins", "explanation": "INNER (matching), LEFT (all left + matching right), RIGHT, FULL OUTER, CROSS (cartesian). Self join for hierarchies."},
            {"name": "Aggregation", "explanation": "COUNT, SUM, AVG, MIN, MAX with GROUP BY. HAVING filters groups. WHERE filters rows before grouping."},
            {"name": "ER Model", "explanation": "Entities (rectangles), attributes (ovals), relationships (diamonds). Cardinality: 1:1, 1:N, M:N. Map to tables with FKs."}
        ],
        "formulas": [
            "Closure: X+ = set of all attributes functionally determined by X",
            "Number of superkeys: 2^(n - |candidate_key|) * (number of candidate keys, accounting for overlap)",
            "BCNF check: for every FD X->Y, is X a superkey?",
            "3NF check: for every FD X->Y, X is superkey OR Y is prime attribute",
            "SQL execution: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY"
        ],
        "solved_examples": [
            {"question": "Find the highest normal form of R(A,B,C,D) with FDs: A->B, BC->D, A->C.", "solution": "A+ = {A,B,C,D}. A is key. Check FDs: A->B (A is superkey, ok). BC->D (BC+ = {B,C,D}, not superkey). Violates BCNF. But D is non-prime, BC is not superkey but D is non-prime. For 3NF: BC->D, is BC superkey? No. Is D prime? No (only key is A). Violates 3NF. Check 2NF: key is A (single), no partial deps. It is in 2NF but not 3NF."},
            {"question": "SQL: Find the second highest salary.", "solution": "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees); -- Or: SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;"},
            {"question": "Convert ER: Student (1) -- enrolls -- (N) Course, with grade attribute on relationship.", "solution": "Students(sid PK, name). Courses(cid PK, title). Since 1:N, FK goes on N-side: Courses table? No, enrolls is M:N actually if a student can take many courses. If truly 1:N (each course has one student), Courses(cid PK, title, sid FK, grade). More likely M:N: Enrollment(sid FK, cid FK, grade, PK=(sid,cid))."}
        ],
        "tips": [
            "For normalization: find candidate keys first using attribute closure, then check each FD.",
            "2NF issues only arise with composite keys. Single-attribute key -> automatically 2NF.",
            "Practice SQL queries on paper - many exams don't have computers.",
            "For ER diagrams, always identify cardinality first (1:1, 1:N, M:N) before mapping to tables.",
            "In TCS NQT, SQL questions are straightforward - focus on joins, GROUP BY, and subqueries."
        ],
    },
    56: {
        "title": "DBMS: Transactions & Indexing",
        "overview": "Transactions ensure database integrity through ACID properties. Concurrency control and indexing optimize performance. This topic covers ACID, serializability, locking protocols, B-tree indexing, hashing, and recovery techniques - all critical for GATE, TCS, Infosys, and Amazon database interview questions.",
        "chapters": [
            {
                "title": "ACID Properties & Transaction States",
                "content": "A transaction is a logical unit of work that must be completed entirely or not at all.\n\nACID Properties:\n  Atomicity: All or nothing. If any part fails, entire transaction rolls back.\n    Ensured by: Undo/redo logs, recovery manager.\n  Consistency: Database moves from one consistent state to another.\n    Ensured by: Integrity constraints, triggers, application logic.\n  Isolation: Concurrent transactions don't interfere with each other.\n    Ensured by: Concurrency control (locking, MVCC).\n  Durability: Once committed, changes persist even after crash.\n    Ensured by: Write-ahead logging (WAL), checkpointing.\n\nTransaction States:\n  Active -> Partially Committed -> Committed\n  Active -> Failed -> Aborted\n  After abort: Restart or Kill.\n\nSchedule: Order of operations from multiple concurrent transactions.\n  Serial Schedule: Transactions execute one after another. Always correct but slow.\n  Non-serial Schedule: Operations interleaved. May or may not be correct.\n\nProblems with Concurrent Execution:\n  1. Lost Update: T1 reads X, T2 reads X, T1 writes X, T2 writes X (T1's update lost).\n  2. Dirty Read: T1 writes X, T2 reads X, T1 aborts. T2 has invalid data.\n  3. Unrepeatable Read: T1 reads X, T2 modifies X, T1 reads X again (different value).\n  4. Phantom Read: T1 reads set of rows, T2 inserts row, T1 reads again (extra row).\n\nIsolation Levels:\n  Read Uncommitted: No protection. Dirty reads possible.\n  Read Committed: No dirty reads. Unrepeatable reads possible.\n  Repeatable Read: No dirty or unrepeatable reads. Phantoms possible.\n  Serializable: Full isolation. No anomalies. Slowest.",
                "key_points": [
                    "ACID: Atomicity (all/nothing), Consistency, Isolation, Durability",
                    "Lost update, dirty read, unrepeatable read, phantom read are the 4 concurrency problems",
                    "Serializable is the strongest isolation level - prevents all anomalies",
                    "WAL (Write Ahead Logging) ensures durability - log before data write",
                    "ACID properties are asked in every database interview and placement exam"
                ],
                "examples": [
                    {"question": "T1: Read(A), A=A-50, Write(A), Read(B), B=B+50, Write(B). Is this atomic?", "solution": "If the system crashes after Write(A) but before Write(B), atomicity requires rollback of A change. The recovery system uses undo logs to restore A to original value. Either both A and B are updated, or neither is."},
                    {"question": "Dirty read scenario: T1 writes A=100, T2 reads A=100, T1 aborts.", "solution": "T2 read a value that was never committed (A=100 was rolled back). T2's computation based on this value is invalid. Read Committed isolation level prevents this by only reading committed values."},
                    {"question": "Which isolation level prevents phantom reads?", "solution": "Serializable. It uses range locks or MVCC to prevent new rows from appearing in a repeated query. Repeatable Read prevents dirty and unrepeatable reads but NOT phantoms in standard SQL (MySQL InnoDB's Repeatable Read does prevent phantoms as an implementation detail)."}
                ],
            },
            {
                "title": "Serializability & Conflict Equivalence",
                "content": "A schedule is serializable if its result is equivalent to some serial schedule.\n\nConflicting Operations: Two operations conflict if:\n  1. They belong to different transactions.\n  2. They access the same data item.\n  3. At least one is a write.\n\nConflict Serializable: Can reorder non-conflicting operations to get a serial schedule.\nTest using Precedence Graph (Serialization Graph):\n  Node for each transaction.\n  Edge Ti -> Tj if Ti has a conflicting operation before Tj's conflicting operation.\n  If graph is acyclic: conflict serializable. Topological sort gives equivalent serial order.\n\nExample:\n  T1: Read(A), Write(A)\n  T2: Read(A), Write(A)\n  Schedule: R1(A), R2(A), W1(A), W2(A)\n  Conflicts: R1W2(A), R2W1(A), W1W2(A).\n  R1 before W2: T1->T2.\n  R2 before W1: T2->T1.\n  Cycle! T1->T2->T1. NOT conflict serializable.\n\nView Serializability (weaker than conflict):\n  Two schedules are view equivalent if:\n  1. Same initial reads (Ti reads initial value of X in both).\n  2. Same read dependencies (If Ti reads X written by Tj, same in both).\n  3. Same final writes (last write to X is by same Ti in both).\n  Every conflict serializable schedule is view serializable. Not vice versa.\n\nRecoverable Schedule: If Tj reads from Ti, Ti must commit before Tj.\nCascadeless: Only read committed values. Prevents cascading aborts.\nStrict: No read or write until the writing transaction commits or aborts.",
                "key_points": [
                    "Conflict serializable: precedence graph has no cycle",
                    "Topological sort of acyclic precedence graph gives equivalent serial order",
                    "View serializability is weaker (harder to test, NP-complete in general)",
                    "Recoverable: don't commit until all transactions you read from have committed",
                    "Serializability testing with precedence graphs is a very common GATE question"
                ],
                "examples": [
                    {"question": "Schedule: R1(A), W2(A), R2(B), W1(B). Is it conflict serializable?", "solution": "Conflicts on A: R1(A) before W2(A) -> T1->T2. Conflicts on B: R2(B) before W1(B) -> T2->T1. Graph: T1->T2->T1. Cycle! NOT conflict serializable."},
                    {"question": "Schedule: R1(A), R2(B), W1(B), W2(A). Is it conflict serializable?", "solution": "Conflicts: R1(A) vs W2(A): T1->T2. R2(B) vs W1(B): T2->T1. Cycle again. NOT conflict serializable."},
                    {"question": "Schedule: R1(A), W1(A), R2(A), W2(A). Is it conflict serializable?", "solution": "Conflicts: W1(A) before R2(A): T1->T2. W1(A) before W2(A): T1->T2. All edges go T1->T2. No cycle. YES, conflict serializable. Equivalent to serial T1,T2."}
                ],
            },
            {
                "title": "Concurrency Control: Locking & 2PL",
                "content": "Lock-Based Protocols:\n  Shared Lock (S): Read access. Multiple transactions can hold S lock simultaneously.\n  Exclusive Lock (X): Write access. Only one transaction can hold. Blocks S and X.\n\nCompatibility Matrix:\n           | S     | X\n  S        | Yes   | No\n  X        | No    | No\n\nTwo-Phase Locking (2PL):\n  Growing Phase: Transaction acquires locks, never releases.\n  Shrinking Phase: Transaction releases locks, never acquires.\n  Guarantees conflict serializability!\n\nVariants:\n  Basic 2PL: May cause deadlock and cascading aborts.\n  Strict 2PL: Hold all X locks until commit/abort. Prevents cascading aborts.\n  Rigorous 2PL: Hold ALL locks (S and X) until commit. Simplest, most restrictive.\n\nDeadlock in Locking:\n  T1 locks A, requests B. T2 locks B, requests A. Circular wait.\n  Solutions: Timeout, deadlock detection (wait-for graph), prevention (wound-wait, wait-die).\n\nWound-Wait:\n  If Ti is older than Tj: Ti 'wounds' (preempts) Tj.\n  If Ti is younger than Tj: Ti waits.\n  Prefers older transactions.\n\nWait-Die:\n  If Ti is older than Tj: Ti waits.\n  If Ti is younger than Tj: Ti dies (rollback and restart).\n  Prefers older transactions.\n\nTimestamp Ordering:\n  Each transaction gets a timestamp. Operations executed in timestamp order.\n  If conflict: younger transaction aborts and restarts.",
                "key_points": [
                    "2PL guarantees conflict serializability but may cause deadlocks",
                    "Strict 2PL: hold X locks until commit. Prevents cascading aborts.",
                    "Shared (S) locks allow concurrent reads; Exclusive (X) locks allow only one writer",
                    "Wound-Wait and Wait-Die prevent deadlock using transaction age",
                    "2PL and locking are the most important concurrency control topics for exams"
                ],
                "examples": [
                    {"question": "Does this follow 2PL? T1: Lock-S(A), Read(A), Lock-X(B), Unlock(A), Write(B), Unlock(B).", "solution": "Growing: Lock-S(A), Lock-X(B). Shrinking: Unlock(A), Unlock(B). No lock acquired after first unlock. YES, follows 2PL."},
                    {"question": "Does this follow 2PL? T1: Lock-S(A), Unlock(A), Lock-X(B), Write(B), Unlock(B).", "solution": "Lock-S(A) -> Unlock(A) -> Lock-X(B): Lock acquired after unlock! NO, does not follow 2PL."},
                    {"question": "Wound-Wait: T1(ts=5) requests lock held by T2(ts=10). What happens?", "solution": "T1 is older (ts=5 < ts=10). In Wound-Wait, older wounds younger. T2 is aborted (wounded), T1 gets the lock. T2 restarts with same timestamp."}
                ],
            },
            {
                "title": "B-Tree & B+ Tree Indexing",
                "content": "Index: Data structure for fast lookups. Without index: O(n) scan. With index: O(log n).\n\nB-Tree of order m:\n  Each node has at most m children and m-1 keys.\n  Each non-root node has at least ceil(m/2) children.\n  All leaves at same level. Balanced.\n  Keys in each node are sorted.\n\nB+ Tree (most common in databases):\n  All data pointers at leaf level (internal nodes only have keys for routing).\n  Leaf nodes linked in a linked list (efficient range queries).\n  Internal node: ceil(m/2) to m children.\n  Leaf node: ceil((m-1)/2) to m-1 keys.\n\nB+ Tree Operations:\n  Search: Start at root, follow appropriate child pointer. O(log n).\n  Insert: Find leaf, insert key. If overflow (> m-1 keys), split node.\n    Split: Middle key promoted to parent. If parent overflows, split recursively.\n  Delete: Find and remove key. If underflow (< ceil((m-1)/2) keys), borrow from sibling or merge.\n\nExample: B+ tree order 3 (max 2 keys per node, max 3 children).\n  Insert 10, 20, 30: [10,20] leaf. Insert 30: overflow, split.\n  Root: [20]. Left leaf: [10]. Right leaf: [20,30]. Leaves linked.\n\nIndexing Types:\n  Primary Index: On primary key, ordered file. Dense or sparse.\n  Secondary Index: On non-key attribute. Always dense.\n  Clustered Index: File physically sorted on index attribute.\n  Unclustered/Non-clustered: File not sorted on index attribute.\n\nNumber of I/O accesses:\n  B+ tree: O(log_m(n)) levels. Each level = 1 disk access. Typically 3-4 levels for millions of records.",
                "key_points": [
                    "B+ tree: data only at leaves, leaves linked. Best for range queries.",
                    "B+ tree of order m: internal nodes have ceil(m/2) to m children",
                    "B+ tree insert: split on overflow, promote middle key",
                    "B+ tree search: O(log_m(n)) disk accesses - very efficient",
                    "B-tree/B+ tree indexing is a core GATE and placement topic"
                ],
                "examples": [
                    {"question": "B+ tree order 4: insert keys 5, 8, 1, 7, 3, 12, 9, 6. Show structure.", "solution": "Max 3 keys/node. Insert 5:[5]. 8:[5,8]. 1:[1,5,8]. 7: overflow! Split: mid=5 promoted. Root:[5]. Leaves: [1]->[5,7,8]. Insert 3: [1,3]->[5,7,8]. Insert 12: [5,7,8,12] overflow. Split mid=8. Root:[5,8]. Leaves: [1,3]->[5,7]->[8,12]. Insert 9: [8,9,12]. Insert 6: [5,6,7] overflow. Split mid=6. Root becomes [5,6,8]. Leaves: [1,3]->[5]->[6,7]->[8,9,12]. Wait, this needs more careful tracing with order 4 rules."},
                    {"question": "How many disk accesses to search in B+ tree with 1 million records, order 100?", "solution": "Levels = ceil(log_100(1,000,000)) = ceil(3) = 3. Plus 1 for leaf data access = 4 total disk accesses. Compared to linear scan: 1,000,000 / records_per_block."},
                    {"question": "Difference between B-tree and B+ tree?", "solution": "B-tree: Data pointers at all nodes. B+ tree: Data only at leaves, internal nodes just route. B+ tree leaves are linked for range queries. B+ tree has better cache utilization for range scans. B+ tree is used in most databases (MySQL InnoDB, PostgreSQL)."}
                ],
            },
            {
                "title": "Hashing & Recovery Techniques",
                "content": "Hashing in DBMS:\n  Static Hashing: Fixed number of buckets. h(key) = key % num_buckets.\n  Problem: Overflow chains when buckets fill up.\n\n  Extendible Hashing:\n  Directory doubles when split needed. Uses global depth and local depth.\n  Only the overflowing bucket is split. Efficient growth.\n\n  Linear Hashing:\n  Buckets split in order (round-robin). Overflow chains handled progressively.\n  No directory needed. Split triggered by load factor threshold.\n\nRecovery Techniques:\n  Log-Based Recovery:\n  Write-Ahead Logging (WAL): Write log record BEFORE modifying database.\n  Log record: <Ti, X, old_value, new_value>\n  Commit record: <Ti, COMMIT>\n\n  Undo Recovery: If Ti didn't commit before crash, undo all its writes.\n  Redo Recovery: If Ti committed before crash, redo all its writes.\n  Undo-Redo: Combined approach.\n\n  Checkpointing:\n  Periodically save database state. On recovery, only process log records after last checkpoint.\n  Reduces recovery time.\n\n  ARIES (Algorithm for Recovery and Isolation Exploiting Semantics):\n  Industry standard recovery algorithm.\n  Three phases: Analysis (find active transactions), Redo (replay all), Undo (rollback uncommitted).\n\nRecovery Example:\n  Log: <T1 start>, <T1, A, 100, 200>, <T2 start>, <T2, B, 50, 100>, <T1 commit>, <CRASH>\n  T1 committed: REDO T1 (A=200). T2 not committed: UNDO T2 (B=50).",
                "key_points": [
                    "Write-Ahead Logging: log before data write. Ensures recoverability.",
                    "After crash: REDO committed transactions, UNDO uncommitted",
                    "Checkpointing reduces recovery time by limiting log to scan",
                    "Extendible hashing: directory-based, doubles on overflow. Efficient.",
                    "Recovery and hashing are important GATE and interview topics"
                ],
                "examples": [
                    {"question": "Log: <T1,A,10,20>, <T2,B,30,40>, <T1 commit>, <T3,C,50,60>, crash. Which to redo/undo?", "solution": "T1 committed: REDO (A=20). T2 not committed: UNDO (B=30). T3 not committed: UNDO (C=50)."},
                    {"question": "Extendible hashing: global depth=1, 2 buckets. Insert keys 1,2,3,4,5 with h(k)=k%4.", "solution": "Initial: directory [0,1]. h(1)=1->bucket1. h(2)=2->bucket0. h(3)=3->bucket1. If bucket1 full (say capacity 2): split bucket1, increase depth. This gets complex - the key insight is only the overflowing bucket splits."},
                    {"question": "Why is WAL necessary for atomicity?", "solution": "If system crashes mid-write, the log tells us what to undo. Without WAL, if data is written before log, we can't know if the write was complete. WAL ensures: if the data change is on disk, the log record is definitely on disk too."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "ACID Properties", "explanation": "Atomicity (all/nothing), Consistency (valid states), Isolation (no interference), Durability (permanent after commit)."},
            {"name": "Serializability", "explanation": "Schedule equivalent to some serial schedule. Test with precedence graph: acyclic = conflict serializable."},
            {"name": "Two-Phase Locking", "explanation": "Growing phase (acquire locks) then shrinking phase (release locks). Guarantees conflict serializability. Strict 2PL holds X locks until commit."},
            {"name": "B+ Tree", "explanation": "Balanced tree index. Data at leaves, linked for range queries. O(log_m(n)) search. Order m: max m children, m-1 keys."},
            {"name": "Write-Ahead Logging", "explanation": "Log record written before data modification. Enables undo (rollback uncommitted) and redo (replay committed) after crash."}
        ],
        "formulas": [
            "B+ tree levels: ceil(log_m(n)) where m = order, n = records",
            "B+ tree internal node: ceil(m/2) to m children",
            "B+ tree leaf node: ceil((m-1)/2) to m-1 key-pointer pairs",
            "Hash function: h(key) = key % num_buckets",
            "2PL: locks_acquired_before_first_release guarantees serializability"
        ],
        "solved_examples": [
            {"question": "Precedence graph for: R1(A), W2(A), R2(B), W1(B). Serializable?", "solution": "R1(A) before W2(A): T1->T2. R2(B) before W1(B): T2->T1. Cycle T1<->T2. NOT conflict serializable."},
            {"question": "B+ tree order 3, keys 1-7. Minimum levels?", "solution": "Order 3: max 2 keys/leaf. 7 keys need at least 4 leaves. Internal node has max 3 children. Root with 3 children, each with 3 children = 9 leaves max. But we need only 4. Root(2 keys)->3 children, 3 leaves. With 7 keys in 4 leaves: 2 levels (root + leaves). Height = 2."},
            {"question": "Strict 2PL: T1 writes A then commits. T2 tries to read A. What happens?", "solution": "T1 holds X lock on A until commit. T2 requests S lock on A. Incompatible (X blocks S). T2 waits. After T1 commits and releases X lock, T2 gets S lock and reads committed value. No dirty read."}
        ],
        "tips": [
            "For serializability: draw the precedence graph. Cycle = not serializable.",
            "ACID is asked as a conceptual question in almost every interview. Know real-world examples.",
            "B+ tree order definition varies: some define order as max children, others as max keys. Clarify!",
            "For recovery questions: committed = REDO, uncommitted = UNDO. Always check the log.",
            "2PL is the most practical concurrency control method - know the variants (basic, strict, rigorous)."
        ],
    },
    57: {
        "title": "CN: OSI & TCP/IP",
        "overview": "Computer networking enables communication between devices. The OSI model provides a 7-layer framework, while TCP/IP is the practical 4-layer model used on the internet. This topic covers both models, protocols at each layer, IP addressing, subnetting, and CIDR - essential knowledge for TCS NQT, Infosys, GATE, and Amazon networking interview questions.",
        "chapters": [
            {
                "title": "OSI Model: 7 Layers",
                "content": "The OSI (Open Systems Interconnection) model has 7 layers. Each layer has specific functions and communicates with adjacent layers.\n\nLayer 7 - Application:\n  User interface. Protocols: HTTP, FTP, SMTP, DNS, DHCP, SNMP.\n  PDU: Data/Message.\n\nLayer 6 - Presentation:\n  Data format translation, encryption, compression.\n  Converts between application and network formats.\n  Examples: SSL/TLS encryption, JPEG/MPEG compression, ASCII/EBCDIC conversion.\n\nLayer 5 - Session:\n  Establishes, manages, terminates sessions.\n  Session checkpointing and recovery. Dialog control (half/full duplex).\n  Examples: NetBIOS, RPC.\n\nLayer 4 - Transport:\n  End-to-end communication. Segmentation, flow control, error control.\n  Protocols: TCP (reliable, connection-oriented), UDP (unreliable, connectionless).\n  PDU: Segment (TCP) / Datagram (UDP). Port numbers identify applications.\n\nLayer 3 - Network:\n  Routing and logical addressing (IP addresses).\n  Protocols: IP, ICMP, ARP, IGMP. Routers operate here.\n  PDU: Packet. Determines best path.\n\nLayer 2 - Data Link:\n  Node-to-node communication. Framing, MAC addressing, error detection.\n  Sublayers: LLC (Logical Link Control), MAC (Media Access Control).\n  Protocols: Ethernet, Wi-Fi, PPP. Switches/bridges operate here.\n  PDU: Frame.\n\nLayer 1 - Physical:\n  Bit transmission over physical medium. Cables, signals, voltages.\n  Devices: Hubs, repeaters, modems.\n  PDU: Bits.\n\nMnemonic (top to bottom): All People Seem To Need Data Processing.\nMnemonic (bottom to top): Please Do Not Throw Sausage Pizza Away.",
                "key_points": [
                    "7 layers: Application, Presentation, Session, Transport, Network, Data Link, Physical",
                    "Transport layer: TCP (reliable) and UDP (fast). Port numbers here.",
                    "Network layer: IP addressing and routing. Routers operate here.",
                    "Data Link layer: MAC addressing. Switches operate here.",
                    "OSI layer questions are the #1 CN topic in placements and GATE"
                ],
                "examples": [
                    {"question": "At which layer does a router operate?", "solution": "Layer 3 (Network layer). Routers use IP addresses to forward packets between different networks. They examine the destination IP in the packet header to make routing decisions."},
                    {"question": "Which layer handles encryption?", "solution": "Layer 6 (Presentation layer) in OSI model. However, in practice (TCP/IP model), encryption via SSL/TLS operates between Application and Transport layers."},
                    {"question": "What is the PDU at each layer?", "solution": "Application/Presentation/Session: Data. Transport: Segment (TCP) or Datagram (UDP). Network: Packet. Data Link: Frame. Physical: Bits."}
                ],
            },
            {
                "title": "TCP/IP Model & Comparison",
                "content": "TCP/IP Model: 4 layers (practical model used on the internet).\n\n1. Network Access (Link) Layer:\n   Combines OSI Physical + Data Link. Handles hardware addressing and physical transmission.\n   Protocols: Ethernet, Wi-Fi, ARP.\n\n2. Internet Layer:\n   Same as OSI Network layer. Routing, logical addressing.\n   Protocols: IP (v4/v6), ICMP, IGMP.\n\n3. Transport Layer:\n   Same as OSI Transport. End-to-end communication.\n   TCP: Connection-oriented, reliable, ordered, flow control (sliding window), congestion control.\n   UDP: Connectionless, unreliable, faster, no overhead.\n\n4. Application Layer:\n   Combines OSI Application + Presentation + Session.\n   Protocols: HTTP, FTP, SMTP, DNS, DHCP, SSH, Telnet.\n\nTCP vs UDP:\n  TCP: Reliable, ordered, error checking, flow control, 3-way handshake.\n     Used for: Web (HTTP), email (SMTP), file transfer (FTP).\n  UDP: Unreliable, no ordering, minimal overhead.\n     Used for: DNS queries, video streaming, VoIP, gaming.\n\nTCP 3-Way Handshake:\n  1. Client -> SYN -> Server\n  2. Server -> SYN+ACK -> Client\n  3. Client -> ACK -> Server\n  Connection established. Data transfer begins.\n\nTCP Connection Termination (4-way):\n  1. Client -> FIN -> Server\n  2. Server -> ACK -> Client\n  3. Server -> FIN -> Client\n  4. Client -> ACK -> Server\n\nOSI vs TCP/IP:\n  OSI: 7 layers, theoretical, strict layer separation.\n  TCP/IP: 4 layers, practical, used on internet, less rigid.",
                "key_points": [
                    "TCP/IP has 4 layers: Network Access, Internet, Transport, Application",
                    "TCP: reliable, 3-way handshake, flow control. UDP: fast, no guarantees.",
                    "TCP 3-way handshake: SYN, SYN-ACK, ACK. Know this sequence.",
                    "DNS uses UDP (port 53) for queries, TCP for zone transfers.",
                    "TCP vs UDP comparison is asked in every networking interview and placement exam"
                ],
                "examples": [
                    {"question": "Why does DNS use UDP instead of TCP?", "solution": "DNS queries are small (single request-response), so the overhead of TCP's 3-way handshake is unnecessary. UDP is faster for small queries. However, DNS uses TCP for zone transfers (large data) and when response exceeds 512 bytes."},
                    {"question": "Trace a TCP connection: Client initiates, sends data 'Hello', then closes.", "solution": "1. SYN (seq=100). 2. SYN-ACK (seq=300, ack=101). 3. ACK (seq=101, ack=301). Connection open. 4. Data 'Hello' (seq=101, 5 bytes). 5. ACK (seq=301, ack=106). 6. FIN (seq=106). 7. ACK (seq=301, ack=107). 8. FIN (seq=301). 9. ACK (seq=107, ack=302). Connection closed."},
                    {"question": "Map HTTP request to OSI layers.", "solution": "Application (L7): HTTP formats request. Presentation (L6): SSL encrypts if HTTPS. Session (L5): Manages connection session. Transport (L4): TCP segments data, port 80/443. Network (L3): IP adds source/dest IP. Data Link (L2): Ethernet adds MAC addresses. Physical (L1): Bits transmitted on wire/wireless."}
                ],
            },
            {
                "title": "IP Addressing & Classes",
                "content": "IPv4: 32-bit address, written as 4 octets in dotted decimal. Example: 192.168.1.100\n\nClassful Addressing:\n  Class A: 0.0.0.0 - 127.255.255.255. Mask: 255.0.0.0 (/8).\n    Network: 8 bits. Host: 24 bits. 2^7-2 = 126 networks. 2^24-2 = 16M hosts each.\n  Class B: 128.0.0.0 - 191.255.255.255. Mask: 255.255.0.0 (/16).\n    Network: 16 bits. Host: 16 bits. 16384 networks. 65534 hosts each.\n  Class C: 192.0.0.0 - 223.255.255.255. Mask: 255.255.255.0 (/24).\n    Network: 24 bits. Host: 8 bits. 2M networks. 254 hosts each.\n  Class D: 224-239. Multicast.\n  Class E: 240-255. Reserved.\n\nSpecial Addresses:\n  0.0.0.0: This network.\n  127.0.0.1: Loopback (localhost).\n  255.255.255.255: Broadcast.\n  Network address: All host bits 0.\n  Broadcast address: All host bits 1.\n\nPrivate IP Ranges (RFC 1918):\n  10.0.0.0/8 (Class A private)\n  172.16.0.0/12 (Class B private)\n  192.168.0.0/16 (Class C private)\n\nIPv6: 128-bit address. Written as 8 groups of 4 hex digits.\n  Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334\n  Simplified: 2001:db8:85a3::8a2e:370:7334\n  Much larger address space: 2^128 addresses.",
                "key_points": [
                    "Class A: first octet 0-127, /8 mask. Class B: 128-191, /16. Class C: 192-223, /24.",
                    "Private IPs: 10.x.x.x, 172.16-31.x.x, 192.168.x.x",
                    "Network address: host bits all 0. Broadcast: host bits all 1.",
                    "Usable hosts = 2^host_bits - 2 (subtract network and broadcast addresses)",
                    "IP addressing and class identification are the most common CN MCQ topics"
                ],
                "examples": [
                    {"question": "What class is 150.10.30.1? How many hosts per network?", "solution": "150 is between 128-191: Class B. Subnet mask: 255.255.0.0 (/16). Host bits: 16. Usable hosts: 2^16 - 2 = 65534."},
                    {"question": "Is 172.20.5.1 a private IP?", "solution": "Private Class B range: 172.16.0.0 - 172.31.255.255. 172.20.5.1 is in this range. YES, it's a private IP."},
                    {"question": "What is the network address of 192.168.5.130/24?", "solution": "Mask /24 = 255.255.255.0. AND with IP: 192.168.5.130 AND 255.255.255.0 = 192.168.5.0. Network address: 192.168.5.0. Broadcast: 192.168.5.255."}
                ],
            },
            {
                "title": "Subnetting & CIDR",
                "content": "Subnetting: Dividing a network into smaller subnetworks.\n\nSubnet Mask: Indicates which bits are network and which are host.\n  /24 = 255.255.255.0 = 11111111.11111111.11111111.00000000\n  /25 = 255.255.255.128 = 25 network bits, 7 host bits.\n\nSubnetting Steps:\n  1. Determine number of subnets needed: 2^subnet_bits >= needed_subnets.\n  2. Determine hosts per subnet: 2^host_bits - 2 >= needed_hosts.\n  3. New mask = original mask + subnet bits.\n\nExample: Subnet 192.168.1.0/24 into 4 subnets.\n  Need 4 subnets: 2^2 = 4. Borrow 2 bits from host. New mask: /26.\n  Subnet 1: 192.168.1.0/26 (hosts: .1-.62, broadcast: .63)\n  Subnet 2: 192.168.1.64/26 (hosts: .65-.126, broadcast: .127)\n  Subnet 3: 192.168.1.128/26 (hosts: .129-.190, broadcast: .191)\n  Subnet 4: 192.168.1.192/26 (hosts: .193-.254, broadcast: .255)\n  Each subnet: 2^6 - 2 = 62 usable hosts.\n\nCIDR (Classless Inter-Domain Routing):\n  Eliminates class boundaries. Any prefix length allowed.\n  Notation: IP/prefix_length. Example: 10.0.0.0/12.\n  Supernetting: Combine multiple networks. Example: 192.168.0.0/24 + 192.168.1.0/24 = 192.168.0.0/23.\n\nVLSM (Variable Length Subnet Masking):\n  Different subnets can have different sizes.\n  Allocate larger subnets first, then smaller ones.\n\nSubnet calculation shortcut:\n  Block size = 256 - last non-zero octet of mask.\n  /26 mask: 255.255.255.192. Block = 256-192 = 64.\n  Subnets start at: .0, .64, .128, .192.",
                "key_points": [
                    "Subnetting borrows bits from host portion to create subnets",
                    "Usable hosts per subnet = 2^host_bits - 2",
                    "Block size = 256 - subnet mask value in the relevant octet",
                    "CIDR notation /n means n bits for network. Enables classless addressing.",
                    "Subnetting calculations are extremely common in GATE, TCS, and CN interviews"
                ],
                "examples": [
                    {"question": "How many subnets and hosts with 192.168.10.0/28?", "solution": "Original /24 network. /28 means 4 extra subnet bits. Subnets = 2^4 = 16. Host bits = 32-28 = 4. Hosts per subnet = 2^4 - 2 = 14."},
                    {"question": "Which subnet does 172.16.45.130/27 belong to?", "solution": "Block size: 256-224(/27 mask last octet)=32. Subnets: .0, .32, .64, .96, .128, .160,... 130 falls in .128 subnet. Network: 172.16.45.128/27. Broadcast: 172.16.45.159. Host range: .129-.158."},
                    {"question": "Supernet 192.168.0.0/24 and 192.168.1.0/24.", "solution": "Both differ only in 3rd octet bit 0. Combine: 192.168.0.0/23. This covers 192.168.0.0-192.168.1.255. 2^9 - 2 = 510 usable hosts."}
                ],
            },
            {
                "title": "Key Protocols at Each Layer",
                "content": "Application Layer Protocols:\n  HTTP (80): Web pages. Request-response. Methods: GET, POST, PUT, DELETE.\n  HTTPS (443): HTTP + TLS encryption.\n  FTP (20/21): File transfer. 20=data, 21=control.\n  SMTP (25): Send email. POP3 (110)/IMAP (143): Receive email.\n  DNS (53): Domain name to IP resolution.\n  DHCP (67/68): Automatic IP address assignment.\n  SSH (22): Secure remote login.\n  Telnet (23): Unsecure remote login.\n\nTransport Layer:\n  TCP (Transmission Control Protocol):\n    Reliable, connection-oriented, flow control, congestion control.\n    Sliding window for flow control. Slow start, congestion avoidance.\n  UDP (User Datagram Protocol):\n    Unreliable, connectionless, no flow control.\n    Header: source port, dest port, length, checksum (only 8 bytes).\n\nNetwork Layer:\n  IP: Routing, fragmentation, addressing.\n  ICMP: Error reporting (ping, traceroute).\n  ARP: IP address -> MAC address resolution.\n  RARP: MAC -> IP (obsolete, replaced by DHCP).\n\nData Link Layer:\n  Ethernet (IEEE 802.3): Most common LAN technology.\n  Wi-Fi (IEEE 802.11): Wireless LAN.\n  MAC address: 48-bit hardware address. Example: AA:BB:CC:DD:EE:FF.\n\nPort Numbers:\n  Well-known: 0-1023 (HTTP=80, HTTPS=443, SSH=22, DNS=53).\n  Registered: 1024-49151.\n  Dynamic: 49152-65535.",
                "key_points": [
                    "HTTP:80, HTTPS:443, FTP:20/21, SSH:22, DNS:53, SMTP:25 - memorize these ports",
                    "ARP resolves IP to MAC address. Used when destination is on same network.",
                    "DHCP assigns IP addresses automatically (DORA: Discover, Offer, Request, Ack)",
                    "ICMP is used by ping and traceroute - diagnostic protocol",
                    "Protocol-port mapping is a very common MCQ topic in every placement exam"
                ],
                "examples": [
                    {"question": "You type www.google.com in browser. Trace the protocol sequence.", "solution": "1. DNS (port 53, UDP): Resolve www.google.com to IP. 2. TCP 3-way handshake to IP on port 443. 3. TLS handshake (encryption). 4. HTTP GET / request over encrypted channel. 5. Server responds with HTML. 6. Browser renders page."},
                    {"question": "ARP: Host A (IP 10.0.0.1, MAC AA) wants to send to Host B (IP 10.0.0.2, MAC unknown). How?", "solution": "A broadcasts ARP request: 'Who has 10.0.0.2? Tell 10.0.0.1 (AA).' All hosts on LAN receive it. Host B responds (unicast): '10.0.0.2 is at MAC BB.' A caches this mapping and sends the frame to MAC BB."},
                    {"question": "DHCP process for a new device joining a network.", "solution": "DORA process: 1. Discover: Client broadcasts 'Any DHCP server?' 2. Offer: Server offers IP address. 3. Request: Client requests offered IP. 4. Acknowledge: Server confirms. Client now has IP, subnet mask, gateway, DNS server."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "OSI Model", "explanation": "7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application. Each has specific functions and PDUs."},
            {"name": "TCP/IP Model", "explanation": "4 layers: Network Access, Internet, Transport, Application. Practical model used on the internet."},
            {"name": "IP Addressing", "explanation": "IPv4: 32-bit, dotted decimal. Classes A-E. Private ranges: 10.x, 172.16-31.x, 192.168.x."},
            {"name": "Subnetting", "explanation": "Divide network into subnets by borrowing host bits. New mask = original + subnet bits. Hosts = 2^host_bits - 2."},
            {"name": "TCP vs UDP", "explanation": "TCP: reliable, ordered, connection-oriented. UDP: unreliable, fast, connectionless. TCP for web/email, UDP for DNS/streaming."}
        ],
        "formulas": [
            "Usable hosts = 2^host_bits - 2",
            "Number of subnets = 2^borrowed_bits",
            "Block size = 256 - subnet mask value",
            "CIDR: /n means n network bits, 32-n host bits",
            "IPv4 total addresses = 2^32 = ~4.3 billion"
        ],
        "solved_examples": [
            {"question": "What class is 130.45.67.89? Network and host portions?", "solution": "130 is 128-191: Class B. Network: 130.45.0.0. Host: 0.0.67.89 (or 67.89 in the host portion). Mask: 255.255.0.0."},
            {"question": "Subnet 10.0.0.0/8 to get at least 500 hosts per subnet.", "solution": "Need 2^h - 2 >= 500. h=9: 510 hosts. Host bits=9, subnet mask=32-9=23. New mask: /23. Subnets = 2^(23-8) = 2^15 = 32768 subnets, each with 510 hosts."},
            {"question": "Is 192.168.5.130 in the same subnet as 192.168.5.200 with /26 mask?", "solution": "/26 block size = 64. 130 is in .128 subnet (128-191). 200 is in .192 subnet (192-255). Different subnets!"}
        ],
        "tips": [
            "Memorize the port numbers: HTTP(80), HTTPS(443), SSH(22), DNS(53), FTP(20/21), SMTP(25).",
            "For subnetting: always calculate block size first (256 - mask). It makes everything easier.",
            "OSI vs TCP/IP comparison table is asked in almost every CN exam.",
            "Practice converting between /notation, dotted decimal mask, and binary mask.",
            "ARP, DHCP, and DNS are the three protocols most frequently asked about in interviews."
        ],
    },
    58: {
        "title": "CN: Protocols & Security",
        "overview": "Network protocols enable reliable communication, and security mechanisms protect data in transit. This topic covers HTTP/HTTPS, DNS, DHCP, ARP, firewalls, encryption fundamentals, SSL/TLS, and network security basics. These are essential concepts tested in TCS NQT, Infosys, GATE, and Amazon networking rounds.",
        "chapters": [
            {
                "title": "HTTP & HTTPS",
                "content": "HTTP (HyperText Transfer Protocol):\n  Application layer protocol for web communication. Port 80.\n  Stateless: Each request is independent (no memory of previous requests).\n  Request-Response model: Client sends request, server sends response.\n\nHTTP Methods:\n  GET: Retrieve data. Idempotent. Parameters in URL.\n  POST: Submit data. Not idempotent. Parameters in body.\n  PUT: Update/replace resource. Idempotent.\n  DELETE: Remove resource. Idempotent.\n  PATCH: Partial update.\n  HEAD: GET without body (headers only).\n\nHTTP Status Codes:\n  1xx: Informational (100 Continue).\n  2xx: Success (200 OK, 201 Created, 204 No Content).\n  3xx: Redirection (301 Moved Permanently, 302 Found, 304 Not Modified).\n  4xx: Client Error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found).\n  5xx: Server Error (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).\n\nHTTP/1.1 vs HTTP/2:\n  HTTP/1.1: Text-based, one request per connection (or keep-alive).\n  HTTP/2: Binary, multiplexing (multiple requests on one connection), header compression, server push.\n\nHTTPS = HTTP + TLS:\n  Encrypts all communication between client and server.\n  Uses SSL/TLS certificates for authentication.\n  Port 443. Prevents eavesdropping, tampering, and impersonation.\n\nCookies & Sessions:\n  Cookies: Small data stored on client. Sent with every request. Used for session management.\n  Sessions: Server-side state. Session ID stored in cookie.",
                "key_points": [
                    "HTTP is stateless - cookies/sessions add statefulness",
                    "GET is idempotent and cacheable; POST is not idempotent",
                    "200=OK, 404=Not Found, 500=Server Error - memorize key status codes",
                    "HTTPS = HTTP + TLS encryption. Uses port 443 instead of 80.",
                    "HTTP methods and status codes are very common in web development and placement interviews"
                ],
                "examples": [
                    {"question": "Difference between GET and POST?", "solution": "GET: Parameters in URL, cacheable, idempotent, limited data length (~2KB). POST: Parameters in body, not cached, not idempotent, no data limit. GET for retrieval, POST for submission."},
                    {"question": "What happens when you get a 301 status code?", "solution": "301 Moved Permanently: The resource has permanently moved to a new URL. Browser should redirect to the new URL (provided in Location header) and update bookmarks. Search engines transfer SEO ranking to new URL."},
                    {"question": "Why is HTTP stateless? How do websites remember logged-in users?", "solution": "HTTP is stateless by design (simpler, scalable). Websites use cookies: after login, server creates session and sends session ID as cookie. Browser sends this cookie with every subsequent request. Server identifies user from session ID."}
                ],
            },
            {
                "title": "DNS & DHCP",
                "content": "DNS (Domain Name System):\n  Resolves domain names to IP addresses. Port 53.\n  Hierarchical structure: Root (.) -> TLD (.com, .org) -> Domain (google.com) -> Subdomain (mail.google.com).\n\nDNS Resolution Process:\n  1. Browser checks cache.\n  2. OS checks /etc/hosts and local DNS cache.\n  3. Query to recursive DNS resolver (usually ISP).\n  4. Resolver queries root server -> TLD server -> authoritative server.\n  5. Authoritative server returns IP address.\n  6. Resolver caches and returns to client.\n\nDNS Record Types:\n  A: Domain -> IPv4 address.\n  AAAA: Domain -> IPv6 address.\n  CNAME: Alias for another domain.\n  MX: Mail server for domain.\n  NS: Nameserver for domain.\n  TXT: Text record (SPF, DKIM for email auth).\n  PTR: Reverse DNS (IP -> domain).\n\nDNS Query Types:\n  Recursive: Resolver does all the work, returns final answer.\n  Iterative: Each server returns referral to next server. Client follows chain.\n\nDHCP (Dynamic Host Configuration Protocol):\n  Automatically assigns IP addresses to devices. Ports 67(server)/68(client).\n  DORA Process:\n  1. Discover: Client broadcasts to find DHCP servers.\n  2. Offer: Server offers an IP address.\n  3. Request: Client requests the offered IP.\n  4. Acknowledge: Server confirms assignment.\n\nDHCP Lease: IP is assigned for a limited time. Client must renew before expiry.\n  At 50% of lease: client unicasts renewal to same server.\n  At 87.5%: client broadcasts renewal to any server.",
                "key_points": [
                    "DNS resolves domain names to IPs. Hierarchical: root -> TLD -> authoritative.",
                    "DNS uses UDP for queries (fast), TCP for zone transfers (reliable).",
                    "DHCP DORA: Discover, Offer, Request, Acknowledge. All broadcasts initially.",
                    "A record maps domain to IPv4. CNAME is an alias. MX is for email.",
                    "DNS and DHCP processes are frequently asked in CN interviews and placements"
                ],
                "examples": [
                    {"question": "Resolve www.example.com step by step.", "solution": "1. Client asks recursive resolver. 2. Resolver asks root server (.): 'Where is .com?' -> referral to .com TLD server. 3. Resolver asks .com TLD: 'Where is example.com?' -> referral to example.com authoritative server. 4. Resolver asks authoritative: 'What is www.example.com?' -> A record: 93.184.216.34. 5. Resolver caches and returns to client."},
                    {"question": "A new laptop connects to Wi-Fi. Describe how it gets an IP.", "solution": "1. Laptop sends DHCP Discover (broadcast: 255.255.255.255). 2. DHCP server sends Offer (IP: 192.168.1.50, mask, gateway, DNS). 3. Laptop sends Request for 192.168.1.50. 4. Server sends Acknowledge. Laptop configured with IP, subnet mask, default gateway, and DNS server."},
                    {"question": "What is the difference between A record and CNAME record?", "solution": "A record: directly maps domain to IP address. Example: example.com -> 93.184.216.34. CNAME: maps alias to another domain name. Example: www.example.com -> example.com. CNAME cannot be used for root domain (naked domain)."}
                ],
            },
            {
                "title": "ARP & Network Address Translation",
                "content": "ARP (Address Resolution Protocol):\n  Resolves IP address to MAC address on a local network.\n  Needed because Ethernet frames use MAC addresses, not IP addresses.\n\nARP Process:\n  1. Host A wants to send to IP 10.0.0.2 on same network.\n  2. A checks ARP cache. If not found:\n  3. A broadcasts ARP request: 'Who has 10.0.0.2? Tell 10.0.0.1.'\n  4. Host B (10.0.0.2) responds with unicast: 'I am 10.0.0.2, my MAC is BB:BB:BB:BB:BB:BB.'\n  5. A caches the mapping and sends the Ethernet frame to MAC BB.\n\nARP Cache: Stores recent IP-MAC mappings. Entries expire after timeout.\n  arp -a (command to view ARP cache).\n\nGratuitous ARP: Host announces its own IP-MAC mapping. Used to detect IP conflicts and update caches.\n\nProxy ARP: Router answers ARP requests on behalf of hosts on other networks.\n\nNAT (Network Address Translation):\n  Translates private IPs to public IPs at the router.\n  Allows multiple devices to share one public IP.\n  Types:\n  Static NAT: One-to-one mapping (private -> public).\n  Dynamic NAT: Pool of public IPs. First-come-first-served.\n  PAT (Port Address Translation) / NAT Overload:\n    Many private IPs share one public IP. Differentiated by port numbers.\n    Most common type. Used in home routers.\n\nNAT Table Entry: (Private IP:Port) <-> (Public IP:Port).\n  Example: 192.168.1.5:5000 <-> 203.0.113.1:40001.\n\nNAT Advantages: Conserves public IPs, adds security (hides internal network).\nNAT Disadvantages: Breaks end-to-end connectivity, complicates P2P, adds latency.",
                "key_points": [
                    "ARP resolves IP to MAC on local network. Uses broadcast request, unicast reply.",
                    "NAT translates private IPs to public. PAT uses port numbers to multiplex.",
                    "PAT (NAT overload) is how home networks share one public IP",
                    "ARP only works within a LAN segment. For different networks, use router/gateway.",
                    "ARP and NAT are frequently tested in CN exams and interviews"
                ],
                "examples": [
                    {"question": "Host A (10.0.0.1) sends to Host B (10.0.0.2) on same LAN. What happens at Data Link layer?", "solution": "A needs B's MAC address. Checks ARP cache - not found. Broadcasts ARP request on LAN. B responds with its MAC. A creates Ethernet frame with src MAC=A's MAC, dst MAC=B's MAC, encapsulating the IP packet. Sends frame."},
                    {"question": "Home network: 3 devices browsing web through one public IP 203.0.113.1. How does NAT handle this?", "solution": "PAT: Device 1 (192.168.1.2:1025) -> NAT -> (203.0.113.1:40001). Device 2 (192.168.1.3:1025) -> NAT -> (203.0.113.1:40002). Device 3 (192.168.1.4:1030) -> NAT -> (203.0.113.1:40003). Return packets matched by port number in NAT table."},
                    {"question": "What is ARP spoofing?", "solution": "Attacker sends fake ARP replies claiming to be the gateway. Victim's ARP cache maps gateway IP to attacker's MAC. All traffic from victim goes through attacker (Man-in-the-Middle). Defense: static ARP entries, ARP monitoring tools, 802.1X authentication."}
                ],
            },
            {
                "title": "Encryption & SSL/TLS",
                "content": "Encryption converts plaintext to ciphertext to protect data confidentiality.\n\nSymmetric Encryption:\n  Same key for encryption and decryption.\n  Fast. Used for bulk data encryption.\n  Algorithms: AES (128/256-bit), DES (56-bit, broken), 3DES, Blowfish.\n  Problem: Key distribution (how to share key securely?).\n\nAsymmetric Encryption (Public Key):\n  Two keys: Public key (encrypt) and Private key (decrypt).\n  Slow but solves key distribution problem.\n  Algorithms: RSA, Diffie-Hellman, ECC.\n  Public key shared openly. Private key kept secret.\n  Also used for digital signatures: sign with private, verify with public.\n\nHashing (one-way function):\n  Produces fixed-size digest. Cannot reverse.\n  Algorithms: MD5 (128-bit, broken), SHA-1 (160-bit, deprecated), SHA-256, SHA-512.\n  Used for: Password storage, data integrity, digital signatures.\n\nSSL/TLS Handshake:\n  1. Client Hello: Supported cipher suites, TLS version.\n  2. Server Hello: Chosen cipher suite, server certificate.\n  3. Client verifies certificate (checks CA signature).\n  4. Key Exchange: Client generates pre-master secret, encrypts with server's public key.\n  5. Both derive session key from pre-master secret.\n  6. Encrypted communication using symmetric key (fast).\n\nDigital Certificate:\n  Contains: Owner's public key, owner info, CA signature, validity period.\n  Verified by checking CA's signature using CA's public key.\n  Chain of trust: Root CA -> Intermediate CA -> Server certificate.",
                "key_points": [
                    "Symmetric: one key, fast (AES). Asymmetric: two keys, slow (RSA). TLS uses both.",
                    "TLS handshake: asymmetric to exchange key, then symmetric for data",
                    "Hashing is one-way: MD5 and SHA-1 are broken, use SHA-256+",
                    "Digital certificates are verified through chain of trust to root CA",
                    "Encryption basics are asked in every security-related interview question"
                ],
                "examples": [
                    {"question": "Why does HTTPS use both symmetric and asymmetric encryption?", "solution": "Asymmetric is secure for key exchange but slow for bulk data. Symmetric is fast but needs secure key exchange. TLS combines both: asymmetric (RSA) to securely exchange a symmetric session key, then symmetric (AES) for fast data encryption. Best of both worlds."},
                    {"question": "How does a digital signature work?", "solution": "Sender: Hash the message (SHA-256). Encrypt hash with sender's PRIVATE key = signature. Receiver: Decrypt signature with sender's PUBLIC key = hash. Hash the received message. Compare: if equal, message is authentic and unmodified."},
                    {"question": "What happens if a server's SSL certificate expires?", "solution": "Browser shows security warning. Connection may be blocked or user must explicitly accept risk. Certificate no longer trusted because CA can't guarantee the key hasn't been compromised after expiry. Server admin must renew certificate."}
                ],
            },
            {
                "title": "Firewalls & Network Security",
                "content": "Firewall: Monitors and controls incoming/outgoing network traffic based on rules.\n\nTypes:\n  Packet Filter Firewall:\n    Examines packet headers (source/dest IP, port, protocol).\n    Stateless: Each packet evaluated independently.\n    Fast but limited. Can't detect application-layer attacks.\n\n  Stateful Firewall:\n    Tracks connection state (established, new, related).\n    More intelligent than packet filter.\n    Can block packets that don't belong to established connections.\n\n  Application Firewall (Proxy):\n    Inspects application-layer data (HTTP content, etc.).\n    Can filter based on URL, content type, etc.\n    Slower but most thorough.\n\n  Next-Generation Firewall (NGFW):\n    Combines stateful inspection + deep packet inspection + IPS.\n    Application awareness, user identity integration.\n\nCommon Network Attacks:\n  DoS/DDoS: Overwhelm server with traffic. Defense: rate limiting, CDN.\n  Man-in-the-Middle: Intercept communication. Defense: TLS, certificate pinning.\n  Phishing: Fake website/email to steal credentials. Defense: awareness, 2FA.\n  SQL Injection: Inject SQL via input fields. Defense: parameterized queries.\n  XSS: Inject malicious script into web pages. Defense: input sanitization.\n  Sniffing: Capture unencrypted traffic. Defense: encryption (TLS).\n\nIDS/IPS:\n  IDS (Intrusion Detection System): Detects attacks, alerts admin.\n  IPS (Intrusion Prevention System): Detects AND blocks attacks.\n\nVPN (Virtual Private Network):\n  Encrypted tunnel over public network. Provides privacy and security.\n  Types: Site-to-site VPN, Remote access VPN.\n  Protocols: IPSec, OpenVPN, WireGuard.",
                "key_points": [
                    "Packet filter: fast, checks headers only. Stateful: tracks connections. Application: inspects content.",
                    "Common attacks: DoS, MITM, phishing, SQL injection, XSS - know defenses for each",
                    "IDS detects, IPS detects and prevents. IPS is inline, IDS is passive.",
                    "VPN creates encrypted tunnel - essential for remote work security",
                    "Network security basics are tested in TCS, Infosys, and cybersecurity interviews"
                ],
                "examples": [
                    {"question": "Firewall rule: Block all incoming traffic on port 23 (Telnet). Why?", "solution": "Telnet transmits data in plaintext, including passwords. Blocking port 23 prevents unencrypted remote access. Use SSH (port 22) instead, which encrypts all communication."},
                    {"question": "How does a DDoS attack work? How to mitigate?", "solution": "DDoS: Thousands of compromised machines (botnet) flood target with traffic, overwhelming servers. Mitigation: CDN (distributes load), rate limiting, IP blacklisting, traffic scrubbing services (Cloudflare, AWS Shield), overprovision bandwidth."},
                    {"question": "What is the difference between symmetric and asymmetric encryption in terms of security?", "solution": "Symmetric (AES): Very fast, but requires both parties to have the same secret key. If key is intercepted, all communication is compromised. Asymmetric (RSA): Slower, but public key can be freely shared. Only private key must be secret. Even if public key is known, data can't be decrypted without private key."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "HTTP/HTTPS", "explanation": "HTTP: stateless web protocol, port 80. HTTPS: HTTP + TLS encryption, port 443. Methods: GET, POST, PUT, DELETE."},
            {"name": "DNS", "explanation": "Resolves domain names to IPs. Hierarchical: root->TLD->authoritative. Uses UDP port 53. Record types: A, CNAME, MX, NS."},
            {"name": "ARP", "explanation": "Resolves IP to MAC on local network. Broadcast request, unicast reply. ARP cache stores recent mappings."},
            {"name": "SSL/TLS", "explanation": "Encryption protocol. Handshake uses asymmetric (key exchange) then symmetric (data). Certificates verified via CA chain of trust."},
            {"name": "Firewall", "explanation": "Controls network traffic. Packet filter (headers), stateful (connection tracking), application (content inspection)."}
        ],
        "formulas": [
            "HTTP ports: HTTP=80, HTTPS=443",
            "DNS port: 53 (UDP for queries, TCP for zone transfer)",
            "DHCP ports: Server=67, Client=68",
            "FTP ports: Control=21, Data=20",
            "SSH port: 22; Telnet port: 23; SMTP port: 25"
        ],
        "solved_examples": [
            {"question": "Trace DNS resolution for mail.google.com.", "solution": "1. Query recursive resolver. 2. Root server -> referral to .com TLD. 3. .com TLD -> referral to google.com authoritative. 4. google.com authoritative returns A/CNAME for mail.google.com. If CNAME, follow to get final A record."},
            {"question": "NAT: Internal host 192.168.1.5 sends HTTP request. Public IP is 1.2.3.4.", "solution": "NAT router translates: src 192.168.1.5:5000 -> 1.2.3.4:40001. Server sees request from 1.2.3.4:40001. Server responds to 1.2.3.4:40001. NAT translates back: dst 1.2.3.4:40001 -> 192.168.1.5:5000."},
            {"question": "Why is MD5 not recommended for password hashing?", "solution": "MD5 is fast (enables brute force), has known collision vulnerabilities, and rainbow tables exist for common passwords. Use bcrypt, scrypt, or Argon2 instead - they are deliberately slow and include salt."}
        ],
        "tips": [
            "Memorize common port numbers - they appear as MCQs in every placement exam.",
            "For DNS questions, remember the resolution hierarchy: cache -> resolver -> root -> TLD -> authoritative.",
            "HTTPS = HTTP + TLS. Know the TLS handshake steps for interview discussions.",
            "Network security questions often ask about attack types and their defenses - know at least 5.",
            "ARP works only within a LAN. For cross-network, the router's MAC is used in the frame."
        ],
    },
    59: {
        "title": "OOP & Design Patterns",
        "overview": "Object-Oriented Programming (OOP) and design patterns are fundamental to software engineering. This topic covers the four pillars of OOP, SOLID principles, common design patterns (Singleton, Factory, Observer, Strategy), UML basics, and the composition vs inheritance debate. These concepts are tested in every software engineering interview at Amazon, Microsoft, Google, TCS, and Infosys.",
        "chapters": [
            {
                "title": "OOP Pillars: Encapsulation, Abstraction, Inheritance, Polymorphism",
                "content": "1. Encapsulation:\n  Bundling data and methods that operate on that data within a class.\n  Access modifiers control visibility: public, private, protected.\n  class BankAccount:\n      def __init__(self):\n          self.__balance = 0  # private\n      def deposit(self, amount):\n          if amount > 0: self.__balance += amount\n      def get_balance(self):\n          return self.__balance\n  Benefit: Data hiding, controlled access, internal changes don't break external code.\n\n2. Abstraction:\n  Hiding implementation details, showing only essential features.\n  Abstract classes and interfaces define contracts.\n  from abc import ABC, abstractmethod\n  class Shape(ABC):\n      @abstractmethod\n      def area(self): pass\n  class Circle(Shape):\n      def __init__(self, r): self.r = r\n      def area(self): return 3.14 * self.r ** 2\n  Benefit: Reduced complexity, focus on 'what' not 'how'.\n\n3. Inheritance:\n  A class (child) inherits properties and methods from another (parent).\n  class Animal:\n      def speak(self): pass\n  class Dog(Animal):\n      def speak(self): return 'Woof!'\n  Types: Single, Multiple (Python), Multilevel, Hierarchical, Hybrid.\n  Diamond Problem: Multiple inheritance ambiguity. Python uses MRO (C3 linearization).\n\n4. Polymorphism:\n  Same interface, different implementations.\n  Compile-time (overloading): Same method name, different parameters. (Not native in Python.)\n  Runtime (overriding): Subclass provides specific implementation of parent method.\n  class Cat(Animal):\n      def speak(self): return 'Meow!'\n  for a in [Dog(), Cat()]: print(a.speak())  # Woof!, Meow!",
                "key_points": [
                    "4 pillars: Encapsulation (data hiding), Abstraction (interface), Inheritance (reuse), Polymorphism (flexibility)",
                    "Encapsulation uses access modifiers: public, private (__ in Python), protected (_ in Python)",
                    "Abstraction uses abstract classes/interfaces to define contracts",
                    "Polymorphism: overloading (compile-time) vs overriding (runtime)",
                    "OOP pillars are asked in every single software engineering interview"
                ],
                "examples": [
                    {"question": "Explain polymorphism with a real-world example.", "solution": "A 'Payment' interface with method process(). CreditCard, PayPal, and UPI classes each implement process() differently. The checkout system calls payment.process() without knowing which payment type - the correct method runs based on the actual object type. This is runtime polymorphism."},
                    {"question": "What is the diamond problem? How does Python solve it?", "solution": "Class D inherits from B and C, both inherit from A. When D calls a method from A, which path? B's version or C's? Python uses MRO (Method Resolution Order) via C3 linearization: D -> B -> C -> A. The first found method in MRO is used."},
                    {"question": "Difference between abstract class and interface?", "solution": "Abstract class: can have implemented methods AND abstract methods. Can have instance variables. Single inheritance (Java). Interface: only method signatures (Java 7), can have default methods (Java 8+). Multiple interfaces allowed. Python: both are done via ABC."}
                ],
            },
            {
                "title": "SOLID Principles",
                "content": "SOLID principles guide good object-oriented design.\n\nS - Single Responsibility Principle (SRP):\n  A class should have only one reason to change.\n  Bad: class UserManager handles authentication, database, and email.\n  Good: AuthService, UserRepository, EmailService - each with one job.\n\nO - Open/Closed Principle (OCP):\n  Open for extension, closed for modification.\n  Add new behavior by creating new classes, not modifying existing ones.\n  Use inheritance/polymorphism. Example: New shape types don't require changing existing area calculation code.\n\nL - Liskov Substitution Principle (LSP):\n  Subclass objects should be substitutable for parent class objects.\n  If function works with Animal, it should work with Dog (a subclass).\n  Violation: Square extends Rectangle but setWidth/setHeight behaves differently.\n\nI - Interface Segregation Principle (ISP):\n  Clients should not depend on interfaces they don't use.\n  Bad: One fat interface with 20 methods. Not all implementors need all methods.\n  Good: Split into smaller, focused interfaces.\n  Example: Printable, Scannable, Faxable instead of one MultiFunctionDevice interface.\n\nD - Dependency Inversion Principle (DIP):\n  High-level modules should not depend on low-level modules. Both should depend on abstractions.\n  Bad: OrderService directly creates MySQLDatabase.\n  Good: OrderService depends on DatabaseInterface. MySQLDatabase implements it.\n  Enables easy swapping of implementations (MySQL -> PostgreSQL).",
                "key_points": [
                    "SRP: One class, one responsibility, one reason to change",
                    "OCP: Extend behavior via new classes, don't modify existing code",
                    "LSP: Subtypes must be substitutable for their base types",
                    "ISP: Many small interfaces > one large interface",
                    "DIP: Depend on abstractions, not concrete implementations"
                ],
                "examples": [
                    {"question": "Identify SOLID violation: class Employee has methods calculatePay(), saveToDatabase(), generateReport().", "solution": "Violates SRP. Employee has three responsibilities: payroll logic, persistence, reporting. If database schema changes, Employee class must change even though pay calculation didn't. Fix: separate into PayrollCalculator, EmployeeRepository, ReportGenerator."},
                    {"question": "How does the Strategy pattern implement OCP?", "solution": "Define a Strategy interface (e.g., SortStrategy). Create concrete strategies (BubbleSort, QuickSort, MergeSort). Context class uses SortStrategy. To add new sorting algorithm, create new class implementing SortStrategy. No existing code is modified. Open for extension (new strategies), closed for modification."},
                    {"question": "LSP violation: Square extends Rectangle. Why?", "solution": "Rectangle: setWidth(w) and setHeight(h) are independent. Square: setWidth must also set height (and vice versa) to maintain square property. Code expecting Rectangle behavior (set width without affecting height) breaks with Square. Fix: don't inherit Square from Rectangle; use a common Shape interface instead."}
                ],
            },
            {
                "title": "Creational Patterns: Singleton & Factory",
                "content": "Design Patterns: Proven solutions to common software design problems.\nCategories: Creational, Structural, Behavioral.\n\nSingleton Pattern:\n  Ensures a class has exactly one instance. Provides global access point.\n  Use cases: Database connection pool, logger, configuration manager.\n\n  class Singleton:\n      _instance = None\n      def __new__(cls):\n          if cls._instance is None:\n              cls._instance = super().__new__(cls)\n          return cls._instance\n\n  s1 = Singleton(); s2 = Singleton()\n  print(s1 is s2)  # True - same instance\n\n  Thread-safe Singleton (using lock):\n  import threading\n  class Singleton:\n      _instance = None\n      _lock = threading.Lock()\n      def __new__(cls):\n          with cls._lock:\n              if cls._instance is None:\n                  cls._instance = super().__new__(cls)\n          return cls._instance\n\nFactory Method Pattern:\n  Creates objects without specifying exact class. Subclasses decide which class to instantiate.\n\n  class Animal:\n      def speak(self): pass\n  class Dog(Animal):\n      def speak(self): return 'Woof'\n  class Cat(Animal):\n      def speak(self): return 'Meow'\n\n  class AnimalFactory:\n      @staticmethod\n      def create(animal_type):\n          if animal_type == 'dog': return Dog()\n          elif animal_type == 'cat': return Cat()\n          raise ValueError(f'Unknown: {animal_type}')\n\n  pet = AnimalFactory.create('dog')\n  print(pet.speak())  # Woof\n\nAbstract Factory: Factory of factories. Creates families of related objects.\n  Example: UIFactory creating Button, TextBox for Windows or Mac.\n\nBuilder Pattern: Constructs complex objects step by step.\n  Example: MealBuilder().addBurger().addDrink().addDessert().build()",
                "key_points": [
                    "Singleton: exactly one instance. Thread safety needed in multi-threaded apps.",
                    "Factory: encapsulates object creation. Client doesn't know concrete class.",
                    "Abstract Factory: creates families of related objects without concrete classes.",
                    "Builder: step-by-step construction of complex objects.",
                    "Singleton and Factory are the two most asked design patterns in interviews"
                ],
                "examples": [
                    {"question": "When would you use Singleton vs Factory?", "solution": "Singleton: When exactly one instance is needed (database connection, config). Factory: When you need to create different types of objects based on input, hiding creation logic. They solve different problems: Singleton controls instance count, Factory controls creation logic."},
                    {"question": "Implement a Logger as Singleton.", "solution": "class Logger: _instance = None; def __new__(cls): if not cls._instance: cls._instance = super().__new__(cls); cls._instance.log_file = open('app.log', 'a'); return cls._instance; def log(self, msg): self.log_file.write(msg + '\\n'). All parts of the application get the same Logger instance and write to the same file."},
                    {"question": "Design a NotificationFactory that creates Email, SMS, or Push notifications.", "solution": "class Notification: def send(self, msg): pass. class EmailNotif(Notification): def send(self, msg): print(f'Email: {msg}'). class SMSNotif(Notification): def send(self, msg): print(f'SMS: {msg}'). class NotifFactory: @staticmethod; def create(type): return {'email': EmailNotif, 'sms': SMSNotif, 'push': PushNotif}[type](). Usage: NotifFactory.create('email').send('Hello')."}
                ],
            },
            {
                "title": "Behavioral Patterns: Observer & Strategy",
                "content": "Observer Pattern:\n  When one object changes state, all dependent objects are notified automatically.\n  Subject (publisher) maintains list of observers (subscribers).\n  Use cases: Event systems, UI updates, notification services.\n\n  class Subject:\n      def __init__(self):\n          self._observers = []\n      def attach(self, observer):\n          self._observers.append(observer)\n      def detach(self, observer):\n          self._observers.remove(observer)\n      def notify(self, data):\n          for obs in self._observers:\n              obs.update(data)\n\n  class Observer:\n      def update(self, data): pass\n  class EmailAlert(Observer):\n      def update(self, data): print(f'Email: {data}')\n  class SMSAlert(Observer):\n      def update(self, data): print(f'SMS: {data}')\n\n  stock = Subject()\n  stock.attach(EmailAlert())\n  stock.attach(SMSAlert())\n  stock.notify('Price changed to $150')  # Both notified\n\nStrategy Pattern:\n  Define a family of algorithms, encapsulate each, make them interchangeable.\n  Client chooses algorithm at runtime.\n\n  class SortStrategy:\n      def sort(self, data): pass\n  class BubbleSort(SortStrategy):\n      def sort(self, data): # bubble sort implementation\n  class QuickSort(SortStrategy):\n      def sort(self, data): # quick sort implementation\n\n  class Sorter:\n      def __init__(self, strategy):\n          self.strategy = strategy\n      def sort(self, data):\n          return self.strategy.sort(data)\n\n  sorter = Sorter(QuickSort())\n  sorter.sort([3,1,2])  # Uses quick sort\n  sorter.strategy = BubbleSort()  # Switch at runtime\n  sorter.sort([3,1,2])  # Now uses bubble sort\n\nCommand Pattern: Encapsulates a request as an object. Supports undo, queue, logging.\nTemplate Method: Defines algorithm skeleton, subclasses fill in steps.\nIterator: Sequential access to collection elements without exposing structure.",
                "key_points": [
                    "Observer: one-to-many dependency. Subject notifies all observers on state change.",
                    "Strategy: algorithm family encapsulated and interchangeable at runtime.",
                    "Observer is used in event-driven programming, MVC, pub-sub systems.",
                    "Strategy eliminates conditional logic (if/else for algorithm selection).",
                    "Observer and Strategy are the most commonly asked behavioral patterns"
                ],
                "examples": [
                    {"question": "Real-world Observer example?", "solution": "YouTube subscription: Channel (Subject) has subscribers (Observers). When channel uploads new video, all subscribers get notified. Subscriber can unsubscribe (detach). New subscribers can join (attach). The channel doesn't need to know subscriber details."},
                    {"question": "When to use Strategy vs if-else?", "solution": "Use Strategy when: algorithms change frequently, many algorithms exist, algorithms are complex, you want to follow OCP. if-else is OK for simple, rarely changing conditions. Strategy adds classes but removes conditional complexity and makes code extensible."},
                    {"question": "Combine Observer + Strategy: Notification system.", "solution": "Subject: OrderService. Observers: NotificationManager. Strategy: NotificationManager uses different strategies (EmailStrategy, SMSStrategy) based on user preferences. When order changes, Subject notifies NotificationManager, which uses the appropriate strategy to send notification."}
                ],
            },
            {
                "title": "UML Basics & Composition vs Inheritance",
                "content": "UML (Unified Modeling Language): Visual language for software design.\n\nClass Diagram:\n  Box with 3 sections: ClassName, Attributes, Methods.\n  + public, - private, # protected.\n  Relationships:\n  Association: A uses B (solid line).\n  Aggregation: A has B (empty diamond). B can exist independently.\n    Example: Department has Employees. Employees exist without Department.\n  Composition: A owns B (filled diamond). B cannot exist without A.\n    Example: House has Rooms. Rooms don't exist without House.\n  Inheritance: A is-a B (solid line with triangle arrowhead).\n  Dependency: A uses B temporarily (dashed line with arrow).\n  Interface: Dashed line with triangle arrowhead.\n\nComposition vs Inheritance:\n  Inheritance (is-a): Dog IS-A Animal. Creates tight coupling.\n  Composition (has-a): Car HAS-A Engine. More flexible.\n\n  'Favor composition over inheritance' - Gang of Four.\n\n  Why composition is preferred:\n  1. Loose coupling: Can change Engine without changing Car.\n  2. Flexible: Can swap components at runtime.\n  3. Avoids fragile base class problem.\n  4. No diamond problem.\n  5. Better encapsulation.\n\n  When to use inheritance:\n  - True is-a relationship (Dog is-a Animal).\n  - Shared behavior across many related types.\n  - Framework requires it (Android Activity).\n\n  When to use composition:\n  - Has-a relationship (Car has-a Engine).\n  - Need to reuse behavior across unrelated types.\n  - Want runtime flexibility.\n\nDependency Injection:\n  Don't create dependencies inside class. Inject them from outside.\n  class Car:\n      def __init__(self, engine): self.engine = engine  # injected\n  car = Car(ElectricEngine())  # or DieselEngine()",
                "key_points": [
                    "Favor composition over inheritance - core OOP design principle",
                    "Aggregation: weak has-a (part can exist alone). Composition: strong has-a (part dies with whole).",
                    "UML class diagrams show relationships: association, aggregation, composition, inheritance",
                    "Dependency injection enables loose coupling and testability",
                    "UML and composition vs inheritance are common in Amazon, Microsoft design interviews"
                ],
                "examples": [
                    {"question": "Model a Library system with UML relationships.", "solution": "Library *--composition-- Shelf (shelves don't exist without library). Shelf o--aggregation-- Book (books exist independently). Book --association-- Author. Student --dependency-- Library (uses temporarily). DigitalBook --inheritance-- Book."},
                    {"question": "Refactor: class FlyingDuck extends Duck extends Bird. Problem?", "solution": "Deep inheritance hierarchy. What about RubberDuck (doesn't fly)? Override fly() to do nothing? Violates LSP. Better: composition. Duck has-a FlyBehavior. FlyingDuck gets FlyWithWings. RubberDuck gets NoFly. Strategy pattern for behaviors."},
                    {"question": "Dependency Injection: Why is 'new MySQLDB()' inside a class bad?", "solution": "Tight coupling: class depends on concrete MySQL implementation. Can't easily switch to PostgreSQL or use mock for testing. Fix: class receives DatabaseInterface via constructor. Caller decides which implementation. class OrderService: def __init__(self, db: Database): self.db = db. Now testable and flexible."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "OOP Pillars", "explanation": "Encapsulation (data hiding), Abstraction (interface), Inheritance (code reuse, is-a), Polymorphism (one interface, many forms)."},
            {"name": "SOLID Principles", "explanation": "SRP (one responsibility), OCP (extend don't modify), LSP (substitutable subtypes), ISP (small interfaces), DIP (depend on abstractions)."},
            {"name": "Singleton Pattern", "explanation": "Exactly one instance of a class. Global access point. Use for: config, logger, connection pool. Thread safety needed."},
            {"name": "Factory Pattern", "explanation": "Creates objects without specifying concrete class. Encapsulates creation logic. Client uses interface, factory decides implementation."},
            {"name": "Observer Pattern", "explanation": "One-to-many dependency. Subject notifies observers on state change. Decouples publisher from subscribers. Used in event systems."}
        ],
        "formulas": [
            "SOLID: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion",
            "Design Pattern Categories: Creational (create), Structural (compose), Behavioral (communicate)",
            "Composition over Inheritance: has-a > is-a for flexibility",
            "UML relationships: Association, Aggregation (empty diamond), Composition (filled diamond), Inheritance (triangle)",
            "Dependency Injection: pass dependencies via constructor/setter, don't create inside class"
        ],
        "solved_examples": [
            {"question": "Design a payment system using Strategy pattern.", "solution": "Interface: PaymentStrategy with method pay(amount). Concrete: CreditCardPayment, UPIPayment, NetBankingPayment. Context: PaymentProcessor(strategy). Usage: processor = PaymentProcessor(UPIPayment()); processor.pay(500). Can switch strategy at runtime."},
            {"question": "Is this good OOP? class AdminUser extends User extends Person.", "solution": "Deep inheritance chain creates fragility. Better: Person has-a Role. Role can be User, Admin, etc. Use composition: class Person: def __init__(self, role: Role). This allows changing roles at runtime and avoids the rigid hierarchy."},
            {"question": "Implement Observer for a stock price alert system.", "solution": "StockPrice (Subject): price attribute, list of investors (observers). When price changes, notify all. Investor (Observer): update(stock, price) method. Investor decides action based on price. subject.attach(investor1); subject.set_price(150) -> all notified."}
        ],
        "tips": [
            "In interviews, explain WHY you chose a pattern, not just how it works.",
            "SOLID principles are asked in every Amazon and Microsoft OOP round.",
            "Start with Singleton, Factory, Observer, Strategy - these are the top 4 patterns asked.",
            "Composition over inheritance: if in doubt, use composition. It's almost always more flexible.",
            "Draw UML class diagrams when discussing design in interviews - it shows structured thinking."
        ],
    },
    # === COMPANY SPECIFIC (Topics 60-65) ===
    60: {
        "title": "TCS NQT Preparation",
        "overview": "TCS NQT (National Qualifier Test) is the gateway to TCS for engineering graduates. It tests cognitive skills (numerical, verbal, reasoning) and optional advanced quantitative ability. Clearing NQT with a high percentile qualifies you for Ninja (~3.3 LPA) or Digital (~7 LPA) roles.",
        "chapters": [
            {
                "title": "TCS NQT Exam Pattern & Strategy",
                "content": "TCS NQT has two parts conducted online.\n\nPart 1 — Cognitive Skills (Mandatory):\n  Numerical Ability: 26 questions\n  Verbal Ability: 24 questions\n  Reasoning Ability: 30 questions\n  Duration: 90 minutes total\n  No negative marking\n\nPart 2 — Advanced Quantitative (Optional, for Digital role):\n  Higher difficulty quant questions\n  Taken separately after Part 1\n\nScoring: Percentile-based. You compete against all test-takers.\n  Ninja role: ~60th percentile cutoff\n  Digital role: ~75th percentile cutoff (varies by year)\n\nKey Strategy:\n  1. Attempt ALL questions (no negative marking)\n  2. Spend max 60-90 seconds per question\n  3. Start with your strongest section\n  4. For guessing, eliminate 2 options first, then pick\n  5. Practice 30 days of daily mock tests before the exam",
                "key_points": ["No negative marking — attempt every single question", "90 minutes for 80 questions = ~67 seconds per question", "Percentile scoring means relative performance matters", "Part 2 is only needed for Digital role (~7 LPA)", "TCS NQT is conducted multiple times a year"],
                "examples": [
                    {"question": "If TCS NQT has 80 questions in 90 minutes, what's the average time per question?", "solution": "90 minutes = 5400 seconds. 5400/80 = 67.5 seconds per question. Strategy: spend 45 sec on easy, 90 sec on medium, skip and return to hard ones."},
                    {"question": "A student scored 72nd percentile. What does this mean?", "solution": "The student scored higher than 72% of all test-takers. This is typically enough for the Ninja role cutoff but may fall short for Digital depending on the year."}
                ],
            },
            {
                "title": "TCS Numerical Ability",
                "content": "Numerical Ability is the highest-weighted section with 26 questions.\n\nMost Tested Topics (by frequency):\n  1. Number System: HCF, LCM, divisibility rules (15% of questions)\n  2. Percentages & Profit/Loss (12%)\n  3. Time & Work, Pipes & Cisterns (10%)\n  4. Time, Speed & Distance (10%)\n  5. Ratio & Proportion (8%)\n  6. Simple & Compound Interest (8%)\n  7. Averages & Ages (7%)\n  8. Permutations & Combinations (5%)\n\nSpeed Techniques:\n  Percentage shortcuts: 10% = divide by 10, 5% = half of 10%, 1% = divide by 100\n  Fraction equivalents: 1/3 = 33.33%, 1/4 = 25%, 1/5 = 20%, 1/6 = 16.67%\n  Time & Work: If A does job in x days, A's 1-day work = 1/x\n  Combined work: 1/x + 1/y = (x+y)/xy\n\nPractice Focus: Speed > accuracy for this section since there's no negative marking.",
                "key_points": ["Number system and percentages together make up ~27% of questions", "Learn fraction-to-percentage conversions by heart", "For time & work: always think in terms of 'work per day'", "Ratio problems often need cross-multiplication", "Practice mental math — no calculator allowed"],
                "examples": [
                    {"question": "A shopkeeper marks goods 40% above cost price and gives 20% discount. Find profit%.", "solution": "Let CP = 100. MP = 140. Discount = 20% of 140 = 28. SP = 140-28 = 112. Profit = 12%. Shortcut: successive % = 40-20-(40×20/100) = 40-20-8 = 12%."},
                    {"question": "A and B can do a job in 12 and 15 days. Working together, how many days?", "solution": "A's rate = 1/12, B's rate = 1/15. Combined = 1/12 + 1/15 = 5/60 + 4/60 = 9/60 = 3/20. Days = 20/3 = 6.67 days."},
                    {"question": "Train 150m long crosses a 250m bridge in 20 sec. Find speed.", "solution": "Total distance = 150+250 = 400m. Time = 20s. Speed = 400/20 = 20 m/s = 20×18/5 = 72 km/h."}
                ],
            },
            {
                "title": "TCS Verbal Ability",
                "content": "Verbal Ability has 24 questions testing English language skills.\n\nQuestion Types:\n  1. Sentence Completion (fill in blanks with correct word)\n  2. Error Spotting (identify grammatical errors)\n  3. Reading Comprehension (short passages, 3-4 questions each)\n  4. Para Jumbles (arrange sentences in correct order)\n  5. Synonyms & Antonyms\n  6. Idioms & Phrases\n\nRC Strategy:\n  Read questions first, then the passage\n  Look for keywords from questions in the passage\n  Eliminate options that are too extreme or absolute\n  'Main idea' questions: look at first and last paragraphs\n\nGrammar Quick Rules:\n  Subject-verb agreement: 'Each of the boys IS' (not are)\n  Tense consistency: don't mix past and present in same sentence\n  Pronoun reference: pronoun must clearly refer to one noun\n  Parallelism: items in a list must have same grammatical form",
                "key_points": ["RC questions are easiest — do them first", "For para jumbles: find the opening sentence (introduces topic), then link sentences with connectors", "Common error: subject-verb agreement with collective nouns", "Learn 200 common synonyms/antonyms for TCS pattern", "Idioms are tested 2-3 times — learn top 50"],
                "examples": [
                    {"question": "Spot the error: 'Each of the students have submitted their assignments on time.'", "solution": "'Each' is singular, so verb should be 'has' not 'have'. Also 'their' should be 'his/her' for strict grammar. Corrected: 'Each of the students has submitted his/her assignment on time.'"},
                    {"question": "Arrange: P-The conference was Q-attended by R-many distinguished S-scholars from abroad", "solution": "Correct order: P-Q-R-S. 'The conference was attended by many distinguished scholars from abroad.' Look for noun-verb agreement and logical flow."}
                ],
            },
            {
                "title": "TCS Reasoning Ability",
                "content": "Reasoning has the most questions (30) and is often the deciding section.\n\nHigh-Frequency Topics:\n  1. Coding-Decoding (letter/number shifting patterns)\n  2. Blood Relations (family tree mapping)\n  3. Seating Arrangement (linear and circular)\n  4. Syllogism (Venn diagram based)\n  5. Series Completion (number and letter series)\n  6. Direction Sense\n  7. Calendar & Clocks\n  8. Data Sufficiency\n\nCoding-Decoding Types:\n  Letter shifting: A→C, B→D (shift by 2)\n  Reverse alphabet: A=26, B=25, ..., Z=1\n  Number coding: Assign numbers to letters\n  Example: If COMPUTER = FQORWZHU (each +3), then DATA = GDWD\n\nBlood Relations Approach:\n  Draw family tree from given info\n  Male: +, Female: -\n  Common relationships: father's brother = uncle, mother's sister = aunt\n  'Son of my father' = brother (not necessarily me!)\n\nSeating Arrangement:\n  Linear: mark positions left to right\n  Circular: fix one person, arrange others relative\n  Use conditions to eliminate impossible arrangements",
                "key_points": ["Coding-decoding and seating arrangement appear in every TCS NQT", "For syllogism: always draw Venn diagrams, never rely on common sense", "Blood relations: systematically draw the family tree", "Series: check differences, ratios, squares, cubes, alternating patterns", "Direction problems: draw NESW compass and trace movement"],
                "examples": [
                    {"question": "If GARDEN = ICTHGS, how is FLOWER encoded?", "solution": "G(+2)=I, A(+2)=C, R(+2)=T, D(+2)=F... Wait, let me check: G→I(+2), A→C(+2), R→T(+2), D→H(+4)? No. G=7→I=9(+2), A=1→C=3(+2), R=18→T=20(+2), D=4→H=8(+4)? Pattern varies. Actually: each letter +2. FLOWER: F(+2)=H, L(+2)=N, O(+2)=Q, W(+2)=Y, E(+2)=G, R(+2)=T = HNQYGT."},
                    {"question": "A is B's sister. C is B's mother. D is C's father. How is A related to D?", "solution": "Draw tree: D (grandfather) → C (mother) → B and A (siblings). A is B's sister, so A is female. A is D's granddaughter."}
                ],
            },
            {
                "title": "TCS Coding Round & Interview",
                "content": "After clearing NQT, candidates face a coding round and interviews.\n\nCoding Round:\n  Languages: C, C++, Java, Python, Perl\n  Problems: 1-2 coding questions in 30 minutes\n  Difficulty: Easy to medium\n  Common types: String manipulation, array operations, basic math\n  Example problems: Reverse words in string, check palindrome, find factorial,\n    print Fibonacci, count vowels, sort array\n\nTechnical Interview:\n  Duration: 15-30 minutes\n  Topics: OOP concepts, DBMS basics (SQL queries), any one programming language,\n    data structures basics, project discussion\n  Common questions: What is polymorphism? Write a SQL query to find 2nd highest salary.\n    Explain your final year project. Difference between stack and queue.\n\nManagerial/HR Round:\n  Tell me about yourself (2-min structured answer)\n  Why TCS? (research TCS's recent initiatives)\n  Strengths and weaknesses\n  Are you comfortable with relocation?\n  Any questions for us?\n\nTips: Be honest, show willingness to learn, dress formally.",
                "key_points": ["Coding round: focus on getting correct output, not optimization", "Learn basic SQL: SELECT, WHERE, JOIN, GROUP BY for interviews", "Prepare a 2-minute 'Tell me about yourself' answer", "Research TCS initiatives: TCS Pace Port, TCS iON, TCS BaNCS", "TCS has 2-year service agreement — be prepared to discuss"],
                "examples": [
                    {"question": "Write code to check if a string is a palindrome.", "solution": "def is_palindrome(s):\n    s = s.lower().replace(' ', '')\n    return s == s[::-1]\n\nprint(is_palindrome('madam'))  # True\nprint(is_palindrome('hello'))  # False"},
                    {"question": "SQL: Find 2nd highest salary from Employee table.", "solution": "SELECT MAX(salary) FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee);\nOR: SELECT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1;"}
                ],
            },
        ],
        "key_concepts": [
            {"name": "NQT Scoring", "explanation": "Percentile-based. Part 1 determines Ninja role eligibility (~3.3 LPA). Part 1 + Part 2 determines Digital role (~7 LPA). No negative marking."},
            {"name": "Time Management", "explanation": "80 questions in 90 minutes = 67 seconds/question. Start with strongest section. Mark and skip hard questions, return later."},
        ],
        "formulas": [],
        "solved_examples": [
            {"question": "In TCS NQT pattern: If 20% of a number is 80, find 30% of that number.", "solution": "20% of x = 80. x = 80 × 100/20 = 400. 30% of 400 = 120."},
            {"question": "Complete the series: 2, 6, 12, 20, 30, ?", "solution": "Differences: 4, 6, 8, 10. Next difference: 12. Answer: 30 + 12 = 42. Pattern: n(n+1) where n=1,2,3,4,5,6."}
        ],
        "tips": ["No negative marking — always attempt every question", "Practice with 60-second time limit per question", "TCS NQT is conducted online — practice on a computer, not paper", "Focus on speed: learn shortcuts for percentages, ratios, time & work", "Do at least 10 full-length NQT mock tests before the exam"],
    },
    61: {
        "title": "Infosys InfyTQ Preparation",
        "overview": "Infosys uses a multi-stage hiring process: Online Test → InfyTQ Certification → Interview. The InfyTQ platform offers free courses (Python, DSA) and certification that gives shortlisting advantage. Roles include System Engineer (~3.6 LPA), SP (~5 LPA), DSE (~8 LPA).",
        "chapters": [
            {
                "title": "Infosys Exam Pattern & Roles",
                "content": "Infosys hiring has multiple tracks and stages.\n\nOnline Test Sections:\n  Quantitative Ability: 15 questions, 25 minutes\n  Logical Reasoning: 15 questions, 25 minutes\n  Verbal Ability: 20 questions, 20 minutes\n  Pseudo-coding/Programming MCQs: 10 questions, 20 minutes\n  Total: 60 questions, 90 minutes\n\nRoles & Packages:\n  SE (System Engineer): ~3.6 LPA — cleared online test + interview\n  PP (Power Programmer) / SP (Specialist Programmer): ~5 LPA — additional coding round\n  DSE (Digital Specialist Engineer): ~8 LPA — harder coding + SQL\n\nInfyTQ Certification:\n  Free online course on Python and DSA basics\n  Completing certification helps in shortlisting\n  Available on Infosys Springboard platform\n  Recommended: complete before campus placement season\n\nHackWithInfy:\n  Annual coding competition for students\n  Top performers get direct interview calls + higher packages\n  3 rounds of increasing difficulty",
                "key_points": ["60 questions in 90 minutes = 90 seconds per question (more relaxed than TCS)", "InfyTQ certification is free and boosts shortlisting chances", "SP and DSE roles have additional coding rounds", "HackWithInfy can lead to direct Power Programmer offers", "Infosys tests pseudo-code output prediction heavily"],
                "examples": [
                    {"question": "What's the key difference between SE and SP roles at Infosys?", "solution": "SE (System Engineer): general tech role, ~3.6 LPA, tested via aptitude + interview. SP (Specialist Programmer): coding-focused role, ~5 LPA, requires passing additional coding round with 3 problems in 60 minutes."}
                ],
            },
            {
                "title": "Infosys Quantitative & Logical Reasoning",
                "content": "Infosys quant and logical sections have distinct patterns.\n\nQuantitative Topics (by frequency):\n  Probability and P&C (highest weightage)\n  Number Series and Pattern Recognition\n  Data Interpretation (tables, bar graphs)\n  Time, Speed & Distance\n  Averages and Allegations\n\nUnique to Infosys — Cryptarithmetic:\n  Letters represent unique digits (0-9)\n  SEND + MORE = MONEY type problems\n  Approach:\n    1. Start with leftmost column (determines carry)\n    2. M must be 1 (only carry possible from 4-digit + 4-digit)\n    3. Work right to left, tracking carries\n    4. Each letter = unique digit\n\nLogical Reasoning Topics:\n  Arrangements (linear, circular, complex)\n  Data Sufficiency (is given info enough to answer?)\n  Pattern Recognition (visual and numerical)\n  Coding-Decoding\n  Deductive Reasoning\n\nData Sufficiency Approach:\n  Answer choices: (A) Statement 1 alone sufficient\n  (B) Statement 2 alone sufficient\n  (C) Both together sufficient\n  (D) Neither sufficient\n  Test each statement independently first",
                "key_points": ["Cryptarithmetic is uniquely tested by Infosys — practice at least 20 problems", "Probability questions are more common than in TCS NQT", "Data sufficiency: test each statement independently, then together", "Number series: check for squares, cubes, Fibonacci, alternating operations", "Practice Infosys-specific mock tests — their pattern differs from TCS"],
                "examples": [
                    {"question": "Cryptarithmetic: AB + BA = CBC. Find A, B, C.", "solution": "Units: B + A = C (or 10+C with carry). Tens: A + B + carry = 10 + B (since C is hundreds digit). If no carry from units: A + B = C and A + B = 10 + B → A = 10 (impossible). So carry = 1 from units: A + B = 10 + C and A + B + 1 = 10 + B → A = 9. Then 9 + B = 10 + C → C = B - 1. Example: A=9, B=2, C=1: 92 + 29 = 121 ✓."},
                    {"question": "Data Sufficiency: Is x > 0? (1) x² > 0. (2) x³ > 0.", "solution": "Statement 1: x² > 0 means x ≠ 0, but x could be positive or negative. NOT sufficient. Statement 2: x³ > 0 means x > 0 (cubing preserves sign). SUFFICIENT. Answer: B."}
                ],
            },
            {
                "title": "Infosys Pseudo-Coding Section",
                "content": "This section tests your ability to trace code execution without running it.\n\nQuestion Types:\n  1. Output prediction: What does this code print?\n  2. Loop tracing: Track variable values through iterations\n  3. Recursion output: Trace recursive calls\n  4. Error identification: Find the bug\n  5. Fill in the blank: Complete the code to achieve goal\n\nTracing Technique:\n  Make a table with columns for each variable\n  Track values after each statement\n  For loops: write iteration number and variable values\n  For recursion: draw call stack\n\nCommon Patterns:\n  Nested loops with counters\n  String operations using ASCII values\n  Array manipulation (reverse, rotate, search)\n  Recursive Fibonacci and factorial\n  Pointer/reference behavior (in C/C++)\n\nExample trace table:\n  i=0: x=1, y=0\n  i=1: x=1, y=1\n  i=2: x=2, y=1\n  i=3: x=3, y=2\n  Pattern: Fibonacci sequence!",
                "key_points": ["Always trace on paper — don't try to compute mentally", "Watch for off-by-one errors in loop boundaries", "For recursion: draw the call tree, then evaluate from leaves up", "ASCII values: A=65, a=97, 0=48 — memorize these", "Infosys pseudo-code is usually in C-like syntax"],
                "examples": [
                    {"question": "What is the output?\nint x = 5;\nfor(int i = 1; i <= 3; i++)\n  x = x + i;\nprint(x);", "solution": "i=1: x = 5+1 = 6. i=2: x = 6+2 = 8. i=3: x = 8+3 = 11. Output: 11."},
                    {"question": "What is the output?\ndef fun(n):\n  if n == 0: return 1\n  return n * fun(n-1)\nprint(fun(4))", "solution": "fun(4) = 4 × fun(3) = 4 × 3 × fun(2) = 4 × 3 × 2 × fun(1) = 4 × 3 × 2 × 1 × fun(0) = 4 × 3 × 2 × 1 × 1 = 24. This is factorial(4) = 24."},
                    {"question": "How many times is 'hello' printed?\nfor i in range(5):\n  for j in range(i):\n    print('hello')", "solution": "i=0: j loops 0 times. i=1: j=0 (1 time). i=2: j=0,1 (2 times). i=3: j=0,1,2 (3 times). i=4: j=0,1,2,3 (4 times). Total: 0+1+2+3+4 = 10 times."}
                ],
            },
            {
                "title": "Infosys Coding Round (SP/DSE)",
                "content": "The SP coding round has 3 problems in 60 minutes on HackerEarth.\n\nDifficulty Distribution:\n  Problem 1: Easy (array/string manipulation)\n  Problem 2: Medium (logic + implementation)\n  Problem 3: Medium-Hard (DSA knowledge helpful)\n\nCommon Problem Types:\n  String processing: anagram check, palindrome, character frequency\n  Array operations: sorting, searching, subarray problems\n  Mathematical: GCD, LCM, prime checking, factorial digits\n  Basic DP: Fibonacci variants, coin change simple version\n  Pattern printing: number/star patterns\n\nFor DSE Role (additional):\n  SQL queries: JOIN, GROUP BY, HAVING, subqueries\n  More complex coding problems\n  System design awareness\n\nCoding Tips:\n  1. Read all 3 problems first, start with easiest\n  2. Handle edge cases: empty input, single element, large values\n  3. Print output in exact format specified\n  4. Test with sample inputs before submitting\n  5. Partial solutions get partial marks — always submit something",
                "key_points": ["3 problems in 60 minutes = 20 minutes each (plan time wisely)", "Start with the easiest problem to secure marks", "Partial solutions earn partial marks — always submit", "For DSE: practice basic SQL on HackerRank", "Python is recommended for speed of coding (if available)"],
                "examples": [
                    {"question": "Check if two strings are anagrams.", "solution": "def are_anagrams(s1, s2):\n    return sorted(s1.lower()) == sorted(s2.lower())\n\nOptimized: Use Counter/frequency array.\nfrom collections import Counter\nreturn Counter(s1.lower()) == Counter(s2.lower())"},
                    {"question": "SQL: Find departments with more than 5 employees.", "solution": "SELECT department, COUNT(*) as emp_count\nFROM Employees\nGROUP BY department\nHAVING COUNT(*) > 5;"}
                ],
            },
            {
                "title": "Infosys Interview Preparation",
                "content": "Infosys interviews typically have a Technical round followed by HR.\n\nTechnical Round (20-30 min):\n  Project discussion: Explain your major project clearly\n    What problem does it solve?\n    What technologies did you use?\n    What was your specific contribution?\n    What challenges did you face?\n  OOP Concepts: 4 pillars, polymorphism types, abstraction vs encapsulation\n  DBMS: Normalization (1NF, 2NF, 3NF), basic SQL, ACID properties\n  Programming: Write simple code on paper/whiteboard\n  OS basics: Process vs thread, deadlock conditions\n\nHR Round (15-20 min):\n  Tell me about yourself\n  Why Infosys?\n  Where do you see yourself in 5 years?\n  Are you open to relocation?\n  Any gaps in education?\n  Strengths and weaknesses\n\nPreparation Checklist:\n  Prepare 2-minute self-introduction\n  Know your resume thoroughly\n  Research Infosys: InfyTQ, Springboard, Lex platform\n  Prepare 2 projects with clear STAR explanations\n  Practice HR questions aloud (not just mentally)",
                "key_points": ["Project discussion is the most important part — know every detail", "Infosys values 'learnability' — show curiosity and growth mindset", "Know at least one programming language deeply", "Research Infosys platforms: Springboard, Lex, InfyTQ", "Dress formally, maintain eye contact, speak clearly"],
                "examples": [
                    {"question": "Tell me about yourself (Infosys format).", "solution": "Structure: 1) Name and education (15 sec). 2) Technical skills and interests (30 sec). 3) Key project or achievement (45 sec). 4) Why Infosys and career goals (30 sec). Total: ~2 minutes. Example: 'I'm [Name], final year B.Tech CSE from [College]. I'm passionate about software development, skilled in Python and Java, with strong fundamentals in DSA and DBMS. My major project was [X] where I [specific contribution]. I'm excited about Infosys because of its focus on innovation and the opportunities to work on cutting-edge technologies.'"},
                    {"question": "Explain polymorphism with an example.", "solution": "Polymorphism = 'many forms'. Two types: Compile-time (method overloading: same method name, different parameters) and Runtime (method overriding: child class redefines parent's method). Example: Shape.area() — Circle overrides with πr², Rectangle with l×w. Same method name, different implementations."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "InfyTQ", "explanation": "Free certification platform by Infosys. Courses on Python and DSA. Completing certification gives advantage in shortlisting. Available on Infosys Springboard."},
            {"name": "Cryptarithmetic", "explanation": "Each letter represents a unique digit. SEND + MORE = MONEY. Solve by analyzing carries column by column, starting from the leftmost. M must be 1 (max carry from addition)."},
            {"name": "HackWithInfy", "explanation": "Annual coding competition. 3 rounds. Top performers get PP/DSE offers directly. Round 1: easy-medium. Round 2: medium-hard. Round 3: design + hard coding."},
        ],
        "formulas": [],
        "solved_examples": [
            {"question": "In Infosys pattern: What is the probability of getting at least one head in 3 coin tosses?", "solution": "P(at least one head) = 1 - P(no heads) = 1 - (1/2)³ = 1 - 1/8 = 7/8 = 0.875."},
            {"question": "Find the output: x=10; for(i=0;i<3;i++) x=x*2; print(x)", "solution": "i=0: x=20. i=1: x=40. i=2: x=80. Output: 80."},
        ],
        "tips": ["Complete InfyTQ certification before placement season", "Practice cryptarithmetic — it's Infosys's signature question type", "For pseudo-code: always trace with a variable table", "In interviews, explain projects using STAR format", "Research Infosys Springboard and mention it in HR round"],
    },
    62: {
        "title": "Wipro NLTH Preparation",
        "overview": "Wipro NLTH (National Level Talent Hunt) tests aptitude, coding, and communication. The exam is conducted on Mettl platform. Roles include Elite (~3.5 LPA) and Turbo (~6.5 LPA) based on test performance. Focus areas: quantitative aptitude, logical reasoning, coding, and written communication.",
        "chapters": [
            {
                "title": "Wipro NLTH Exam Structure",
                "content": "Wipro NLTH has a structured multi-round selection process.\n\nRound 1 — Online Aptitude Test (60 min):\n  Quantitative Ability: 16 questions\n  Logical Reasoning: 14 questions\n  Verbal Ability: 20 questions\n  Total: 50 questions, 60 minutes\n\nRound 2 — Online Coding Test (60 min):\n  2 coding problems\n  Languages: C, C++, Java (Python may not be available)\n  Platform: Mettl (get familiar with the interface)\n\nRound 3 — Written Communication (15 min):\n  Essay writing on a general topic\n  200-300 words expected\n  Evaluated for grammar, coherence, structure\n\nRound 4 — Technical Interview (15-30 min)\nRound 5 — HR Interview (10-15 min)\n\nRoles & Packages:\n  Elite: ~3.5 LPA (standard performance)\n  Turbo: ~6.5 LPA (high performance in online test)\n  Selection for Turbo based on combined aptitude + coding score",
                "key_points": ["50 aptitude questions in 60 min = 72 seconds per question", "Mettl platform — practice on Mettl before the exam", "Written communication is unique to Wipro — practice essay writing", "Python may not be available — know C/C++/Java for coding round", "Turbo role selection depends on overall online test performance"],
                "examples": [
                    {"question": "How should you distribute time in Wipro's aptitude test?", "solution": "50 questions in 60 minutes. Suggested: Verbal (20Q × 45sec = 15min), Quant (16Q × 90sec = 24min), Logical (14Q × 90sec = 21min). Start with verbal if it's your strength. This leaves buffer time."}
                ],
            },
            {
                "title": "Wipro Aptitude & Reasoning",
                "content": "Wipro's aptitude section has specific patterns.\n\nQuantitative Focus Areas:\n  Percentages and Profit/Loss (most frequent)\n  Time, Speed & Distance\n  Probability (basic)\n  Data Interpretation (bar graphs, tables)\n  Averages and Mixtures\n\nLogical Reasoning Unique Topics:\n  Venn Diagrams (VERY important for Wipro)\n    3-circle Venn diagram problems\n    'How many like only tea?' type questions\n    Formula: Only A = n(A) - n(A∩B) - n(A∩C) + n(A∩B∩C)\n\n  Input-Output (Wipro specialty):\n    Given input sequence and operation, predict output\n    Usually involves sorting with specific rules\n    Track step by step\n\n  Coding-Decoding: Similar to TCS but simpler patterns\n\n  Arrangements: Linear seating with 5-6 people\n\nVerbal Ability:\n  Reading Comprehension (2 passages)\n  Sentence Correction\n  Fill in the blanks (vocabulary)\n  Synonyms/Antonyms",
                "key_points": ["Venn diagrams are tested in EVERY Wipro exam — master 2-circle and 3-circle formulas", "Input-output problems: trace each step systematically", "Data interpretation: practice reading bar graphs and tables quickly", "Wipro verbal is moderate difficulty — focus on RC for easy marks", "Practice percentage shortcuts — they save time across all aptitude sections"],
                "examples": [
                    {"question": "In a class of 100: 60 like Cricket, 40 like Football, 20 like both. How many like only Cricket?", "solution": "Venn diagram: Only Cricket = Total Cricket - Both = 60 - 20 = 40. Only Football = 40 - 20 = 20. Neither = 100 - (40 + 20 + 20) = 20."},
                    {"question": "Wipro Input-Output: Input '25 14 36 8 42'. Step 1 sorts smallest to front. Step 2 sorts largest to back. What's Step 2?", "solution": "Step 1: 8 25 14 36 42 (8 moved to front). Step 2: 8 25 14 36 42 (42 already at back, next largest 36 moved: 8 14 25 36 42). Trace each step carefully."}
                ],
            },
            {
                "title": "Wipro Coding Round",
                "content": "Two coding problems in 60 minutes. Focus on correctness.\n\nProblem Types:\n  1. Array manipulation: rotate, reverse, find max/min, remove duplicates\n  2. String operations: count characters, reverse words, check palindrome\n  3. Mathematical: prime checking, factorial, Fibonacci, GCD\n  4. Pattern printing: pyramid, diamond, number patterns\n  5. Basic sorting: bubble sort, selection sort implementation\n\nCoding Tips for Wipro:\n  1. Read problem statement twice — understand I/O format\n  2. Handle edge cases: empty input, single element, negative numbers\n  3. Use standard I/O (scanf/printf for C, Scanner for Java)\n  4. Test with given sample inputs first\n  5. Submit even partial solutions (you may get partial marks)\n  6. Don't overthink — Wipro coding is easy-medium level\n\nCommon Mistakes:\n  - Wrong I/O format (extra spaces, missing newlines)\n  - Integer overflow for large numbers\n  - Off-by-one errors in loops\n  - Not reading the problem carefully",
                "key_points": ["2 problems in 60 min — aim to solve both", "Difficulty is easy-medium — no advanced DSA needed", "Focus on correct I/O format matching expected output", "Know at least C or Java since Python may not be available", "Pattern printing is frequently asked — practice 10 patterns"],
                "examples": [
                    {"question": "Rotate array left by k positions: arr = [1,2,3,4,5], k=2", "solution": "Method 1 (simple): temp = arr[:k], arr = arr[k:] + temp → [3,4,5,1,2]\nMethod 2 (in-place): Reverse first k, reverse rest, reverse all.\n  Reverse [1,2] → [2,1,3,4,5]\n  Reverse [3,4,5] → [2,1,5,4,3]\n  Reverse all → [3,4,5,1,2]"},
                    {"question": "Print this pattern for n=4:\n1\n12\n123\n1234", "solution": "for i in range(1, n+1):\n    for j in range(1, i+1):\n        print(j, end='')\n    print()"}
                ],
            },
            {
                "title": "Wipro Written Communication",
                "content": "Unique to Wipro — a 15-minute essay writing test.\n\nFormat:\n  Given a topic (usually general/opinion-based)\n  Write 200-300 words\n  Evaluated by AI on grammar, coherence, relevance\n\nCommon Topics:\n  Technology: 'Impact of AI on jobs', 'Social media pros and cons'\n  Education: 'Online vs offline education', 'Importance of soft skills'\n  General: 'Work-life balance', 'Role of youth in nation building'\n  Current affairs: 'Climate change solutions', 'Digital India'\n\nEssay Structure (use this template):\n  Paragraph 1 (Introduction): Define topic, state your position (3-4 sentences)\n  Paragraph 2 (Body 1): First argument with example (4-5 sentences)\n  Paragraph 3 (Body 2): Second argument or counter-argument (4-5 sentences)\n  Paragraph 4 (Conclusion): Summarize, restate position (2-3 sentences)\n\nGrammar Checklist:\n  ✓ Subject-verb agreement\n  ✓ Consistent tense (don't mix past and present)\n  ✓ No sentence fragments\n  ✓ Proper use of articles (a, an, the)\n  ✓ Vary sentence length",
                "key_points": ["15 minutes is tight — don't overthink, start writing within 2 minutes", "Structure: intro → body 1 → body 2 → conclusion", "Grammar matters more than vocabulary — keep it simple and correct", "Use connectors: However, Furthermore, In addition, On the other hand", "Practice writing 5 essays on common topics before the exam"],
                "examples": [
                    {"question": "Write opening paragraph on: 'Impact of AI on employment'", "solution": "Artificial intelligence is rapidly transforming every industry, from healthcare to finance. While some fear that AI will replace human jobs, others argue that it will create new opportunities. The reality is nuanced — AI will automate repetitive tasks but also generate demand for skills in AI development, data analysis, and human-AI collaboration. This essay examines both perspectives."}
                ],
            },
            {
                "title": "Wipro Interview Tips",
                "content": "Wipro interviews are generally straightforward.\n\nTechnical Interview (15-30 min):\n  Core topics:\n    OOP: 4 pillars, explain with real-world examples\n    DBMS: Normalization, SQL queries, ACID properties\n    One programming language in depth\n    OS: Process vs thread, deadlock (basic)\n  Project discussion: know your project end-to-end\n  Common questions:\n    What is virtual function?\n    Difference between abstract class and interface?\n    What are types of joins in SQL?\n    Explain your project architecture.\n\nHR Interview (10-15 min):\n  Tell me about yourself\n  Why Wipro?\n  Comfort with relocation\n  Are you okay with the service agreement (bond)?\n  Salary expectations (don't negotiate — fixed for freshers)\n  Where do you see yourself in 5 years?\n\nWipro-Specific Knowledge:\n  Wipro's SPIRIT values: Success, Integrity, Respect, Ingenuity, Trust\n  Wipro Holmes: AI/automation platform\n  Wipro FullStride Cloud: cloud services\n  Founder: Azim Premji\n  CEO: Thierry Delaporte (verify current)",
                "key_points": ["Technical questions are basic — not deep DSA or system design", "Know Wipro's SPIRIT values and mention them in HR round", "Service agreement is standard — show you're comfortable with commitment", "Project discussion: practice explaining in 3 minutes with STAR format", "Be prepared for 'Why not a higher-paying company?' question"],
                "examples": [
                    {"question": "Why Wipro? (sample answer)", "solution": "I admire Wipro's commitment to innovation, especially with platforms like Holmes for AI-driven solutions. Wipro's SPIRIT values, particularly integrity and trust, align with my personal principles. I'm excited about the opportunity to work on diverse projects across industries and grow professionally in a company known for its strong ethical foundation."},
                    {"question": "Difference between abstract class and interface?", "solution": "Abstract class: can have both abstract and concrete methods, supports constructors, allows member variables. Interface: all methods are abstract (until Java 8 default methods), no constructors, only constants. Use abstract class for IS-A with shared code; use interface for CAN-DO capability."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Wipro NLTH", "explanation": "National Level Talent Hunt — Wipro's campus hiring program. Multi-stage: aptitude + coding + essay + interviews. Elite (~3.5 LPA) and Turbo (~6.5 LPA) roles."},
            {"name": "Mettl Platform", "explanation": "Online assessment platform used by Wipro. Get familiar with its interface, code editor, and submission process before the actual exam."},
        ],
        "formulas": [],
        "solved_examples": [
            {"question": "Wipro Venn: 60 like A, 50 like B, 30 like C, 15 like A&B, 10 like B&C, 12 like A&C, 5 like all. How many like at least one?", "solution": "n(A∪B∪C) = n(A)+n(B)+n(C)-n(A∩B)-n(B∩C)-n(A∩C)+n(A∩B∩C) = 60+50+30-15-10-12+5 = 108."},
        ],
        "tips": ["Practice Venn diagram problems — they appear every time", "Write 5 timed essays (15 min each) before the exam", "Know C or Java for coding — Python isn't always available", "Wipro bond period: be positive about it in interviews", "Mettl practice: do at least one mock test on the Mettl platform"],
    },
    63: {
        "title": "Accenture Preparation",
        "overview": "Accenture's hiring process includes Cognitive Assessment, Coding Assessment (with SQL), and Communication Assessment (video + typing). Roles: Associate (~4.5 LPA), ASE (~6.5 LPA), Advance ASE (~11 LPA). The process is known for its communication and personality evaluation alongside technical skills.",
        "chapters": [
            {
                "title": "Accenture Exam Pattern",
                "content": "Accenture has a unique multi-format assessment.\n\nRound 1 — Cognitive Assessment (50 min):\n  English Ability: 20 questions\n  Analytical Ability: 20 questions\n  Problem Solving: 20 questions\n  Total: 60 questions, 50 minutes\n  IMPORTANT: Sections are individually timed!\n\nRound 2 — Coding Assessment (60 min):\n  2 coding problems + 1 SQL query\n  Languages: C, C++, Java, Python\n  SQL: Basic to intermediate level\n\nRound 3 — Communication Assessment:\n  Video interview: Answer behavioral questions on camera\n  Typing test: Minimum 25 WPM with accuracy\n  Evaluated by AI for clarity, confidence, grammar\n\nRound 4 — Interview (combined technical + HR):\n  Single round, 20-30 min\n  Mix of technical and behavioral questions\n\nRoles & Selection:\n  Associate Software Engineer (ASE): Standard selection\n  Advance ASE: Based on academic performance + test scores\n  Package varies: ~4.5 to ~11 LPA",
                "key_points": ["Sections are INDIVIDUALLY timed — you can't skip between sections", "Communication assessment is AI-evaluated — speak clearly to camera", "Typing test requires 25+ WPM — practice beforehand", "SQL is part of the coding assessment — learn basic queries", "Accenture values communication as much as technical skills"],
                "examples": [
                    {"question": "If Accenture gives 50 minutes for 60 questions, how much time per question?", "solution": "50 min = 3000 sec. 3000/60 = 50 seconds per question. This is tight! Strategy: English (20Q in ~12min), Analytical (20Q in ~18min), Problem Solving (20Q in ~20min)."}
                ],
            },
            {
                "title": "Accenture Cognitive Assessment",
                "content": "Three individually-timed sections testing different abilities.\n\nEnglish Ability (20Q):\n  Prepositions (in, on, at, by usage)\n  Articles (a, an, the — definite vs indefinite)\n  Active-Passive Voice conversion\n  Direct-Indirect Speech\n  Sentence Improvement/Correction\n  Tips: Focus on grammar rules, not vocabulary\n\nAnalytical Ability (20Q):\n  Data Sufficiency (most frequent)\n  Visual/Abstract Reasoning (pattern in shapes)\n  Coded Relationships ('if A>B and B>C, then...')\n  Mirror/Water Images\n  Blood Relations\n  Tips: Practice visual pattern questions — unique to Accenture\n\nProblem Solving (20Q):\n  Number Series (find next term)\n  Algebra (basic equations)\n  Probability (coin/dice/cards)\n  Geometry basics (triangles, circles)\n  Sequences with multiple operations\n  Tips: Speed matters — learn to identify patterns quickly",
                "key_points": ["English section: grammar > vocabulary for Accenture", "Visual reasoning is unique to Accenture — practice shape patterns", "Data sufficiency appears in analytical section", "Sections are timed independently — can't go back to previous section", "Practice under timed conditions to build speed"],
                "examples": [
                    {"question": "Fill in: She has been working here ___ 2019.", "solution": "Answer: 'since'. 'Since' is used with a specific point in time (2019). 'For' is used with a duration (for 5 years). 'From' is incorrect in present perfect continuous tense."},
                    {"question": "Visual pattern: Circle, Square, Triangle, Circle, Square, ?", "solution": "The pattern repeats every 3 shapes: Circle, Square, Triangle. Next: Triangle. Always look for the cycle length first."}
                ],
            },
            {
                "title": "Accenture Coding & SQL",
                "content": "Coding assessment has 2 coding problems + 1 SQL query in 60 minutes.\n\nCoding Problems:\n  Problem 1: Easy (string/array manipulation)\n  Problem 2: Medium (logic + implementation)\n\nCommon Coding Topics:\n  String operations: reverse, palindrome, character count\n  Array: sorting, searching, duplicates\n  Mathematical: prime, factorial, GCD/LCM\n  Pattern: number/star printing\n  Basic recursion\n\nSQL Query:\n  Accenture asks one SQL problem — usually worth 1/3 of coding marks!\n  Topics tested:\n    SELECT with WHERE clause\n    JOIN (INNER, LEFT, RIGHT)\n    GROUP BY with HAVING\n    Aggregate functions (COUNT, SUM, AVG, MAX, MIN)\n    Subqueries (basic)\n    ORDER BY\n\nSQL Practice:\n  Master these query patterns:\n  1. 'Find employees with salary > average salary'\n  2. 'Find department with most employees'\n  3. 'Find duplicate records'\n  4. 'Find nth highest salary'\n  5. 'Join two tables and filter results'",
                "key_points": ["SQL is essentially free marks — learn it thoroughly", "Coding difficulty is easy-medium, similar to Wipro", "Practice at least 20 SQL problems on HackerRank", "For coding: focus on correct output format", "Python is usually available — use it for faster coding"],
                "examples": [
                    {"question": "SQL: Find employees earning more than average salary.", "solution": "SELECT name, salary FROM Employee WHERE salary > (SELECT AVG(salary) FROM Employee);"},
                    {"question": "SQL: Find department with maximum employees.", "solution": "SELECT department FROM Employee GROUP BY department ORDER BY COUNT(*) DESC LIMIT 1;\nOR: SELECT department FROM Employee GROUP BY department HAVING COUNT(*) = (SELECT MAX(cnt) FROM (SELECT COUNT(*) as cnt FROM Employee GROUP BY department) t);"},
                    {"question": "Find the second most frequent character in a string.", "solution": "from collections import Counter\ndef second_frequent(s):\n    freq = Counter(s)\n    sorted_chars = sorted(freq, key=freq.get, reverse=True)\n    return sorted_chars[1] if len(sorted_chars) > 1 else None"}
                ],
            },
            {
                "title": "Accenture Communication Assessment",
                "content": "Unique to Accenture — evaluates communication skills via AI.\n\nVideo Assessment:\n  3-5 behavioral questions, 1-2 minutes per answer\n  Recorded via webcam, evaluated by AI\n  Common questions:\n    'Why do you want to join Accenture?'\n    'Describe a challenging situation and how you handled it.'\n    'What are your strengths and weaknesses?'\n    'Where do you see yourself in 5 years?'\n\nVideo Tips:\n  Look at the camera (not the screen)\n  Speak clearly at moderate pace\n  Use structured answers (STAR format)\n  Good lighting, neutral background\n  Practice with phone camera before the actual test\n  Dress formally (at least top half visible)\n\nTyping Test:\n  Minimum 25 WPM required\n  Accuracy matters as much as speed\n  Practice on typing.com or keybr.com\n  35-40 WPM is comfortable for passing\n\nAI Evaluation Criteria:\n  Clarity of speech\n  Confidence (eye contact, body language)\n  Grammar and vocabulary\n  Relevance and structure of answers",
                "key_points": ["Video is AI-evaluated — clear speech and eye contact matter most", "Practice speaking to camera with structured answers", "Typing test: 25 WPM minimum, practice to reach 35+ WPM", "Dress formally even for video assessment", "Record practice sessions and review for improvement"],
                "examples": [
                    {"question": "Video question: 'Describe a time you worked in a team to achieve a goal.'", "solution": "STAR format: Situation: 'In my 3rd year, our team had to build a project for the database course.' Task: 'I was responsible for backend and database design.' Action: 'I organized daily standups, divided tasks, helped a teammate learn SQL, and we used Git for collaboration.' Result: 'We completed the project 3 days early and scored the highest in class. I learned that clear communication and helping others builds team efficiency.'"}
                ],
            },
            {
                "title": "Accenture Interview",
                "content": "Single combined Technical + HR round, lasting 20-30 minutes.\n\nTechnical Questions:\n  OOP Basics: 4 pillars, inheritance types, polymorphism\n  DBMS: Normalization, ER diagrams, basic SQL\n  Programming: Explain code, debug, basic logic\n  Project: Detailed discussion of your main project\n  Current tech: What is cloud computing? What is AI/ML?\n\nHR/Behavioral Questions:\n  Tell me about yourself\n  Why Accenture? (research their values: Think Straight, Talk Straight)\n  Salary expectations (don't negotiate for fresher role)\n  Relocation comfort\n  Bond/service agreement acceptance\n  Any questions for the interviewer?\n\nAccenture Values to Mention:\n  Client Value Creation\n  One Global Network\n  Respect for the Individual\n  Best People\n  Integrity\n  Stewardship\n\nTips:\n  Accenture's interview is relatively easier than product companies\n  Focus on communication and confidence\n  Know your resume thoroughly — they will ask about everything on it\n  Be prepared for 'tell me about a failure' type questions",
                "key_points": ["Single combined round — both technical and HR in one sitting", "Communication and confidence matter more than deep technical knowledge", "Research Accenture's values and recent news", "Know your resume thoroughly — every line may be questioned", "Puzzles may be asked: practice 10-15 common interview puzzles"],
                "examples": [
                    {"question": "Puzzle: How many times do clock hands overlap in 24 hours?", "solution": "In 12 hours, hands overlap 11 times (not 12, because at 12:00 they start together and the next overlap is around 1:05). In 24 hours: 11 × 2 = 22 times."},
                    {"question": "What is cloud computing? (Accenture interview)", "solution": "Cloud computing delivers computing services (servers, storage, databases, networking) over the internet. Types: IaaS (infrastructure), PaaS (platform), SaaS (software). Examples: AWS, Azure, Google Cloud. Benefits: scalability, cost-efficiency, global access. Accenture's cloud practice helps companies migrate to and optimize cloud infrastructure."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Accenture Assessment", "explanation": "Three distinct assessments: Cognitive (timed sections), Coding (2 problems + SQL), Communication (video + typing). Each evaluates different skills."},
            {"name": "AI Video Evaluation", "explanation": "Accenture uses AI to evaluate video responses. Factors: clarity, confidence, eye contact, grammar, answer structure. Practice speaking to camera."},
        ],
        "formulas": [],
        "solved_examples": [
            {"question": "Accenture SQL: Find names of employees who earn more than their manager.", "solution": "SELECT e.name FROM Employee e JOIN Employee m ON e.manager_id = m.id WHERE e.salary > m.salary;"},
        ],
        "tips": ["Sections are individually timed — practice each section separately", "SQL is the easiest marks in coding round — don't skip it", "For video: practice with Pramp or record yourself answering questions", "Typing practice: reach 35+ WPM on keybr.com before the test", "Research Accenture's latest acquisitions and service offerings"],
    },
    64: {
        "title": "Amazon SDE Preparation",
        "overview": "Amazon SDE (Software Development Engineer) hiring is highly competitive. The process involves an Online Assessment (OA) with 2 coding problems, followed by 4-5 onsite/virtual interview loops. Amazon uniquely evaluates Leadership Principles (LPs) alongside technical skills. SDE-1 package: ~30-45 LPA (campus).",
        "chapters": [
            {
                "title": "Amazon Hiring Process",
                "content": "Amazon's SDE hiring has distinct stages.\n\nStage 1 — Resume Screening:\n  Strong DSA projects, competitive programming, open source\n  CGPA cutoff varies (usually 7.0+)\n  Referrals help get past screening\n\nStage 2 — Online Assessment (OA):\n  2 coding problems in 70 minutes\n  Difficulty: LeetCode Medium to Hard\n  Work Simulation: Multiple-choice LP-based scenarios\n  Platform: Amazon's own assessment tool\n\nStage 3 — Phone Screen (sometimes):\n  45 min: 1 coding problem + LP questions\n  Code on shared editor (CoderPad/Amazon Chime)\n\nStage 4 — Onsite/Virtual Interviews:\n  4-5 loops, each 45-60 minutes\n  Each loop: 30 min coding + 15 min LP questions\n  One loop is 'Bar Raiser' (most important)\n  Bar Raiser evaluates LP depth and culture fit\n\nTimeline:\n  Campus: August-November\n  Off-campus: Year-round\n  Result: Usually within 5 business days\n\nRoles:\n  SDE-1: Entry level (~30-45 LPA total compensation)\n  Includes base salary + signing bonus + RSUs (stocks)",
                "key_points": ["OA has 2 coding problems + work simulation (LP scenarios)", "Bar Raiser interview is the most important loop", "Each interview loop has both coding AND LP questions", "Amazon offers ~30-45 LPA for SDE-1 (base + bonus + stocks)", "Practice LeetCode Amazon-tagged problems (aim for 150+ solved)"],
                "examples": [
                    {"question": "How is Amazon's interview structure different from service companies?", "solution": "Service companies (TCS, Infosys): aptitude test → 1 technical interview → HR. Amazon: OA (hard coding) → 4-5 technical loops with coding + Leadership Principles in each. Every interviewer independently evaluates. All must agree to hire ('hire bar'). Much more rigorous."}
                ],
            },
            {
                "title": "Amazon OA & Coding Preparation",
                "content": "The OA is your first filter — prepare thoroughly.\n\nOA Problem Patterns (most common):\n  1. Two Pointer / Sliding Window\n  2. BFS/DFS on Graphs (connected components, shortest path)\n  3. Dynamic Programming (medium level)\n  4. Greedy Algorithms (activity selection, intervals)\n  5. Tree problems (traversals, LCA, path sum)\n  6. String manipulation with HashMap\n\nTop 20 Amazon-Asked Problems:\n  Two Sum, 3Sum, Container With Most Water\n  LRU Cache, Meeting Rooms II\n  Number of Islands, Word Ladder\n  Merge Intervals, Insert Interval\n  Longest Substring Without Repeating Characters\n  Top K Frequent Elements\n  Course Schedule (topological sort)\n  Word Break, Coin Change\n  Trapping Rain Water\n  Serialize/Deserialize Binary Tree\n\nWork Simulation:\n  16 scenario-based questions\n  Choose the MOST and LEAST effective action\n  Based on Amazon Leadership Principles\n  Example: 'A team member misses a deadline. What do you do?'\n  Think: what would Amazon want? (Ownership, Dive Deep)\n\nCoding Approach:\n  1. Clarify requirements (5 min)\n  2. Discuss approach and complexity (5 min)\n  3. Code cleanly (20 min)\n  4. Test with examples (5 min)\n  5. Optimize if time permits",
                "key_points": ["LeetCode Medium-Hard is the target difficulty", "BFS/DFS and DP are the most common problem categories", "Work simulation evaluates Leadership Principles — study all 16 LPs", "Write clean, readable code — variable names matter", "Always discuss time and space complexity before coding"],
                "examples": [
                    {"question": "Number of Islands: Given a 2D grid of '1's (land) and '0's (water), count islands.", "solution": "BFS/DFS approach: For each unvisited '1', start BFS/DFS to mark all connected '1's as visited. Increment island count.\ndef numIslands(grid):\n    count = 0\n    for i in range(len(grid)):\n        for j in range(len(grid[0])):\n            if grid[i][j] == '1':\n                dfs(grid, i, j)  # mark connected as '0'\n                count += 1\n    return count\nTime: O(M×N), Space: O(M×N) for recursion stack."},
                    {"question": "Merge Intervals: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]", "solution": "Sort by start time. Iterate: if current.start <= prev.end, merge (extend end to max). Else, add new interval.\nintervals.sort()\nmerged = [intervals[0]]\nfor s, e in intervals[1:]:\n    if s <= merged[-1][1]:\n        merged[-1][1] = max(merged[-1][1], e)\n    else:\n        merged.append([s, e])\nTime: O(n log n), Space: O(n)."}
                ],
            },
            {
                "title": "Amazon Leadership Principles",
                "content": "Amazon's 16 Leadership Principles are evaluated in EVERY interview loop.\n\nTop LPs Asked (in order of frequency):\n  1. Customer Obsession: Start with customer, work backwards\n  2. Ownership: Think long-term, never say 'that's not my job'\n  3. Dive Deep: Operate at all levels, stay connected to details\n  4. Bias for Action: Speed matters, calculated risk-taking\n  5. Deliver Results: Focus on key inputs, deliver with quality\n  6. Earn Trust: Be honest, benchmark yourself against the best\n  7. Insist on Highest Standards: Continuously raise the bar\n  8. Learn and Be Curious: Always be learning, explore new possibilities\n\nOther LPs:\n  Invent and Simplify, Are Right A Lot, Hire and Develop the Best,\n  Think Big, Frugality, Have Backbone (Disagree and Commit),\n  Strive to be Earth's Best Employer, Success and Scale Bring Responsibility\n\nSTAR Method for LP Answers:\n  Situation: Set the context (2-3 sentences)\n  Task: Your specific responsibility (1-2 sentences)\n  Action: What YOU did (detail, 4-5 sentences)\n  Result: Measurable outcome (2-3 sentences)\n\nKey: Prepare 2-3 unique STAR stories per LP. Total: ~15 polished stories.\nEach story can cover multiple LPs with different emphasis.",
                "key_points": ["Prepare 15+ polished STAR stories covering all major LPs", "Customer Obsession, Ownership, and Dive Deep are asked most frequently", "Use 'I' not 'we' — Amazon wants to know YOUR specific contribution", "Quantify results: 'reduced latency by 40%' not 'improved performance'", "Bar Raiser specifically probes LP depth — superficial answers won't pass"],
                "examples": [
                    {"question": "Tell me about a time you took ownership beyond your role. (Ownership LP)", "solution": "STAR: Situation: 'During our college project, the frontend developer dropped out a week before submission.' Task: 'As the backend developer, the frontend wasn't my responsibility, but the project grade depended on it.' Action: 'I spent 3 nights learning React basics, used templates to build a functional UI, and integrated it with my backend API. I also documented the setup process for the team.' Result: 'We submitted on time, scored 92%, and the professor highlighted our project as best in class. I also gained frontend skills I now use regularly.'"},
                    {"question": "Tell me about a time you disagreed with a team member. (Have Backbone LP)", "solution": "STAR: Situation: 'In a hackathon, my teammate wanted to use a complex microservices architecture for our 24-hour project.' Task: 'I believed a simpler monolithic approach was better for the time constraint.' Action: 'I respectfully presented my reasoning with a time estimate for each approach, showing microservices would take 20+ hours just for setup. I proposed we could refactor to microservices later if we won.' Result: 'Team agreed. We finished in 18 hours, won 2nd place. The judge praised our working demo over teams with ambitious but incomplete architectures.'"}
                ],
            },
            {
                "title": "Amazon Coding Interview Deep Dive",
                "content": "Each onsite loop has 30 minutes of coding. Here's how to excel.\n\nInterview Flow:\n  0-5 min: Introduction, problem statement\n  5-10 min: Clarifying questions, discuss approach\n  10-35 min: Code on whiteboard/shared editor\n  35-40 min: Test with examples, discuss optimization\n  40-45 min: LP questions (1-2 questions)\n\nMust-Know Data Structures:\n  Arrays, Strings, HashMaps (most common)\n  Trees (BST, Binary Tree) — LCA, traversals, path problems\n  Graphs — BFS, DFS, topological sort\n  Stacks, Queues, Heaps (priority queue)\n  Linked Lists — reverse, cycle detection, merge\n\nMust-Know Algorithms:\n  Binary Search and its variants\n  Two Pointer technique\n  Sliding Window\n  BFS/DFS\n  Dynamic Programming (1D and 2D)\n  Sorting (merge sort, quick sort)\n  Greedy algorithms\n\nCommunication During Coding:\n  Think aloud — explain your reasoning as you code\n  If stuck, explain what you're thinking, not silence\n  Ask for hints gracefully: 'I'm considering approach X, does that seem reasonable?'\n  After coding, trace through with a small example\n  Proactively discuss edge cases",
                "key_points": ["Think aloud — silence is the biggest red flag in Amazon interviews", "Always start with brute force, then optimize", "Discuss time/space complexity for every solution", "Trees and graphs appear in nearly every Amazon loop", "Test your code with examples before saying 'done'"],
                "examples": [
                    {"question": "LRU Cache: Design O(1) get and put operations.", "solution": "Use HashMap + Doubly Linked List. HashMap: key → node for O(1) lookup. DLL: maintains order (most recent at head, least recent at tail).\nget(key): if in map, move node to head, return value. Else -1.\nput(key, val): if exists, update + move to head. Else create node at head, add to map. If over capacity, remove tail node from DLL and map.\nTime: O(1) for both operations. Space: O(capacity)."},
                    {"question": "Course Schedule: Can you finish all courses given prerequisites?", "solution": "Topological sort using BFS (Kahn's algorithm). Build adjacency list + in-degree array. Add all nodes with in-degree 0 to queue. Process: remove from queue, reduce neighbors' in-degree, add new 0-degree nodes. If processed count == total courses, possible.\nTime: O(V+E), Space: O(V+E)."}
                ],
            },
            {
                "title": "Amazon System Design & Tips",
                "content": "System design knowledge expected varies by level.\n\nSDE-1 (New Grad):\n  Low-Level Design (OOP-based)\n  Design parking lot, library management, elevator system\n  Focus: classes, interfaces, design patterns, SOLID\n  Example: 'Design a URL shortener'\n    Classes: URLShortener, URLMapping, Analytics\n    Database: key-value store (key=short_code, value=long_url)\n    Algorithm: base62 encoding of auto-increment ID\n    API: POST /shorten, GET /{short_code}\n\nSDE-2+ (Experienced):\n  High-Level System Design\n  Design Instagram, Netflix, Uber\n  Topics: load balancing, caching, database sharding, CDN\n\nGeneral Tips:\n  1. Apply to Amazon early — interviews fill up fast\n  2. If you fail OA, you can reapply after 6 months\n  3. Amazon's bar is high — only ~1% of applicants get offers\n  4. Mock interviews are essential — practice with peers or Pramp\n  5. Don't memorize solutions — understand patterns\n  6. Sleep well before interviews — stamina matters for 4-5 loops\n\nNegotiation:\n  Amazon's compensation has 4 components: base, signing bonus, RSUs, relocation\n  RSUs vest over 4 years (5%, 15%, 40%, 40%)\n  Don't negotiate aggressively for new grad — offers are fairly standard",
                "key_points": ["SDE-1: focus on OOP/LLD design, not distributed systems", "Amazon interviews are 4-5 loops in one day — build stamina", "Only ~1% of applicants get offers — prepare thoroughly", "Mock interviews are the best preparation — do at least 10", "RSU vesting: 5/15/40/40 over 4 years — understand your compensation"],
                "examples": [
                    {"question": "Design a URL shortener (SDE-1 level).", "solution": "API: POST /api/shorten {long_url} → {short_url}. GET /{code} → redirect to long_url.\nDatabase: Table(id, short_code, long_url, created_at).\nAlgorithm: Use auto-increment ID, convert to base62 (a-z, A-Z, 0-9). ID 1000 → base62 = 'g8'. 6-char code supports 62^6 = 56 billion URLs.\nClasses: URLService(shorten, redirect), Base62Encoder, URLRepository.\nAdditional: analytics tracking, expiry, rate limiting."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Leadership Principles", "explanation": "Amazon's 16 cultural tenets evaluated in every interview. Top 3: Customer Obsession, Ownership, Dive Deep. Prepare STAR stories for each."},
            {"name": "Bar Raiser", "explanation": "Special interviewer from a different team. Ensures hiring bar stays high. Focuses on LP depth and long-term potential. Has veto power."},
            {"name": "STAR Method", "explanation": "Situation-Task-Action-Result. Amazon's expected format for behavioral answers. Focus on 'Action' (what YOU did) and 'Result' (quantifiable outcome)."},
        ],
        "formulas": [],
        "solved_examples": [
            {"question": "Two Sum: Given array and target, find two indices that sum to target.", "solution": "HashMap approach: for each num, check if (target - num) exists in map. If yes, return indices. Else, add num:index to map.\ndef twoSum(nums, target):\n    seen = {}\n    for i, n in enumerate(nums):\n        if target - n in seen:\n            return [seen[target-n], i]\n        seen[n] = i\nTime: O(n), Space: O(n)."},
        ],
        "tips": ["Solve 150+ LeetCode problems (focus on Amazon-tagged medium)", "Prepare 15+ STAR stories covering different Leadership Principles", "Practice coding on whiteboard/paper — not just IDE", "Mock interviews: do at least 10 with peers or on Pramp", "Study LPs as seriously as DSA — they carry equal weight"],
    },
    65: {
        "title": "Microsoft SDE Preparation",
        "overview": "Microsoft SDE hiring involves Online Coding Test, Group Fly Round (pen-paper coding), and 3-4 technical interviews. Microsoft evaluates problem solving, coding quality, design thinking, and growth mindset. SDE package: ~40-47 LPA (campus) including base + stocks. Microsoft loves tree, graph, and design problems.",
        "chapters": [
            {
                "title": "Microsoft Hiring Process",
                "content": "Microsoft's campus hiring has distinctive rounds.\n\nStage 1 — Online Coding Test:\n  3 coding problems in 90 minutes\n  Platform: Codility or similar\n  Difficulty: LeetCode Easy-Medium\n  Used as initial filter\n\nStage 2 — Group Fly Round:\n  20-30 shortlisted candidates in a room\n  Pen and paper coding (no laptop!)\n  1-2 problems in 30 minutes\n  Interviewers walk around observing\n  ~50% elimination rate\n  Tips: Write clean code, proper syntax, test with examples\n\nStage 3 — Technical Interviews (3-4 rounds):\n  Each round: 45-60 minutes\n  Round 1: Data Structures & Algorithms\n  Round 2: Problem Solving (harder)\n  Round 3: System Design / OOP Design\n  Round 4: Hiring Manager (technical + behavioral)\n\nEach round is progressively harder\nAll interviewers submit independent feedback\nHiring manager makes final call\n\nPackage:\n  Base salary: ~18-22 LPA\n  Stocks: ~15-20 LPA (vest over 4 years)\n  Signing bonus: ~5-7 LPA\n  Total: ~40-47 LPA for SDE (campus)",
                "key_points": ["Group Fly is unique to Microsoft — practice writing code on paper", "3-4 interview rounds with increasing difficulty", "Microsoft offers ~40-47 LPA total compensation for campus SDE", "Design round tests OOP/LLD, not distributed systems for new grads", "Hiring manager round is both technical and behavioral"],
                "examples": [
                    {"question": "How is Microsoft's Group Fly different from a normal coding test?", "solution": "Group Fly: pen-and-paper coding with interviewers watching. No IDE, no auto-complete, no running code. They evaluate: code correctness, clarity, approach discussion, how you handle being stuck. Tips: practice writing syntactically correct code on paper, use proper indentation, add comments."}
                ],
            },
            {
                "title": "Microsoft Coding Preparation",
                "content": "Microsoft's coding interviews focus on specific patterns.\n\nMost Asked Topics (in order):\n  1. Trees (BST, Binary Tree) — Microsoft's favorite!\n     LCA, diameter, path sum, serialize/deserialize\n     Level-order, zigzag traversal, views (left, right, top)\n  2. Arrays & Strings — two pointer, sliding window\n  3. Linked Lists — reverse, merge, cycle, LRU\n  4. Graphs — BFS, DFS, connected components\n  5. Dynamic Programming — medium level\n  6. Design Data Structures — implement stack/queue/map\n\nTop Microsoft-Asked Problems:\n  Reverse a Linked List\n  LCA of Binary Tree\n  Diameter of Binary Tree\n  Validate BST\n  Merge K Sorted Lists\n  Design MinStack (push, pop, top, getMin in O(1))\n  Spiral Matrix Traversal\n  Clone Graph\n  Longest Palindromic Substring\n  Median of Two Sorted Arrays\n\nCoding Quality Matters:\n  Microsoft values clean, readable code\n  Use meaningful variable names (not i, j, k for everything)\n  Add brief comments for complex logic\n  Handle edge cases explicitly\n  Discuss multiple approaches before coding",
                "key_points": ["Trees are Microsoft's #1 topic — solve 30+ tree problems on LeetCode", "Know how to write code on paper (Group Fly) — syntax must be correct", "Microsoft evaluates code quality, not just correctness", "Practice: LCA, tree diameter, BST validation, views — these repeat", "Design data structure problems (MinStack, LRU Cache) are frequently asked"],
                "examples": [
                    {"question": "LCA of Binary Tree: Find lowest common ancestor of nodes p and q.", "solution": "Recursive: if root is None or root==p or root==q, return root. Search left and right subtrees. If both return non-None, root is LCA. If only one returns non-None, that's the LCA.\ndef lca(root, p, q):\n    if not root or root == p or root == q:\n        return root\n    left = lca(root.left, p, q)\n    right = lca(root.right, p, q)\n    if left and right: return root\n    return left or right\nTime: O(n), Space: O(h)."},
                    {"question": "Design MinStack: push, pop, top, getMin all in O(1).", "solution": "Use two stacks: main stack + min stack. min_stack always has current minimum at top.\npush(x): main.push(x). If x <= min_stack.top(), min_stack.push(x).\npop(): if main.top() == min_stack.top(), min_stack.pop(). main.pop().\ngetMin(): return min_stack.top().\nAlternative: store (value, current_min) tuples in single stack."}
                ],
            },
            {
                "title": "Microsoft Design Round",
                "content": "For SDE (new grad), Microsoft tests Low-Level Design (LLD/OOP).\n\nCommon LLD Problems:\n  1. Design Chess Game\n  2. Design Elevator System\n  3. Design Parking Lot\n  4. Design Tic-Tac-Toe\n  5. Design File System\n  6. Design Library Management System\n  7. Design Snake Game\n\nApproach for LLD:\n  1. Clarify requirements (2 min)\n  2. Identify classes/objects (5 min)\n  3. Define relationships (HAS-A, IS-A) (3 min)\n  4. Write key interfaces and classes (15 min)\n  5. Discuss design patterns used (5 min)\n\nDesign Patterns to Know:\n  Singleton: Game instance, Logger\n  Factory: Piece creation in chess, Vehicle in parking\n  Strategy: Payment methods, Move validation\n  Observer: Event notification, Elevator updates\n  State: Elevator states (idle, moving, door_open)\n\nSOLID in Design:\n  Show Single Responsibility: separate Board, Piece, Game classes\n  Show Open/Closed: new piece types without modifying existing code\n  Show Dependency Inversion: depend on interfaces, not concrete classes",
                "key_points": ["Practice top 5 LLD problems — they cover most patterns", "Start with identifying classes and their responsibilities", "Use design patterns naturally — don't force them", "Draw class diagrams to communicate your design", "SOLID principles should be evident in your design"],
                "examples": [
                    {"question": "Design a Parking Lot system.", "solution": "Classes: ParkingLot (singleton), Floor, ParkingSpot (types: Compact, Large, Handicapped), Vehicle (Car, Truck, Motorcycle), Ticket, Payment.\nRelationships: ParkingLot has Floors. Floor has ParkingSpots. Vehicle parks in ParkingSpot.\nKey methods: parkVehicle(vehicle) → Ticket, unpark(ticket) → Payment.\nPatterns: Singleton (ParkingLot), Factory (VehicleFactory), Strategy (PricingStrategy: hourly, daily, monthly).\nEdge cases: full parking, wrong spot type, payment failure."},
                    {"question": "Design Tic-Tac-Toe with O(1) move validation.", "solution": "Instead of checking entire board after each move, maintain row_count, col_count, diag_count, anti_diag_count arrays. Each player contributes +1 or -1. If any count reaches ±n, that player wins.\nClasses: Game, Board, Player. Board has move(row, col, player) that returns winner or None. O(1) per move check instead of O(n²)."}
                ],
            },
            {
                "title": "Microsoft Behavioral & Culture",
                "content": "Microsoft evaluates 'Growth Mindset' — their core cultural value.\n\nGrowth Mindset (CEO Satya Nadella's philosophy):\n  Learn from failures, not just successes\n  Embrace challenges as opportunities\n  Effort is the path to mastery\n  'Learn-it-all' > 'Know-it-all'\n\nBehavioral Questions:\n  1. Tell me about a time you failed and what you learned.\n  2. How do you handle disagreements with teammates?\n  3. Describe the hardest bug you've fixed.\n  4. How do you learn new technologies?\n  5. Tell me about a time you helped someone on your team.\n\nAnswer Format:\n  Use STAR method but emphasize learning and growth\n  Microsoft wants to see: humility, curiosity, collaboration\n  Don't just describe what happened — reflect on what you learned\n\nMicrosoft-Specific Knowledge:\n  Azure (cloud platform)\n  VS Code (development tool)\n  GitHub (acquired by Microsoft)\n  LinkedIn (owned by Microsoft)\n  Microsoft 365, Teams\n  AI: Copilot, Azure OpenAI Service\n\nHiring Manager Round:\n  Final round, most senior interviewer\n  Mix of technical + behavioral + career goals\n  May ask: 'Why Microsoft over Google/Amazon?'\n  Key: show genuine interest in Microsoft's mission",
                "key_points": ["Growth mindset is THE core value — every answer should show learning", "Failure stories are valued — show you grew from the experience", "'Learn-it-all' mentality over 'know-it-all'", "Research Microsoft's recent AI initiatives (Copilot, Azure OpenAI)", "Hiring manager round: show long-term thinking about your career"],
                "examples": [
                    {"question": "Tell me about a time you failed. (Growth Mindset)", "solution": "STAR: Situation: 'In a coding competition, I tried to implement a complex graph algorithm I'd only read about.' Task: 'I needed to solve the problem within the time limit.' Action: 'I spent 2 hours on the complex approach and couldn't debug it. I realized I should have started with a simpler BFS that would have gotten 70% test cases.' Result: 'I scored 0 on that problem. Lesson learned: start simple, optimize later. I now always implement brute force first. This approach helped me in the next competition where I solved all problems.'"},
                    {"question": "Why Microsoft? (sample answer)", "solution": "'I'm drawn to Microsoft's mission to empower every person and organization. As a developer, I use VS Code and GitHub daily — products that genuinely improve developer productivity. Microsoft's growth mindset culture, pioneered by Satya Nadella, aligns with how I approach learning. I'm especially excited about the AI innovations with Copilot and Azure OpenAI, and I want to contribute to tools that millions of developers rely on.'"}
                ],
            },
            {
                "title": "Microsoft Tips & Final Prep",
                "content": "Practical tips for Microsoft interview success.\n\nGroup Fly Preparation:\n  Practice writing code on paper for 2 weeks before\n  Syntax must be correct — no squiggly lines to auto-fix\n  Write clearly and legibly\n  Use proper indentation\n  Start with approach, then code, then test with example\n  If stuck, show your thinking — interviewers observe problem-solving\n\nInterview Day Tips:\n  Arrive early, dress smart casual (Microsoft is less formal)\n  Each round: new interviewer, fresh start\n  Ask clarifying questions — interviewers expect this\n  Think aloud — explain your reasoning\n  If given a hint, take it gracefully and build on it\n  After coding, trace through your code with an example\n  Mention edge cases even if you don't code them all\n\nPreparation Timeline (4 weeks):\n  Week 1-2: LeetCode Medium (focus on trees, arrays, strings)\n  Week 3: LLD practice + mock interviews\n  Week 4: Behavioral prep + review\n  Daily: 2-3 LeetCode problems + 1 LLD session\n\nMock Interviews:\n  Practice with peers, Pramp, or interviewing.io\n  Simulate real conditions: 45 min, no IDE\n  Get feedback on communication, not just correctness\n\nExplore Program:\n  Microsoft Explore: for freshman/sophomore interns\n  Rotation across PM, Design, and SDE\n  Great way to get early Microsoft experience",
                "key_points": ["Group Fly: practice writing code on paper with correct syntax", "Microsoft dress code: smart casual (less formal than consulting firms)", "Tree problems repeat — LCA, diameter, views, path sum — know them cold", "Mock interviews with peers are the #1 preparation method", "4-week prep plan: 2 weeks DSA, 1 week design, 1 week behavioral"],
                "examples": [
                    {"question": "Paper coding: Write binary search for a sorted array.", "solution": "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = left + (right - left) // 2  # avoid overflow\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n\n# Test: arr = [1,3,5,7,9], target = 5\n# left=0, right=4, mid=2, arr[2]=5=target → return 2 ✓"},
                    {"question": "What to do if you're stuck in a Microsoft interview?", "solution": "1) Don't panic — take a breath. 2) Explain what you're thinking: 'I'm considering X approach but I'm not sure about Y.' 3) Relate to a similar problem: 'This reminds me of [pattern].' 4) Ask for a hint: 'Could you point me in the right direction?' 5) Work through a smaller example. Interviewers want to see your problem-solving process, not just the answer."}
                ],
            },
        ],
        "key_concepts": [
            {"name": "Growth Mindset", "explanation": "Microsoft's core culture value. Learn from failures, embrace challenges, believe in improvement through effort. Show this in every behavioral answer."},
            {"name": "Group Fly", "explanation": "Pen-and-paper coding round with 20-30 candidates. Interviewers observe coding approach, clarity, and problem-solving. ~50% elimination. Practice writing code by hand."},
            {"name": "Bar for SDE", "explanation": "Microsoft evaluates: coding ability, problem-solving approach, design thinking, communication, and growth mindset. All must be above bar. No single weak area is acceptable."},
        ],
        "formulas": [],
        "solved_examples": [
            {"question": "Diameter of Binary Tree (Microsoft favorite).", "solution": "Diameter = longest path between any two nodes (may not pass through root).\ndef diameter(root):\n    self.ans = 0\n    def depth(node):\n        if not node: return 0\n        L = depth(node.left)\n        R = depth(node.right)\n        self.ans = max(self.ans, L + R)\n        return max(L, R) + 1\n    depth(root)\n    return self.ans\nTime: O(n), Space: O(h). At each node, diameter through it = left_depth + right_depth."},
        ],
        "tips": ["Trees are Microsoft's #1 topic — solve all LeetCode tree mediums", "Practice writing code on paper for Group Fly — correct syntax is essential", "Growth mindset: frame failures as learning opportunities in every behavioral answer", "Mock interviews are essential — do at least 10 before the actual interview", "Research Microsoft's AI strategy (Copilot, Azure) and mention it in 'Why Microsoft?'"],
    },
}
