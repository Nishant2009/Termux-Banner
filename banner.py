import os

os.system("""command -v lolcat > /dev/null 2>&1 || { echo >&2 "...";echo "";echo "";echo "[^^] lolcat Installing...";pip install git+https://github.com/Nishant2009/lolcat.git;clear; }
command -v toilet > /dev/null 2>&1 || { echo >&2 "...";echo "";echo "";echo "[^^] Toilet Installing...";pkg install toilet;clear; }
command -v figlet > /dev/null 2>&1 || { echo >&2 "...";echo "";echo "";echo "[^^] Figlet Installing...";pkg install figlet;clear; }""")

name = input('What To Write On Banner (eg. NISHANT):  ')
is_skipped = False
with open("..//usr//etc//bash.bashrc", "r") as r, open("ab.txt", "w") as w:
  for line in r:
    line_to_match = line
    if line[-1] == '\n':
      line_to_match = line[:-1]
    if (line_to_match != 'clear'):
      w.write(line)
    else:
      is_skipped = True
      break
if is_skipped:
  os.remove("..//usr//etc//bash.bashrc")
  os.rename('ab.txt' ,"../usr/etc/bash.bashrc")
else:
  os.remove('ab.txt')

with open("..//usr//etc//bash.bashrc", "a") as w:
  w.write('\nclear\ncowsay -f eyes '+name+' | lolcat \ntoilet -f big         '+ name+' | lolcat\necho -e " \e[36m\t    Everything is Possible..!!"')

