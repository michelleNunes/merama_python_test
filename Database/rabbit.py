import pika
import json


class Rabbit(object):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
    except:
        print("Login Error")

    @staticmethod
    def addinformation(response):
        Rabbit.channel.queue_declare(queue='additem', durable=True)

        information = {"data": response,
                       "created_at": response['date_created'],
                       "updated_at": response['last_updated'],
                       "id": response['id']}

        Rabbit.channel.basic_publish(exchange='',
                                     routing_key='additem',
                                     body=json.dumps(information),
                                     properties=pika.BasicProperties(delivery_mode=2, ))
        print(" [x] Sent information")
        Rabbit.channel.close()
