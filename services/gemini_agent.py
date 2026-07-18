import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
from models import AnalysisResult, CoverLetterResponse

load_dotenv()

# Initialize the new Google GenAI client (REST based)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL_ID = "gemini-2.0-flash"


ANALYSIS_SYSTEM_PROMPT = """You are CareerPilot AI, an expert career agent for college students.
Your task is to analyze a student's resume and match them against internship opportunities.

You must return a VALID JSON object (no markdown, no code blocks, raw JSON only) with this exact structure:
{
  "profile": {
    "name": "string",
    "email": "string or null",
    "education": "string (degree, college, year)",
    "skills": ["skill1", "skill2", ...],
    "projects": ["project1 description", ...],
    "experience": ["experience1 description", ...],
    "interests": ["interest1", ...],
    "summary": "2-3 sentence professional summary of the student"
  },
  "matches": [
    {
      "internship_id": number,
      "company": "string",
      "role": "string",
      "location": "string",
      "stipend": "string",
      "description": "string",
      "apply_link": "string",
      "match_percentage": number (0-100),
      "required_skills": ["skill1", ...],
      "matching_skills": ["skill1", ...],
      "missing_skills": ["skill1", ...],
      "skill_gaps": [
        {
          "skill": "string",
          "estimated_days": number,
          "why_important": "one sentence explaining why this skill matters for the role"
        }
      ],
      "reason": "2-3 sentence explanation of why this internship was recommended for this student"
    }
  ],
  "next_best_action": "string (single most important personalized action the student should take right now to improve their chances)"
}

Rules:
- Select ONLY the top 3 best-matching internships from the provided list
- match_percentage must be realistic (based on actual skill overlap)
- missing_skills must be from the internship's required_skills that the student lacks
- estimated_days should be realistic learning estimates (Docker: 3 days, Python basics: 7 days, etc.)
- next_best_action must be ONE specific, personalized, actionable recommendation - not generic advice
- Be honest about skill gaps but encouraging in tone
"""


def run_analysis_agent(resume_text: str, internships: list, preferred_role: str = None, github_url: str = None) -> AnalysisResult:
    """Run the main career analysis agent using Gemini."""
    
    role_hint = f"\nStudent's preferred role: {preferred_role}" if preferred_role else ""
    github_hint = f"\nStudent's GitHub: {github_url}" if github_url else ""
    
    user_prompt = f"""STUDENT RESUME:
{resume_text}
{role_hint}
{github_hint}

AVAILABLE INTERNSHIPS (analyze all and pick top 3 matches):
{json.dumps(internships, indent=2)}

Analyze the resume against all internships and return the top 3 matches as a JSON object following the exact schema specified."""

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[ANALYSIS_SYSTEM_PROMPT, user_prompt],
        config=types.GenerateContentConfig(
            temperature=0.3,
            response_mime_type="application/json",
        )
    )
    
    result_dict = json.loads(response.text)
    return AnalysisResult(**result_dict)


def generate_cover_letter(profile: dict, company: str, role: str, description: str, required_skills: list, missing_skills: list) -> str:
    """Generate a personalized cover letter for a specific internship."""
    
    prompt = f"""Write a professional, personalized cover letter for the following student applying to this internship.

STUDENT PROFILE:
Name: {profile.get('name', 'the applicant')}
Education: {profile.get('education', '')}
Skills: {', '.join(profile.get('skills', []))}
Projects: {'; '.join(profile.get('projects', []))}
Experience: {'; '.join(profile.get('experience', []))}
Summary: {profile.get('summary', '')}

INTERNSHIP:
Company: {company}
Role: {role}
Description: {description}
Required Skills: {', '.join(required_skills)}

INSTRUCTIONS:
- Write a compelling 3-paragraph cover letter
- First paragraph: Express genuine interest in the company and role
- Second paragraph: Highlight relevant skills and projects that match the role
- Third paragraph: Show enthusiasm, mention willingness to learn, professional closing
- Address it "Dear Hiring Manager,"
- Sign off with the student's name
- Keep it under 300 words
- Do NOT mention missing skills as weaknesses
- Sound human, confident, and enthusiastic
- Return only the cover letter text, no extra commentary"""

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
        )
    )
    
    return response.text.strip()
