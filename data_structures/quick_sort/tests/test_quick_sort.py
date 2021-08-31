from quick_sort import __version__
from quick_sort.quick_sort import quick_sort

def test_version():
    assert __version__ == '0.1.0'


def test_success_sort():
    array=[36,24,12,1,15,3]
    actual=quick_sort(array,0,5)
    expected=[1,3,12,15,24,36]
    assert actual==expected

def test_Reverse_sort():
    array=[25,22,16,8,2,-1]
    actual=quick_sort(array,0,5)
    expected=[-1,2,8,16,22,25]
    assert actual==expected

def test_few_uniques_sort():
    array=[3,6,4,3,3,4]
    actual=quick_sort(array,0,5)
    expected=[3,3,3,4,4,6]
    assert actual==expected

def test_nearly_sorted_sort():
    array=[2,3,5,7,13,11]
    actual=quick_sort(array,0,5)
    expected=[2,3,5,7,11,13]
    assert actual==expected