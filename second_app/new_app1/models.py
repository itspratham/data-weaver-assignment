from django.db import models


# Create your models here.
class Product(models.Model):
    reference_product_id = models.CharField(max_length=100)
    account_code = models.CharField(max_length=100)
    crawl_page_counter = models.CharField(max_length=100)
    postal_zip_code = models.CharField(max_length=100)
    postal_zip_name = models.CharField(max_length=100)
    store_code = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    admin_name1 = models.CharField(max_length=100)
    bundle_versions_row_pk_hash = models.CharField(max_length=100)
    major_version_end_time = models.CharField(max_length=100)
    bundle_variant_field_mapping = models.CharField(max_length=100)
    bundle_definition = models.CharField(max_length=100)
    fulfilment_modes = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    bundle_match_type = models.CharField(max_length=100)
    bundle_definition_hash = models.CharField(max_length=100)

    class Meta:
        app_label = 'new_app1'

class Price(models.Model):
    reference_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    available_price = models.CharField(max_length=100)
    class Meta:
        app_label = 'new_app1'


class SKU(models.Model):
    reference_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100)

    class Meta:
        app_label = 'new_app1'


class ProductSource(models.Model):
    reference_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    class Meta:
        app_label = 'new_app1'
