#-*- coding: utf-8 -*-
from nose.tools import *
from map import *
from tests.tools import assert_response

client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
	global client # let python know you want to use the global client variable in this function
	# Check that we get a 404 on the / URL
	resp = client.get('/')
	assert_response(resp, status=302)
	
	# test to make sure a GET request to /hello works (returns a 200 status code)
	resp = client.get('/game')
	assert_response(resp)
	
	# make sure the default values work when POST has no data
	resp = client.post('/game')
	assert_response(resp, contains="You Died")

	# test that we get an expected response for specific input data
	testdata = {'userinput': 'tell a joke'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="Laser Weapon Armory")
	
	testdata = {'userinput': '132'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="The Bridge")
	
	testdata = {'userinput': 'slowly place the bomb'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="Escape Pod")
	
	testdata = {'userinput': '2'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="You Made It!")
	