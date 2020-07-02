import tweepy

auth = tweepy.OAuthHandler("API TOKEN", "API TOKEN SECRET")
auth.set_access_token("ACCESS TOKEN", "ACCESS TOKEN SECRET")

api = tweepy.API(auth)

timeline = api.home_timeline()


def readtweets():
    for tweets in timeline:
        print(f"{tweets.user.name} tweeted {tweets.text}")


def tweet(txt1):
    api.update_status(txt1)


def findfriends(handle):
    user = api.get_user(handle)
    print("User Details:")
    print(user.name, "\n", user.description ,"\n", user.location, "\n Followers")
    for f in user.followers():
        print(f.name)


def updateprofile(status):
    api.update_profile(description = status)


def search(keyword):
    for tweets in api.search(q=keyword, lang="en", rpp=10):
        print(f"{tweets.user.name}:{tweets.text}")


while True:
    choice = int(
        input("Please enter the function that you would like to use \n 1.Read tweets on timeline \n 2.Tweet from "
              "account \n 3. Search for user \n 4. Update Description \n 5. Get Tweet feed \n"))
    if choice == 1:
        readtweets()
    elif choice == 2:
        txt1 = input("What's on your mind?\n")
        tweet(txt1)
    elif choice == 3:
        handle = input("Enter your friends name\n")
        findfriends(handle)
    elif choice == 4:
        status = input("What describes you\n")
        updateprofile(status)
    elif choice == 5:
        keyword = input("What is the area of your interest\n")
        search(keyword)
    else:
        print("invalid choice -_-")

