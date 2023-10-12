import os
import sys
import re

# use: python hexo-html.py <category>/<markdown-slide-file.md>

post = sys.argv[1]
md_path = "./source/_posts/" + post

if not os.path.exists(md_path):
    print("not exist post file: {}".format(post))
    sys.exit(1)
with open(md_path, "r+") as f:
    lines = f.readlines()
    for line in lines:
        match_res = re.match("date: ", line)
        if match_res:
            break
    if not match_res:
        print("not has property: date")
        sys.exit()
    [year, mon, day] = line.split(' ')[1].split('-')
    html_path = "./public/" + \
        str(year) + "/" + str(mon)+"/" + str(day) + "/" + post.split('.')[0]
    print("generate html file in \"{}\"".format(html_path))

os.system("reveal-md " + md_path + " --static " + html_path)
