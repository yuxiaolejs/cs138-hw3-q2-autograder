
import subprocess
import threading

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

def run(string):
    try:
        result = subprocess.run(['mentor', 'q2.cfg', 'accept', string], capture_output=True, text=True, check=True)
        act = result.stdout.strip()
        expected = "Input is accepted." if isValid(string) else "Input is not accepted."
        if act != expected:
            print("Failed for string: ----- ", string)
            print("  Expected:", expected)
            print("  Actual:", act)
    except subprocess.CalledProcessError:
        print("Failed to run command.")

def generate_string_sequential(n,length):
    string = ""
    while n > 0:
        string = chr(97 + n % 3) + string
        n = n // 3
    while len(string) < length:
        string = "a" + string
    return string

def test_string_size(len, size):
    print("Length of ", len, "has",size, "strings")
    for j in range(0, size):
        run(generate_string_sequential(j, len))
        print("Tested:", j, "/", size, end="\r")

def test_sequential(num):
    threads = []
    for i in range(1, num + 1):
        size =  3 ** (i)
        thread = threading.Thread(target=test_string_size, args=(i, size))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

def test(num):
    for _ in range(num):
        string = generate_string_sequential(100)
        run(string)


test_sequential(18)