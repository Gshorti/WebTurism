def TagFilter(request, response):
    tags = request.GET["tags"]
    tags = tags.split(',')
    res = []
    for item in response.data:
        for tag in item["tags"]:
            for filter_tag in tags:
                if filter_tag == tag:
                    if item not in res:
                        res.append(item)
    return res