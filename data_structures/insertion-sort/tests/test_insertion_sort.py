from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort


def test_version():
    assert __version__ == '0.1.0'

def test_insertion_sort():
    array_sort=[8,4,23,42,16,15]
    actual=insertion_sort(array_sort)
    expected=[4,8,15,16,23,42]
    assert actual ==expected

def test_reverse_sort():
    array_sort=[55,30,18,9,4,-1]
    actual=insertion_sort(array_sort)
    expected=[-1,4,9,18,30,55]
    assert actual ==expected

def test_few_uniques_sort():
    array_sort=[3,3,6,4,4,6]
    actual=insertion_sort(array_sort)
    expected=[3,3,4,4,6,6]
    assert actual ==expected

def test_nearly_sorted_sort():
    array_sort=[1,2,4,5,15,9]
    actual=insertion_sort(array_sort)
    expected=[1,2,4,5,9,15]
    assert actual ==expected