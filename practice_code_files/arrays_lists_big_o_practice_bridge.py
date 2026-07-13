"""
ARRAYS, LISTS, AND BIG-O PRACTICE BRIDGE
========================================

Course checkpoint
-----------------
This practice file is designed for the material completed from:

    Lectures 12-22: Big O and Space Complexity
    Lectures 25-43: One-Dimensional and Two-Dimensional Arrays
    Lectures 46-57: Python Lists and List Comprehensions

Purpose
-------
This is NOT another full course.

It is a short 2-3 day bridge between:
    1. Understanding the lectures
    2. Writing code independently
    3. Starting "Practice Test 1: List Interview Questions"

Recommended schedule
--------------------
Day 1:
    Section A
    Exercises 1-7

Day 2:
    Exercises 8-14

Day 3:
    Exercises 15-18
    Re-solve any 5 previous exercises without looking
    Start the course's List Interview Questions practice test

Rules
-----
For the first attempt, avoid these built-ins unless explicitly allowed:

    sum()
    max()
    min()
    sort()
    sorted()
    reverse()
    reversed()
    count()
    index()
    set()

For every exercise, write:

    # Approach:
    # Time Complexity:
    # Space Complexity:
    # In-place or new result:

Important
---------
You are not expected to master arrays completely before moving forward.

The goal is:
    "I can independently write basic array/list logic and explain
    its time and space complexity."
"""


# ============================================================
# SECTION A: QUICK RECALL FROM COMPLETED LECTURES
# ============================================================

def lecture_recall():
    """
    Complete this section from memory before starting the exercises.

    Do not spend more than 30-45 minutes here.
    """

    # --------------------------------------------------------
    # A1. Python array module
    # --------------------------------------------------------

    # Uncomment and complete:
    #
    # from array import array
    #
    # integer_array = array("i", [1, 2, 3, 4])
    #
    # Tasks:
    # 1. Print the first element.
    # 2. Append 5.
    # 3. Insert 10 at index 1.
    # 4. Traverse all values.
    # 5. Remove one value.
    # 6. Explain why array elements must use the same type.

    # --------------------------------------------------------
    # A2. Python list operations
    # --------------------------------------------------------

    numbers = [10, 20, 30, 40]

    # Write examples of:
    # 1. Access using positive indexing
    # 2. Access using negative indexing
    # 3. Update an element
    # 4. append()
    # 5. insert()
    # 6. pop()
    # 7. remove()
    # 8. slicing
    # 9. membership using "in"
    # 10. len()

    # --------------------------------------------------------
    # A3. Three traversal styles
    # --------------------------------------------------------

    # Direct traversal:
    # for value in numbers:
    #     ...

    # Index traversal:
    # for index in range(len(numbers)):
    #     ...

    # enumerate:
    # for index, value in enumerate(numbers):
    #     ...

    # --------------------------------------------------------
    # A4. List comprehensions
    # --------------------------------------------------------

    # Create using list comprehensions:
    # 1. Squares of [1, 2, 3, 4]
    # 2. Even numbers from [1, 2, 3, 4, 5, 6]
    # 3. Positive values from [-2, 4, 0, -1, 7]
    # 4. Convert ["1", "2", "3"] to integers

    pass


# ============================================================
# SECTION B: SHARED TEST DATA
# ============================================================

EMPTY = []

SINGLE = [5]

SORTED = [1, 2, 3, 4, 5]

REVERSE_SORTED = [5, 4, 3, 2, 1]

DUPLICATES = [1, 2, 2, 3, 3, 3]

ALL_EQUAL = [7, 7, 7, 7]

MIXED = [-5, 0, 4, -2, 8, 0, 1]

ALL_NEGATIVE = [-8, -3, -11, -2]

WITH_ZEROES = [0, 1, 0, 3, 12]

MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


# ============================================================
# EXERCISE 1: CALCULATE THE SUM
# ============================================================

def calculate_sum(numbers):
    """
    Return the sum of all values.

    Return 0 for an empty list.

    Do not use sum().

    Examples:
        calculate_sum([10, 20, 30]) -> 60
        calculate_sum([]) -> 0

    Add:
        # Approach:
        # Time Complexity:
        # Space Complexity:
        # In-place or new result:
    """
    total = 0
    for number in numbers:
        total +=number
    return total



# ============================================================
# EXERCISE 2: FIND THE MAXIMUM
# ============================================================

def find_maximum(numbers):

    """
    Return the largest value.

    Return None for an empty list.

    Do not use max() or sorting.

    Examples:
        find_maximum([4, 9, 2, 7]) -> 9
        find_maximum([-8, -3, -12, -5]) -> -3
        find_maximum([]) -> None

    Pitfall:
        Do not initialize the maximum as 0.
    """
    if not numbers:
        return None
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest

def find_maximum(numbers):
    max = None
    for num in numbers:
        if max is None or max < num:
            max = num
    return max


find_maximum([4, 9, 2, 7])
find_maximum([-8, -3, -12, -5])
find_maximum([])

# ============================================================
# EXERCISE 3: COUNT OCCURRENCES
# ============================================================


def count_occurrences(numbers, target):
    """
    Return how many times target appears.

    Do not use count().

    Examples:
        count_occurrences([1, 2, 2, 3, 2], 2) -> 3
        count_occurrences([1, 2, 3], 8) -> 0
    """
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count






# ============================================================
# EXERCISE 4: FIND THE FIRST INDEX
# ============================================================

def find_first_index(numbers, target):
    """
    Return the first index containing target.

    Return -1 when target is absent.

    Do not use index().

    Examples:
        find_first_index([8, 4, 6, 4], 4) -> 1
        find_first_index([8, 4, 6], 10) -> -1
    """
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


# ============================================================
# EXERCISE 5: COUNT NUMBER TYPES
# ============================================================
# %%
def count_number_types(numbers):
    """
    Count positive, negative, and zero values.

    Return:

        {
            "positive": ...,
            "negative": ...,
            "zero": ...
        }

    Example:
        count_number_types([-2, 0, 4, -1, 7, 0])

        returns:

        {
            "positive": 2,
            "negative": 2,
            "zero": 2
        }
    """
    positive = 0
    negative = 0
    zero = 0

    for num in numbers:
        if num < 0:
            negative += 1
        elif num > 0:
            positive += 1
        else:
            zero += 1
    return {
        "positive": positive,
        "negative": negative,
        "zero": zero
    }



# ============================================================
# EXERCISE 6: FIND ALL MATCHING INDEXES
# ============================================================

def find_all_indexes(numbers, target):
    """
    Return every index at which target appears.

    Examples:
        find_all_indexes([5, 2, 5, 7, 5], 5) -> [0, 2, 4]
        find_all_indexes([1, 2, 3], 9) -> []
    """
    index_list = []
    for index in range(len(numbers)):
        if numbers[index] == target:
            index_list.append(index)
    return index_list




# ============================================================
# EXERCISE 7: CHECK WHETHER SORTED
# ============================================================

def is_sorted_ascending(numbers):
    """
    Return True when the list is in non-decreasing order.

    Equal adjacent values are allowed.

    Examples:
        is_sorted_ascending([1, 2, 2, 5]) -> True
        is_sorted_ascending([1, 4, 3, 5]) -> False
        is_sorted_ascending([]) -> True
        is_sorted_ascending([5]) -> True

    Hint:
        Compare numbers[index] with numbers[index + 1].
    """
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            return False
    return True





# ============================================================
# EXERCISE 8: SECOND-LARGEST DISTINCT VALUE
# ============================================================

def find_second_largest(numbers):
    """
    Return the second-largest DISTINCT value.

    Return None when it does not exist.

    Do not use:
        sorted()
        sort()
        set()

    Examples:
        find_second_largest([10, 5, 8, 10, 3]) -> 8
        find_second_largest([7, 7, 7]) -> None
        find_second_largest([5]) -> None
        find_second_largest([-2, -8, -3]) -> -3
    """











def find_second_largest(numbers):
    largest = None
    second_largest = None
    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest

# ============================================================
# EXERCISE 9: REVERSE IN PLACE
# ============================================================

def reverse_in_place(numbers):
    """
    Reverse the original list.

    Do not use:
        reverse()
        reversed()
        slicing
        another result list

    Example:
        values = [1, 2, 3, 4, 5]
        reverse_in_place(values)
        values -> [5, 4, 3, 2, 1]

    Hint:
        Use left and right indexes.
    """
    left_index = 0
    right_index = len(numbers) -1

    while left_index < right_index:
        temporary = numbers[left_index]
        numbers[left_index] = numbers[right_index]
        numbers[right_index] = temporary


        left_index = left_index + 1
        right_index = right_index - 1
    return numbers


# ============================================================
# EXERCISE 10: FILTER EVEN NUMBERS
# ============================================================

def filter_even_numbers(numbers):
    """
    Return a NEW list containing only even values.

    Preserve order.

    Example:
        filter_even_numbers([1, 2, 3, 4, 5, 6])
        -> [2, 4, 6]

    First solve with a normal loop.

    Optional:
        Solve again using a list comprehension.
    """
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
            # even_list = [x for x in numbers if x % 2 == 0]
    return even_list


# ============================================================
# EXERCISE 11: REPLACE NEGATIVES WITH ZERO
# ============================================================

def replace_negatives_with_zero(numbers):
    """
    Modify the original list.

    Replace every negative number with 0.

    Example:
        values = [-4, 2, -1, 5, 0]
        replace_negatives_with_zero(values)
        values -> [0, 2, 0, 5, 0]
    """
    for index in range(len(numbers)):
        if numbers[index] < 0:
            numbers[index] = 0
    return numbers


# ============================================================
# EXERCISE 12: REMOVE ALL OCCURRENCES
# ============================================================

def remove_all_occurrences(numbers, target):
    """
    Return a NEW list excluding target.

    Preserve the order of remaining elements.

    Examples:
        remove_all_occurrences([1, 3, 2, 3, 4, 3], 3)
        -> [1, 2, 4]

        remove_all_occurrences([5, 5], 5)
        -> []

    Optional:
        Solve again using conditional list comprehension.
    """
    new_list = []
    for num in numbers:
        if num != target:
            new_list.append(num)
    return new_list

    # new_list = [x for x in numbers if x != target]



# ============================================================
# EXERCISE 13: REMOVE DUPLICATES
# ============================================================

def remove_duplicates(numbers):

    """
    Return a NEW list containing only first occurrences.

    Preserve order.

    Do not use set().

    Examples:
        remove_duplicates([4, 2, 4, 1, 2, 3])
        -> [4, 2, 1, 3]

        remove_duplicates([])
        -> []

    An O(n^2) solution is acceptable at this stage.
    """
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list


# ============================================================
# EXERCISE 14: MOVE ZEROES TO THE END
# ============================================================

def move_zeroes_to_end(numbers):
    """
    Move all zeroes to the end of the original list.

    Preserve the relative order of non-zero elements.

    Example:
        values = [0, 1, 0, 3, 12]
        move_zeroes_to_end(values)
        values -> [1, 3, 12, 0, 0]

    Progression:
        Attempt 1: Additional list is acceptable.
        Attempt 2: Solve in place.
    """







    new_list = []
    count = []
    for index in range(len(numbers)):
        if numbers[index] != 0:
            new_list.append(numbers[index])
        else:
            count.append(0)
    final_list = new_list + count
    return final_list

def move_zeros_to_end_2nd_method(numbers):
    write_index = 0
    for index in range(len(numbers)):
        if numbers[index] != 0:
            numbers[write_index] = numbers[index]

            write_index += 1

    while write_index < len(numbers):
        numbers[write_index] = 0
        write_index +=1
    return numbers














def move_zeros_to_end_2nd_method(numbers):
    # this tells us where to place the next non-zero number.
    write_index = 0
    for read_index in range(len(numbers)):

        if numbers[read_index] != 0:

            #put that non zero number at the right index
            numbers[write_index] = numbers[read_index]

            #move write_index   one step right that means we will increase the number of the index by 1.
            write_index += 1

    #All the non zero numbers are at the start.
    #put zeroes in every remaining position.
    while write_index < len(numbers):
        numbers[write_index] = 0
        write_index +=1
    return numbers








# ============================================================
# EXERCISE 15: MANUAL INSERTION
# ============================================================

def insert_at(numbers, index, value):
    """
    Insert value at index by manually shifting elements.

    Modify the original list.

    Do not use insert().

    You may use append(None) once to create extra space.

    Examples:
        values = [10, 20, 30, 40]
        insert_at(values, 2, 99)
        values -> [10, 20, 99, 30, 40]

        values = [10, 20]
        insert_at(values, 0, 5)
        values -> [5, 10, 20]

        values = [10, 20]
        insert_at(values, 2, 30)
        values -> [10, 20, 30]

    Raise IndexError when:
        index < 0
        or
        index > len(numbers)

    Big-O question:
        Why is insertion in the middle O(n)?
    """
    if index < 0 or index > len(numbers):
        raise IndexError("index out of range")
    # numbers = [10,20,30,40]
    #here len(numbers) = 4
    # old last item is at index 3.

    numbers.append(None)
      # numbers = [10,20,30,40, None]
    # here len(numbers) = 5
    # old last item is index len(numbers) -2
    old_last_index = len(numbers) -2

    while old_last_index >= index:
        numbers[old_last_index +1] = numbers[old_last_index]
        old_last_index -= 1
    numbers[index] = value
    return numbers

# ============================================================
# EXERCISE 16: MANUAL DELETION
# ============================================================

def delete_at(numbers, index):
    """
    Delete the value at index by manually shifting values left.

    Modify the original list.

    Do not use:
        del
        remove()

    You may use pop() once after shifting.

    Example:
        values = [10, 20, 30, 40]
        delete_at(values, 1)
        values -> [10, 30, 40]

    Raise IndexError when:
        index < 0
        or
        index >= len(numbers)

    Big-O question:
        Why is deletion from the middle O(n)?
    """
    pass


# ============================================================
# EXERCISE 17: ROW SUMS IN A 2D ARRAY
# ============================================================

def calculate_row_sums(matrix):
    """
    Return the sum of each row.

    Do not use sum().

    Example:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        calculate_row_sums(matrix)
        -> [6, 15, 24]

    Additional cases:
        calculate_row_sums([]) -> []
        calculate_row_sums([[]]) -> [0]

    Complexity:
        Use r for rows and c for columns.
    """
    sum_list = []
    sum = 0

    for row in range(len(matrix)):
        print(row)
        for num in matrix[row]:
            sum = sum + num
        sum_list.append(sum)
        sum = 0
    return sum_list
    #     for num in row:
    #         sum = sum + num
    #         sum_list.append(sum)
    #     sum = 0
    # return sum_list




# ============================================================
# EXERCISE 18: SEARCH A 2D ARRAY
# ============================================================

def find_in_matrix(matrix, target):
    """
    Return the first location of target.

    Return:
        (row_index, column_index) when found
        (-1, -1) when absent

    Example:
        matrix = [
            [4, 8, 2],
            [7, 5, 1]
        ]

        find_in_matrix(matrix, 5) -> (1, 1)
        find_in_matrix(matrix, 10) -> (-1, -1)

    Search row by row from left to right.

    Complexity:
        Use r for rows and c for columns.
    """


    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == target:
                return (row, column)

    return (-1, -1)





def calculate_avg_temp():
    days = int(input("Enter How many days you want to calculate the AVERAGE TEMPERATURE"))
    temp_sum = 0
    temp_list = []
    for i in range(days):
        input_temp = int(input(f"Input the temperature for day {i+1}"))
        temp_list.append(input_temp)
        temp_sum = temp_sum + input_temp
    average = temp_sum/days

    above = []
    for i in temp_list:
        if i > average:
            above.append(i)


    return f"The average temperature for {days} days is {average} and number of days above average is {len(above)} and temperatures are as follows{above}"






# ============================================================
# SECTION C: BIG-O CLASSIFICATION PRACTICE
# ============================================================

def big_o_classification():
    """
    Write the time and space complexity for every snippet.

    Do this without running the code first.
    """

    numbers = [1, 2, 3, 4, 5]

    # Snippet 1
    # print(numbers[0])
    #
    # Time:
    # Space:

    # Snippet 2
    # for number in numbers:
    #     print(number)
    #
    # Time:
    # Space:

    # Snippet 3
    # for first in numbers:
    #     for second in numbers:
    #         print(first, second)
    #
    # Time:
    # Space:

    # Snippet 4
    # result = []
    # for number in numbers:
    #     result.append(number * 2)
    #
    # Time:
    # Space:

    # Snippet 5
    # for number in numbers:
    #     print(number)
    #
    # for number in numbers:
    #     print(number)
    #
    # Raw expression:
    # Simplified complexity:

    # Snippet 6
    # for first in numbers:
    #     for second in numbers:
    #         print(first, second)
    #
    # for number in numbers:
    #     print(number)
    #
    # Raw expression:
    # Dominant term:
    # Simplified complexity:

    # Snippet 7
    # first = [1, 2, 3]
    # second = [10, 20, 30, 40]
    #
    # for value in first:
    #     print(value)
    #
    # for value in second:
    #     print(value)
    #
    # Use different input terms:
    # Complexity:

    # Snippet 8
    # for left_value in first:
    #     for right_value in second:
    #         print(left_value, right_value)
    #
    # Use different input terms:
    # Complexity:

    pass


# ============================================================
# SECTION D: LIST PITFALLS
# ============================================================

def list_pitfalls():
    """
    Explain what is wrong or surprising in each example.
    """

    # Pitfall 1: Aliasing
    #
    # first = [1, 2, 3]
    # second = first
    # second.append(4)
    #
    # What is first now?
    # Why?
    # How would you create an independent shallow copy?

    # Pitfall 2: Removing while traversing
    #
    # numbers = [1, 2, 2, 2, 3]
    #
    # for number in numbers:
    #     if number == 2:
    #         numbers.remove(number)
    #
    # Why can this skip elements?
    # Write a safer solution.

    # Pitfall 3: Incorrect nested-list creation
    #
    # matrix = [[0] * 3] * 3
    # matrix[0][0] = 9
    #
    # Why do multiple rows change?
    # Write the correct version using a list comprehension.

    # Pitfall 4: Modifying during index traversal
    #
    # numbers = [1, 2, 3, 4]
    #
    # for index in range(len(numbers)):
    #     numbers.pop()
    #
    # Why can index-based modification become unsafe?

    pass


# ============================================================
# OPTIONAL BONUS EXERCISES
# ============================================================

def find_minimum(numbers):
    """
    BONUS 1:
    Return the smallest value.

    Return None for an empty list.

    Do not use min().
    """
    pass


def calculate_average(numbers):
    """
    BONUS 2:
    Return the average.

    Return None for an empty list.

    Do not use sum().
    """
    pass


def merge_arrays(first, second):
    """
    BONUS 3:
    Return a new list containing first followed by second.

    Do not use:
        first + second
        extend()
    """
    pass


def flatten_matrix(matrix):
    """
    BONUS 4:
    Flatten a 2D list.

    Example:
        flatten_matrix([[1, 2], [3, 4]])
        -> [1, 2, 3, 4]
    """
    pass


# ============================================================
# TEST HELPER
# ============================================================

def print_test(test_name, actual, expected):
    status = "PASS" if actual == expected else "FAIL"

    print(f"{status}: {test_name}")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")
    print()


# ============================================================
# AUTOMATED TESTS
# ============================================================

def run_tests():
    """
    These tests will fail until the functions are completed.

    Recommended usage:
        1. Complete one function.
        2. Uncomment only its tests.
        3. Run the file.
        4. Fix failures before moving on.
    """

    print("=" * 64)
    print("ARRAYS, LISTS, AND BIG-O PRACTICE TESTS")
    print("=" * 64)
    print()

    print_test("calculate_sum normal", calculate_sum([10, 20, 30]), 60)
    print_test("calculate_sum empty", calculate_sum([]), 0)

    print_test("find_maximum positive", find_maximum([4, 9, 2, 7]), 9)
    print_test(
        "find_maximum negative",
        find_maximum([-8, -3, -12, -5]),
        -3,
    )
    print_test("find_maximum empty", find_maximum([]), None)

    print_test(
        "count_occurrences multiple",
        count_occurrences([1, 2, 2, 3, 2], 2),
        3,
    )
    print_test(
        "count_occurrences absent",
        count_occurrences([1, 2, 3], 8),
        0,
    )

    print_test(
        "find_first_index exists",
        find_first_index([8, 4, 6, 4], 4),
        1,
    )
    print_test(
        "find_first_index absent",
        find_first_index([8, 4, 6], 10),
        -1,
    )

    print_test(
        "count_number_types",
        count_number_types([-2, 0, 4, -1, 7, 0]),
        {"positive": 2, "negative": 2, "zero": 2},
    )

    print_test(
        "find_all_indexes multiple",
        find_all_indexes([5, 2, 5, 7, 5], 5),
        [0, 2, 4],
    )
    print_test(
        "find_all_indexes absent",
        find_all_indexes([1, 2, 3], 9),
        [],
    )

    print_test(
        "is_sorted_ascending sorted",
        is_sorted_ascending([1, 2, 2, 5]),
        True,
    )
    print_test(
        "is_sorted_ascending unsorted",
        is_sorted_ascending([1, 4, 3, 5]),
        False,
    )
    print_test("is_sorted_ascending empty", is_sorted_ascending([]), True)

    print_test(
        "find_second_largest normal",
        find_second_largest([10, 5, 8, 10, 3]),
        8,
    )
    print_test(
        "find_second_largest all equal",
        find_second_largest([7, 7, 7]),
        None,
    )
    print_test(
        "find_second_largest negative",
        find_second_largest([-2, -8, -3]),
        -3,
    )

    values = [1, 2, 3, 4, 5]
    reverse_in_place(values)
    print_test("reverse_in_place", values, [5, 4, 3, 2, 1])

    print_test(
        "filter_even_numbers",
        filter_even_numbers([1, 2, 3, 4, 5, 6]),
        [2, 4, 6],
    )

    values = [-4, 2, -1, 5, 0]
    replace_negatives_with_zero(values)
    print_test(
        "replace_negatives_with_zero",
        values,
        [0, 2, 0, 5, 0],
    )

    print_test(
        "remove_all_occurrences",
        remove_all_occurrences([1, 3, 2, 3, 4, 3], 3),
        [1, 2, 4],
    )

    print_test(
        "remove_duplicates",
        remove_duplicates([4, 2, 4, 1, 2, 3]),
        [4, 2, 1, 3],
    )

    values = [0, 1, 0, 3, 12]
    move_zeroes_to_end(values)
    print_test("move_zeroes_to_end", values, [1, 3, 12, 0, 0])

    values = [10, 20, 30, 40]
    insert_at(values, 2, 99)
    print_test(
        "insert_at middle",
        values,
        [10, 20, 99, 30, 40],
    )

    values = [10, 20, 30, 40]
    delete_at(values, 1)
    print_test("delete_at middle", values, [10, 30, 40])

    print_test(
        "calculate_row_sums",
        calculate_row_sums(MATRIX),
        [6, 15, 24],
    )

    test_matrix = [
        [4, 8, 2],
        [7, 5, 1],
    ]

    print_test(
        "find_in_matrix exists",
        find_in_matrix(test_matrix, 5),
        (1, 1),
    )
    print_test(
        "find_in_matrix absent",
        find_in_matrix(test_matrix, 10),
        (-1, -1),
    )


# ============================================================
# READINESS CHECKLIST
# ============================================================

READINESS_CHECKLIST = """
READINESS CHECKLIST
===================

Before starting Practice Test 1: List Interview Questions:

[ ] I can use the Python array module for basic operations.
[ ] I understand arrays conceptually use indexed storage.
[ ] I can traverse using values, indexes, and enumerate().
[ ] I can use slicing without confusing start and stop indexes.
[ ] I can write a basic and conditional list comprehension.
[ ] I understand aliasing versus copying a list.
[ ] I avoid unsafe removal while iterating over the same list.
[ ] I can calculate sum, maximum, counts, and search manually.
[ ] I can compare adjacent values using index + 1.
[ ] I can reverse a list using two indexes.
[ ] I understand in-place versus new-result solutions.
[ ] I understand why middle insertion and deletion are O(n).
[ ] I can describe O(1), O(n), O(n^2), and O(log n).
[ ] I can drop constants and non-dominant terms.
[ ] I can use different variables for different inputs.
[ ] I can describe matrix traversal as O(r * c).
[ ] I have re-solved at least 5 exercises without looking.

Once most boxes are checked, start the course interview questions.
Do not wait for perfect confidence.
"""


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print(READINESS_CHECKLIST)

    # Complete functions gradually.
    # Uncomment this only when you want to run the tests.
    #
    # run_tests()
