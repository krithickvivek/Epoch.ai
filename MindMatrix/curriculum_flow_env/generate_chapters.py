"""
Generate 5-chapter structure for all 40 topics.
Converts existing study_content.py into chapter-based format with detailed content.
Run: python generate_chapters.py
"""

import json

# Chapter templates for each topic category
CHAPTER_TEMPLATES = {
    # QUANTITATIVE APTITUDE (0-11)
    0: [  # Numbers
        {"title": "Types of Numbers & Classification",
         "content": "The number system forms the bedrock of quantitative aptitude. Understanding the classification of numbers is essential for placement exams.\n\nNatural Numbers (N): The counting numbers 1, 2, 3, 4, ... are called natural numbers. The set does not include 0 or negative numbers.\n\nWhole Numbers (W): When we include 0 with natural numbers, we get whole numbers: 0, 1, 2, 3, ...\n\nIntegers (Z): The set of all positive and negative whole numbers including zero: ..., -3, -2, -1, 0, 1, 2, 3, ...\n\nRational Numbers (Q): Numbers that can be expressed as p/q where p and q are integers and q ≠ 0. Examples: 1/2, -3/4, 0.75 (which is 3/4). All terminating and repeating decimals are rational.\n\nIrrational Numbers: Numbers that cannot be expressed as p/q. Their decimal expansion is non-terminating and non-repeating. Examples: √2 = 1.41421356..., π = 3.14159265..., e = 2.71828...\n\nReal Numbers (R): The union of rational and irrational numbers. Every point on the number line corresponds to a real number.\n\nComplex Numbers: Numbers of the form a + bi where i = √(-1). These are beyond the scope of most placement exams but are occasionally tested in IT company rounds.",
         "key_points": ["Natural ⊂ Whole ⊂ Integer ⊂ Rational ⊂ Real", "0 is a whole number but NOT a natural number", "Every integer is a rational number (can be written as n/1)", "√2, √3, √5, π, e are all irrational numbers", "Between any two rational numbers, there are infinite rational numbers"],
         "examples": [
             {"question": "Classify the following: -7, 0, 3/5, √3, 2.333..., π", "solution": "-7: Integer, Rational\n0: Whole, Integer, Rational\n3/5: Rational (not integer)\n√3: Irrational (√3 = 1.7320508...)\n2.333... = 7/3: Rational (repeating decimal)\nπ: Irrational"},
             {"question": "Is 0.101001000100001... rational or irrational?", "solution": "Irrational. The pattern never repeats — each time, one more 0 is added. Since the decimal is non-terminating and non-repeating, it is irrational."}
         ]},
        {"title": "Divisibility Rules",
         "content": "Divisibility rules are shortcuts that help determine whether a number is divisible by another without performing actual division. These save significant time in competitive exams.\n\nDivisibility by 2: A number is divisible by 2 if its last digit is even (0, 2, 4, 6, 8).\n\nDivisibility by 3: A number is divisible by 3 if the sum of its digits is divisible by 3. Example: 726 → 7+2+6 = 15, and 15 ÷ 3 = 5, so 726 is divisible by 3.\n\nDivisibility by 4: A number is divisible by 4 if the last two digits form a number divisible by 4. Example: 1324 → last two digits = 24, 24 ÷ 4 = 6, so 1324 is divisible by 4.\n\nDivisibility by 5: A number is divisible by 5 if it ends in 0 or 5.\n\nDivisibility by 6: A number is divisible by 6 if it is divisible by BOTH 2 and 3.\n\nDivisibility by 8: A number is divisible by 8 if the last three digits form a number divisible by 8.\n\nDivisibility by 9: A number is divisible by 9 if the sum of its digits is divisible by 9.\n\nDivisibility by 11: A number is divisible by 11 if the difference between the sum of digits at odd positions and the sum of digits at even positions is 0 or a multiple of 11. Example: 121 → (1+1) - 2 = 0, divisible by 11.",
         "key_points": ["For 2: check last digit is even", "For 3 and 9: check sum of digits", "For 4: check last 2 digits; for 8: check last 3 digits", "For 11: alternating sum of digits = 0 or multiple of 11", "For 6: must satisfy BOTH rules for 2 and 3"],
         "examples": [
             {"question": "Is 4,83,269 divisible by 11?", "solution": "Digits from right: 9, 6, 2, 3, 8, 4\nOdd positions (1st, 3rd, 5th from right): 9 + 2 + 8 = 19\nEven positions (2nd, 4th, 6th): 6 + 3 + 4 = 13\nDifference: 19 - 13 = 6 ≠ 0 or 11\nSo 4,83,269 is NOT divisible by 11."},
             {"question": "Find the smallest 6-digit number divisible by 12.", "solution": "Smallest 6-digit number = 100000.\n100000 ÷ 12 = 8333.33...\nSo 8334 × 12 = 100008.\nThe smallest 6-digit number divisible by 12 is 100008."}
         ]},
        {"title": "Prime Numbers & Factorization",
         "content": "A prime number is a natural number greater than 1 that has exactly two factors: 1 and itself. Understanding primes is crucial for problems on HCF, LCM, and number properties.\n\nFirst 25 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.\n\nKey facts about primes:\n• 2 is the only even prime number\n• 1 is NOT a prime number (it has only one factor)\n• Every even number greater than 2 can be expressed as the sum of two primes (Goldbach's Conjecture)\n• There are infinitely many primes\n\nPrime Factorization: Every composite number can be expressed as a unique product of prime factors. This is called the Fundamental Theorem of Arithmetic.\n\nFinding number of factors: If N = p^a × q^b × r^c, then:\n• Total number of factors = (a+1)(b+1)(c+1)\n• Sum of factors = [(p^(a+1) - 1)/(p-1)] × [(q^(b+1) - 1)/(q-1)] × ...\n\nTo check if a number n is prime: Check divisibility by all primes up to √n. If none divide n, it is prime.",
         "key_points": ["2 is the smallest and only even prime", "1 is NOT prime (has only 1 factor)", "To test primality of n, check primes up to √n", "Number of factors of p^a × q^b = (a+1)(b+1)", "Twin primes differ by 2: (3,5), (5,7), (11,13), (17,19), (29,31)"],
         "examples": [
             {"question": "Find the number of factors of 360.", "solution": "360 = 2³ × 3² × 5¹\nNumber of factors = (3+1)(2+1)(1+1) = 4 × 3 × 2 = 24 factors."},
             {"question": "Is 397 prime?", "solution": "√397 ≈ 19.9. Check primes up to 19: 2, 3, 5, 7, 11, 13, 17, 19.\n397 is odd (not ÷2), digit sum=19 (not ÷3), doesn't end in 0/5 (not ÷5).\n397÷7=56.7, 397÷11=36.09, 397÷13=30.5, 397÷17=23.4, 397÷19=20.9.\nNone divide evenly. 397 is PRIME."}
         ]},
        {"title": "Remainders & Modular Arithmetic",
         "content": "When a number N is divided by D, we get: N = D × Q + R, where Q is the quotient and R is the remainder (0 ≤ R < D). Remainder problems are extremely common in placement exams.\n\nKey Remainder Properties:\n• Remainder of (a+b) ÷ n = [Rem(a÷n) + Rem(b÷n)] mod n\n• Remainder of (a×b) ÷ n = [Rem(a÷n) × Rem(b÷n)] mod n\n• Remainder of (a^k) ÷ n: Find the cycle of remainders\n\nCyclicity of Remainders: When we compute a^1, a^2, a^3, ... mod n, the remainders eventually repeat in a cycle. This is key for solving problems like 'Find remainder when 2^100 is divided by 7.'\n\nPowers of 2 mod 7: 2^1=2, 2^2=4, 2^3=1, 2^4=2, 2^5=4, 2^6=1... Cycle length = 3.\n\nFermat's Little Theorem: If p is prime and gcd(a,p)=1, then a^(p-1) ≡ 1 (mod p). This is powerful for large exponents.\n\nWilson's Theorem: (p-1)! ≡ -1 (mod p) for any prime p.",
         "key_points": ["N = D × Q + R where 0 ≤ R < D", "Remainders of sum/product = sum/product of remainders (mod divisor)", "Find cyclicity pattern for power-remainder problems", "Fermat's Little: a^(p-1) ≡ 1 (mod p) when p is prime", "Negative remainders: if R is negative, add D to get positive remainder"],
         "examples": [
             {"question": "Find the remainder when 7^222 is divided by 5.", "solution": "7 mod 5 = 2. So we need 2^222 mod 5.\nCycle of 2^n mod 5: 2, 4, 3, 1, 2, 4, 3, 1, ... (cycle length 4)\n222 ÷ 4 = 55 remainder 2.\nSo 2^222 mod 5 = 2^2 mod 5 = 4.\nRemainder = 4."},
             {"question": "What is the remainder when 17 × 23 × 31 is divided by 7?", "solution": "17 mod 7 = 3, 23 mod 7 = 2, 31 mod 7 = 3.\nProduct of remainders: 3 × 2 × 3 = 18.\n18 mod 7 = 4.\nRemainder = 4."}
         ]},
        {"title": "Number System Practice & Exam Patterns",
         "content": "Placement exams test number systems through various question patterns. Here we cover the most frequently tested patterns with strategies.\n\nPattern 1 — Finding the Largest/Smallest Number: 'Find the largest 4-digit number divisible by 88.' Strategy: Divide the boundary number by the divisor, take floor/ceil, multiply back.\n\nPattern 2 — Sum of Numbers in a Range: 'Find sum of all 3-digit numbers divisible by 7.' Use AP formula: count = (last-first)/d + 1, sum = count × (first+last)/2.\n\nPattern 3 — Unit Digit Problems: The unit digit of a product depends only on the unit digits of the factors. Powers of numbers have cyclicity in their unit digits: 2→{2,4,8,6}, 3→{3,9,7,1}, 7→{7,9,3,1}, 8→{8,4,2,6}.\n\nPattern 4 — Factorial Problems: 'How many trailing zeros in 100!?' Count = ⌊100/5⌋ + ⌊100/25⌋ + ⌊100/125⌋ = 20 + 4 + 0 = 24 zeros.\n\nPattern 5 — Number of Digits: Number of digits in N = ⌊log₁₀(N)⌋ + 1.",
         "key_points": ["Unit digit cycles: 2→cycle 4, 3→cycle 4, powers of 4 and 9→cycle 2", "Trailing zeros in n! = Σ⌊n/5^k⌋ for k=1,2,3...", "For sum of AP: S = n(first+last)/2", "Highest power of p in n! = Σ⌊n/p^k⌋", "LCM questions often hide in 'bells ringing together' problems"],
         "examples": [
             {"question": "How many trailing zeros does 250! have?", "solution": "Count factors of 5 in 250!:\n⌊250/5⌋ = 50\n⌊250/25⌋ = 10\n⌊250/125⌋ = 2\n⌊250/625⌋ = 0\nTotal = 50 + 10 + 2 = 62 trailing zeros."},
             {"question": "Find the unit digit of 7^95.", "solution": "Unit digit cycle of 7: 7, 9, 3, 1 (cycle length 4)\n95 ÷ 4 = 23 remainder 3\nUnit digit = 3rd in cycle = 3."}
         ]}
    ],
}

# For topics 1-39, generate chapter structure from existing content
def generate_chapter_names():
    """Return dict of topic_id -> list of 5 chapter titles."""
    return {
        1: ["Finding HCF — Methods & Shortcuts", "Finding LCM — Prime Factorization & Division", "HCF × LCM Relationship & Applications", "Word Problems on HCF & LCM", "Advanced HCF-LCM Problems for Placement"],
        2: ["Basic Percentage Conversions", "Percentage Change & Increase/Decrease", "Successive Percentage Changes", "Percentages in Data Interpretation", "Advanced Percentage Problems"],
        3: ["Cost Price, Selling Price & Profit/Loss", "Markup, Discount & Selling Price", "Successive Discounts", "Dishonest Dealing & Faulty Weights", "Mixed Profit/Loss Problems"],
        4: ["Ratio Fundamentals", "Proportion — Direct & Inverse", "Mixtures & Alligation", "Compounded Ratios", "Advanced Ratio Word Problems"],
        5: ["Work Rate Fundamentals", "Multiple Workers & Combined Work", "Pipes & Cisterns", "Efficiency, Wages & Work Sharing", "Complex Time & Work Problems"],
        6: ["Speed, Distance & Time Basics", "Relative Speed & Meeting Problems", "Problems on Trains", "Boats & Streams", "Races & Circular Motion"],
        7: ["Simple Interest Formula & Basics", "Finding Principal, Rate & Time", "Comparing Simple Interest Amounts", "SI in Banking & Investment", "Mixed SI Problems"],
        8: ["Compound Interest Formula", "CI vs SI — Finding the Difference", "Half-yearly & Quarterly Compounding", "Growth, Depreciation & Population", "Advanced CI Problems"],
        9: ["Basic Average Calculation", "Weighted Average", "Average of Combined Groups", "Running Average & Data Changes", "Average in Data Interpretation"],
        10: ["Age Relationships & Basic Equations", "Past & Future Age Problems", "Ratio-based Age Problems", "Family Age Problems", "Complex Multi-person Age Equations"],
        11: ["Factorial & Fundamental Counting", "Permutations (nPr)", "Combinations (nCr)", "Special Cases — Circular, Identical Objects", "Probability Basics"],
        12: ["Letter Coding Patterns", "Number Coding", "Mixed Coding Systems", "Sentence & Condition Coding", "Advanced Pattern Recognition"],
        13: ["Relation Types & Terminology", "Single Person Blood Relations", "Family Tree Construction", "Coded Blood Relations", "Complex Family Puzzles"],
        14: ["Basic Directions & Compass Points", "Distance Calculation & Displacement", "Shadow & Time-based Direction", "Complex Path Problems", "Advanced Direction Sense"],
        15: ["Linear Arrangement Basics", "Circular Seating Arrangement", "Double Row Arrangement", "Conditional Arrangements", "Complex Multi-constraint Puzzles"],
        16: ["Venn Diagrams for Syllogism", "All/Some/No Statements", "Definite Conclusions", "Possibility-based Conclusions", "Complex Multi-Statement Syllogisms"],
        17: ["Arithmetic Progressions (AP)", "Geometric Progressions (GP)", "Mixed & Complex Series", "Wrong Number Detection", "Advanced Pattern Recognition"],
        18: ["Word Analogies", "Number Analogies", "Letter & Symbol Analogies", "Mixed Analogies", "Complex Relationship Analogies"],
        19: ["Statements & Assumptions", "Statements & Arguments", "Course of Action", "Cause & Effect", "Critical Reasoning & Strengthening/Weakening"],
        20: ["Common Synonyms (A-M)", "Common Synonyms (N-Z)", "Context-based Synonym Selection", "Synonym Patterns in Exams", "Advanced Vocabulary Practice"],
        21: ["Common Antonyms", "Prefix-based Antonyms (un-, in-, dis-)", "Context Antonyms", "Tricky Antonym Pairs", "Exam-oriented Antonym Practice"],
        22: ["Grammar-based Sentence Completion", "Vocabulary-based Fill-ins", "Idiom & Phrase Completion", "Dual Blank Sentences", "Paragraph-level Completion"],
        23: ["Finding the Main Idea", "Inference Questions", "Vocabulary in Context", "Author's Tone & Attitude", "Different Passage Types & Strategies"],
        24: ["Identifying Opening & Closing Sentences", "Using Linking Words & Transitions", "Pronoun Reference Method", "Chronological & Logical Ordering", "Practice Strategies for Para Jumbles"],
        25: ["Subject-Verb Agreement Errors", "Tense Errors", "Preposition Errors", "Pronoun & Article Errors", "Common Exam Error Patterns"],
        26: ["Common Idioms (A-L)", "Common Idioms (M-Z)", "Phrasal Verbs", "Proverbs & Their Meanings", "Exam-oriented Idiom Practice"],
        27: ["Reading & Understanding Tables", "Calculations from Table Data", "Percentage-based Table Problems", "Ratio & Comparison from Tables", "Multi-table Analysis"],
        28: ["Reading Bar Graphs", "Simple Calculations from Bars", "Grouped & Clustered Bar Graphs", "Stacked Bar Graphs", "Comparative Bar Graph Analysis"],
        29: ["Reading Pie Charts — Angles & Percentages", "Calculations from Pie Charts", "Comparative Pie Charts", "Pie Charts Combined with Tables", "Advanced Pie Chart Problems"],
        30: ["Reading Line Graphs", "Trends, Slopes & Rate of Change", "Multiple Line Comparison", "Combined Chart Interpretation", "Advanced Line Graph Problems"],
        31: ["Variables, Constants & Data Types in C", "Operators & Expressions", "Control Flow — if, else, switch", "Functions & Scope", "Arrays, Pointers & Memory"],
        32: ["Primitive Data Types & Sizes", "Type Casting — Implicit & Explicit", "Arithmetic & Relational Operators", "Logical & Bitwise Operators", "Operator Precedence & Associativity"],
        33: ["if-else & Nested Conditions", "switch-case Statements", "for Loop & Variations", "while & do-while Loops", "break, continue & Nested Loops"],
        34: ["1D Arrays — Declaration & Traversal", "2D Arrays & Matrix Operations", "String Basics & Operations", "String Library Functions", "Array & String Problem Solving"],
        35: ["Pointer Basics — Declaration & Dereferencing", "Pointer Arithmetic", "Pointers & Arrays Relationship", "Dynamic Memory — malloc, calloc, free", "Common Pointer Pitfalls"],
        36: ["Classes, Objects & Constructors", "Inheritance — Types & Usage", "Polymorphism — Overloading & Overriding", "Encapsulation & Abstraction", "SOLID Principles & Design Patterns Intro"],
        37: ["Stacks & Queues", "Linked Lists — Singly, Doubly, Circular", "Trees — Binary, BST, Traversals", "Graphs — BFS, DFS, Representation", "Hashing & Hash Tables"],
        38: ["Sorting — Bubble, Selection, Insertion, Merge, Quick", "Searching — Linear, Binary & Variants", "Recursion & Backtracking", "Time & Space Complexity (Big-O)", "Greedy Algorithms & Dynamic Programming Intro"],
        39: ["SELECT, WHERE & Basic Queries", "JOINs — INNER, LEFT, RIGHT, FULL", "GROUP BY, HAVING & Aggregation", "Subqueries & Nested Queries", "DDL, DML & Database Design Basics"],
    }


def build_generic_chapter(topic_title, ch_title, ch_num):
    """Build a chapter with content derived from the chapter title."""
    return {
        "title": ch_title,
        "content": f"This chapter covers {ch_title.lower()} as part of the {topic_title} topic. Understanding this concept is essential for placement exams conducted by top companies like TCS, Infosys, Wipro, and Cognizant.\n\nThe key to mastering this area is consistent practice with timed problem-solving. Focus on understanding the underlying logic rather than memorizing formulas. Most placement questions in this area test your ability to apply concepts quickly under time pressure.\n\nPractice solving at least 20-30 problems from this chapter before moving to the next. Use resources like IndiaBix, GeeksforGeeks, and previous year placement papers for additional practice.",
        "key_points": [
            f"Understand the fundamentals of {ch_title.lower()} thoroughly",
            f"Practice with placement-style MCQs from IndiaBix and GFG",
            f"Time yourself — most exams give 1-2 minutes per question",
            f"Review solved examples to understand the approach",
            f"Connect this with other {topic_title} concepts"
        ],
        "examples": [
            {"question": f"Sample placement question on {ch_title}", "solution": f"Approach: Identify the concept from {ch_title}, apply the relevant formula or logic, and verify your answer by substitution."},
        ]
    }


def main():
    """Add chapters to study_content.py."""
    import sys
    sys.path.insert(0, '.')
    from curriculum_flow_env.study_content import STUDY_CONTENT

    chapter_names = generate_chapter_names()

    # Add detailed chapters for topic 0 (Numbers)
    STUDY_CONTENT[0]["chapters"] = CHAPTER_TEMPLATES[0]

    # Add chapters for all other topics
    for tid in range(1, 40):
        if tid in chapter_names:
            chapters = []
            for i, ch_title in enumerate(chapter_names[tid]):
                chapters.append(build_generic_chapter(
                    STUDY_CONTENT[tid]["title"], ch_title, i+1
                ))
            STUDY_CONTENT[tid]["chapters"] = chapters

    # Write back
    output_lines = ['"""Study materials for all 40 placement topics — 5 chapters per topic."""\n\nSTUDY_CONTENT = {\n']

    for tid in sorted(STUDY_CONTENT.keys()):
        data = STUDY_CONTENT[tid]
        output_lines.append(f'    {tid}: {{\n')
        output_lines.append(f'        "title": {json.dumps(data["title"])},\n')
        output_lines.append(f'        "overview": {json.dumps(data.get("overview", ""))},\n')

        # Chapters
        if "chapters" in data:
            output_lines.append(f'        "chapters": [\n')
            for ch in data["chapters"]:
                output_lines.append(f'            {{\n')
                output_lines.append(f'                "title": {json.dumps(ch["title"])},\n')
                output_lines.append(f'                "content": {json.dumps(ch["content"])},\n')
                output_lines.append(f'                "key_points": {json.dumps(ch["key_points"])},\n')
                output_lines.append(f'                "examples": {json.dumps(ch["examples"])},\n')
                output_lines.append(f'            }},\n')
            output_lines.append(f'        ],\n')

        # Keep existing fields
        if "key_concepts" in data:
            output_lines.append(f'        "key_concepts": {json.dumps(data["key_concepts"])},\n')
        if "formulas" in data:
            output_lines.append(f'        "formulas": {json.dumps(data["formulas"])},\n')
        if "solved_examples" in data:
            output_lines.append(f'        "solved_examples": {json.dumps(data["solved_examples"])},\n')
        if "tips" in data:
            output_lines.append(f'        "tips": {json.dumps(data["tips"])},\n')

        output_lines.append(f'    }},\n')

    output_lines.append('}\n')

    outpath = 'curriculum_flow_env/study_content.py'
    with open(outpath, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"Written {len(output_lines)} lines to {outpath}")

    # Verify
    topics_with_chapters = sum(1 for d in STUDY_CONTENT.values() if "chapters" in d)
    print(f"Topics with chapters: {topics_with_chapters}/40")


if __name__ == "__main__":
    main()
