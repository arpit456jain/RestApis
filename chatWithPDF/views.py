from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import summarize_pdf, ask_pdf,test_llm

class SummarizeView(APIView):
    def post(self, request):
        pdf_file = request.FILES.get("pdf")
        if not pdf_file:
            return Response({"error": "PDF file required"}, status=status.HTTP_400_BAD_REQUEST)

        summary = summarize_pdf(pdf_file)
        return Response({"summary": summary}, status=status.HTTP_200_OK)


class AskPDFView(APIView):
    def post(self, request):
        pdf_file = request.FILES.get("pdf")
        question = request.data.get("question")

        if not pdf_file or not question:
            return Response({"error": "PDF and question required"}, status=status.HTTP_400_BAD_REQUEST)

        answer = ask_pdf(pdf_file, question)
        return Response({"answer": answer}, status=status.HTTP_200_OK)



class LLMTestView(APIView):
    def get(self, request):
        try:
            response = test_llm()
            return Response({"response": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)