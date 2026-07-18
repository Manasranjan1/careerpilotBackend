import os
import json
from groq import Groq
from dotenv import load_dotenv
from models import AnalysisResult

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))
MODEL_ID = "llama-3.3-70b-versatile"


ANALYSIS_SYSTEM_PROMPT = """You are CareerPilot AI, an expert career agent for college students.
Your task is to analyze a student's resume and match them against internship opportunities.

You must return a VALID JSON object (no markdown, no code blocks, raw JSON only) with this exact structure:
{
  "profile": {
    "name": "string",
    "email": "string or null",
    "education": "string (degree, college, year)",
    "skills": ["skill1", "skill2"],
    "projects": ["project1 description"],
    "experience": ["experience1 description"],
    "interests": ["interest1"],
    "summary": "2-3 sentence professional summary of the student"
  },
  "matches": [
    {
      "internship_id": 1,
      "company": "string",
      "role": "string",
      "location": "string",
      "stipend": "string",
      "description": "string",
      "apply_link": "string",
      "match_percentage": 95,
      "required_skills": ["skill1"],
      "matching_skills": ["skill1"],
      "missing_skills": ["skill1"],
      "skill_gaps": [
        {
          "skill": "string",
          "estimated_days": 5,
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
- Output raw JSON ONLY. No markdown formatting like ```json
"""


def run_analysis_agent(resume_text: str, internships: list, preferred_role: str = None, github_url: str = None) -> AnalysisResult:
    """Run the main career analysis agent using Groq (Llama 3)."""
    
    role_hint = f"\nStudent's preferred role: {preferred_role}" if preferred_role else ""
    github_hint = f"\nStudent's GitHub: {github_url}" if github_url else ""
    
    user_prompt = f"""STUDENT RESUME:
{resume_text}
{role_hint}
{github_hint}

AVAILABLE INTERNSHIPS (analyze all and pick top 3 matches):
{json.dumps(internships, indent=2)}

Analyze the resume against all internships and return the top 3 matches as a JSON object following the exact schema specified."""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": ANALYSIS_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        model=MODEL_ID,
        temperature=0.1,
        response_format={"type": "json_object"}
    )
    
    result_text = response.choices[0].message.content
    result_dict = json.loads(result_text)
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

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a professional career coach and expert cover letter writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=MODEL_ID,
        temperature=0.7,
    )
    
    return response.choices[0].message.content.strip()
