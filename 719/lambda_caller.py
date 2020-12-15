from typing import Dict
import json
import boto3

sqs = boto3.client('sqs')
input_queue_url = 'https://sqs.us-east-2.amazonaws.com/131392866514/719-input'
output_queue_url = 'https://sqs.us-east-2.amazonaws.com/131392866514/719-output'

def enqueue_bulk(min_i: int, max_i: int):
	seg_size = 100
	series = []
	for i in range(min_i, max_i - seg_size + 3, seg_size):
		series.append((i, min(i + seg_size, max_i)))

	response = sqs.send_message_batch(
	    QueueUrl=input_queue_url,
	    Entries=[
	    	{
	    		'Id': str(min_i) + '_' + str(max_i),
		    	'MessageBody': json.dumps({
					"min_i": min_i,
					"max_i": max_i
				})
			}
			for min_i, max_i in series
	    ]
	)


def clear_queues():
	for queue_url in [input_queue_url, output_queue_url]:
		while True:
			responses = sqs.receive_message(
			    QueueUrl=queue_url,
			    MaxNumberOfMessages=10,
			    VisibilityTimeout=30,
			    WaitTimeSeconds=20
			)
			if 'Messages' not in responses:
				break
			for message in responses['Messages']:
				sqs.delete_message(
				    QueueUrl=queue_url,
				    ReceiptHandle=message['ReceiptHandle']
				)

def hash_queue_message(body: Dict) -> str:
	return str(body['min_i']) + '_' + str(body['max_i'])

def long_poll_receive():
	the_sum = 0
	processed_vals = set()
	while True:
		responses = sqs.receive_message(
		    QueueUrl=output_queue_url,
		    AttributeNames=[
		        'SentTimestamp'
		    ],
		    MaxNumberOfMessages=10,
		    MessageAttributeNames=[
		        'All'
		    ],
		    VisibilityTimeout=30,
		    WaitTimeSeconds=20
		)
		if 'Messages' not in responses:
			break

		for message in responses['Messages']:
			body_decoded = json.loads(message['Body'])
			hashed_val = hash_queue_message(body_decoded)
			if hashed_val not in processed_vals:
				the_sum += body_decoded['sum']
				print(body_decoded['sum'])
				processed_vals.add(hashed_val)

			sqs.delete_message(
			    QueueUrl=output_queue_url,
			    ReceiptHandle=message['ReceiptHandle']
			)
	print(the_sum)

clear_queues()

MAX = 10 ** 6
SEGMENT_SIZE = 1000
for minn in range(2, MAX - SEGMENT_SIZE + 3, SEGMENT_SIZE):
	print(minn, min(MAX + 1, minn + SEGMENT_SIZE))
	enqueue_bulk(minn, min(MAX + 1, minn + SEGMENT_SIZE))

long_poll_receive()
