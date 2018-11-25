import fibo
#fibo.fib(1000)
#print(fibo.fib2(1000))
#print(fibo.__name__)
myfib = fibo.fib
#print(myfib.__name__)
#myfib(500)
import fibo as biff
#biff.fib(500)
from fibo import fib as fibonacci
#fibonacci(300)

#print(dir(fibo))   # Names imported from fibo module

#print(dir())        # All names currently defined

import builtins
print(dir(builtins))     # All built-in functions and variables

# One of the variable mentioned in builtins is 'credits'
# Now that 'import builtins' is commented out, look at credits
#print(credits)
