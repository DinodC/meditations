from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_bonus():
    rv = web.get('/Bonus/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'Meditations', rv.data)

def test_about():
    rv = web.get('/About/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'The quotes are based on the new translation by Gregory Hays', rv.data)

def test_contact():
    rv = web.get('/Contact/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'For eventual feedbacks, you can reach me via:', rv.data)
