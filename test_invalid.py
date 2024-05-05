# Open the file in read mode
file = open('gen.out', 'r')

# Read the contents of the file
content = file.read()

# Close the file
file.close()

# Print the contents
arr = content.split("\n")

def isValid(str):
    a = 0
    b = 0
    flag = False
    for i in range(len(str)):
        if str[i] == 'c':
            flag = True
        if flag:
            if str[i] == 'b':
                b += 1
        else:
            if str[i] == 'a':
                a += 1
    return a > b

def testInvalid():
    for i in range(len(arr)):
        if not isValid(arr[i]):
            print("Invalid string: " + arr[i])
            
testInvalid()