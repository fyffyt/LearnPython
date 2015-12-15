#!/usr/bin/env python

class TestClass():
    def setUp(self):
        print("TestClass.setUp")

    @staticmethod
    def tearDown():
        print("TestClass.tearDown")



if __name__ == "__main__":
    t = TestClass()
    print(t.setUp)
    print(t.tearDown)
    print(TestClass.setUp)
    print(TestClass.tearDown)
    #print(getattr(type(t), "setUp"))
    #print(getattr(type(t), "tearDown"))
    print(dir(t))
    print(getattr(TestClass, "setUp"))
    print(getattr(TestClass, "tearDown"))
