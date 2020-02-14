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
import unittest

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
        commits = requests.get(f'https://api.github.com/users/{username}/{repo_name}/repos')
        list_.append(f"Repo: {repo_name} Number of commits: {len(commits.json())}")

    return list_


def main():
    """ Get an input"""
    username = input("Enter the github username: ")
    result(username)


class TestResult(unittest.TestCase):
    """ test result() """
    def testResult(self):
        list1 = ['Repo: cs61b Number of commits: 2', 'Repo: HW09 Number of commits: 2',
                 'Repo: SSW567 Number of commits: 2', 'Repo: SSW810 Number of commits: 2',
                 'Repo: Triangle567 Number of commits: 2']
        self.assertEqual(result("deng125125"), list1)
        self.assertEqual(result("John567"), [])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)