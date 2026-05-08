class Test:
    def __init__(self):
        self._age = 25

t = Test()

print(t.__dict__)

# ouput
# with __ underscore : {'_Test__age': 25}
# with _ underscore : {'_age': 25}