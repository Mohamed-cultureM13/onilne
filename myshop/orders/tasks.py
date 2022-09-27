from django.core.mail import send_mail
from .models import Order
#This API was deprecated , and then removed in celery >=5.0
#That is suggested to change from celery import task into 
#from celery import shared_task, then it works! 
from celery import shared_task

@shared_task
def order_created(order_id):
	"""
	Task to send to an e-mail notification when an order is
	successfully created.
	"""
	order = Order.objects.get(id=order_id)
	subject = 'Order nr. {}'.format(order.id)
	message = 'Dear {},\n\nYou have successfully placed an order.\
			   Your order id is {}.'.format(order.first_name, order.id)
	mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
	return mail_sent
