import sys
import requests

class activitychecker:
    def getGithubActivity(self, username:str):

        
        url = f"https://api.github.com/users/{username}/events/public"


        try:
            response = requests.get(url)

            response.raise_for_status()

            data =  response.json()

            print(data)
        except requests.exceptions.RequestException as e:
            print(e)


if __name__ == "__main__":
    username = input("input username: ")
    t = activitychecker()
    t.getGithubActivity(username)