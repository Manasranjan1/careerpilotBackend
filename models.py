from pydantic import BaseModel
from typing import List, Optional


class SkillGap(BaseModel):
    skill: str
    estimated_days: int
    why_important: str


class InternshipMatch(BaseModel):
    internship_id: int
    company: str
    role: str
    location: str
    stipend: str
    description: str
    apply_link: str
    match_percentage: int
    required_skills: List[str]
    matching_skills: List[str]
    missing_skills: List[str]
    skill_gaps: List[SkillGap]
    reason: str


class UserProfile(BaseModel):
    name: str
    email: Optional[str] = None
    education: str
    skills: List[str]
    projects: List[str]
    experience: List[str]
    interests: List[str]
    summary: str


class AnalysisResult(BaseModel):
    profile: UserProfile
    matches: List[InternshipMatch]
    next_best_action: str


class CoverLetterRequest(BaseModel):
    profile: UserProfile
    internship_company: str
    internship_role: str
    internship_description: str
    required_skills: List[str]
    missing_skills: List[str]


class CoverLetterResponse(BaseModel):
    cover_letter: str
