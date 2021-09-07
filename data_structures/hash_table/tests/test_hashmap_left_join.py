from hash_table.hash_table import Hashtable
from hash_table.hashmap_left_join import left_join




def test_one():
    hashtable1 = Hashtable()
    hashtable1.add('fond', 'enamored')
    hashtable1.add('wrath', 'anger')
    hashtable1.add('diligent', 'employed')
    hashtable1.add('outift', 'garb')
    hashtable1.add('guide', 'usher')

    hashtable2 = Hashtable()
    hashtable2.add('fond', 'averse')
    hashtable2.add('wrath', 'delight')
    hashtable2.add('diligent', 'idle')
    hashtable2.add('guide', 'follow')
    hashtable2.add('flow', 'jam')

    actual = left_join(hashtable1, hashtable2)

    expected = [['diligent', 'employed', 'idle'],
                ['outift', 'garb', None],
                ['fond', 'enamored', 'averse'],
                ['guide', 'usher', 'follow'],
                ['wrath', 'anger', 'delight']
                ]
    assert expected == actual



def test_hash_one_empty():
    hashtable1 = Hashtable()

    hashtable2 = Hashtable()
    hashtable2.add('fond', 'averse')
    hashtable2.add('wrath', 'delight')
    hashtable2.add('diligent', 'idle')
    hashtable2.add('guide', 'follow')
    hashtable2.add('flow', 'jam')

    actual = left_join(hashtable1, hashtable2)

    expected = "right table is empty"

    assert expected == actual



def test_hash_two_empty():
    hashtable1 = Hashtable()
    hashtable1.add('fond', 'enamored')
    hashtable1.add('wrath', 'anger')
    hashtable1.add('diligent', 'employed')
    hashtable1.add('outift', 'garb')
    hashtable1.add('guide', 'usher')

    hashtable2 = Hashtable()

    actual = left_join(hashtable1, hashtable2)

    expected = [['diligent', 'employed', None],
                ['outift', 'garb', None],
                ['fond', 'enamored', None],
                ['guide', 'usher', None],
                ['wrath', 'anger', None]
                ]

    assert expected == actual

