  
from merge_sort import __version__
from merge_sort.merge_sort import merge_sort

def test_version():
    assert __version__ == '0.1.0'


def test_success_sort():
    array=[20,18,12,4,14,6]
    actual=merge_sort(array)
    expected=[4,6,12,14,18,20]
    assert actual==expected

def test_Reverse_sort():
    array=[30,25,22,11,7,-5]
    actual=merge_sort(array)
    expected=[-5,7,11,22,25,30]
    assert actual==expected

def test_few_uniques_sort():
    array=[1,3,2,1,1,2]
    actual=merge_sort(array)
    expected=[1,1,1,2,2,3]
    assert actual==expected

def test_nearly_sorted_sort():
    array=[1,2,4,6,12,10]
    actual=merge_sort(array)
    expected=[1,2,4,6,10,12]
    assert actual==expected