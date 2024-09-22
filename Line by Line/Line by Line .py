import math

def calculate_percentage_increase(n, p):
    """
    Calculates the percentage increase required for the N-line solution to have
    an equal chance of success as the (N-1)-line solution.

Args:
    n (int): The number of lines in the original solution.
    p (float): The original success percentage.

    Returns:
    float: The percentage increase required.
    """
    # Convert p from a percentage to a fraction
p_fraction = p / 100.0

    # Calculate the new percentage that makes success rate of N lines equal to (N-1) lines
p_new_fraction = math.pow(p_fraction, (n - 1) / n)

    # Convert back to percentage
p_new = p_new_fraction * 100.0

    # Return the increase required
    return p_new - p

def read_test_case():
    """
    Reads and validates input for a single test case.
    """
    n, p = map(float, input().split())
    n = int(n)

    if n < 2 or n > 1000 or p < 1 or p > 99:
        raise ValueError("Invalid input: test case has invalid values.")

    return n, p

def main():
    try:
test_cases = int(input())
    except ValueError:
print("Invalid input: unable to read test cases.")
        return

    if test_cases<= 0:
print("Invalid input: number of test cases must be positive.")
        return

    for i in range(test_cases):
        try:
            n, p = read_test_case()
percentage_increase = calculate_percentage_increase(n, p)

            # Output the result formatted to 6 decimal places
print(f"Case #{i + 1}: {percentage_increase:.6f}")
        except Exception as e:
print(f"Error in test case {i + 1}: {str(e)}")

if __name__ == "__main__":
main()
