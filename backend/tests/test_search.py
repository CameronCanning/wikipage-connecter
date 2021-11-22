def test_Te(client):
    res = client.get('/search', query_string = {'search_string': 'Te'})
    print(res.json['results'])
    assert(
        ['Television show', 
        'Texas', 
        'Tennessee', 
        'Tesla, Inc.', 
        'Ted Bundy', 
        'Ten Commandments', 
        'Ted Kaczynski', 
        'Ted Lasso', 
        'Tencent'] 
        == 
        res.json['results'])

def test_blank(client):
    res = client.get('/search', query_string = {'search_string': ''})
    assert([] == res.json['results'])