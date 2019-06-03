

def f1():
    print("F1 executed")

def f2():
    print("F2 executed")

# When executed as script directly the value of attribute "__name__" will be "__main__"
# When being imported the value of attribute "__name__" will be the module name.
# For ex: the currnt module name would be as s1
if __name__ == "__main__":
    f1()
    f2()