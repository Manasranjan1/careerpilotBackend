from fastapi import APIRouter, HTTPException
from services.ai_agent import generate_cover_letter
from models import CoverLetterRequest, CoverLetterResponse

router = APIRouter()


@router.post("/cover-letter", response_model=CoverLetterResponse)
async def create_cover_letter(request: CoverLetterRequest):
    """
    Generate a personalized cover letter for a specific internship.
    Called on-demand when the user clicks 'Generate Cover Letter'.
    """
    try:
        cover_letter = generate_cover_letter(
            profile=request.profile.model_dump(),
            company=request.internship_company,
            role=request.internship_role,
            description=request.internship_description,
            required_skills=request.required_skills,
            missing_skills=request.missing_skills,
        )
        return CoverLetterResponse(cover_letter=cover_letter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cover letter generation failed: {str(e)}")
