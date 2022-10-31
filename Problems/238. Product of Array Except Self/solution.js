/**
 * @param {number[]} nums
 * @return {number[]}
 */
 const productExceptSelf = nums => {
  let totalProduct = 1;
  let productWithoutZero = 1;
  let onlyZeros = true;
  let seenZero = false;
  for (let i = 0; i < nums.length; i++) {
      if (nums[i] === 0) {
          if (seenZero) {
              productWithoutZero *= 0;
          } else {
              seenZero = true;
          }
      } else {
          productWithoutZero *= nums[i];
          onlyZeros = false;
      }
      totalProduct *= nums[i];
  }
  
  const ans = [];
  for (let i = 0; i < nums.length; i++) {
      if (nums[i] === 0) {
          ans.push(onlyZeros ? 0 : productWithoutZero);
      } else {
          ans.push(totalProduct / nums[i]);   
      }
  }
  
  return ans;
};

// Time complexity: O(n)
// Space complexity: O(1), without taking into consideration the ans array.
// Pattern: Arrays
// Time used: Didn't count it but roughly 35-40min