# any pytest file must start with test_


def test_firstmethod():
    print("hello")


# If two methods have same names, the second method will be overriden by the first one, and will execute only the second one
def test_firstmethod():
    print("hello2")


def test_secondmethod():
    Message = "Hi"
    assert Message == "Hello", "Test Failed because assertion failed"

def test_thirdmethod():
    print("This is te third method")
