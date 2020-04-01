import random
import unittest
import link_handler
import disassemble
import markdowntohtml


class TestSampleInputs(unittest.TestCase):
    """ Tests of different markdown format conversions """

    def testBlankInput(self):
        """ Test blank input. """
        self.assertEqual(markdowntohtml.convert(''), '')

    def testHeaders(self):
        """ Test header counts """
        self.assertEqual(markdowntohtml.convert('# test'), '<h1>test</h1>')
        self.assertEqual(markdowntohtml.convert('## test'), '<h2>test</h2>')
        self.assertEqual(markdowntohtml.convert('### test'), '<h3>test</h3>')
        self.assertEqual(markdowntohtml.convert('#### test'), '<h4>test</h4>')
        self.assertEqual(markdowntohtml.convert('##### test'), '<h5>test</h5>')
        self.assertEqual(markdowntohtml.convert('###### test'), '<h6>test</h6>')

    def testNormal(self):
        """ Test header counts """
        self.assertEqual(markdowntohtml.convert('LUL'), '<p>LUL</p>')

    def testBasicLink(self):
        """ Test just a link by itself """
        self.assertEqual(markdowntohtml.convert('[Mailchimp](https://www.mailchimp.com)'), '<p><a href="https://www.mailchimp.com">Mailchimp</a></p>')


    def testLinkInParagraph(self):
        """ Test link formation inside a paragraph block """
        self.assertEqual(markdowntohtml.convert('This is a paragraph [with an inline link](http://google.com). Neat, eh?'), '<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>')

    def testLinkInHeader(self):
        """ Test link inside a header """
        self.assertEqual(markdowntohtml.convert('## This is a header [with a link](http://yahoo.com)'), '<h2>This is a header <a href="http://yahoo.com">with a link</a></h2>')

    def testLinkHeader(self):
        """ Test link inside a header """
        self.assertEqual(markdowntohtml.convert('# [link header](http://yahoo.com)'), '<h1><a href="http://yahoo.com">link header</a></h1>')

    def testMalformedLink(self):
        """ Test where link formatting is off by a character"""
        self.assertEqual(markdowntohtml.convert('(Mailchimp)[https://www.mailchimp.com]'),'<p>(Mailchimp)[https://www.mailchimp.com]</p>')





if __name__ == '__main__':
    unittest.main()