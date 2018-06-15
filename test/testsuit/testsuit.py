import unittest
from config.config import basedir
from lib import HTMLTestRunner_PY3


suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase')
# unittest.TextTestRunner(verbosity=2).run(suite)
outfile = open(basedir + "/report/Report.html", "wb")
runner = HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='全国城市油价 Test Report',
    description='测试'
    )
runner.run(suite)
outfile.close()
from lib import send_mail
send_mail.send_mail_testreport('test')