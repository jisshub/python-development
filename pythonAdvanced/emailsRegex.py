# finding users with email ends with @gmail.com

# program-1(Basic)
import re

# myEmail = ["jissmon@gmail.com", "jerin@yahoo.com"]
# # create a regex pattern
# searchPattern = re.compile("@gmail\.com")
# for email in myEmail:
#     # search that pattern in given email
#     if searchPattern.search(email):
#         print(email)

# program - 2(Advanced)
gmailusers = []


def find_gmail_users(getUserINfo):
    # create a regex pattern
    searchPattern = re.compile("@gmail\.com")
    for getOne in getUserINfo:
        for user_name, email in getOne.items():
            # search that regex in the given argument
            if searchPattern.search(getOne['email']):
                # print(getOne["name"])
                gmailusers.append(getOne['name'])
                break
    return gmailusers


getUserLists = [{"name": "jissmon", "email": "jiss@gmail.com"},
                {"name": "jerin", "email": "jerin@yahoo.in"},
                {"name": "jeffin", "email": "jeffin@gmail.com"}
                ]

f = find_gmail_users(getUserLists)
print(f)
