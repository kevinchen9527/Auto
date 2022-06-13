from MyQR import myqr
import os

myqr.run(words='http://www.baidu.com', picture=os.path.abspath(os.path.dirname(__file__)) + '/a.jpg', colorized=True)


