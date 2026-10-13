/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Original code used two separate loops:
 * - The first loop calculated the sum.
 * - The second loop calculated the product.
 *
 * I changed the code to use one loop for both calculations.
 * This means we do not need to go through the array twice.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * Time complexity is O(n) because we need to visit every number.
 * Space complexity is O(1) because we use a fixed number of variables.
 * O(n) is the best possible time complexity for this task.
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  // Calculate the sum and product in the same loop
  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}
