# qgbd: quick git branch deleter
#    because I spend too much time manually deleting branches
# 
# usage: qgbd
# - check boxes
# - y/n confirm
# - delete branches

import subprocess
import inquirer

def main():
    br = subprocess.check_output(["git", "branch"])
    branches = [b for b in br.split() if b != b'*']
    qs = [
        inquirer.Checkbox(
            "Branches",
            message="Check to remove branch",
            choices=branches
        )
    ]

    res = inquirer.prompt(qs)

    to_delete = [str(b, 'utf-8') for b in res["Branches"]]
    cmd = "git branch -D {}".format(" ".join(to_delete))
    res = input('will run: "{}" \nok? (y/n): '.format(cmd))
    if res != 'y':
        print("Canceled, try again")
    else:
        res = subprocess.check_output(cmd.split(" "))
        print(str(res, 'utf-8'))

if __name__ == "__main__":
    main()