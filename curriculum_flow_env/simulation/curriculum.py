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
    # DSA Deep Dive (40-51)
    40: "dsa_arrays", 41: "dsa_linked_lists", 42: "dsa_stacks_queues",
    43: "dsa_trees", 44: "dsa_graphs", 45: "dsa_hashing",
    46: "dsa_dynamic_programming", 47: "dsa_searching_sorting",
    48: "dsa_recursion_backtracking", 49: "dsa_greedy",
    50: "dsa_bit_manipulation", 51: "dsa_string_algorithms",
    # Core CS Subjects (52-59)
    52: "os_processes_threads", 53: "os_memory_management",
    54: "os_scheduling_deadlocks", 55: "dbms_normalization_sql",
    56: "dbms_transactions_indexing", 57: "cn_osi_tcpip",
    58: "cn_protocols_security", 59: "oop_design_patterns",
    # Company Specific (60-65)
    60: "company_tcs", 61: "company_infosys", 62: "company_wipro",
    63: "company_accenture", 64: "company_amazon", 65: "company_microsoft",
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
    # DSA Deep Dive
    40: "Arrays & Matrices", 41: "Linked Lists", 42: "Stacks & Queues",
    43: "Trees & BST", 44: "Graphs", 45: "Hashing",
    46: "Dynamic Programming", 47: "Searching & Sorting",
    48: "Recursion & Backtracking", 49: "Greedy Algorithms",
    50: "Bit Manipulation", 51: "String Algorithms",
    # Core CS
    52: "OS: Processes & Threads", 53: "OS: Memory Management",
    54: "OS: Scheduling & Deadlocks", 55: "DBMS: Normalization & SQL",
    56: "DBMS: Transactions & Indexing", 57: "CN: OSI & TCP/IP",
    58: "CN: Protocols & Security", 59: "OOP & Design Patterns",
    # Company Specific
    60: "TCS NQT Prep", 61: "Infosys InfyTQ Prep", 62: "Wipro NLTH Prep",
    63: "Accenture Prep", 64: "Amazon SDE Prep", 65: "Microsoft Prep",
}

TOPIC_DIFFICULTIES = {
    0: 1, 1: 2, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3,
    7: 2, 8: 3, 9: 2, 10: 3, 11: 4,
    12: 2, 13: 2, 14: 2, 15: 3, 16: 3, 17: 2, 18: 2, 19: 4,
    20: 1, 21: 1, 22: 2, 23: 3, 24: 3, 25: 2, 26: 2,
    27: 2, 28: 2, 29: 2, 30: 3,
    31: 1, 32: 2, 33: 2, 34: 3, 35: 4, 36: 3, 37: 4, 38: 4, 39: 3,
    # DSA Deep Dive
    40: 2, 41: 3, 42: 3, 43: 4, 44: 5, 45: 3,
    46: 5, 47: 2, 48: 4, 49: 3, 50: 4, 51: 3,
    # Core CS
    52: 3, 53: 4, 54: 4, 55: 3, 56: 4, 57: 3, 58: 3, 59: 4,
    # Company Specific
    60: 2, 61: 2, 62: 2, 63: 2, 64: 5, 65: 5,
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
    # DSA chain
    (40, 41), (40, 42), (42, 43), (43, 44), (40, 45),
    (47, 48), (48, 46), (48, 49), (40, 50), (40, 51), (47, 40),
    # Core CS chain (no strict prerequisites between CS modules, but within sub-areas)
    (52, 53), (53, 54), (55, 56), (57, 58), (36, 59),
    # Company prep has no prerequisite locks (all unlocked)
]

TOPIC_GROUPS = {
    "quantitative_aptitude": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "logical_reasoning": [12, 13, 14, 15, 16, 17, 18, 19],
    "verbal_ability": [20, 21, 22, 23, 24, 25, 26],
    "data_interpretation": [27, 28, 29, 30],
    "programming": [31, 32, 33, 34, 35, 36, 37, 38, 39],
    "dsa_deep_dive": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51],
    "core_cs": [52, 53, 54, 55, 56, 57, 58, 59],
    "company_specific": [60, 61, 62, 63, 64, 65],
}

GROUP_DISPLAY_NAMES = {
    "quantitative_aptitude": "Quantitative Aptitude",
    "logical_reasoning": "Logical Reasoning",
    "verbal_ability": "Verbal Ability",
    "data_interpretation": "Data Interpretation",
    "programming": "Programming & CS",
    "dsa_deep_dive": "DSA Deep Dive",
    "core_cs": "Core CS Subjects",
    "company_specific": "Company Specific",
}

GROUP_COLORS = {
    "quantitative_aptitude": "#2196f3",
    "logical_reasoning": "#ff9800",
    "verbal_ability": "#4caf50",
    "data_interpretation": "#9c27b0",
    "programming": "#f44336",
    "dsa_deep_dive": "#00bcd4",
    "core_cs": "#795548",
    "company_specific": "#607d8b",
}

NUM_TOPICS = 66
MASTERY_THRESHOLD = 0.8
UNLOCK_THRESHOLD = 0.7
