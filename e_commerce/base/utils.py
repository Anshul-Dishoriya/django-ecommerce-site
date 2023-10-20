from .models import Product , Cart
from .custom_ml_algo import K_Nearest_Neighbor

# get the products that the ml algo has recomended
def get_products(predictions):
    products = Product.objects
    ls = []
    for product_id, _ in predictions:
        ls.append(products.get(id=product_id))
    return ls

# model that creates the model object and predicts the oucome
def create_model_predict_products():
    model = K_Nearest_Neighbor()
    cart_data = [[i.products.id, i.products.category] for i in Cart.objects.all()]
    model.fit(cart_data)

    product_data = [[i.id, i.category] for i in Product.objects.all()]
    return model.predict(product_data)



