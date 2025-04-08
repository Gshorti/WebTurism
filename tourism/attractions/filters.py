def TagFilter(request, response):
    tags = request.GET["tags"]
    tags = tags.split(',')
    for item in response:
        for tag in item["tags"]:
            print(tag)