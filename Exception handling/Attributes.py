try:
    try:
        raise TypeError
    except ValueError:
        print("inner Exception handled ")
        print("next command")
except TypeError:
 print("outer Exception handled")
else:
 print("no Exceptions")
