from django.urls import path
from voting.views import StudentsListView, StudentAddView, StudentEditView, StudentDeleteView
from voting.views import CandidatesListView, CandidateAddView, CandidateEditView, CandidateDeleteView
from voting.views import CheckRollFormView
from voting import views

urlpatterns = [
    path('checkRoll/', CheckRollFormView.as_view(), name='checkRoll'),
    path('stdList/', StudentsListView.as_view(), name='stdList'),
    path('stdAdd/', StudentAddView.as_view(), name='stdAdd'),
    path('stdsAdd/', views.studentsAdd, name='stdsAdd'),
    path('stdEdit/<int:pk>/', StudentEditView.as_view(), name='stdEdit'),
    path('stdDel/<int:pk>/', StudentDeleteView.as_view(), name='stdDel'),
    path('stdsDel/', views.studentsDelete, name='stdsDel'),
    path('cndList/', CandidatesListView.as_view(), name='cndList'),
    path('cndAdd/', CandidateAddView.as_view(), name='cndAdd'),
    path('cndEdit/<int:pk>/', CandidateEditView.as_view(), name='cndEdit'),
    path('cndDel/<int:pk>/', CandidateDeleteView.as_view(), name='cndDel'),
]