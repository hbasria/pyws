# coding=utf-8

import suds
import unittest2 as unittest

from testcases.base import BaseTestCaseMixin


class RaisesExceptionTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_simple(self):
        try:
            self.service.raises_exception('hello')
        except suds.WebFault, e:
            self.assertEqual(e.fault.faultstring, 'hello error')
            return
        self.assertTrue(False, 'Exception hasn\'t been thrown')

    def test_unicode(self):
        try:
            self.service.raises_exception(u'лопата')
        except suds.WebFault, e:
            self.assertEqual(e.fault.faultstring, u'лопата error')
            return
        self.assertTrue(False, 'Exception hasn\'t been thrown')
