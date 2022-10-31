/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 const isIsomorphic = (s, t) => {
  const mapS = {};
  const mapT = {};
  
  for (let i = 0; i < s.length; i++) {
      if ((s[i] in mapS && mapS[s[i]] !== t[i]) || (t[i] in mapT && mapT[t[i]] !== s[i])) {
          return false;
      }
      mapS[s[i]] = t[i];
      mapT[t[i]] = s[i];
  }
  
  return true;
};

// Time complexity; O(n)
// Space complexity: O(n)
// Pattern: Arrays & Hashing
// Time used: 16min (Had to briefly watch NeetCode's explanation of the problem to understand it)