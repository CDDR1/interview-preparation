def encode(strs):
  encodedString = ""
  for word in strs:
    encodedString += str(len(word)) + ":" + word
  return encodedString

def decode(str):
  decodedString = []

  i = 0
  while i < len(str):
    currWordLen = ""
    while str[i] != ":":
      currWordLen += str[i]
      i += 1
      
    currWord = ""
    for j in range(i + 1, i + int(currWordLen) + 1):
      currWord += str[j]
    i = j + 1
    decodedString.append(currWord)
    
  return decodedString

a = encode(["lint","code","love","you"])
print(a)
b = decode(a)
print(b)

# Is worth noting that I wrote this code on repl.it because LintCode didn't
# let me log in, so I'm not 100% sure that this code beats all the test cases. 