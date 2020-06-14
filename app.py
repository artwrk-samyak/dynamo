import boto3

def get_details(table):
    client = boto3.client('dynamodb')       #connection
    response = str(client.describe_table(TableName=table))
    print(response)

def put_value(table):
    dynamodb = boto3.resource('dynamodb')       #connection
    response = dynamodb.Table(table).put_item(
       Item={
            'Artist_Id': 25,
            'ArtwrkTitle': "Painting",
           }
    )
    print(response)

get_details("Test_Profile")
#put_value("Test_Profile")   
