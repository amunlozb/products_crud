# products/models.py
from django.db import models
from django.core.serializers import serialize, deserialize


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_star_range(self):
        new_rating = max(1, min(int(self.rating), 5))
        return range(new_rating)

    @staticmethod
    def exportar_json(file_path):
        products = Product.objects.all()
        data = serialize('json', products)
        with open(file_path, 'w') as file:
            file.write(data)

    """ 
    from products.models import Product
    Product.exportar_json('exports/products.json') 
    """

    @staticmethod
    def importar_json(file_path):
        with open(file_path, 'r') as file:
            data = file.read()

        for obj in deserialize('json', data):
            obj.save()

        print('Importación exitosa')

    """ 
    from products.models import Product
    Product.importar_json('exports/products.json') 
    """
