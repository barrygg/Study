# Sort of built-in function range
class MyError(Exception):
    def __init__(self, text):
        self.txt = text 

		
def my_range(*args):
    try:
        if len(args) == 3:
	    start = args[0]
	    stop = args[1]
	    step = args[2]
	elif len(args) == 2:
	    start = 0
	    stop = args[0]
	    step = args[1]
        elif len(args) == 1:
	    start = 0
	    stop = args[0]
	    step = 1
	else:
	    raise MyError('Too many or no arguments')
		
	for a in args:
	    if isinstance(a, int) is False:
	        raise MyError('Not integer arguments')
		
	if step == 0:
	    raise MyError("Step shouldn't be zero")
		
	if start >= stop and step > 0 or stop >= start and step < 0:
	    raise MyError('Wrong arguments order')
		
	i = start
        result=[]
        if step > 0:
            while i < stop:
                result.append(i)
                i += step
        elif step < 0:
            while i > stop:
                result.append(i)
                i += step
        return result
	except MyError as mr:
	    print(mr)

