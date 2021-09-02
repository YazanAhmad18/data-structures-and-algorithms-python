from hash_table import __version__
from hash_table.hash_table import Hashtable

def test_version():
    assert __version__ == '0.1.0'



def test_hash_table_add():
    hashtable = Hashtable()
    hashtable.add('name', 'yazan')
    hash = hashtable.hash('name')
    actual = hashtable._buckets[hash].head.value
    expected = {'name': 'yazan'}
    assert actual == expected



def test_hash_table_get():
    hashtable = Hashtable()
    hashtable.add('name', 'yazan')
    actual = hashtable.get('name')
    expected = 'yazan'
    assert actual == expected



def test_hash_table_contains_True():
    hashtable = Hashtable()
    hashtable.add('name', 'yazan')
    actual = hashtable.contains('name')
    expected = True
    assert actual == expected



def test_hash_table_contains_false():
    hashtable = Hashtable()
    actual = hashtable.contains('phone')
    expected = False
    assert actual == expected



def test_hash_table_collision():
    hashtable = Hashtable()
    hashtable.add('name', 'yazan')
    hashtable.add('mane', 'ahmad')
    actual = hashtable.get('name')
    expected = 'yazan'
    assert actual == expected



def test_hash_key_index():
    hashtable = Hashtable()
    actual = hashtable.hash('name')
    expected = 491
    assert actual == expected

