import json


def get_help_message(description):
    helpmsg = description
    helpmsg += '**$help** - ``Display this help message.``\n'
    helpmsg += '**$story** - ``tell a story``\n'
    helpmsg += '\t``list``\n'
    helpmsg += '\t``begin <title>``\n'

    return helpmsg


def get_example_votes():
    votes = [
                {'voter': 'cryptos', 'weight': 10676, 'rshares': '6392530356', 'percent': 500, 'reputation': '46108001423569', 'time': '2018-03-05T19:27:33'},
                {'voter': 'tezcatlipoka', 'weight': 5493, 'rshares': '5759840361', 'percent': 10000, 'reputation': 0, 'time': '2018-03-09T02:54:09'},
                {'voter': 'markangeltrueman', 'weight': 4450, 'rshares': '4665857771', 'percent': 1600, 'reputation': '7099622673688', 'time': '2018-03-06T18:00:27'},
                {'voter': 'robinhaney', 'weight': 70881, 'rshares': '74324188713', 'percent': 10000, 'reputation': '8938920329167', 'time': '2018-03-09T02:55:12'},
                {'voter': 'pioner888777', 'weight': 28381, 'rshares': '29759164241', 'percent': 10000, 'reputation': '9890043868901', 'time': '2018-03-09T02:54:54'},
                {'voter': 'steemitstats', 'weight': 1291, 'rshares': 1041448335, 'percent': 500, 'reputation': '323301638489', 'time': '2018-03-05T18:15:36'},
                {'voter': 'oyvindsabo', 'weight': 431, 'rshares': 451994571, 'percent': 1600, 'reputation': '918876767304', 'time': '2018-03-06T17:35:39'},
                {'voter': 'tdre', 'weight': 2762, 'rshares': 723793454, 'percent': 10000, 'reputation': '185903820208', 'time': '2018-03-05T18:45:24'},
                {'voter': 'ryacha21', 'weight': 7071, 'rshares': '7414658176', 'percent': 10000, 'reputation': '5364734720999', 'time': '2018-03-09T02:54:27'},
                {'voter': 'passive', 'weight': 78707, 'rshares': '82530976445', 'percent': 10000, 'reputation': '474302221577', 'time': '2018-03-09T02:55:21'},
                {'voter': 'markus.light', 'weight': 19676, 'rshares': '5158050014', 'percent': 10000, 'reputation': '3139416244678', 'time': '2018-03-05T19:04:15'},
                {'voter': 'limesoda', 'weight': 227806, 'rshares': '108856445148', 'percent': 10000, 'reputation': '383149359571', 'time': '2018-03-05T19:23:12'},
                {'voter': 'k3lda', 'weight': 8522, 'rshares': 2233986154, 'percent': 10000, 'reputation': '280912295054', 'time': '2018-03-05T19:09:36'},
                {'voter': 'mwfiae', 'weight': 93015, 'rshares': '14622965272', 'percent': 10000, 'reputation': '2766711671734', 'time': '2018-03-05T18:44:39'},
                {'voter': 'kurodevs', 'weight': 572, 'rshares': 599210225, 'percent': 10000, 'reputation': '31284109437', 'time': '2018-03-05T19:45:51'},
                {'voter': 'trufflepig', 'weight': 628, 'rshares': 659032341, 'percent': 3200, 'reputation': '166896963971', 'time': '2018-03-06T17:35:12'},
                {'voter': 'derasmo', 'weight': 0, 'rshares': 0, 'percent': 0, 'reputation': '462498278517', 'time': '2018-03-09T06:36:06'}
            ]

    return votes


def build_post(title, body):
    return {'title': title, 'body': body}


def build_postid(username, permlink):
    return {'username': username, 'permlink': permlink}


class PostMetadata:

    def __init__(self):
        self.app = "storybot/0.1.0"
        self.format = "markdown"

        self.storybot = dict()

    def set_value(self, **kwargs):
        self.storybot.update(kwargs)

    def get_json(self):
        output = dict()
        output['app'] = self.app
        output['format'] = self.format
        output['storybot'] = self.storybot

        return json.dumps(output)
