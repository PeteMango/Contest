import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_db_impl import InMemoryDBImpl


class Level3Tests(unittest.TestCase):
    """
    The test class below includes 10 tests for Level 3.

    All have the same score.
    You are not allowed to modify this file, but feel free to read the source code to better understand what is happening in every specific case.
    """

    failureException = Exception


    fixed_timestamp = 160000000

    @classmethod
    def setUp(cls):
        cls.db = InMemoryDBImpl()

    @timeout(0.4)
    def test_level_3_case_01_simple_set_and_get(self):
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp, 50)
        self.assertEqual(self.db.get_at('foo', 'bar', self.fixed_timestamp + 20), 'baz')
        self.assertEqual(self.db.get_at('foo', 'bar', self.fixed_timestamp + 30), 'baz')
        self.assertIsNone(self.db.get_at('foo', 'bar', self.fixed_timestamp + 50))
        self.assertIsNone(self.db.get_at('foo', 'bar', self.fixed_timestamp + 80))

    @timeout(0.4)
    def test_level_3_case_02_simple_set_get_and_scan(self):
        self.db.set_at('key1', 'field1', 'value1', self.fixed_timestamp + 10)
        self.assertEqual(self.db.get_at('key1', 'field1', self.fixed_timestamp + 11), 'value1')
        self.db.set_at_with_ttl('key1', 'field1', 'str', self.fixed_timestamp + 20, 20)
        self.assertEqual(self.db.get_at('key1', 'field1', self.fixed_timestamp + 21), 'str')
        self.db.set_at_with_ttl('key1', 'field2', 'c', self.fixed_timestamp + 22, 38)
        self.assertEqual(self.db.get_at('key1', 'field1', self.fixed_timestamp + 23), 'str')
        expected = ['field1(str)', 'field2(c)']
        self.assertEqual(self.db.scan_by_prefix_at('key1', 'field', self.fixed_timestamp + 30), expected)
        self.assertFalse(self.db.scan_by_prefix_at('key1', 'foo', self.fixed_timestamp + 31))
        self.assertEqual(self.db.scan_by_prefix_at('key1', 'field', self.fixed_timestamp + 32), expected)
        expected = ['field2(c)']
        self.assertEqual(self.db.scan_by_prefix_at('key1', 'field', self.fixed_timestamp + 50), expected)
        self.assertFalse(self.db.scan_by_prefix_at('key1', 'field', self.fixed_timestamp + 60))

    @timeout(0.4)
    def test_level_3_case_03_simple_set_get_del_and_scan(self):
        self.db.set_at('foo', 'bar', 'baz', self.fixed_timestamp + 100)
        self.db.set_at_with_ttl('key', 'key', 'value', self.fixed_timestamp + 200, 800)
        self.assertEqual(self.db.get_at('foo', 'bar', self.fixed_timestamp + 400), 'baz')
        expected = ['key(value)']
        self.assertEqual(self.db.scan_by_prefix_at('key', 'k', self.fixed_timestamp + 700), expected)
        self.assertTrue(self.db.delete_at('foo', 'bar', self.fixed_timestamp + 800))
        self.assertFalse(self.db.delete_at('foo', 'bar', self.fixed_timestamp + 850))
        self.assertTrue(self.db.delete_at('key', 'key', self.fixed_timestamp + 900))
        self.assertFalse(self.db.delete_at('key', 'key', self.fixed_timestamp + 1100))
        self.assertFalse(self.db.scan_at('key', self.fixed_timestamp + 1200))
        self.assertFalse(self.db.scan_at('foo', self.fixed_timestamp + 1300))

    @timeout(0.4)
    def test_level_3_case_04_multiple_objects_with_same_key_1(self):
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp, 100)
        expected = ['bar(baz)']
        self.assertEqual(self.db.scan_at('foo', self.fixed_timestamp + 25), expected)
        self.db.set_at_with_ttl('foo', 'key1', 'bar', self.fixed_timestamp + 30, 70)
        self.db.set_at_with_ttl('foo', 'key2', 'baz', self.fixed_timestamp + 35, 65)
        self.db.set_at_with_ttl('key1', 'foo', 'ooo', self.fixed_timestamp + 40, 260)
        expected = ['key1(bar)', 'key2(baz)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'key', self.fixed_timestamp + 50), expected)
        self.db.set_at_with_ttl('foo', 'key3', 'bal', self.fixed_timestamp + 60, 20)
        expected = ['key1(bar)', 'key2(baz)', 'key3(bal)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'key', self.fixed_timestamp + 70), expected)
        expected = ['key1(bar)', 'key2(baz)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'ke', self.fixed_timestamp + 80), expected)
        self.assertFalse(self.db.scan_by_prefix_at('foo', 'k', self.fixed_timestamp + 100))
        self.db.set_at_with_ttl('foo', 'key1', 'bar', self.fixed_timestamp + 120, 30)
        self.db.set_at_with_ttl('foo', 'key2', 'baz', self.fixed_timestamp + 125, 35)
        self.db.set_at_with_ttl('foo', 'k', 'value', self.fixed_timestamp + 130, 40)
        expected = ['k(value)', 'key1(bar)', 'key2(baz)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'k', self.fixed_timestamp + 140), expected)
        self.assertIsNone(self.db.get_at('foo', 'key1', self.fixed_timestamp + 152))
        self.assertEqual(self.db.get_at('foo', 'key2', self.fixed_timestamp + 154), 'baz')
        expected = ['k(value)', 'key2(baz)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'k', self.fixed_timestamp + 155), expected)
        self.assertEqual(self.db.get_at('foo', 'key2', self.fixed_timestamp + 156), 'baz')
        self.assertTrue(self.db.delete_at('foo', 'key2', self.fixed_timestamp + 158))
        expected = ['k(value)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'k', self.fixed_timestamp + 165), expected)
        self.assertFalse(self.db.scan_by_prefix_at('foo', 'k', self.fixed_timestamp + 170))
        self.db.set_at('foo', 'key1', 'something', self.fixed_timestamp + 200)
        expected = ['key1(something)']
        self.assertEqual(self.db.scan_at('foo', self.fixed_timestamp + 210), expected)

    @timeout(0.4)
    def test_level_3_case_05_multiple_objects_with_same_key_2(self):
        self.db.set_at_with_ttl('a', 'b', 'c', self.fixed_timestamp + 10, 90)
        self.db.set_at_with_ttl('aaa', 'bbb', 'ccc', self.fixed_timestamp + 15, 175)
        self.db.set_at_with_ttl('a', 'bb', 'cc', self.fixed_timestamp + 20, 60)
        self.db.set_at_with_ttl('aaa', 'bb', 'd', self.fixed_timestamp + 22, 198)
        self.db.set_at_with_ttl('a', 'bc', 'ca', self.fixed_timestamp + 24, 46)
        self.db.set_at_with_ttl('a', 'bbc', 'cc', self.fixed_timestamp + 25, 146)
        expected = ['b(c)', 'bb(cc)', 'bbc(cc)', 'bc(ca)']
        self.assertEqual(self.db.scan_by_prefix_at('a', 'b', self.fixed_timestamp + 30), expected)
        self.db.set_at_with_ttl('a', 'bcc', 'caa', self.fixed_timestamp + 38, 12)
        self.assertEqual(self.db.scan_by_prefix_at('a', 'b', self.fixed_timestamp + 50), expected)
        self.assertTrue(self.db.delete_at('a', 'bc', self.fixed_timestamp + 55))
        self.assertFalse(self.db.delete_at('a', 'bb', self.fixed_timestamp + 80))
        expected = ['b(c)', 'bbc(cc)']
        self.assertEqual(self.db.scan_by_prefix_at('a', 'b', self.fixed_timestamp + 95), expected)
        expected = ['bbc(cc)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 160), expected)

    @timeout(0.4)
    def test_level_3_case_06_resets(self):
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp + 30, 90)
        self.db.set_at_with_ttl('foo', 'two', 'three', self.fixed_timestamp + 40, 60)
        self.db.set_at_with_ttl('foo', 'two', 'four', self.fixed_timestamp + 42, 108)
        self.db.set_at_with_ttl('foo', 'bar', 'boo', self.fixed_timestamp + 50, 30)
        self.assertIsNone(self.db.get_at('foo', 'bar', self.fixed_timestamp + 90))
        self.assertFalse(self.db.scan_by_prefix_at('foo', 'b', self.fixed_timestamp + 95))
        self.db.set_at_with_ttl('foo', 'two', 'five', self.fixed_timestamp + 100, 100)
        self.assertFalse(self.db.delete_at('foo', 'bar', self.fixed_timestamp + 120))
        expected = ['two(five)']
        self.assertEqual(self.db.scan_at('foo', self.fixed_timestamp + 140), expected)
        self.db.set_at_with_ttl('foo', 'two', 'four', self.fixed_timestamp + 150, 40)
        self.db.set_at_with_ttl('foo', 'two', 'four', self.fixed_timestamp + 160, 40)
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp + 170, 10)
        self.assertFalse(self.db.scan_by_prefix_at('foo', 'b', self.fixed_timestamp + 190))
        self.assertEqual(self.db.get_at('foo', 'two', self.fixed_timestamp + 192), 'four')
        self.assertIsNone(self.db.get_at('foo', 'two', self.fixed_timestamp + 200))

    @timeout(0.4)
    def test_level_3_case_07_resets_and_deletes_with_same_key(self):
        self.db.set_at_with_ttl('key1', 'field1', 'value1', self.fixed_timestamp + 5, 95)
        self.db.set_at_with_ttl('key1', 'field2', 'value2', self.fixed_timestamp + 6, 44)
        self.db.set_at_with_ttl('key2', 'field1', 'value3', self.fixed_timestamp + 7, 33)
        self.db.set_at_with_ttl('key3', 'field1', 'value4', self.fixed_timestamp + 8, 82)
        self.db.set_at_with_ttl('key3', 'field2', 'value5', self.fixed_timestamp + 9, 83)
        self.db.set_at_with_ttl('key3', 'field3', 'value6', self.fixed_timestamp + 10, 90)
        self.assertFalse(self.db.scan_by_prefix_at('ke3', 'fi', self.fixed_timestamp + 11))
        self.db.set_at_with_ttl('key1', 'field2', 'value7', self.fixed_timestamp + 20, 40)
        self.db.set_at_with_ttl('key2', 'field1', 'value8', self.fixed_timestamp + 21, 29)
        self.db.set_at_with_ttl('key3', 'field1', 'value9', self.fixed_timestamp + 22, 118)
        self.db.set_at_with_ttl('key3', 'fld5', 'value10', self.fixed_timestamp + 23, 200)
        self.assertEqual(self.db.get_at('key1', 'field1', self.fixed_timestamp + 30), 'value1')
        expected = ['field1(value1)']
        self.assertEqual(self.db.scan_by_prefix_at('key1', 'fiel', self.fixed_timestamp + 80), expected)
        self.assertTrue(self.db.delete_at('key1', 'field1', self.fixed_timestamp + 82))
        self.assertTrue(self.db.delete_at('key3', 'field2', self.fixed_timestamp + 85))
        self.assertFalse(self.db.delete_at('key2', 'field1', self.fixed_timestamp + 87))
        self.assertFalse(self.db.delete_at('key4', 'field1', self.fixed_timestamp + 100))
        self.assertFalse(self.db.scan_at('key1', self.fixed_timestamp + 110))
        self.assertFalse(self.db.scan_at('key2', self.fixed_timestamp + 111))
        expected = ['field1(value9)', 'fld5(value10)']
        self.assertEqual(self.db.scan_at('key3', self.fixed_timestamp + 112), expected)
        self.assertFalse(self.db.scan_at('key4', self.fixed_timestamp + 113))

    @timeout(0.4)
    def test_level_3_case_08_random_ordered_operations(self):
        self.assertFalse(self.db.delete_at('key', 'key', self.fixed_timestamp + 10))
        self.assertFalse(self.db.delete_at('key', 'key2', self.fixed_timestamp + 20))
        self.assertFalse(self.db.scan_by_prefix_at('key', 'k', self.fixed_timestamp + 25))
        self.assertIsNone(self.db.get_at('A', 'B', self.fixed_timestamp + 30))
        self.assertIsNone(self.db.get_at('key', 'key', self.fixed_timestamp + 40))
        self.assertFalse(self.db.scan_at('A', self.fixed_timestamp + 50))
        self.assertFalse(self.db.delete_at('key', 'key', self.fixed_timestamp + 52))
        self.db.set_at_with_ttl('key', 'key', 'aaaaa', self.fixed_timestamp + 60, 1940)
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp + 70, 101)
        self.assertFalse(self.db.delete_at('key', 'bar', self.fixed_timestamp + 80))
        self.assertFalse(self.db.delete_at('key', 'key2', self.fixed_timestamp + 90))
        self.assertEqual(self.db.get_at('key', 'key', self.fixed_timestamp + 100), 'aaaaa')
        self.db.set_at_with_ttl('key', 'key', 'otherValue', self.fixed_timestamp + 120, 20)
        self.assertFalse(self.db.scan_by_prefix_at('key', 'k', self.fixed_timestamp + 150))
        self.db.set_at('foo', 'bar', 'baz', self.fixed_timestamp + 173)
        self.assertEqual(self.db.get_at('foo', 'bar', self.fixed_timestamp + 200), 'baz')
        self.assertFalse(self.db.delete_at('key', 'key', self.fixed_timestamp + 210))

    @timeout(0.4)
    def test_level_3_case_09_mixed_multiple_operations_1(self):
        self.db.set_at_with_ttl('a', 'b', 'c', self.fixed_timestamp, 20)
        self.db.set_at_with_ttl('a', 'c', 'd', self.fixed_timestamp + 15, 35)
        self.assertIsNone(self.db.get_at('c', 'a', self.fixed_timestamp + 17))
        expected = ['c(d)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 25), expected)
        self.db.set_at_with_ttl('a', 'd', 'e', self.fixed_timestamp + 30, 70)
        self.assertFalse(self.db.delete_at('a', 'c', self.fixed_timestamp + 50))
        self.assertFalse(self.db.delete_at('a', 'c', self.fixed_timestamp + 51))
        self.db.set_at('a', 'e', 'f', self.fixed_timestamp + 52)
        self.assertFalse(self.db.delete_at('a', 'b', self.fixed_timestamp + 53))
        self.db.set_at_with_ttl('a', 'f', 'g', self.fixed_timestamp + 58, 4)
        self.assertIsNone(self.db.get_at('a', 'c', self.fixed_timestamp + 60))
        self.assertFalse(self.db.scan_by_prefix_at('a', 'f', self.fixed_timestamp + 65))
        self.db.set_at_with_ttl('a', 'b', 'c', self.fixed_timestamp + 120, 50)
        expected = ['e(f)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 200), expected)
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 250), expected)
        self.db.set_at_with_ttl('a', 'b', 'c', self.fixed_timestamp + 500, 4 * self.fixed_timestamp)
        expected = ['b(c)']
        self.assertEqual(self.db.scan_by_prefix_at('a', 'b', 5 * self.fixed_timestamp + 300), expected)
        expected = ['e(f)']
        self.assertEqual(self.db.scan_at('a', 6 * self.fixed_timestamp), expected)

    @timeout(0.4)
    def test_level_3_case_10_mixed_multiple_operations_2(self):
        self.db.set_at_with_ttl('a', 'a', 'b', self.fixed_timestamp, 40)
        self.db.set_at_with_ttl('a', 'aaa', 'c', self.fixed_timestamp + 10, 60)
        expected = ['a(b)', 'aaa(c)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 20), expected)
        self.assertTrue(self.db.delete_at('a', 'a', self.fixed_timestamp + 30))
        self.assertFalse(self.db.delete_at('a', 'a', self.fixed_timestamp + 45))
        self.assertTrue(self.db.delete_at('a', 'aaa', self.fixed_timestamp + 50))
        self.assertFalse(self.db.delete_at('a', 'aaa', self.fixed_timestamp + 55))
        self.db.set_at_with_ttl('a', 'aaa', 'b', self.fixed_timestamp + 60, 2)
        self.db.set_at_with_ttl('a', 'aaa', 'c', self.fixed_timestamp + 65, 6)
        self.assertFalse(self.db.scan_at('bc', self.fixed_timestamp + 68))
        expected = ['aaa(c)']
        self.assertEqual(self.db.scan_by_prefix_at('a', 'aaa', self.fixed_timestamp + 70), expected)
        self.assertIsNone(self.db.get_at('a', 'aaa', self.fixed_timestamp + 72))
        self.assertFalse(self.db.delete_at('a', 'aaa', self.fixed_timestamp + 80))
        self.db.set_at('A', 'aaa', 'B', self.fixed_timestamp + 100)
        self.assertFalse(self.db.scan_by_prefix_at('a', 'aa', self.fixed_timestamp + 170))
        self.db.set_at_with_ttl('A', 'aaa', 'B', self.fixed_timestamp + 200, 30)
        self.assertFalse(self.db.scan_by_prefix_at('A', 'a', self.fixed_timestamp + 230))
        self.db.set_at_with_ttl('A', 'aaa', 'B', self.fixed_timestamp + 300, 30)
        self.db.set_at('A', 'aaa', 'B', self.fixed_timestamp + 310)
        expected = ['aaa(B)']
        self.assertEqual(self.db.scan_by_prefix_at('A', 'aa', self.fixed_timestamp + 400), expected)
        self.assertEqual(self.db.scan_by_prefix_at('A', 'a', 5 * self.fixed_timestamp), expected)
