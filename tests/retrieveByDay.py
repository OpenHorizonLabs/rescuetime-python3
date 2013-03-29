import sys
import datetime

sys.path.append('./')
sys.path.append('../')

from api.service.Service import Service
from api.access.AnalyticApiKey import AnalyticApiKey
from api.model.ResponseData import ResponseData

# replace with your own, otherwise nothing will be returned.
apikey = 'B63C4fZ0bQb6iu1EXYPMhsFLT_VqUhutPiu9fIwP'

if __name__ == '__main__':
    s = Service()
    s.debug(s.server_loc)
    k = AnalyticApiKey(apikey, s)
    s.debug('exists: ' + str(k.exists()))
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)
    r = ResponseData(k, **{'op': 'select',
                           'vn': 0,
                           'pv': 'rank',
                           'rb': yesterday.strftime('%Y-%m-%d'),
                           're': today.strftime('%Y-%m-%d')
                       })
    r.sync()
    s.debug('data object: ' + str(r.object))
    s.debug('=============')
    for k in r.object:
        s.debug("\n\tkey: %s\n\tvalue:%s\n-------\n" % (str(k), str(r.object[k])))
        if k == 'rows':
            for ro in r.object[k]:
                s.debug("\n\t\trow(%d): %s\n-------\n" % (len(ro), str(ro)))
