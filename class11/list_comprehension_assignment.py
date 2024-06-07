#Nested loops comprehension

print("=="*50)
l = [i + j + k for i in range(3) for j in range(3) for k in range(3)]
print("[i + j + k for i in range(3) for j in range(3) for k in range(3)]")
print(l)
print("=="*50)
l = [chr(index) for index in [118, 97, 114, 110, 105, 107, 97]]
print("[chr(index) for index in [118, 97, 114, 110, 105, 107, 97]]")
print(l)
print("=="*50)
l = [ True if ele in "aeiou" else False for ele in "The Great Saga"]
print('[ True if ele in "aeiou" else False for ele in "The Great Saga"]')
print(l)
print("=="*50)
l = ["x"*i*j for i in range(5,1,-1) for j in range(1,3) if i+j <6 ]
print('["x"*i*j for i in range(5,1,-1) for j in range(1,3) if i+j <6 ]')
print(l)
print("=="*50)
l = [ ele.upper() if ele in ["aa","bb", "cc", "dd"] else ele.title() for ele in [ chr(k)+chr(j) for k in range(ord('a'), ord('e')) for j in range(ord('a'), ord('e')) ]]
print('[ ele.upper() if ele in ["aa","bb", "cc", "dd"] else ele.title() for ele in [ chr(k)+chr(j) for k in range(ord("a"), ord("e")) for j in range(ord("a"), ord("e")) ]]')
print(l)
print("=="*50)