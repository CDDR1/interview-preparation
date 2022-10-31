/**
 * @param {number[]} nums
 * @return {number}
 */
 const majorityElement = nums => {
  const map = {};
  
  for (const num of nums) {
      if (num in map) {
          map[num]++;
      } else {
          map[num] = 1;
      }
  }
  
  const halfLength = nums.length / 2;
  for (const num of nums) {
      if (map[num] > halfLength) {
          return num;
      }
  }
};

// Time complexity: O(n)
// Space complexity: O(n)
// Pattern: Arrays & Hashing
// Time used: 9min

