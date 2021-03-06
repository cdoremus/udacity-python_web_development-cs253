'''
Created on May 6, 2012

@author: h87966
'''
import unittest
from unit3.blog_entry import BlogData
from google.appengine.ext import testbed
from unit3.blog_datastore_appengine import BlogAppengineDataStore

class Test(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.storage = BlogAppengineDataStore()
        
    
    def tearDown(self):
        self.testbed.deactivate()

    def testPut(self):
        data = BlogData(subject='Foo',content='Foo blog')
        data.put()
        pass

    def test_save(self):
        b3 = BlogData(subject='blog1',content='This is blog1')
        self.storage.save(b3)
        b3a = self.storage.fetch(1)
        self.assertEquals(b3.content, b3a.content, "Blog " + str(b3) + ' was not saved. This was saved instead: ' + str(b3a))
        pass

    def test_fetch(self):
        b = BlogData(subject='blog1',content='This is blog1')
        expected = b.subject 
        self.storage.save(b)
        b1 = self.storage.fetch(1)
        self.assertEquals(expected, b1.subject, "Blog with id " + str(expected) + ' was not found.')
        pass

    def test_fetchAll(self):
        self.storage.save(BlogData(subject='blog1',content='This is blog1'))
        self.storage.save(BlogData(subject='blog2',content='This is blog2'))
        expected = 2
        actual = self.storage.fetchAll()
        print actual
        self.assertEquals(expected, actual.count(), "Blog count of " + str(expected) + ' size was not found.')

        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPut']
    unittest.main()