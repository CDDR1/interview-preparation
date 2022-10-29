/**
 * @param {number[]} nums
 * @return {number}
 */
 var countDistinctIntegers = function(nums) {
  const set = new Set();
  for (const num of nums) {
      set.add(num);
      const temp = num.toString();
      if (temp.length >= 2) {
          let newS = "";
          for (let i = temp.length - 1; i >= 0; i--) {
              newS += temp[i];
          }
          set.add(parseInt(newS));
      }
  }
  
  return set.size;
};



// Time complexity: O(n * m) where n is the length of the array 
// and m is the average number of digits that each number of the array has. 

// Space complexity: O(n * m)
// Pattern: Arrays
// Time used: 28min