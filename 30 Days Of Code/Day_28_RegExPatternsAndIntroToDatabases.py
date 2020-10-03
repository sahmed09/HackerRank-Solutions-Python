import re

if __name__ == '__main__':
    N = int(input())
    data = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        # email_pattern = r"^[a-z.]+@gmail\.com$"
        email_pattern = r".*@gmail\.com$"

        if re.search(email_pattern, emailID):
            data.append(firstName)

    print(*sorted(data), sep="\n")
