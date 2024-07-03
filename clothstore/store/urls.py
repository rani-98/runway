from django.urls import path
from .views import (
    products,
    test_view,
    add_to_wishlist,
    remove_from_wishlist,
    product_view,
    wishlist,
)


urlpatterns = [
    path("", products, name="store"),
    # path("new", new_product, name="new_product"),
    path("store/wishlist", add_to_wishlist, name="wishlist"),
    path(
        "store/remove-wishlist/<int:shirt_id>",
        remove_from_wishlist,
        name="remove_wishlist",
    ),
    path("store/wish-list", wishlist, name="wish_list"),
    path("store/product/<int:product_id>", product_view, name="product"),
]