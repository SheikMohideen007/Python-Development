str="hello bro I'm Sheik"
# Now function PAUSES and REMEMBERS state. this is the power of generator in python. it can be used to generate a sequence of values over time, instead of computing them all at once and sending them back. this is useful when working with large datasets or when you want to create an infinite sequence of values.
def generator(str):
    for i in range(len(str)):
        yield str[i]

gen=generator(str)

for i in gen:
    print(i)