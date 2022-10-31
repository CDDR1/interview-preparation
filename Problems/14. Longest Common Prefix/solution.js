/**
 * @param {string[]} strs
 * @return {string}
 */
 const longestCommonPrefix = strs => {
  let longest = strs[0];
  
  for (let i = 1; i < strs.length; i++) {
      let temp = "";
      let j = 0;
      while (j < longest.length && j < strs[i].length && longest[j] === strs[i][j]) {
          temp += strs[i][j];
          j++;
      }
      longest = temp;
  }
  
  return longest;
};


// Time complexity: O(n * m)
// Space complexity: O(n * m)
// Pattern: Arrays
// Time spent: 21min