class MyHashSet {
  constructor() {
      this.items = [];
  }
  
  add(key) {
      for (const item of this.items) {
          if (item === key) {
              return;
          }
      }
      
      this.items.push(key);
  }
  
  remove(key) {
      for (let i = 0; i < this.items.length; i++) {
          if (this.items[i] === key) {
              this.items[i] = -1;
          }
      }
  }
  
  contains(key) {
      for (const item of this.items) {
          if (item === key) {
              return true;
          }
      }
      
      return false;
  }
}

// Time complexity: O(n)
// Space complexity: O(n)
// Pattern: Arrays & Hashing
// Time used: 13 min




