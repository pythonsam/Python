def sub(a,b):
    return a - b

def add(a, b):
    return a + b

def test_add():
    r = add(5, 5)
    rv = add(10, 10)
    print(' \n\n ::: ADD is ::: \n')
    assert r == 10, ' Add is not working'
    assert rv == 20, ' Add is not working'

def test_sub():
    r = sub(10,5)
    print(' \n\n ::: SUB is ::: \n')
    assert r == 5, 'sub function is not working'

def test_string():
    s = 'sriram'
    print(' \n\n ::: STRING is ::: \n')
    assert isinstance(s, str), 'sub function is not working'


