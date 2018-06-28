
from hashlib import md5


class MD5:
    encoding = 'utf-8'

    @classmethod
    def md5(cls, b:bytes):
        if not isinstance(b,bytes):
            try:
                b = b.encode(cls.encoding)
            except Exception as e:
                raise TypeError('expect str or bytes but receive %s' % b.__class__.__name__)
        return md5(b).hexdigest()

class ImageBytes:
    '''
    image 容器 
    '''
    def __init__(self):
        self.img = b''

    def write(self, img):
        self.img = img

