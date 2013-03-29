import sys

sys.path.append('./')
sys.path.append('../')

from api.service.Service import Service
from api.access.AnalyticApiKey import AnalyticApiKey


def test1():
    s = Service()
    s.debug(s.server_loc)
    k = AnalyticApiKey('B63bQg1ipu37TmXLK4aH3gZgLWFmYJltMb2CBjCs', s)
    s.debug('exists: ' + str(k.exists()))


def test2():
    s = Service()
    s.debug(s.server_loc)
    k = AnalyticApiKey('xxx', s)
    k.exists()
    s.debug('exists: ' + str(k.exists()))


if __name__ == '__main__':
    test1()
    test2()
