import ybc_box,urllib.request,pyperclip
url = ybc_box.enterbox('url?')
response = urllib.request.urlopen(url)
res = response.read().decode("utf-8")
pyperclip.copy(res)
print(res)
