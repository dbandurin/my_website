from flask_frozen import Freezer
from myapp import app

freezer = Freezer(app)

if __name__ == '__main__':

        @freezer.register_generator
        def pred_repair():
            for product in models.Product.all():
                yield {'product_id': product.id}

        freezer.freeze()
