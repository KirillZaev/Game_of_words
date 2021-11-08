from django.urls import path

from .views import InstructionPageView, GamePageView, topic_game, lose_game, AddPageView, start_game

urlpatterns = [
   path('', InstructionPageView.as_view(), name='instruction'),
   path('game/<int:top>', GamePageView.as_view(), name='game'),
   path('topic/', topic_game, name='topic'),
   path('add/', AddPageView.as_view(), name='add'),
   path('start_game/', start_game, name='start_game'),
   path('lose/', lose_game, name='lose'),
]