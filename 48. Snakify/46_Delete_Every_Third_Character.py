s = str(input())
news = ""

for i in range(len(s)):
  if i % 3 != 0:
    news += s[i]

print(news)
