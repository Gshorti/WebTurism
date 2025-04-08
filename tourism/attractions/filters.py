def TagFilter(request, response):
    tags = request.GET["tags"]
    if tags != "NaN":
        tags = tags.split(',')
        res = []
        for item in response.data:
            for tag in item["tags"]:
                for filter_tag in tags:
                    if filter_tag == tag:
                        if item not in res:
                            res.append(item)
        if len(res) > 0:
            return res
        else:
            return response.data
    else:
        return response.data