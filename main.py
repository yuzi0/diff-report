import difflib

text1 = open("test1.c", encoding='UTF-8').readlines()
text2 = open("test2.c", encoding='UTF-8').readlines()

d = difflib.HtmlDiff(wrapcolumn = 80)
difference = d.make_file(text1, text2, diffonly=True, fromdesc="Before code", todesc="After code")
with open("diff.html", "w") as f:
    for line in difference.splitlines():
        print (line, file=f)