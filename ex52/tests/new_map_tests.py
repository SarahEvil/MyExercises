#-*- coding: utf-8 -*-
from nose.tools import *
from new_map import *
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
	assert_response(resp, contains="Oopsie")

	# test that we get an expected response for specific input data
	testdata = {'userinput': 'Yes'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="Northpole")
	
	testdata = {'userinput': 'continue'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="Advice")
	
	testdata = {'userinput': 'No'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="CandyCaneForest")
	
	testdata = {'userinput': 'Dont you eat the yellow snow!'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="GumDropSea")
	
	testdata = {'userinput': '3'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="Lincoln Tunnel")
	
	testdata = {'userinput': 'ignore gum'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="Central Park")
	
	testdata = {'userinput': 'is singing loud for all to hear!'}
	resp = client.post('/game', data=testdata)
	assert_response(resp, contains="Victory")

	
	
	
	
	
	