"""
Counts the occurrences of a binary pattern in the binary Fibonacci sequence.

In this problem binary fibonacci means the concatenation of binary bits like following:

f(0) = 0
f(1) = 1
f(2) = f(1) + f(0) = 10
f(3) = f(2) + f(1) = 101
f(4) = f(3) + f(2) = 10110
f(5) = f(4) + f(3) = 10110101
f(6) = f(5) + f(4) = 1011010110110
...

Given a binary pattern, you need to count the number of occurences of the pattern in the binary fibonacci sequence.

Input:
pattern = 10
n = 6

Output:
5

Explanation:
The binary fibonacci sequence is:
f(6) = 1011010110110
10_1_10_10_1_10_1_10
The pattern 10 occurs 5 times in the sequence. (1-2, 4-5, 6-7, 9-10, 12-13)
"""

from typing import Union, Dict


def bin_to_dec(n: Union[str, int]) -> int:
    """
    Converts a binary number to its decimal representation.

    Args:
    - n: A binary number (either as a string or an integer).

    Returns:
    - int: The decimal representation of the binary number.
    """
    assert isinstance(n, str) or isinstance(
        n, int), "Input must be a string or an integer!"
    dec = 0
    for i, bit in enumerate(reversed(str(n))):
        dec += int(bit) * (2 ** i)
    return dec


def no_of_bits(n: int) -> int:
    """
    Determines the number of bits required to represent an integer.

    Args:
    - n: An integer.

    Returns:
    - int: The number of bits required to represent the integer.
    """
    assert isinstance(n, int), "Input must be an integer!"
    if n == 0:
        return 1
    return n.bit_length()


def num2bin(n: int) -> str:
    """
    Converts an integer to its binary representation.

    Args:
    - n: An integer.

    Returns:
    - str: The binary representation of the integer.
    """
    return bin(n)[2:]


def binary_fibonacci(n: int) -> int:
    """
    Calculates the binary Fibonacci number at a given index.

    Args:
    - n: An index for the binary Fibonacci sequence.

    Returns:
    - int: The binary Fibonacci number at the specified index.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    fn_2, fn_1 = 0, 1
    for _ in range(2, n+1):
        bit_len = no_of_bits(fn_2)
        fn = (fn_1 << bit_len) | fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn


class Solution:
    @staticmethod
    def count_using_string_matching(pattern: str, n: int) -> int:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence using string matching.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - int: The count of occurrences of the pattern.
        """
        fib_n = binary_fibonacci(n)
        pattern_num = bin_to_dec(pattern)
        n_bin = num2bin(fib_n)
        pattern_bin = num2bin(pattern_num)
        pattern_len = len(pattern_bin)
        n_bin_len = len(n_bin)

        count = 0
        for idx in range(n_bin_len - pattern_len + 1):
            # Check if the substring matches the pattern
            if n_bin[idx:idx+pattern_len] == pattern_bin:
                count += 1
            idx += 1

        return count

    @staticmethod
    def count_using_logical_operations(pattern: str, n: int) -> int:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence using logical operations.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - int: The count of occurrences of the pattern.
        """
        n_fib = binary_fibonacci(n)
        pattern_num = bin_to_dec(pattern)
        pattern_len = no_of_bits(pattern_num)
        n_len = no_of_bits(n_fib)

        pattern_mask = (1 << pattern_len) - 1
        shifted_n_fib = n_fib << 1
        count = 0

        for _ in range(n_len - pattern_len + 1):
            shifted_n_fib >>= 1
            masked_n_fib = shifted_n_fib & pattern_mask
            if masked_n_fib == pattern_num:
                count += 1

        return count

    def count_following_pattern_in_count_sequence(self, pattern: str, n: int) -> int:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence
        by observing the pattern in the counts of Fibonacci numbers.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - int: The count of occurrences of the pattern.
        """
        pattern_len = no_of_bits(bin_to_dec(pattern))
        break_count = 0
        idx = 1
        fib_dict = {}
        # Find the first five count in binary fibonacii sequence where the length of the binary representation is sufficient
        while break_count != 5:
            n_fib = binary_fibonacci(idx)
            n_bin_len = no_of_bits(n_fib)

            if n_bin_len >= pattern_len:
                fib_dict[idx] = self.count_using_logical_operations(
                    pattern, idx)
                break_count += 1
            idx += 1
		
		# Check if the last five count in binary fibonacii sequence form the desired pattern in their counts
        fib_dict_items = list(fib_dict.items())
        fib_pattern_in_counts = []
        for _ in range(len(fib_dict_items)-2):
            _, last_count = fib_dict_items.pop()
            _, second_last_count = fib_dict_items[-1]
            _, third_last_count = fib_dict_items[-2]
            fib_pattern_in_counts.append(last_count == (
                second_last_count + third_last_count + 1))

        follows_fib_pattern = all(fib_pattern_in_counts)
		
		# Check if there is an alternate plus one pattern in the counts of binary fibonacii sequence
        alternate_plus_one_fib_pattern = False
        fib_dict_items = list(fib_dict.items())
        for idx in range(len(fib_dict_items)-2):
            last_n, last_count = fib_dict_items.pop()
            _, second_last_count = fib_dict_items[-1]
            _, third_last_count = fib_dict_items[-2]
            if last_count == (second_last_count + third_last_count + 1):
                alternate_plus_one_fib_pattern = True
                break

        if n in fib_dict:
            return fib_dict[n]

        add_one = follows_fib_pattern | alternate_plus_one_fib_pattern

        last_count = fib_dict[last_n]
        second_last_count, third_last_count = fib_dict[last_n -
                                                       1], fib_dict[last_n-2]
		
		# Calculate the counts of pattern in binary fibonacii numbers up to the desired index
        for _ in range(last_n, n+1):
            last_count = second_last_count + third_last_count
            if add_one:
                if follows_fib_pattern:
                    last_count += 1
                elif alternate_plus_one_fib_pattern:
                    last_count += 1
                    alternate_plus_one_fib_pattern = False
                else:
                    alternate_plus_one_fib_pattern = True

            third_last_count, second_last_count = second_last_count, last_count

        return last_count

    def count_binary_pattern_occurences_in_binary_fibonacci(self, pattern: str, n: int) -> Dict[str, int]:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence
        using multiple methods and returns the counts.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - Dict[str, int]: A dictionary containing counts using different methods.
        """
        results = {}
        # Using string matching
        results["string_matching"] = self.count_using_string_matching(
            pattern, n)
        # Using logical operations
        results["logical_operations"] = self.count_using_logical_operations(
            pattern, n)
        # Using following pattern in count sequence
        results["following_pattern_in_count_sequence"] = self.count_following_pattern_in_count_sequence(
            pattern, n)
        return results

    def count_binary_pattern(self, pattern: str, n: int) -> int:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence
        up to a given index.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - int: The count of occurrences of the pattern.
        """
        return self.count_using_string_matching(pattern, n)

    def count_binary_pattern_upto_n(self, pattern: str, n: int) -> Dict[int, int]:
        """
        Counts the occurrences of a binary pattern in the binary Fibonacci sequence
        up to each index up to n.

        Args:
        - pattern: The binary pattern to search for.
        - n: The index up to which to search in the binary Fibonacci sequence.

        Returns:
        - Dict[int, int]: A dictionary containing counts up to each index.
        """
        results = {}
        for i in range(n+1):
            results[i] = self.count_binary_pattern(pattern, i)
        return results


def test_binary_fibonacci():
    test_1 = num2bin(binary_fibonacci(0))
    assert test_1 == "0", f"Test case 1 failed! Expected: 0, Got: {test_1}"
    test_2 = num2bin(binary_fibonacci(1))
    assert test_2 == "1", f"Test case 2 failed! Expected: 1, Got: {test_2}"
    test_3 = num2bin(binary_fibonacci(2))
    assert test_3 == "10", f"Test case 3 failed! Expected: 10, Got: {test_3}"
    test_4 = num2bin(binary_fibonacci(3))
    assert test_4 == "101", f"Test case 4 failed! Expected: 101, Got: {test_4}"
    test_5 = num2bin(binary_fibonacci(4))
    assert test_5 == "10110", f"Test case 5 failed! Expected: 10110, Got: {test_5}"
    test_6 = num2bin(binary_fibonacci(5))
    assert test_6 == "10110101", f"Test case 6 failed! Expected: 10110101, Got: {test_6}"
    test_7 = num2bin(binary_fibonacci(6))
    assert test_7 == "1011010110110", f"Test case 7 failed! Expected: 1011010110110, Got: {test_7}"


def test_count_binary_pattern():
    sol = Solution()

    test_1 = sol.count_binary_pattern_occurences_in_binary_fibonacci("10", 6)
    assert test_1 == {"string_matching": 5, "logical_operations": 5,
                      "following_pattern_in_count_sequence": 5}, f"Test case 1 failed! Expected: 5, Got: {test_1}"

    test_2 = sol.count_following_pattern_in_count_sequence(
        "10110101101101", 96)
    assert test_2 == 7540113804746346428, f"Test case 2 failed! Pattern: 10110101101101, n: 96, Expected: 7540113804746346428, Got: {test_2}"


if __name__ == "__main__":
    test_binary_fibonacci()
    test_count_binary_pattern()
    print("All test cases passed!")
