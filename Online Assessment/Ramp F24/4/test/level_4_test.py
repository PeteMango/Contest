import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_db_impl import InMemoryDBImpl


class Level4Tests(unittest.TestCase):
    """
    The test class below includes 10 tests for Level 4.

    All have the same score.
    You are not allowed to modify this file, but feel free to read the source code to better understand what is happening in every specific case.
    """

    failureException = Exception


    fixed_timestamp = 160000000

    @classmethod
    def setUp(cls):
        cls.db = InMemoryDBImpl()

    @timeout(0.4)
    def test_level_4_case_01_simple_set_and_backup(self):
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp, 100)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 20), 1)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 30), 1)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 100), 0)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 120), 0)

    @timeout(0.4)
    def test_level_4_case_02_simple_backup_and_restore(self):
        self.assertEqual(self.db.backup(self.fixed_timestamp), 0)
        self.db.restore(self.fixed_timestamp + 1, self.fixed_timestamp)
        self.db.set_at_with_ttl('key', 'field', 'str', self.fixed_timestamp + 100, 200)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 200), 1)
        self.db.restore(self.fixed_timestamp + 250, self.fixed_timestamp)
        self.assertIsNone(self.db.get_at('key', 'field', self.fixed_timestamp + 300))
        self.assertEqual(self.db.backup(self.fixed_timestamp + 350), 0)
        self.db.restore(self.fixed_timestamp + 400, self.fixed_timestamp + 200)
        self.assertEqual(self.db.get_at('key', 'field', self.fixed_timestamp + 450), 'str')
        self.assertIsNone(self.db.get_at('key', 'field', self.fixed_timestamp + 500))

    @timeout(0.4)
    def test_level_4_case_03_backup_and_restore_with_other_operations(self):
        self.db.set_at('foo', 'bar', 'baz', self.fixed_timestamp + 100)
        self.db.set_at_with_ttl('key', 'key', 'value', self.fixed_timestamp + 120, 1880)
        self.db.set_at_with_ttl('key', 'key', 'value', self.fixed_timestamp + 170, 680)
        self.db.set_at_with_ttl('bar', 'baz', 'foo', self.fixed_timestamp + 200, 100)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 250), 3)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 270), 3)
        self.db.set_at_with_ttl('boo', 'text1', 'text2', self.fixed_timestamp + 300, 900)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 850), 2)
        self.assertEqual(self.db.get_at('foo', 'bar', self.fixed_timestamp + 900), 'baz')
        self.assertFalse(self.db.scan_by_prefix_at('key', 'k', self.fixed_timestamp + 920))
        self.assertTrue(self.db.delete_at('foo', 'bar', self.fixed_timestamp + 950))
        self.assertFalse(self.db.delete_at('key', 'key', self.fixed_timestamp + 960))
        self.db.restore(self.fixed_timestamp + 970, self.fixed_timestamp + 250)
        expected = ['key(value)']
        self.assertEqual(self.db.scan_at('key', self.fixed_timestamp + 980), expected)
        self.assertEqual(self.db.scan_at('key', self.fixed_timestamp + 1021), expected)
        self.db.restore(self.fixed_timestamp + 1030, self.fixed_timestamp + 850)
        self.assertFalse(self.db.scan_at('key', self.fixed_timestamp + 1040))
        expected = ['text1(text2)']
        self.assertEqual(self.db.scan_at('boo', self.fixed_timestamp + 1041), expected)
        self.assertFalse(self.db.scan_at('bar', self.fixed_timestamp + 1042))

    @timeout(0.4)
    def test_level_4_case_04_multiple_objects_with_same_key_1(self):
        self.db.set_at_with_ttl('foo', 'key1', 'b', self.fixed_timestamp + 30, 70)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 31), 1)
        self.db.set_at_with_ttl('foo', 'key2', 'baz', self.fixed_timestamp + 35, 25)
        self.db.set_at_with_ttl('key1', 'foo', 'ooo', self.fixed_timestamp + 40, 60)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 41), 2)
        self.db.set_at_with_ttl('foo', 'key3', 'boo', self.fixed_timestamp + 60, 20)
        self.db.restore(self.fixed_timestamp + 110, self.fixed_timestamp + 35)
        self.db.set_at_with_ttl('foo', 'key2', 'baz', self.fixed_timestamp + 112, 8)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 115), 1)
        self.db.restore(self.fixed_timestamp + 118, self.fixed_timestamp + 50)
        self.db.set_at_with_ttl('foo', 'key1', 'bar', self.fixed_timestamp + 120, 30)
        self.db.set_at_with_ttl('foo', 'k', 'value', self.fixed_timestamp + 130, 40)
        expected = ['k(value)', 'key1(bar)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'k', self.fixed_timestamp + 140), expected)
        self.db.restore(self.fixed_timestamp + 150, self.fixed_timestamp + 148)
        expected = ['key1(b)']
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'k', self.fixed_timestamp + 155), expected)
        self.assertIsNone(self.db.get_at('foo', 'key2', self.fixed_timestamp + 156))
        self.assertFalse(self.db.delete_at('foo', 'key2', self.fixed_timestamp + 158))
        self.assertEqual(self.db.scan_by_prefix_at('foo', 'key', self.fixed_timestamp + 213), expected)
        self.assertFalse(self.db.scan_at('key1', self.fixed_timestamp + 214))

    @timeout(0.4)
    def test_level_4_case_05_multiple_objects_with_same_key_2(self):
        self.db.set_at_with_ttl('a', 'b', 'c', self.fixed_timestamp + 10, 90)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 13), 1)
        self.db.set_at_with_ttl('aaa', 'bbb', 'ccc', self.fixed_timestamp + 15, 75)
        self.db.set_at_with_ttl('a', 'bb', 'cc', self.fixed_timestamp + 20, 60)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 21), 2)
        self.db.set_at_with_ttl('aaa', 'bb', 'd', self.fixed_timestamp + 22, 30)
        self.db.set_at_with_ttl('a', 'bc', 'ca', self.fixed_timestamp + 24, 26)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 25), 2)
        expected = ['b(c)', 'bb(cc)', 'bc(ca)']
        self.assertEqual(self.db.scan_by_prefix_at('a', 'b', self.fixed_timestamp + 30), expected)
        self.db.set_at('a', 'bcc', 'caa', self.fixed_timestamp + 48)
        self.assertTrue(self.db.delete_at('a', 'b', self.fixed_timestamp + 55))
        self.assertEqual(self.db.backup(self.fixed_timestamp + 60), 2)
        expected = ['bcc(caa)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 140), expected)
        self.assertFalse(self.db.scan_at('aaa', self.fixed_timestamp + 160))
        self.db.restore(self.fixed_timestamp + 170, self.fixed_timestamp + 25)
        self.assertTrue(self.db.delete_at('a', 'bb', self.fixed_timestamp + 180))
        self.assertFalse(self.db.delete_at('a', 'bc', self.fixed_timestamp + 195))
        expected = ['b(c)']
        self.assertEqual(self.db.scan_by_prefix_at('a', 'b', self.fixed_timestamp + 200), expected)
        self.db.restore(self.fixed_timestamp + 210, self.fixed_timestamp + 15)
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 220), expected)
        self.assertFalse(self.db.scan_at('a', self.fixed_timestamp + 2000))
        self.db.set_at('a', 'b', 'c', self.fixed_timestamp + 3000)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 3550), 1)
        self.db.restore(self.fixed_timestamp + 4010, self.fixed_timestamp + 3550)
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 4210), expected)
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 4260), expected)
        self.db.restore(self.fixed_timestamp + 5000, self.fixed_timestamp + 4000)
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 5200), expected)
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 5270), expected)

    @timeout(0.4)
    def test_level_4_case_06_random_ordered_operations(self):
        self.assertFalse(self.db.delete_at('key', 'key', self.fixed_timestamp + 10))
        self.assertFalse(self.db.delete_at('key', 'key2', self.fixed_timestamp + 20))
        self.assertFalse(self.db.scan_by_prefix_at('key', 'key', self.fixed_timestamp + 25))
        self.assertIsNone(self.db.get_at('A', 'B', self.fixed_timestamp + 30))
        self.assertIsNone(self.db.get_at('key', 'key', self.fixed_timestamp + 40))
        self.assertFalse(self.db.scan_by_prefix_at('key', 'key', self.fixed_timestamp + 50))
        self.assertFalse(self.db.delete_at('key', 'key', self.fixed_timestamp + 52))
        self.assertEqual(self.db.backup(self.fixed_timestamp + 55), 0)
        self.db.set_at_with_ttl('key', 'key', 'aaaaa', self.fixed_timestamp + 60, 1940)
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp + 70, 101)
        self.assertFalse(self.db.delete_at('key', 'bar', self.fixed_timestamp + 80))
        self.assertFalse(self.db.delete_at('key', 'key2', self.fixed_timestamp + 90))
        self.assertEqual(self.db.backup(self.fixed_timestamp + 100), 2)
        self.db.set_at_with_ttl('key', 'key', 'otherValue', self.fixed_timestamp + 120, 20)
        self.db.restore(self.fixed_timestamp + 130, self.fixed_timestamp + 99)
        self.assertFalse(self.db.scan_by_prefix_at('key', 'key', self.fixed_timestamp + 150))
        self.db.restore(self.fixed_timestamp + 160, self.fixed_timestamp + 100)
        expected = ['key(aaaaa)']
        self.assertEqual(self.db.scan_by_prefix_at('key', 'k', self.fixed_timestamp + 200), expected)
        self.assertEqual(self.db.scan_by_prefix_at('key', 'k', self.fixed_timestamp + 201), expected)
        self.db.restore(self.fixed_timestamp + 250, self.fixed_timestamp + 110)
        self.assertEqual(self.db.scan_at('key', self.fixed_timestamp + 270), expected)
        self.assertEqual(self.db.scan_by_prefix_at('key', 'key', self.fixed_timestamp + 350), expected)

    @timeout(0.4)
    def test_level_4_case_07_mixed_multiple_operations_1(self):
        self.assertEqual(self.db.backup(self.fixed_timestamp), 0)
        self.db.set_at_with_ttl('a', 'b', 'c', self.fixed_timestamp + 2, 100)
        self.db.restore(self.fixed_timestamp + 3, self.fixed_timestamp + 1)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 4), 0)
        self.db.set_at_with_ttl('a', 'b', 'c', self.fixed_timestamp + 5, 15)
        self.db.set_at_with_ttl('a', 'c', 'd', self.fixed_timestamp + 15, 35)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 17), 1)
        self.db.set_at_with_ttl('a', 'd', 'e', self.fixed_timestamp + 30, 70)
        self.assertFalse(self.db.delete_at('a', 'c', self.fixed_timestamp + 50))
        self.assertFalse(self.db.delete_at('a', 'c', self.fixed_timestamp + 51))
        self.db.set_at('a', 'e', 'f', self.fixed_timestamp + 52)
        self.assertFalse(self.db.delete_at('a', 'b', self.fixed_timestamp + 53))
        self.db.set_at_with_ttl('a', 'f', 'g', self.fixed_timestamp + 58, 4)
        self.db.restore(self.fixed_timestamp + 60, self.fixed_timestamp + 20)
        expected = ['c(d)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 65), expected)

    @timeout(0.4)
    def test_level_4_case_08_mixed_multiple_operations_2(self):
        self.db.set_at_with_ttl('a', 'a', 'b', self.fixed_timestamp, 100)
        self.db.set_at_with_ttl('a', 'd', 'c', self.fixed_timestamp + 10, 60)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 20), 1)
        self.assertTrue(self.db.delete_at('a', 'a', self.fixed_timestamp + 30))
        self.assertTrue(self.db.delete_at('a', 'd', self.fixed_timestamp + 50))
        self.db.set_at_with_ttl('a', 'd', 'b', self.fixed_timestamp + 60, 2)
        self.db.set_at_with_ttl('a', 'd', 'c', self.fixed_timestamp + 65, 5)
        self.db.restore(self.fixed_timestamp + 66, self.fixed_timestamp + 20)
        expected = ['a(b)', 'd(c)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 68), expected)
        expected = ['a(b)']
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 120), expected)
        self.assertEqual(self.db.scan_at('a', self.fixed_timestamp + 140), expected)
        self.assertFalse(self.db.scan_at('a', self.fixed_timestamp + 160))

    @timeout(0.4)
    def test_level_4_case_09_resets(self):
        self.db.set_at_with_ttl('foo', 'bar', 'baz', self.fixed_timestamp + 30, 90)
        self.db.set_at_with_ttl('foo', 'two', 'three', self.fixed_timestamp + 40, 60)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 41), 1)
        self.db.set_at_with_ttl('foo', 'two', 'four', self.fixed_timestamp + 42, 118)
        self.db.set_at_with_ttl('foo', 'bar', 'boo', self.fixed_timestamp + 50, 30)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 52), 1)
        expected = ['two(four)']
        self.assertEqual(self.db.scan_at('foo', self.fixed_timestamp + 95), expected)
        self.db.set_at_with_ttl('foo', 'two', 'five', self.fixed_timestamp + 100, 100)
        self.assertFalse(self.db.delete_at('foo', 'bar', self.fixed_timestamp + 120))
        self.assertEqual(self.db.backup(self.fixed_timestamp + 122), 1)
        self.db.restore(self.fixed_timestamp + 160, self.fixed_timestamp + 100)
        self.assertEqual(self.db.scan_by_prefix_at('foo', 't', self.fixed_timestamp + 180), expected)
        self.assertFalse(self.db.scan_by_prefix_at('foo', 'b', self.fixed_timestamp + 220))
        self.assertFalse(self.db.scan_at('foo', self.fixed_timestamp + 2200))

    @timeout(0.4)
    def test_level_4_case_10_resets_and_deletes_with_same_keys(self):
        self.db.set_at_with_ttl('key1', 'field1', 'value1', self.fixed_timestamp + 5, 145)
        self.db.set_at_with_ttl('key1', 'field2', 'value2', self.fixed_timestamp + 6, 144)
        self.db.set_at_with_ttl('key2', 'field1', 'value3', self.fixed_timestamp + 7, 133)
        self.db.set_at_with_ttl('key3', 'field1', 'value4', self.fixed_timestamp + 8, 182)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 9), 3)
        self.db.set_at_with_ttl('key3', 'field2', 'value5', self.fixed_timestamp + 10, 182)
        self.db.set_at_with_ttl('key3', 'field3', 'value6', self.fixed_timestamp + 11, 89)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 12), 3)
        self.db.set_at_with_ttl('key1', 'field2', 'value7', self.fixed_timestamp + 20, 40)
        self.db.set_at_with_ttl('key2', 'field1', 'value8', self.fixed_timestamp + 21, 29)
        self.db.set_at_with_ttl('key3', 'field1', 'value9', self.fixed_timestamp + 22, 48)
        self.assertEqual(self.db.backup(self.fixed_timestamp + 23), 3)
        expected = ['field1(value9)', 'field2(value5)', 'field3(value6)']
        self.assertEqual(self.db.scan_by_prefix_at('key3', 'fi', self.fixed_timestamp + 30), expected)
        self.assertFalse(self.db.scan_by_prefix_at('key2', 'fi', self.fixed_timestamp + 80))
        expected = ['field2(value5)', 'field3(value6)']
        self.assertEqual(self.db.scan_by_prefix_at('key3', 'fi', self.fixed_timestamp + 81), expected)
        self.assertTrue(self.db.delete_at('key1', 'field1', self.fixed_timestamp + 82))
        self.assertTrue(self.db.delete_at('key3', 'field2', self.fixed_timestamp + 85))
        self.assertFalse(self.db.delete_at('key2', 'field1', self.fixed_timestamp + 87))
        self.assertFalse(self.db.delete_at('key4', 'field1', self.fixed_timestamp + 100))
        self.assertFalse(self.db.scan_at('key', self.fixed_timestamp + 120))
        self.db.restore(self.fixed_timestamp + 130, self.fixed_timestamp + 13)
        expected = ['field1(value4)', 'field2(value5)', 'field3(value6)']
        self.assertEqual(self.db.scan_by_prefix_at('key3', 'fie', self.fixed_timestamp + 135), expected)
        self.db.restore(self.fixed_timestamp + 140, self.fixed_timestamp + 9)
        expected = ['field1(value1)', 'field2(value2)']
        self.assertEqual(self.db.scan_by_prefix_at('key1', 'fi', self.fixed_timestamp + 271), expected)
        self.assertFalse(self.db.scan_by_prefix_at('key2', 'fiel', self.fixed_timestamp + 272))
        expected = ['field1(value4)']
        self.assertEqual(self.db.scan_by_prefix_at('key3', 'f', self.fixed_timestamp + 273), expected)
        self.assertFalse(self.db.scan_by_prefix_at('key4', 'fie', self.fixed_timestamp + 274))
