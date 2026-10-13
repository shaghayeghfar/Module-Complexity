/**
 * Remove duplicate values from a sequence, preserving the order
 * of the first occurrence of each value.
 *
 * The original code used two loops to check whether each value
 * was already in the result array.
 *
 * I changed the code to use a Set. A Set stores each value only
 * once and keeps the order in which values were added.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * The original time complexity was O(n^2) because we searched
 * the result array for every item in the input array.
 *
 * The new time complexity is O(n) on average because we go
 * through the input array once.
 *
 * The space complexity is O(n) because we may need to store
 * all the unique items in the Set and the returned array.
 *
 * O(n) is optimal because we need to check every item in
 * the input array to find all unique values.
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  // Create a Set to store unique items
  const uniqueItems = new Set();

  // Go through the input array and add each item to the Set
  for (const item of inputSequence) {
    uniqueItems.add(item);
  }

  // Convert the Set back into an array
  return [...uniqueItems];
}
