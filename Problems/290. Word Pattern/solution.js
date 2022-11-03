/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */

// NOTES: 
// - pattern will have at least one character.
// - only lowercase english characters for both strings.
// - not leading or trailling spaces.

// map1 = {"hello": 0,  "car": 3, "yellow": 2, }
// map2 = {"j": 0, "k": 3, "l": 2, }
// pattern = "jklk"  s = "hello car yellow car"

const wordPattern = (pattern, s) => {
  const words = [];
  let temp = "";
  
  for (let i = 0; i < s.length; i++) {
      if (s[i] !== " ") {
          temp += s[i];
      } else {
          words.push(temp);
          temp = "";
      }
      
      if (i === s.length - 1) {
          words.push(temp);
      }
  }
  
  
  if (words.length !== pattern.length) {
      return false;
  }
  
  const map1 = {};
  const map2 = {};
  
  for (let i = 0; i < pattern.length; i++) {
      if (pattern[i] in map2 && words[i] in map1) {
          // check value
          if (map2[pattern[i]] !== map1[words[i]]) {
              return false;
          }
          
          map2[pattern[i]] = i;
          map1[words[i]] = i;
      } 
      else if (!map2[pattern[i]] && !map1[words[i]]) {
          // add them into their respective maps
          map2[pattern[i]] = i;
          map1[words[i]] = i;
      } 
      else if ((!map2[pattern[i]] && words[i] in map1) || (pattern[i] in map2 && !map1[words[i]])) {
          console.log('here')
          return false;
      }
  }
  
  return Object.keys(map1).length === Object.keys(map2).length ? true : false;
};


// Time complexity: O(n + m), where n is the length of s and m is the length of pattern.
// Space complexity: O(m)
// Pattern: Arrays & Hashing
// Time used: 44min