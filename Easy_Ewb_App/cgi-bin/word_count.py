#! /usr/bin/env python3
import cgi
import cgitb
import os.path
import html
import re
cgitb.enable()
# 文字化け対策
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#自動でutf-8にエンコードされて出力される

FILE_LOG = "nigen-sikkaku.txt"

# 以下関数
def print_html1(body, sum):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
<html><head><meta charset="utf-8">
<title>数</title></head><body>
<h1>文章の単語の数を数える</h1>
<div><form>
検索したい単語：<input type="text" name="body" size="40">
<input type="submit" value="検索">
<input type="hidden" name="mode" value="serach">
</form></div><hr>
[{0}]は{1}回出現しました。
</body></html>
    """.format(body, sum))
    jump('myapp.py')

def print_html2(sum):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
<html><head><meta charset="utf-8">
<title>数</title></head><body>
<h1>文章の単語の数を数える</h1>
<div><form>
検索したい単語：<input type="text" name="body" size="20">
<input type="submit" value="検索">
<input type="hidden" name="mode" value="serach">
</form></div><hr>
{0}
</body></html>
    """.format(sum))
    jump('myapp.py')

def mode_read(form):
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            log = f.read()
    print_html2(log)

def jump(url):
    print("")
    print('<html><head>')
    print('<meta http-equiv="refresh" contnt="0;'+url+'">')
    print('</head><body>')
    print('<a href="'+url+'">もう一度検索</a></body></html>')

def mode_serach(form):
    body = form.getvalue("body", "")
    body = html.escape(body)
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            log = f.read()
    matches = re.findall(str(body), log)
    word_sum = len(matches)
    print_html1(str(body), word_sum)

def main():
    form = cgi.FieldStorage() #URLパラメータの取得
    mode = form.getvalue("mode", "read")
    if mode == "read": mode_read(form)
    elif mode == "serach": mode_serach(form)
    else: mode_read(form)

if __name__ == "__main__":
    main()
