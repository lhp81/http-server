import unittest
from request_handler import *

# tests to see if non-get requests raise an exception
class TestsForMyRequestHandler(unittest.TestCase):

    def testFailUnlessRaises(self):
        for s in ('POST /index.html HTTP/1.1 \r\n \
                        Host: www.example.com \r\n \
                        <CRLF>',
                  'PUT /index.html HTTP/1.1 \r\n \
                        Host: www.example.com \r\n \
                        <CRLF>',
                  'DELETE /index.html HTTP/1.1 \r\n \
                        Host: www.example.com \r\n \
                       <CRLF>'):
            self.failUnlessRaises(ParseException, parse_request, s)

    def testEqual(self):
        tester = parse_request('GET /index.html HTTP/1.1 \r\n \
                        Host: www.example.com \r\n \
                        <CRLF>')
        self.assertEqual(tester, '/index.html')


class TestsForTheResponseBuilder(unittest.TestCase):
    """These will test the response builder to see if it does the right thing
    and to see if it can be tricked."""

    def testForCorrectResponse(self):
        
if __name__ == '__main__':
    unittest.main()