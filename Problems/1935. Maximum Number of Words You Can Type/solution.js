/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
 const canBeTypedWords = (text, brokenLetters) => {
  const broken = new Set(brokenLetters); // O(brokenLetters.length)
  let counter = 0;
  let brokenWord = false;
  
  for (let i = 0; i < text.length; i++) {
      brokenWord = false;
      while (i < text.length && text[i] !== " ") {
          if (broken.has(text[i])) {
              brokenWord = true
          }
          i++;    
      }
      if (!brokenWord) {
          counter++;   
      }
  }
  
  return counter;
};

// Time complexity: O(n + m), where n is the length of the string and m is the length of brokenLetters.
// SPace complexity: O(m)
// Pattern: Arrays & Hashing
// Time used: 32min

