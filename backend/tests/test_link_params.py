def test_link_params(client):
    rv = client.get('/link', query_string = {'start': 'Almond', 'end': 'Canada'})
    print('\n\t', end='')
    print(rv.data)
    assert b'{"end":"Canada","start":"Almond"}\n' in rv.data