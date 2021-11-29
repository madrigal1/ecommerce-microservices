import pika,json,os,django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product


cloud_url = "amqps://grwcxnpd:riS-NtEcw-u317IJw8fESetC6FbJRtCN@mustang.rmq.cloudamqp.com/grwcxnpd"
params = pika.URLParameters(cloud_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch,method,properties,body):
    print("Recieved in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print(f"Product {id} likes increased: {product.likes}")

channel.basic_consume(queue="admin",on_message_callback=callback,auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
