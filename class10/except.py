try:
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    print(a/b)
except Exception as err:
    print("Error:", err)