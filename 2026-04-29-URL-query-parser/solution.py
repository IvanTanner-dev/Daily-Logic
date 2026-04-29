def parse_url_query(url):

    query_string = url.split("?")[1]
    pairs = [pair.split("=") for pair in query_string.split("&")]
    dict_pairs = {key: value for key, value in pairs}
    return dict_pairs