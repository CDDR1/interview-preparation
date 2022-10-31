/**
 * @param {string[]} emails
 * @return {number}
 */

// Notes: 
// - can arr be empty? no
// - can there be empty strings? no
// - carl@leetcode.com

const numUniqueEmails = emails => {
  const uniqueEmails = new Set();
  
  for (const email of emails) {
      let filteredEmail = "";
      let i = 0;
      while (email[i] !== "+" && email[i] !== "@") {
          if (email[i] !== ".") {
              filteredEmail += email[i];
          }
          i++;
      }
      
      while (email[i] !== "@") {
          i++;
      }
      
      for (let j = i; j < email.length; j++) {
          filteredEmail += email[j];
      }
      
      uniqueEmails.add(filteredEmail);
  }

  return uniqueEmails.size;
};

// Time complexity: O(n * m), where n is the length of the emails array
//                  and m is the average length of the strings inside the array.

// Space complexity: O(n)
// Pattern: Arrays
// Time used before looking at solution: 33min