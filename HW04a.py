"""
Take as input a GitHub user ID.
The output from the function will be a list of the names of the repositories that the user has,
along with the number of commits that are in each of the listed repositories.
Like "
Repo: Triangle567 Number of commits: 10
Repo: Square567 Number of commits: 27
"
"""
import requests

def result(username):
    """ Take a user ID.
        The output from the function will be a list of the names of the repositories that the user has,
        along with the number of commits that are in each of the listed repositories.
    """
    list_ = list()
    request = requests.get(f'https://api.github.com/users/{username}/repos')
    json = request.json()
    for i in range(0,len(json)):
        repo_name = json[i]['name']
        commits = requests.get(f'https://api.github.com/repos/{username}/{repo_name}/commits')
        list_.append(f"Repo: {repo_name} Number of commits: {len(commits.json())}")

    return list_


def main():
    """ Get an input username and print result(username)"""
    username = input("Enter the github username: ")
    print(result(username))