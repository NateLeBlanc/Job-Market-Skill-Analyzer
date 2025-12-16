from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobPosting(BaseModel):
    job_id: str
    source: str
    title: str
    company: Optional[str]
    location: Optional[str]
    description: str
    requirements_text: Optional[str] = None
    date_posted: Optional[datetime]