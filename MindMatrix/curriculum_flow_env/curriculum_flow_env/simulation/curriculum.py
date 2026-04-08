"""Curriculum constants — IndiaBix placement preparation topics."""

# ━━━ TOPIC CATEGORIES AND SUBTOPICS ━━━
# Based on IndiaBix placement preparation structure

TOPIC_NAMES = {
    # Quantitative Aptitude (0-11)
    0: "numbers", 1: "hcf_lcm", 2: "percentages", 3: "profit_loss",
    4: "ratio_proportion", 5: "time_work", 6: "time_distance",
    7: "simple_interest", 8: "compound_interest", 9: "averages",
    10: "problems_on_ages", 11: "permutations_combinations",
    # Logical Reasoning (12-19)
    12: "coding_decoding", 13: "blood_relations", 14: "direction_sense",
    15: "seating_arrangement", 16: "syllogism", 17: "number_series",
    18: "analogies", 19: "logical_deduction",
    # Verbal Ability (20-26)
    20: "synonyms", 21: "antonyms", 22: "sentence_completion",
    23: "reading_comprehension", 24: "para_jumbles", 25: "spotting_errors",
    26: "idioms_phrases",
    # Data Interpretation (27-30)
    27: "tables", 28: "bar_graphs", 29: "pie_charts", 30: "line_graphs",
    # Programming & CS (31-39)
    31: "c_basics", 32: "data_types_operators", 33: "control_flow",
    34: "arrays_strings", 35: "pointers_references", 36: "oop_concepts",
    37: "data_structures", 38: "algorithms_basics", 39: "sql_basics",
}

TOPIC_DISPLAY_NAMES = {
    0: "Numbers", 1: "HCF & LCM", 2: "Percentages", 3: "Profit & Loss",
    4: "Ratio & Proportion", 5: "Time & Work", 6: "Time & Distance",
    7: "Simple Interest", 8: "Compound Interest", 9: "Averages",
    10: "Problems on Ages", 11: "Permutations & Combinations",
    12: "Coding-Decoding", 13: "Blood Relations", 14: "Direction Sense",
    15: "Seating Arrangement", 16: "Syllogism", 17: "Number Series",
    18: "Analogies", 19: "Logical Deduction",
    20: "Synonyms", 21: "Antonyms", 22: "Sentence Completion",
    23: "Reading Comprehension", 24: "Para Jumbles", 25: "Spotting Errors",
    26: "Idioms & Phrases",
    27: "Tables", 28: "Bar Graphs", 29: "Pie Charts", 30: "Line Graphs",
    31: "C Basics", 32: "Data Types & Operators", 33: "Control Flow",
    34: "Arrays & Strings", 35: "Pointers & References", 36: "OOP Concepts",
    37: "Data Structures", 38: "Algorithms Basics", 39: "SQL Basics",
}

TOPIC_DIFFICULTIES = {
    0: 1, 1: 2, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3,
    7: 2, 8: 3, 9: 2, 10: 3, 11: 4,
    12: 2, 13: 2, 14: 2, 15: 3, 16: 3, 17: 2, 18: 2, 19: 4,
    20: 1, 21: 1, 22: 2, 23: 3, 24: 3, 25: 2, 26: 2,
    27: 2, 28: 2, 29: 2, 30: 3,
    31: 1, 32: 2, 33: 2, 34: 3, 35: 4, 36: 3, 37: 4, 38: 4, 39: 3,
}

# Prerequisite edges: must master before unlocking next
PREREQUISITE_EDGES = [
    # Quant chain
    (0, 1), (0, 2), (2, 3), (0, 4), (4, 5), (4, 6),
    (2, 7), (7, 8), (0, 9), (0, 10), (0, 11),
    # Reasoning chain
    (12, 15), (12, 16), (17, 19), (18, 19),
    # Verbal chain
    (20, 22), (21, 22), (22, 23), (22, 24), (22, 25),
    # Data Interpretation chain
    (27, 28), (27, 29), (28, 30), (29, 30),
    # Programming chain
    (31, 32), (32, 33), (33, 34), (34, 35), (33, 36), (36, 37), (37, 38), (31, 39),
]

TOPIC_GROUPS = {
    "quantitative_aptitude": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "logical_reasoning": [12, 13, 14, 15, 16, 17, 18, 19],
    "verbal_ability": [20, 21, 22, 23, 24, 25, 26],
    "data_interpretation": [27, 28, 29, 30],
    "programming": [31, 32, 33, 34, 35, 36, 37, 38, 39],
}

GROUP_DISPLAY_NAMES = {
    "quantitative_aptitude": "Quantitative Aptitude",
    "logical_reasoning": "Logical Reasoning",
    "verbal_ability": "Verbal Ability",
    "data_interpretation": "Data Interpretation",
    "programming": "Programming & CS",
}

GROUP_COLORS = {
    "quantitative_aptitude": "#2196f3",
    "logical_reasoning": "#ff9800",
    "verbal_ability": "#4caf50",
    "data_interpretation": "#9c27b0",
    "programming": "#f44336",
}

NUM_TOPICS = 40
MASTERY_THRESHOLD = 0.8
UNLOCK_THRESHOLD = 0.7
