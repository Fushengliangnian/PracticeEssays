UNDEFINED = object()

fn = lambda x: UNDEFINED if str(x).lower() == 'all' else True if str(x).lower() == 'true' else False

print(UNDEFINED, type(UNDEFINED))
if UNDEFINED:
    print("True")
else:
    print("False")

print(fn("true"))


def func(x):
    if str(x).lower() == 'all':
        return UNDEFINED
    else:
        if str(x).lower() == 'true':
            return True
        else:
            return False


lia = [8, 897.8, 754, 5]
print(lia.index(8))
