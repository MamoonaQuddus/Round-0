from math import gcd
from collections import defaultdict

# Function to calculate the maximum number of points that lie on a line
def calculateMaxPoints(n, points):
maxPoints = 0

    for i in range(n):
slope_map = defaultdict(int)  # Dictionary to store the slope frequencies
sameX = 0  # To count vertical lines
samePoint = 0  # To count identical points

        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
dy = points[j][1] - points[i][1]

            if dx == 0 and dy == 0:
                # If points are the same
samePoint += 1
elif dx == 0:
                # If x-coordinates are the same (vertical line)
sameX += 1
            else:
                # Reduce (dx, dy) by their greatest common divisor to normalize the slope
                g = gcd(dx, dy)
                dx //= g
dy //= g

                # Ensure the direction of the slope is consistent by making dx positive
                if dx < 0:
                    dx = -dx
dy = -dy

                # Add the slope as a pair (dx, dy) to the dictionary
slope_map[(dx, dy)] += 1

        # Update maxPoints with the maximum frequency for vertical lines
maxPoints = max(maxPoints, sameX + samePoint + 1)

        if slope_map:
            # Calculate the maximum frequency for the slopes
maxSlopeCount = max(slope_map.values())
maxPoints = max(maxPoints, maxSlopeCount + samePoint + 1)

    # Return the maximum number of points on a line
    return maxPoints

# Main function
def main():
    t = int(input())  # Number of test cases

    for testCase in range(t):
        n = int(input())  # Number of points

        # Read the points
        points = [tuple(map(int, input().split())) for _ in range(n)]

        # Calculate the maximum number of points that lie on a line
maxPoints = calculateMaxPoints(n, points)

        # Print the result as the minimum number of points that need to be moved
print(f"Case #{testCase + 1}: {n - maxPoints}")

# Call the main function
if __name__ == "__main__":
main()
