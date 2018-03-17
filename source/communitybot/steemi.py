import datetime

from timeit import default_timer as timer

from communitybot.settings import STEEM_NODES, STEEM_BOT_POSTING_KEY, STEEM_BOT_ACCOUNT, STEEM_API_MODE
from communitybot.utils import get_example_votes, build_postid

from steem import Steem
from steem.account import Account
from steem.post import Post
from steem.utils import derive_permlink, construct_identifier

_steem_account = None
_steem_conn = None

_last_post_id = None
_last_post_created = None


def can_post():
    global _last_post_created

    if _last_post_created is None:
        return True
    else:
        now = datetime.datetime.utcnow()
        if 20 < (now - _last_post_created).total_seconds():
            return True

    return False


def update_last_post(postid):
    global _last_post_id
    global _last_post_created

    identifier = construct_identifier(postid['username'], postid['permlink'])

    if identifier is not _last_post_id:
        steemd_instance = get_steem_conn()
        steem_post = Post(identifier, steemd_instance=steemd_instance)

        _last_post_id = identifier
        _last_post_created = steem_post.get('created')


def get_steem_acc():
    global _steem_account
    if _steem_account is None:
        _steem_account = Account(STEEM_BOT_ACCOUNT, get_steem_conn())

    return _steem_account


def get_votepower():
    account = get_steem_acc()

    # TODO: calculate real voting power
    # const secondsago = (new Date().getTime() - new Date(botStatus.last_vote_time + "Z").getTime()) / 1000;
    # const votingPower = botStatus.voting_power + (10000 * secondsago / 432000);    

    votepower = account.voting_power()

    return votepower


def get_steem_conn():
    global _steem_conn
    if _steem_conn is None:
        _steem_conn = Steem(nodes=STEEM_NODES, keys=[STEEM_BOT_POSTING_KEY, ])

    return _steem_conn


def steemi_post_steempython(post, parentid=None):
    reply_identifier = None
    if parentid is not None:
        reply_identifier = construct_identifier(parentid['username'], parentid['permlink'])

    if 'permlink' in post:
        permlink = post['permlink']
    else:
        permlink = derive_permlink(post['title'], reply_identifier)

    steemd_instance = get_steem_conn()
    steemd_instance.commit.post(post['title'], post['body'], STEEM_BOT_ACCOUNT, permlink=permlink, reply_identifier=reply_identifier, tags="testing")

    postid = build_postid(STEEM_BOT_ACCOUNT, permlink)

    return postid


def steemi_post_debug(post, parentid=None):
    print('steemi post:\n%s' % '\n'.join(post))

    username = 'derasmo'
    if parentid is None:
        permlink = 'a-story-to-test'
    else:
        permlink = 're--a-story-to-test'
        print('steemi post: parent identifier is set\n%s' % '\n'.join(parentid))

    postid = build_postid(username, permlink)

    return postid


# post: {'title': <string>, 'body': <body>, 'permlink': <string>}
def steemi_post(post, apimode=STEEM_API_MODE):
    postid = None
    if apimode == 'debug':
        postid = steemi_post_debug(post)
    elif can_post():
        if apimode == 'steempython':
            postid = steemi_post_steempython(post)

        update_last_post(postid)

    return postid


def steemi_comment(parentid, post, apimode=STEEM_API_MODE):
    permlink = None
    if apimode == 'debug':
        permlink = steemi_post_debug(post, parentid)

    if apimode == 'steempython':
        permlink = steemi_post_steempython(post, parentid)

    return permlink


# postid: {'username': <string>, 'permlink': <string>}
def steemi_get_votes_steempython(postid):
    steemd_instance = get_steem_conn()
    votes = steemd_instance.get_active_votes(postid['username'], postid['permlink'])

    return votes


def steemi_get_votes_debug(postid):
    votes = get_example_votes()

    return votes


def steemi_get_votes(postid, apimode=STEEM_API_MODE):
    votes = []

    if apimode == 'debug':
        votes = steemi_get_votes_debug(postid)

    if apimode == 'steempython':
        votes = steemi_get_votes_steempython(postid)

    return votes


def steemi_vote_up_steempython(postid):
    identifier = construct_identifier(postid['username'], postid['permlink'])
    steemd_instance = get_steem_conn()

    steem_post = Post(identifier, steemd_instance=steemd_instance)

    already_voted = False
    for active_vote in steem_post.get("active_votes", []):
        if active_vote.get("voter") == STEEM_BOT_ACCOUNT:
            already_voted = True
            break

    if not already_voted:
        steem_post.vote(100, STEEM_BOT_ACCOUNT)


def steemi_vote_up_debug(postid):
    identifier = construct_identifier(postid['username'], postid['permlink'])
    print('steemi vote up: %s' % identifier)


def steemi_vote_up(postid, apimode=STEEM_API_MODE):
    if apimode == 'debug':
        steemi_vote_up_debug(postid)

    if apimode == 'steempython':
        steemi_vote_up_steempython(postid)
