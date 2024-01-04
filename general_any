import copy
import cPickle as pickle


class General(object):
    def clone(self):
        return copy.deepcopy(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def dumps(self):
        return pickle.dumps(self)


class Any(General):
    pass


class TestAny(Any):
    pass


def test_copy():
    a = TestAny()
    a.lst = [1, (2, 3), {"a": 1, "b": [1, [2, 3]]}]
    b = a  # copy object
    assert b is a


def test_clone():
    a = TestAny()
    a.lst = [1, (2, 3), {"a": 1, "b": [1, [2, 3]]}]
    c = a.clone()
    assert c is not a
    assert c.lst == a.lst


def test_eq():
    a = TestAny()
    a.lst = [1, (2, 3), {"a": 1, "b": [1, [2, 3]]}]
    c = a.clone()
    assert c == a
    a.lst = [1, (2, 3), {"a": 1, "b": [1, [2, 4]]}]
    assert c != a
    d = TestAny()
    d.lst = [1, (2, 3), {"a": 1, "b": [1, [2, 4]]}]
    assert d == a


def test_checktype():
    a = TestAny()
    a.lst = [1, (2, 3), {"a": 1, "b": [1, [2, 3]]}]
    assert isinstance(a, TestAny)


def test_type():
    a = TestAny()
    a.lst = [1, (2, 3), {"a": 1, "b": [1, [2, 3]]}]
    assert type(a) == TestAny



test_copy()
test_clone()
test_eq()
test_checktype()
test_type()
