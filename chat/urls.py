from django.urls import path

from chat.views import(
	private_chat_room_view,
	create_or_return_private_chat,
)

urlpatterns = [
    path('create_or_return_private_chat/', create_or_return_private_chat, name='create-or-return-private-chat'),
    path('', private_chat_room_view, name='private-chat-room'),
]

app_name = 'chat'