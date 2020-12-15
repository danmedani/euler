import boto3
import json

import math
sqs = boto3.client('sqs')
output_queue_url = 'https://sqs.us-east-2.amazonaws.com/131392866514/719-output'


def break_number(num: int, i: int):
	right_half = num % (10 ** i)
	left_half = int((num - right_half) / (10 ** i))
	return left_half, right_half

def get_max_i(num: int) -> int:
	if num <= 1:
		return 1
	i = 0
	while num > (10 ** i):
		i += 1
	return i

def adds_up(total: int, num_left: int) -> bool:
	if total < 0:
		return False
	if num_left == 0:
		return total == 0

	for i in range(get_max_i(num_left)):
		left_half, right_half = break_number(num_left, i)
		# print(left_half, right_half)
		if adds_up(
			total=total-left_half,
			num_left=right_half
		):
			return True

	return False

def is_S(square: int) -> bool:
	return adds_up(total=int(math.sqrt(square)), num_left=square)

def get_sum(min_i: int, max_i: int) -> int:
    s = 0
    for i in range(min_i, max_i):
    	squared = i * i
    	if is_S(squared):
    		s += (squared)
    	i += 1
    return s


def lambda_handler(event, context):
	s = 0
	for record in event['Records']:
		params = json.loads(record['body'])
		s += get_sum(params['min_i'], params['max_i'])

	sqs.send_message(
	    QueueUrl=output_queue_url,
	    MessageBody=json.dumps({
	    	"min_i": params['min_i'],
	    	"max_i": params['max_i'],
			"sum": s
		})
	)
	return {}
