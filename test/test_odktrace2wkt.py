# # coding=utf-8
# """Resources test.
#
# .. note:: This program is free software; you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation; either version 2 of the License, or
#      (at your option) any later version.
#
# """
#
# __author__ = 'smwltwesa6@gmail.com'
# __date__ = '2019-09-07'
# __copyright__ = 'Copyright 2019, Samweli Mwakisambwe'
#
# from .utilities import get_qgis_app
#
# from ..odktrace2wkt import ODKTrace2WKT
#
# from qgis.core import *
#
# import unittest
# import os
#
# QGIS_APP, CANVAS, IFACE, PARENT = get_qgis_app()
#
#
# class ODKTrace2WKTTest(unittest.TestCase):
#     """Tests main components
#     """
#
#     def setUp(self):
#         """Runs before each test."""
#         self.main = ODKTrace2WKT(None)
#
#     def tearDown(self):
#         """Runs after each test."""
#         self.main = None
#
#     def test_delimiter_detection(self):
#         """ Test delimiter can be detected """
#
#         testdir = os.path.abspath(os.path.join(
#             os.path.realpath(os.path.dirname(__file__))))
#
#         testdata = os.path.join(testdir, 'data')
#         input_dir = os.path.join(testdata, 'input')
#
#         file_path = os.path.join(input_dir, 'test_input.csv')
#         output_delimiter = self.main.detect_csv_delimiter(file_path)
#         expected_delimiter = ','
#
#         self.assertEqual(
#             expected_delimiter, output_delimiter)
#
#
# if __name__ == "__main__":
#     suite = unittest.makeSuite(ODKTrace2WKTTest)
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)
