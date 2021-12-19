def test_no_params(client):
    rv = client.get('/link')
    assert rv.status_code == 400

def test_one_params(client):
    rv = client.get('/link', query_string = {'start': 'Almond'})
    assert rv.status_code == 400

def test_both_params(client):
    rv = client.get('/link', query_string = {'start': 'Almond', 'end': 'Canada'})
    assert rv.status_code == 200

def test_replace(client):
    rv = client.get('link', query_string = {'start': 'Big Bang', 'end': 'Wow Air'})
    assert rv.status_code == 200