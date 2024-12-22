class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} has logged in.")

    def logout(self):
        print(f"{self.username} has logged out.")

    def post(self, content):
        print(f"{self.username} posted: {content}")

    def change_password(self, new_password):
        self.password = new_password
        print(f"{self.username} has changed their password.")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story):
        print(f"{self.username} shared a story: {story}")

    def add_follower(self):
        self.number_of_followers += 1 #Use += for proper increment
        print(f"{self.username} gained a new follower! Total followers: {self.number_of_followers}")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        self.number_of_tweets += 1 #Use += for proper increment
        print(f"{self.username} tweeted: {tweet_content}. Total tweets: {self.number_of_tweets}")

kylmlbb = InstagramAccount("kylmlbb", "pass123", 500)
kylmlbb.login()
kylmlbb.post("Hello, Instagram!")
kylmlbb.add_follower()
kylmlbb.share_story("Check out my new story!")
kylmlbb.logout()

Jordi_Raffles = TwitterAccount("Jordi Raffles", "pass456", 1500)
Jordi_Raffles.login()
Jordi_Raffles.post("Hello, Twitter!")
Jordi_Raffles.tweet("This is my first tweet!")
Jordi_Raffles.logout()
