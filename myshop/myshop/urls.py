from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns # for urls internationalization
# For django to serve the uploaded media files using development server
from django.conf import settings ######################################
from django.conf.urls.static import static ############################
#######################################################################
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    
    #Make sure that you include this URL pattern before the shop.urls pattern
    #Since it's more restrictive than the latter.
    #cart app url
	path(_('cart/'), include('cart.urls', namespace='cart')),
	
	#orders app url 
    #Also we add this before shop.urls pattern
    path(_('orders/'), include('orders.urls', namespace='orders')),
    
    #payment app url
    #Also we add this before shop.urls pattern
    path(_('payment/'), include('payment.urls', namespace='payment')),
    
    #coupon app url
    path(_('coupons/'), include('coupons.urls', namespace='coupons')),
    
    #rosetta url
    path('rosetta/', include('rosetta.urls')),
    
    #shop app url
    path('', include('shop.urls', namespace='shop')),
    
    
)
# For django to serve the uploaded media files using development server
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Remember that we only serve static files this way during development.
#In a production environment, you should never server static fiels with Django
