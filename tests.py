import unittest
from main import InstagramBot


class InstagramBotTests(unittest.TestCase):
    def setUp(self) -> None:
        # All tests will fail until you replace the username and password below with valid entries
        super(InstagramBotTests, self).setUp()
        self.bot = InstagramBot("username", "password")

    def test_login(self):
        signIn = self.bot.signIn()
        self.assertTrue(signIn)

    def test_follow_user(self):
        # TODO: need to handle login to pass
        followed = self.bot.followWithUsername('therock')
        self.assertTrue(followed)

    def test_unfollow_user(self):
        unfollowed = self.bot.unfollowWithUsername('therock')
        self.assertTrue(unfollowed)

    def test_get_users_followers(self):
        # TODO: need to handle login to pass
        followers = self.bot.getUserFollowers("therock", 10)
        self.assertTrue(len(followers) == 10)


if __name__=='__main__':
    unittest.main()
