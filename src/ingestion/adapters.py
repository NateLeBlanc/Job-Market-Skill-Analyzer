from datetime import datetime
from typing import Dict

from storage.schema import JobPosting
from parsing.section_extractor import extract_requirements

def adzuna_to_job_posting(raw:Dict) -> JobPosting:
    description = raw.get("description", "")

    return JobPosting(
        job_id=raw.get("id"),
        source="adzuna",
        title=raw.get("title"),
        company=raw.get("company", {}).get("display_name"),
        location=raw.get("location", {}).get("display_name"),
        description=description,
        requirements_text=extract_requirements(description),
        date_posted=datetime.fromisoformat(
            raw["created"].replace("Z", "")
        ) if raw.get("created") else None
    )