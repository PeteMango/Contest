import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_db_impl import InMemoryDBImpl


class Level1Tests(unittest.TestCase):
    """
    The test class below includes 10 tests for Level 1.

    All have the same score.
    You are not allowed to modify this file, but feel free to read the source code to better understand what is happening in every specific case.
    """

    failureException = Exception


    @classmethod
    def setUp(cls):
        cls.db = InMemoryDBImpl()

    @timeout(0.4)
    def test_level_1_case_01_simple_set_and_get_1(self):
        self.db.set('employee1', 'city', 'Annapolis')
        self.db.set('employee2', 'id', '0123')
        self.assertEqual(self.db.get('employee1', 'city'), 'Annapolis')

    @timeout(0.4)
    def test_level_1_case_02_simple_set_and_get_2(self):
        self.assertIsNone(self.db.get('dept4', 'name'))
        self.assertIsNone(self.db.get('dept4', 'name'))
        self.db.set('dept4', 'name', 'Main')
        self.assertEqual(self.db.get('dept4', 'name'), 'Main')
        self.assertEqual(self.db.get('dept4', 'name'), 'Main')

    @timeout(0.4)
    def test_level_1_case_03_simple_set_get_and_delete(self):
        self.db.set('book1', 'title', 'Island')
        self.assertEqual(self.db.get('book1', 'title'), 'Island')
        self.assertTrue(self.db.delete('book1', 'title'))
        self.assertIsNone(self.db.get('book1', 'title'))

    @timeout(0.4)
    def test_level_1_case_04_multiple_objects_with_same_key(self):
        self.db.set('user1', 'firstName', 'Greg')
        self.db.set('user1', 'lastName', 'Wright')
        self.db.set('lastName', 'user1', 'error')
        self.assertEqual(self.db.get('user1', 'lastName'), 'Wright')
        self.assertEqual(self.db.get('user1', 'firstName'), 'Greg')
        self.assertIsNone(self.db.get('user1', 'Greg'))
        self.assertIsNone(self.db.get('user1', 'Wright'))
        self.assertIsNone(self.db.get('user1', 'city'))
        self.assertFalse(self.db.delete('user1', 'city'))
        self.db.set('user1', 'city', 'London')
        self.assertEqual(self.db.get('user1', 'firstName'), 'Greg')
        self.assertEqual(self.db.get('user1', 'lastName'), 'Wright')
        self.assertEqual(self.db.get('user1', 'city'), 'London')
        self.assertEqual(self.db.get('lastName', 'user1'), 'error')

    @timeout(0.4)
    def test_level_1_case_05_multiple_unused_deletes(self):
        self.db.set('A', 'BC', 'D')
        self.db.set('AB', 'C', 'E')
        self.assertFalse(self.db.delete('BC', 'A'))
        self.assertIsNone(self.db.get('BC', 'A'))
        self.assertEqual(self.db.get('A', 'BC'), 'D')
        self.assertTrue(self.db.delete('A', 'BC'))
        self.assertFalse(self.db.delete('A', 'BC'))
        self.assertFalse(self.db.delete('B', 'AC'))
        self.assertFalse(self.db.delete('A', 'BC'))
        self.assertIsNone(self.db.get('A', 'BC'))
        self.assertEqual(self.db.get('AB', 'C'), 'E')

    @timeout(0.4)
    def test_level_1_case_06_resets(self):
        self.db.set('foo', 'bar', 'baz')
        self.db.set('foo', 'two', 'three')
        self.db.set('foo', 'bar', 'boo')
        self.assertEqual(self.db.get('foo', 'bar'), 'boo')
        self.assertEqual(self.db.get('foo', 'two'), 'three')
        self.db.set('foo', 'two', 'four')
        self.assertTrue(self.db.delete('foo', 'bar'))
        self.assertIsNone(self.db.get('foo', 'bar'))
        self.db.set('foo', 'two', 'four')
        self.db.set('foo', 'two', 'four')
        self.db.set('foot', 'wo', 'five')
        self.db.set('foo', 'bar', 'baz')
        self.assertEqual(self.db.get('foo', 'bar'), 'baz')
        self.assertEqual(self.db.get('foo', 'two'), 'four')

    @timeout(0.4)
    def test_level_1_case_07_resets_and_deletes_with_same_keys(self):
        self.db.set('key1', 'field1', 'value1')
        self.db.set('key1', 'field2', 'value2')
        self.db.set('key2', 'field1', 'value3')
        self.db.set('key3', 'field1', 'value4')
        self.db.set('key3', 'field2', 'value5')
        self.db.set('key3', 'field3', 'value6')
        self.db.set('key1', 'field2', 'value7')
        self.db.set('key2', 'field1', 'value8')
        self.db.set('key3', 'field1', 'value9')
        self.assertTrue(self.db.delete('key1', 'field1'))
        self.assertTrue(self.db.delete('key3', 'field2'))
        self.assertTrue(self.db.delete('key2', 'field1'))
        self.assertFalse(self.db.delete('key4', 'field1'))
        self.assertIsNone(self.db.get('key1', 'field1'))
        self.assertEqual(self.db.get('key1', 'field2'), 'value7')
        self.assertIsNone(self.db.get('key2', 'field1'))
        self.assertIsNone(self.db.get('key2', 'field2'))
        self.assertEqual(self.db.get('key3', 'field1'), 'value9')
        self.assertIsNone(self.db.get('key3', 'field2'))
        self.assertEqual(self.db.get('key3', 'field3'), 'value6')

    @timeout(0.4)
    def test_level_1_case_08_random_ordered_operations(self):
        self.assertFalse(self.db.delete('key', 'key'))
        self.assertFalse(self.db.delete('key', 'key2'))
        self.assertIsNone(self.db.get('A', 'B'))
        self.assertIsNone(self.db.get('key', 'key'))
        self.assertFalse(self.db.delete('key', 'key'))
        self.db.set('key', 'key', 'aaaaa')
        self.db.set('foo', 'bar', 'baz')
        self.assertIsNone(self.db.get('foo', 'baz'))
        self.assertFalse(self.db.delete('key', 'bar'))
        self.assertFalse(self.db.delete('key', 'key2'))
        self.assertEqual(self.db.get('key', 'key'), 'aaaaa')
        self.assertIsNone(self.db.get('k', 'eykey'))
        self.db.set('key', 'key', 'otherValue')
        self.assertEqual(self.db.get('key', 'key'), 'otherValue')

    @timeout(0.4)
    def test_level_1_case_09_mixed_multiple_operations_1(self):
        self.db.set('a', 'b', 'c')
        self.db.set('a', 'c', 'd')
        self.assertIsNone(self.db.get('c', 'a'))
        self.db.set('a', 'd', 'e')
        self.assertTrue(self.db.delete('a', 'c'))
        self.assertFalse(self.db.delete('a', 'c'))
        self.db.set('a', 'e', 'f')
        self.assertTrue(self.db.delete('a', 'b'))
        self.db.set('a', 'f', 'g')
        self.assertIsNone(self.db.get('a', 'c'))
        self.assertIsNone(self.db.get('a', 'b'))
        self.assertEqual(self.db.get('a', 'd'), 'e')

    @timeout(0.4)
    def test_level_1_case_10_mixed_multiple_operations_2(self):
        self.db.set('a', 'a', 'b')
        self.assertIsNone(self.db.get('a', 'b'))
        self.db.set('a', 'A', 'c')
        self.assertEqual(self.db.get('a', 'a'), 'b')
        self.assertTrue(self.db.delete('a', 'a'))
        self.assertTrue(self.db.delete('a', 'A'))
        self.db.set('a', 'A', 'b')
        self.db.set('a', 'A', 'c')
        self.assertIsNone(self.db.get('a', 'a'))
        self.assertEqual(self.db.get('a', 'A'), 'c')
