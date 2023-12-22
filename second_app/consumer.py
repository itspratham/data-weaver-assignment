import json
import pika
from sys import path
from os import environ
import django

path.append('/second_app/second_app/settings.py')  # Your path to settings.py
environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_app.settings')
django.setup()

from new_app1.models import Product, Price, SKU, ProductSource

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='quotes', durable=True)


def callback(ch, method, properties, body):
    data1 = json.loads(body)
    data = json.loads(data1["meta_info"].replace("'", '"'))
    if properties.content_type == 'share_details':
        product = Product.objects.filter(reference_product_id=data["reference_product_id"]).exists()
        if product:
            product = Product.objects.get(reference_product_id=data["reference_product_id"])
            product.account_code = data["account_code"],
            product.crawl_page_counter = data["crawl_page_counter"],
            product.postal_zip_code = data["postal_zip_code"],
            product.postal_zip_name = data["postal_zip_name"],
            product.store_code = data["store_code"],
            product.place_name = data["place_name"],
            product.admin_name1 = data["admin_name1"],
            product.bundle_versions_row_pk_hash = data["bundle_versions_row_pk_hash"],
            product.major_version_end_time = data["major_version_end_time"],
            product.bundle_variant_field_mapping = data["bundle_variant_field_mapping"],
            product.bundle_definition = data["bundle_definition"],
            product.fulfilment_modes = data["fulfilment_modes"],
            product.seller_name = data["seller_name"],
            product.bundle_match_type = data["bundle_match_type"],
            product.bundle_definition_hash = data["bundle_definition_hash"]
            product.save()

        else:
            product = Product(
                reference_product_id=data["reference_product_id"],
                account_code=data["account_code"],
                crawl_page_counter=data["crawl_page_counter"],
                postal_zip_code=data["postal_zip_code"],
                postal_zip_name=data["postal_zip_name"],
                store_code=data["store_code"],
                place_name=data["place_name"],
                admin_name1=data["admin_name1"],
                bundle_versions_row_pk_hash=data["bundle_versions_row_pk_hash"],
                major_version_end_time=data["major_version_end_time"],
                bundle_variant_field_mapping=data["bundle_variant_field_mapping"],
                bundle_definition=data["bundle_definition"],
                fulfilment_modes=data["fulfilment_modes"],
                seller_name=data["seller_name"],
                bundle_match_type=data["bundle_match_type"],
                bundle_definition_hash=data["bundle_definition_hash"])
            product.save()
        price = Price.objects.filter(reference_product_id=data["reference_product_id"]).exists()
        import pdb;pdb.set_trace()
        if not price:
            price = Price(reference_product_id=product,
                          available_price=data1["available_price"])
            price.save()
        else:
            price = Price.objects.get(reference_product_id=product.reference_product_id,
                                      )
            price.available_price = data1["available_price"]
            price.save()

        sku = SKU.objects.filter(reference_product_id=data["reference_product_id"]).exists()
        if not sku:
            sku = SKU(reference_product_id=product,
                      stock=data1["stock"])
            sku.save()
        else:
            sku = SKU.objects.get(reference_product_id=product.reference_product_id)
            sku.stock = data1["stock"]
            sku.save()

        product_source = ProductSource.objects.filter(reference_product_id=data["reference_product_id"]).exists()
        if not product_source:
            product_source = ProductSource(reference_product_id=product,
                                           source=data1["source"])
            product_source.save()
        else:
            product_source = ProductSource.objects.get(reference_product_id=product.reference_product_id)
            product_source.source = data1["source"]
            product_source.save()
    import datetime
    print("data", data1, "finished", datetime.datetime.now())


channel.basic_consume(queue='quotes', on_message_callback=callback)
print("Started Consuming...")
channel.start_consuming()
channel.close()
