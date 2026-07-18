import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

supabase: Client = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_KEY"]
)


def get_all_internships() -> list:
    """Fetch all internship records from Supabase."""
    response = supabase.table("internships").select("*").execute()
    return response.data


def get_internship_by_id(internship_id: int) -> dict:
    """Fetch a single internship by ID."""
    response = supabase.table("internships").select("*").eq("id", internship_id).single().execute()
    return response.data
