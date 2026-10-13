/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * The original code used two loops to check every possible pair
 * of numbers. This can take a long time when the array is large.
 *
 * I changed the code to use a Set to remember the numbers
 * we have already checked.
 *
 * For each number, we calculate the number we need to find
 * to reach the target. If we have already seen that number,
 * we return true.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * The original time complexity was O(n^2) because we used
 * two loops to check the pairs of numbers.
 *
 * The new time complexity is O(n) on average because we
 * only need to go through the array once.
 *
 * The space complexity is O(n) because the Set can store
 * up to all the numbers in the array.
 *
 * O(n) is the optimal time complexity for this approach
 * because we may need to check every number in the array.
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seenNumbers = new Set();

  for (const num of numbers) {
    const neededNumber = target - num;

    // Check if we have already seen the number we need
    if (seenNumbers.has(neededNumber)) {
      return true;
    }

    // Remember this number for the next checks
    seenNumbers.add(num);
  }

  return false;
}
