README.txt

Quandoo QA Home Assessment
=========================

Prerequisites
-------------

1. Either Python 2 or 3

2. Install unittest-xml-reporting: pip install unittest-xml-reporting

Running the Tests
-----------------

1. Open the folder in the command line

2. To run all tests: python -m unittest quandoo

3. To run a single test: python -m unittest quandoo.TestQuandoo.test_login_successs

4. To run all tests and generate xml report: python -m quandoo

Notes
-----

I’m afraid I haven’t used Cucumber professionally before, though I’d be very keen to learn this, and hopefully the code I’ve written could be reasonably easily adapted for that.

At the moment each test just runs arbitrarily in either Firefox or Chrome, but obviously that could be adapted based on whatever your process it.

Hopefully you don’t have any trouble running the tests, but just in case I’ve included a quick video, quandoo.gif.

To see the xml report, run step 4 above and then look in ./test-reports/.


Sam Alexander
23/01/2018
