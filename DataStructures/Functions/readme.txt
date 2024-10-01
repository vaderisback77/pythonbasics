Functions covered 
1. Lambda [param]: expression --> A single line function that runs an expression and returns a function object.

res = lambda x: x**2 
res(2)


2. map(func, iterables) --> runs func on the iterables and returns an iterator object (have to use list to see contents)

3. filter(func, iterable) --> Takes only a single iterable and returns an iterator object (have to use list to see contents). 
Also checks for a truthy condition and only returns the Truthy values 
0, "", None => False
Everything else => True

4. zip(iterables) --> Zips the elements of 2 or more iterables and returns an iterator object containing the tuple of elements of both 
iterables

5. List Comprehension (do x for x in iterable) --> Cleaner way of running a function on an iterable if you want to something on every element of the iterable

6. reduce(func, iterables) --> reduces runs the function starting from every element in the iterable until the last element 