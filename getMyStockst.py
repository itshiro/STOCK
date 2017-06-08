# -*- coding: utf-8 -*- 
##
## BeautifulSoup使ってXpath使う破片
##
import json
import datetime
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('mystocks_t')

mystocks = {}
response = table.scan(
#    FilterExpression=Attr('datetime').eq('Panasonic')
)

items = response['Items']
for item in items:
	print (item)
