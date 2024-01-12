'''Create a function eq_all that determines if all elements of any iterable are equal; the iterable may be infinite. Return value is a bool.

Examples
eq_all('aaa')   : True
eq_all('abc')   : False
eq_all('')      : True

eq_all([0,0,0]) : True
eq_all([0,1,2]) : False
eq_all([])      : True'''

# code
def eq_all(iterable):
    # iter() to create an iterator from the iterable
    iterator = iter(iterable)
    
    try:
        ref_val = next(iterator)
    except StopIteration:
        # If the iterable is empty, return True
        return True
    return all(element == ref_val for element in iterator)
