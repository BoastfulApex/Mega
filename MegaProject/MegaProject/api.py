from rest_framework import routers
from mega.views import *

router =routers.DefaultRouter()

router.register('categories', CategoryView, basename='categories')
router.register('products', ProductView, basename='products')
router.register('blogs', BlogView, basename='blogs')