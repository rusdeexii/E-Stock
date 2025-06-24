from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),

    # # Authentication (login/logout/token)
    path('/auth', include('core.auth.urls')),


    # User management (CRUD, profile, etc.)
    path('/users', include('core.user.urls')),

    # # อื่น ๆ ที่คุณจะทำในอนาคต
    # path('api/products/', include('core.product.urls')),
    # path('api/stock/', include('core.stock.urls')),
    # path('api/warehouse/', include('core.warehouse.urls')),
    # path('api/supplier/', include('core.supplier.urls')),
    # path('api/purchase/', include('core.purchase.urls')),
]
