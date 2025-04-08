def TagFilter(request, response):
    tags = request.GET["tags"]
    tags = tags.split(',')
    res = []
    for item in response:
        for tag in item["tags"]:
           res.append(tag)
    return res