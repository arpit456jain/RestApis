from django.urls import path
from .views import SummarizeView, AskPDFView,LLMTestView

urlpatterns = [
    path('summarize/', SummarizeView.as_view(), name='summarize'),
    path('ask/', AskPDFView.as_view(), name='ask-pdf'),
    path("test-llm/", LLMTestView.as_view(), name="test-llm"),
]
