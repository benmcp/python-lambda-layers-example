import json
import numpy as np

def hello(event, context):
	arr = np.arange(15).reshape(3, 5)
	b = arr.tolist()

	body = {
		"result": b
	}

	response = {
		"statusCode": 200,
		"body":json.dumps(body)
	}

	return response