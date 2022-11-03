/**
 * @param {string} s
 * @return {string[]}
 */

// NOTES:
// - Can I get an empty string? In that case, should I return an empty array?

// "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
//   l         r
// set = {"AAAAACCCCC", "AAAACCCCCAA"}
// current string = "AAAACCCCCAA"
// ans = []

const findRepeatedDnaSequences = s => {
  if (s.length < 10) {
      return [];
  }
  
  const seen = new Set();
  const ans = new Set();
  
  for (let i = 9; i < s.length; i++) {
      const sub = s.slice(i - 9, i + 1);
      if (seen.has(sub)) {
          ans.add(sub);
      } else {
          seen.add(sub);
      }
  }
  
  return [...ans];
};

// Looked at solution after 25 min. Completely stuck.

//                                      IMPORTANT NOTE
// =======================================================================================
// My approach was correct. After watching NeetCode's video, I realised that using the 
// built-in "slice" function of the language is ok, I just thought it wasn't allowed. If
// it's allowed, then this problem is very trivial. The only part that I missed was adding
// the repeated sub strings into a set before turning them into an array, to avoid repeated
// strings in the solution array. 

// I believe NeetCode's time complexity analysis is wront tho. He says it's O(n), but for
// each character in the input string you're using slice, which probably takes O(n) time. So, 
// the time complexity should be O(n^2), because for n characters we are doing n additional 
// iterations. It can also be O(n * m), where n is the length of the input string and m is
// the length of each one of the sub strings, which we know is always 10 in this case, so 
// time copmlexity can be O(n * 10). But then, would this in the end be O(n)???

// After looking at the discussion section, yes. It looks like the time complexity, indeed, 
// is O(n) because m will always be equal to 10, so it's a constant and we can drop the 
// constants. 

// Time complexity: O(n)
// Space complexity: O(n), where n is the length of the input string. 
// Pattern: Arrays & Hashing, Sliding Window.
