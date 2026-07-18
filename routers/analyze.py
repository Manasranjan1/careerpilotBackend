from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from services.pdf_parser import extract_text_from_pdf
from services.ai_agent import run_analysis_agent
from services.internship_db import get_all_internships
from models import AnalysisResult

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResult)
async def analyze_resume(
    resume: UploadFile = File(...),
    preferred_role: Optional[str] = Form(None),
    github_url: Optional[str] = Form(None),
):
    """
    Main AI agent endpoint.
    Accepts a PDF resume, extracts text, loads internships,
    runs the Gemini analysis agent, and returns structured results.
    """
    # Validate file type
    if not resume.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    # Read file bytes
    pdf_bytes = await resume.read()
    if len(pdf_bytes) > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(status_code=400, detail="File size exceeds 10MB limit.")
    
    # Extract text from PDF
    try:
        resume_text = extract_text_from_pdf(pdf_bytes)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Failed to parse PDF: {str(e)}")
    
    if not resume_text or len(resume_text) < 50:
        raise HTTPException(status_code=422, detail="Could not extract sufficient text from the PDF. Please ensure the PDF is not image-only.")
    
    # Load all internships from database
    try:
        internships = get_all_internships()
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database error: {str(e)}")
    
    if not internships:
        raise HTTPException(status_code=503, detail="No internship data available. Please seed the database first.")
    
    # Run the AI agent
    try:
        result = run_analysis_agent(
            resume_text=resume_text,
            internships=internships,
            preferred_role=preferred_role,
            github_url=github_url
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI agent error: {str(e)}")
    
    return result
