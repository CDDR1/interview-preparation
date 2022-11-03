/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */

// notes: 
// - needle might be longer than haystack.

// EXAMPLE:
// haystack = "codiiseawng iseat fun and iseat niseaw"  
//                 i

// needle = "iseaw"
//           j

const strStr = (haystack, needle) => {
  if (needle.length > haystack.length) {
      return -1;
  }
  
  let j = 0;
  for (let i = 0; i <= haystack.length; i++) {
      if (haystack[i] === needle[j]) {
          const firstOcurrenceIndex = i;
          let foundOcurrence = true;
          for (j = 1; j < needle.length; j++) {
              if (haystack[i + j] !== needle[j]) {
                  // i += j;
                  j = 0;
                  foundOcurrence = false;
                  break;
              }
          }
          if (foundOcurrence) {
              return i;   
          }
      }
  }
  
  return -1;
};

// Time complexity: O(n * m)
// Space complexity: O(1)
// Pattern: Arrays
// Time used: 45min