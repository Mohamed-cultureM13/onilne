from django.urls import path
from apiviews import ProductDetail, ProductList, ChooseProduct

urlpatterns = [
	path("detail/", ProductDetail.as_view(), name="product_detail"),
	path("list/", ProductList.as_view(), name="product_list"),
	path("choose/", ChooseProduct.as_view(), name="choose_product"),
]
