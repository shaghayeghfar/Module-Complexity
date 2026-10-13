/**
 * Finds common items between two arrays.
 *
 * The original code used includes() to search the second array
 * for each item in the first array. This can take a long time
 * when the arrays are large.
 *
 * I changed the code to use a Set for faster searching.
 * First, we store the items from the second array in a Set.
 * Then, we check which items from the first array are in the Set.
 * We use another Set to remove duplicate items from the result.
 *
 * Time Complexity: O(n + m)
 * Space Complexity: O(n + m)
 * Optimal Time Complexity: O(n + m)
 *
 * The original time complexity was O(n * m) because we searched
 * the second array for every item in the first array.
 *
 * The new time complexity is O(n + m) on average because
 * we create a Set and then check the items in the first array.
 *
 * The space complexity is O(n + m) because the Sets and the
 * resulting array can store items from the input arrays.
 *
 * O(n + m) is optimal because we need to check the arrays
 * to find their common items.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);

  const commonItems = firstArray.filter((item) => secondSet.has(item));

  return [...new Set(commonItems)];
};
