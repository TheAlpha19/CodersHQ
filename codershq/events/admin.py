from django.contrib import admin

from codershq.events.models import Event

#admin.site.register(Event) #ROLLBACK to Normacy
@admin.register(Event)	#Adding Extra codes to send request to eventbrite.
class EventAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):	#change is bool, Request: <class 'django.core.handlers.wsgi.WSGIRequest'>, Object: <class 'codershq.events.models.Event'>
		print("Object: {}".format(obj.short_description))	#obj is the instance of Evemt model
		'''
		Eventbrite conf goes here.. starting with creation
		https://www.eventbrite.com/platform/docs/create-events
		'''
		super().save_model(request, obj, form, change) #saving everything
