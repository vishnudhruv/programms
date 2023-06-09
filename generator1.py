def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30
gen = mygenerator() 
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))