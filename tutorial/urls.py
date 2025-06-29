from django.urls import path, include
from tutorial import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('getAllStudent/', views.allStudent),
    path('getStudent/<int:pk>', views.student_detail),
    path('saveStudent/', views.saveStudent),

    #function based views
    path('StudentDetailsByFunctionView/', views.StudentDetailsByFunctionView),

    #class based views
    path('StudentDetailsByClassView/', views.StudentDetailsByClassView.as_view()),

    #using modelSerializer
    path('EmployeeDetailsByFunctionApiView/', views.EmployeeDetailsByFunctionApiView),
    path('EmployeeDetailsByClassApiView/', views.EmployeeDetailsByClassApiView.as_view()),


    #using modelMixin
    path('EmployeeDetailsByModelMixinGetOrCreate/', views.EmployeeDetailsByModelMixinGetOrCreate.as_view()),
    path('EmployeeDetailsByModelMixinUpdateAndDestroy/<int:pk>/', views.EmployeeDetailsByModelMixinUpdateAndDestroy.as_view()),

    #using ConcreteView
    path('ConcreteViewGetORCreate/', views.ConcreteViewGetORCreate.as_view()),
    path('ConcreteViewGetUpdateDelete/<int:pk>/', views.ConcreteViewGetUpdateDelete.as_view()),

    path("getToken/",obtain_auth_token),

    path("getJWTToken/",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("refreshJWTToken/",TokenRefreshView.as_view(),name='token_refresh'),
    path("verifyJWTToken/",TokenVerifyView.as_view(),name='token_verify'),

    
]