import pickle
from nose.tools import assert_equal
from pomp.contrib.item import Item, Field


class TItem(Item):
    f1 = Field()
    f2 = Field()
    f3 = Field()


def test_item():

    # item as a dict
    i = TItem()
    assert_equal(['f1', 'f2', 'f3'], list(i.keys()))

    i.f1 = 1
    i.f3 = 3
    assert_equal([1, None, 3], list(i.values()))

    # item as a object
    i = TItem('f1', f3='f3', f2='f2')
    assert_equal(i.f1, 'f1')
    assert_equal(i.f2, 'f2')
    assert_equal(i.f3, 'f3')
    assert_equal(['f1', 'f2', 'f3'], list(i.keys()))

    # change attributes
    i.f1 = 'f1_new'
    i.f2 = 'f2_new'
    assert_equal(i.f1, 'f1_new')
    assert_equal(i.f2, 'f2_new')
    assert_equal(i.f3, 'f3')
    assert_equal(['f1', 'f2', 'f3'], list(i.keys()))

    # pickling
    assert_equal(i, pickle.loads(pickle.dumps(i)))
