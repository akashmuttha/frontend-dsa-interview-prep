"""Guided practice for the questions in InterviewQuestions.py.

How to use this file
--------------------
1. Work on one exercise at a time.
2. Before coding, explain the input, output, state, and edge cases aloud.
3. Use Hint 1 before Hint 2. Do not jump to a solution.
4. After a solution works, write its time and space complexity.

Keep your own attempts below each function. Do not copy a solution into this
file before you can explain the approach in your own words.
"""


# ============================================================
# 1. MISSING NUMBER
# ============================================================

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def missing_number(numbers, n):
    """Return the one missing integer from the expected range 1 through n.

    Examples:
        missing_number([1, 2, 3, 4, 6], 6) -> 5
        missing_number([2, 3, 4], 4) -> 1

    Before coding:
        - What values are expected to exist?
        - Is the output one number or a list?
        - What happens when you find the missing value?

    Hint 1: Compare the expected values with the values that were given.
    Hint 2: There is also a math-based approach when exactly one value is
            missing.

    Time Complexity:
    Space Complexity:
    """
    # we have formula arithmetic sum = n * (n+1) /2
    sum1 = 100 * (100 +1)/2
    sum2 = sum(numbers)

    missing_number = sum1 - sum2
    return missing_number


# ============================================================
# 2. TWO SUM: RETURN INDEXES
# ============================================================

def two_sum_indexes(numbers, target):
    """Return indexes of two different values whose sum equals target.

    Assume exactly one valid answer exists.

    Examples:
        two_sum_indexes([2, 7, 11, 15], 9) -> [0, 1]
        two_sum_indexes([3, 2, 4], 6) -> [1, 2]

    Before coding:
        - Do you return values or indexes?
        - How will you avoid using the same index twice?
        - What pair of positions are you comparing?

    Hint 1: Start with two loops and make the second loop start after the
            first index.
    Hint 2: Later, ask: "What value do I need to reach target?"

    Time Complexity:
    Space Complexity:
    """

    for index1 in range(len(numbers)):
        second = target - numbers[index1]

        for index2 in range(index1 + 1, len(numbers)):
            if numbers[index2] == second:
                return index1,  index2











# ============================================================
# 3. FIND A NUMBER
# ============================================================

def find_number_index(numbers, target):
    """Return the first index of target, or -1 when it is absent.

    Examples:
        find_number_index([4, 8, 2, 8], 8) -> 1
        find_number_index([4, 8, 2], 9) -> -1

    Before coding:
        - Does the output require a value or a position?
        - Can you stop after the first match?

    Hint 1: This is a first-match, early-return problem.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 4. MAX PRODUCT OF TWO DISTINCT ELEMENTS
# ============================================================

def max_product_of_two(numbers):
    """Return the maximum product from two different elements.

    Examples:
        max_product_of_two([1, 7, 3, 4, 9, 5]) -> 63
        max_product_of_two([5, 2]) -> 10

    Before coding:
        - Which two values would create the largest product for positive input?
        - What state must be tracked while scanning?
        - What should happen for fewer than two values?

    Hint 1: Track the two largest values seen so far.
    Hint 2: Think about how an old largest value changes when a new largest
            value appears.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 5. MIDDLE OF A LIST
# ============================================================

def middle_values(numbers):
    """Return a new list without the first and last elements.

    Examples:
        middle_values([1, 2, 3, 4]) -> [2, 3]
        middle_values([1, 2]) -> []

    Before coding:
        - Does this modify the original list or create a new result?
        - What should happen for lists shorter than two items?

    Hint 1: Python slicing can express a continuous middle range.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 6. DIAGONAL SUM OF A SQUARE MATRIX
# ============================================================

def diagonal_sum(matrix):
    """Return the sum of the top-left to bottom-right diagonal.

    Example:
        diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 15

    Before coding:
        - What is special about each diagonal location?
        - Which row and column indexes match for a diagonal item?

    Hint 1: At every main-diagonal position, the row index equals the column
            index.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 7. BEST AND SECOND-BEST DISTINCT SCORE
# ============================================================

def best_two_scores(scores):
    """Return (largest, second_largest_distinct) from scores.

    Examples:
        best_two_scores([84, 85, 86, 87, 85, 90]) -> (90, 87)
        best_two_scores([7, 7, 7]) -> (7, None)

    Before coding:
        - What two values must stay available during traversal?
        - How should duplicates of the largest value behave?

    Hint 1: Use two value trackers, not two counters.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 8. REMOVE DUPLICATES WHILE PRESERVING ORDER
# ============================================================

def remove_duplicates(numbers):
    """Return a new list containing first occurrences only.

    Examples:
        remove_duplicates([1, 1, 2, 2, 3, 4, 5]) -> [1, 2, 3, 4, 5]
        remove_duplicates([]) -> []

    Before coding:
        - Is this an in-place or new-result problem?
        - How do you know whether a value was already kept?

    Hint 1: Begin with a result list and only add values not already kept.
    Hint 2: Later, a set can make membership checks faster.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 9. FIND EVERY VALUE PAIR WITH A TARGET SUM
# ============================================================

def pair_sum_values(numbers, target):
    """Return every value pair whose sum equals target.

    Example:
        pair_sum_values([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
        -> [(2, 5), (4, 3), (3, 4), (-2, 9)]

    Before coding:
        - Do you need values, indexes, or both?
        - How will you avoid pairing a number with itself?
        - Should reversed pairs count separately? Follow the expected output.

    Hint 1: Compare each position with later positions only.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 10. CONTAINS DUPLICATE
# ============================================================

def contains_duplicate(numbers):
    """Return True when any value appears more than once.

    Examples:
        contains_duplicate([1, 2, 3, 1]) -> True
        contains_duplicate([1, 2, 3, 4]) -> False

    Before coding:
        - Can you return as soon as a duplicate is found?
        - What data structure can remember previously seen values?

    Hint 1: Keep a record of values already seen.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 11. CHECK PERMUTATION
# ============================================================

def is_permutation(first, second):
    """Return True when both lists contain the same values with the same counts.

    Examples:
        is_permutation([1, 2, 3], [3, 1, 2]) -> True
        is_permutation([1, 2, 2], [1, 2, 3]) -> False

    Before coding:
        - What quick check can reject inputs with different lengths?
        - Do repeated values matter?
        - Is modifying the input allowed?

    Hint 1: Sorting copies is one approach; frequency counting is another.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# 12. ROTATE A SQUARE MATRIX CLOCKWISE
# ============================================================

def rotate_matrix_clockwise(matrix):
    """Rotate a square matrix 90 degrees clockwise in place.

    Example:
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_matrix_clockwise(matrix)
        # matrix becomes [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    Before coding:
        - Is the matrix square?
        - Does the task require a new matrix or modification in place?
        - Can you break rotation into two simpler matrix operations?

    Hint 1: A clockwise rotation can be built from a transpose and a reversal
            of each row.

    Time Complexity:
    Space Complexity:
    """
    pass


# ============================================================
# SELF-REVIEW TEMPLATE
# ============================================================

SELF_REVIEW = """
For each completed question, answer:

1. What exactly was the input and required output?
2. What state did I need to track?
3. What changed during each iteration?
4. Which edge cases did I test?
5. Time complexity:
6. Space complexity:
7. Is the input modified or is a new result returned?
8. Can I re-solve it tomorrow without looking?
"""
