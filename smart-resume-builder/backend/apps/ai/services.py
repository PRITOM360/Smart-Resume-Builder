from django.conf import settings
from openai import OpenAI
from .utils import analyze_resume_content

class AIService:
    def __init__(self):
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_resume_content(self, job_description):
        response = self.openai_client.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate resume content based on the following job description: {job_description}",
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def analyze_resume(self, resume_text):
        analysis_results = analyze_resume_content(resume_text)
        return analysis_results

    def generate_cover_letter(self, job_description, user_info):
        prompt = f"Generate a cover letter for a job with the following description: {job_description}. " \
                 f"User information: {user_info}."
        response = self.openai_client.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()