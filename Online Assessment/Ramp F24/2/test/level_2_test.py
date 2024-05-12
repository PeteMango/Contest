import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_db_impl import InMemoryDBImpl


class Level2Tests(unittest.TestCase):
    """
    The test class below includes 10 tests for Level 2.

    All have the same score.
    You are not allowed to modify this file, but feel free to read the source code to better understand what is happening in every specific case.
    """

    failureException = Exception


    @classmethod
    def setUp(cls):
        cls.db = InMemoryDBImpl()

    @timeout(0.4)
    def test_level_2_case_01_simple_set_and_scan(self):
        self.assertFalse(self.db.scan('employee'))
        self.db.set('employee', 'city', 'Annapolis')
        self.db.set('employee', 'id', '0123')
        expected = ['city(Annapolis)', 'id(0123)']
        self.assertEqual(self.db.scan('employee'), expected)

    @timeout(0.4)
    def test_level_2_case_02_simple_set_get_and_scan(self):
        self.assertFalse(self.db.scan_by_prefix('dept4', 'fi'))
        self.db.set('dept4', 'first', '1')
        self.db.set('dept4', 'second', '2')
        self.db.set('dept4', 'fifth', '5')
        expected = ['fifth(5)', 'first(1)']
        self.assertEqual(self.db.scan_by_prefix('dept4', 'fi'), expected)
        self.assertEqual(self.db.get('dept4', 'first'), '1')
        expected = ['second(2)']
        self.assertEqual(self.db.scan_by_prefix('dept4', 'sec'), expected)

    @timeout(0.4)
    def test_level_2_case_03_simple_set_get_delete_and_scan(self):
        self.db.set('book1', 'title', 'Island')
        self.assertEqual(self.db.get('book1', 'title'), 'Island')
        expected = ['title(Island)']
        self.assertEqual(self.db.scan('book1'), expected)
        self.assertTrue(self.db.delete('book1', 'title'))
        self.assertFalse(self.db.scan_by_prefix('book1', 'tit'))
        self.assertFalse(self.db.scan('book1'))

    @timeout(0.4)
    def test_level_2_case_04_multiple_objects_with_same_field_1(self):
        self.db.set('user1', 'firstname', 'Greg')
        self.db.set('user2', 'firstname', 'Paul')
        expected = ['firstname(Greg)']
        self.assertEqual(self.db.scan_by_prefix('user1', 'first'), expected)
        self.assertFalse(self.db.scan_by_prefix('user', 'fir'))
        self.assertFalse(self.db.scan_by_prefix('user2', 'name'))

    @timeout(0.4)
    def test_level_2_case_05_multiple_objects_with_same_field_2(self):
        self.db.set('a', 'b', 'c')
        self.db.set('aaa', 'bbb', 'ccc')
        self.db.set('a', 'bb', 'cc')
        self.db.set('aaa', 'bb', 'd')
        self.db.set('a', 'bc', 'ca')
        expected = ['b(c)', 'bb(cc)', 'bc(ca)']
        self.assertEqual(self.db.scan_by_prefix('a', 'b'), expected)
        self.assertTrue(self.db.delete('a', 'bb'))
        expected = ['b(c)', 'bc(ca)']
        self.assertEqual(self.db.scan_by_prefix('a', 'b'), expected)
        self.assertTrue(self.db.delete('a', 'b'))
        self.assertTrue(self.db.delete('a', 'bc'))
        expected = ['bb(d)', 'bbb(ccc)']
        self.assertEqual(self.db.scan_by_prefix('aaa', 'b'), expected)
        self.assertTrue(self.db.delete('aaa', 'bbb'))
        self.assertTrue(self.db.delete('aaa', 'bb'))
        self.assertFalse(self.db.scan_by_prefix('aaa', 'b'))
        self.db.set('a', 'bc', 'ca')
        self.db.set('aaa', 'bb', 'd')
        self.db.set('a', 'bb', 'cc')
        self.db.set('aaa', 'bbb', 'ccc')
        self.db.set('a', 'b', 'c')
        expected = ['b(c)', 'bb(cc)', 'bc(ca)']
        self.assertEqual(self.db.scan('a'), expected)

    @timeout(0.4)
    def test_level_2_case_06_resets(self):
        self.db.set('foo', 'bar', 'baz')
        self.db.set('foo', 'two', 'three')
        self.db.set('foo', 'bar', 'boo')
        self.assertEqual(self.db.get('foo', 'bar'), 'boo')
        expected = ['bar(boo)', 'two(three)']
        self.assertEqual(self.db.scan('foo'), expected)
        self.db.set('foo', 'two', 'four')
        self.assertTrue(self.db.delete('foo', 'bar'))
        self.assertFalse(self.db.scan_by_prefix('foo', 'b'))
        self.db.set('foo', 'two', 'four')
        self.db.set('foo', 'two', 'four')
        self.db.set('foo', 'bar', 'baz')
        expected = ['bar(baz)', 'two(four)']
        self.assertEqual(self.db.scan('foo'), expected)
        self.assertEqual(self.db.get('foo', 'two'), 'four')

    @timeout(0.4)
    def test_level_2_case_07_resets_and_deletes_with_same_keys(self):
        self.db.set('key1', 'field1', 'value1')
        self.db.set('key1', 'field2', 'value2')
        self.db.set('key2', 'field1', 'value3')
        self.db.set('key3', 'field1', 'value4')
        self.db.set('key3', 'field2', 'value5')
        self.db.set('key3', 'field3', 'value6')
        expected = ['field1(value4)', 'field2(value5)', 'field3(value6)']
        self.assertEqual(self.db.scan_by_prefix('key3', 'fiel'), expected)
        self.db.set('key1', 'field2', 'value7')
        self.db.set('key2', 'field1', 'value8')
        self.db.set('key3', 'field1', 'value9')
        self.db.set('key1', 'fact', 'value10')
        self.assertEqual(self.db.get('key1', 'field1'), 'value1')
        expected = ['field1(value1)', 'field2(value7)']
        self.assertEqual(self.db.scan_by_prefix('key1', 'fi'), expected)
        self.assertTrue(self.db.delete('key1', 'field1'))
        self.assertTrue(self.db.delete('key3', 'field2'))
        self.assertTrue(self.db.delete('key2', 'field1'))
        self.assertFalse(self.db.delete('key4', 'field1'))
        expected = ['fact(value10)', 'field2(value7)']
        self.assertEqual(self.db.scan('key1'), expected)
        self.assertEqual(self.db.get('key1', 'field2'), 'value7')
        self.assertIsNone(self.db.get('key3', 'field2'))

    @timeout(0.4)
    def test_level_2_case_08_random_ordered_operations(self):
        self.assertFalse(self.db.scan_by_prefix('key', 'key'))
        self.assertFalse(self.db.delete('key', 'key'))
        self.assertFalse(self.db.delete('key', 'key2'))
        self.assertFalse(self.db.scan_by_prefix('key', 'key'))
        self.assertIsNone(self.db.get('key', 'key'))
        self.assertFalse(self.db.scan_by_prefix('k', 'key'))
        self.assertFalse(self.db.delete('key', 'key'))
        self.db.set('key', 'key', 'aaaaa')
        self.db.set('foo', 'bar', 'baz')
        self.assertFalse(self.db.delete('key', 'bar'))
        self.assertFalse(self.db.delete('key', 'key2'))
        self.assertEqual(self.db.get('key', 'key'), 'aaaaa')
        self.db.set('key', 'key', 'otherValue')
        expected = ['key(otherValue)']
        self.assertEqual(self.db.scan('key'), expected)
        self.assertFalse(self.db.scan_by_prefix('key', 'e'))

    @timeout(0.4)
    def test_level_2_case_09_mixed_multiple_operations_1(self):
        self.db.set('a', 'b', 'c')
        self.db.set('a', 'c', 'd')
        self.assertIsNone(self.db.get('c', 'a'))
        expected = ['c(d)']
        self.assertEqual(self.db.scan_by_prefix('a', 'c'), expected)
        self.assertEqual(self.db.scan_by_prefix('a', 'c'), expected)
        self.db.set('a', 'd', 'e')
        self.assertTrue(self.db.delete('a', 'c'))
        self.assertFalse(self.db.delete('a', 'c'))
        self.db.set('a', 'e', 'f')
        self.assertTrue(self.db.delete('a', 'b'))
        self.db.set('a', 'f', 'g')
        self.assertIsNone(self.db.get('a', 'c'))
        expected = ['d(e)', 'e(f)', 'f(g)']
        self.assertEqual(self.db.scan('a'), expected)

    @timeout(0.4)
    def test_level_2_case_10_mixed_multiple_operations_2(self):
        self.db.set('a', 'a', 'b')
        self.db.set('a', 'A', 'c')
        expected = ['a(b)']
        self.assertEqual(self.db.scan_by_prefix('a', 'a'), expected)
        self.assertTrue(self.db.delete('a', 'a'))
        self.assertTrue(self.db.delete('a', 'A'))
        self.assertFalse(self.db.scan('a'))
        self.db.set('a', 'A', 'b')
        self.db.set('a', 'A', 'c')
        expected = ['A(c)']
        self.assertEqual(self.db.scan('a'), expected)
        self.assertEqual(self.db.scan_by_prefix('a', 'A'), expected)
        self.assertEqual(self.db.get('a', 'A'), 'c')
        self.db.set('A', 'A', 'B')
        expected = ['A(B)']
        self.assertEqual(self.db.scan('A'), expected)
