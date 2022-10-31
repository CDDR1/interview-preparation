/**
 * @param {number[]} nums
 * @return {number[]}
 */
// NOTES:
// - does the order of the elements in the output array matter? No.
// - Can I get an empty array? No, size will be at least 1. 
// - Can I assume that the numbers are only integers? Yes.

const findDisappearedNumbers = nums => {
  const seen = new Set();
  
  for (const num of nums) {
      seen.add(num);
  }
  
  const ans = [];
  for (let i = 1; i <= nums.length; i++) {
      if (!(seen.has(i))) {
          ans.push(i);
      }
  }
  
  return ans;
};

// Time complexity: O(n)
// Space complexity: O(n)
// Pattern: Arrays & Hashing
// TIme used: 12min