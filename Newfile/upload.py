# -*- coding: utf-8 -*-

import oss2
import os
import time

auth = oss2.Auth('LTAIFcCSQbaxqnH4', 'GSwfkfacUODUA7iC9Ph5trvuVNmOJx')
bucket = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', 'pdfdocument')
#service = oss2.Service(auth, 'oss-cn-shanghai.aliyuncs.com')
#print([b.name for b in oss2.BucketIterator(service)])

localfilepath = (r'C:\Python27\Scripts\pdf')
filenames = []
while 1:
    for filename in os.listdir(localfilepath):
        #filenames.append(filename)
        time.sleep(2)
        with open(localfilepath + '\\' + filename, 'rb') as localfile:
            bucket.put_object('docpdf'+'/'+filename, localfile)
        time.sleep(2)
        os.remove(localfilepath + '\\' + filename)
        time.sleep(2)
        print filename + r' was uploaded successfully!'

