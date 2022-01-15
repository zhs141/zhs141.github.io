from django.shortcuts import render

def klvchen(req):
    print("前端数据: ", req.POST)
    print("file:", req.FILES)

    for item in req.FILES:
        obj = req.FILES.get(item)      # 获取要写入的文件
        filename = obj.name()          # 获取文件名
        f = open(filename, 'wb')
        for line in obj.chunks():      # 分块写入
            f.write(line)
        f.close()

    return render(req, "bianjiqi.html")
