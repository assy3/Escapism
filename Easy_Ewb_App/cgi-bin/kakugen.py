#! /usr/bin/env python3

# 文字化け対策
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#自動でutf-8にエンコードされて出力される

print("Content-Type: text/html; charset=utf-8")

print("")

print("<html><head><meta charset='utf-8'></head><body>")
print("うこうこ")
print("</body></html>")

if __name__ == '__main__':
    sys.exit(main())