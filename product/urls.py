from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('sub-category', SubCategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = router.urls