str="hello bro I'm Sheik"
# Now function PAUSES and REMEMBERS state. this is the power of generator in python. it can be used to generate a sequence of values over time, instead of computing them all at once and sending them back. this is useful when working with large datasets or when you want to create an infinite sequence of values.
"""Why Generators Are Powerful

Without generators:

nums = [1,2,3,4,5]

stores ALL values in memory.

Generators:

(i for i in range(1000000000))

produce one value at a time.

Extremely memory efficient.

Real World Use Cases

Generators are used heavily in:

AI pipelines
streaming APIs
ETL processing
large CSV reading
log processing
async systems
TensorFlow/PyTorch data loading"""    
def generator(str):
    for i in range(len(str)):
        yield str[i]

gen=generator(str)

for i in gen:
    print(i)

