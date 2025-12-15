import os
import requests
from typing import List, Dict
from dotenv import load_dotenv

from .base_client import BaseJobClient

load_dotenv()

class AdzunaClient(BaseJobClient):
    BASE_URL = "https://api.adzuna.com/v1/api/jobs"

    def __init__(self, country: str = "us"):
        self.app_id = os.getenv("ADZUNA_APP_ID")
        self.app_key = os.getenv("ADZUNA_APP_KEY")

        if not self.app_id or not self.app_key:
            raise ValueError("Missing Adzuna API credentials")
        self.country = country
    
    def fetch_jobs(
            self,
            query: str,
            location: str,
            limit: int = 50
    ) -> List[Dict]:
        results = []
        page = 1
        page_size = min(limit, 50)

        while len(results) < limit:
            response = requests.get(
                f"{self.BASE_URL}/{self.country}/search/{page}",
                params={
                    "app_id": self.app_id,
                    "app_key": self.app_key,
                    "what": query,
                    "where": location,
                    "results_per_page": page_size,
                    "content-type": "application/json"
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            batch = data.get("results", [])
            if not batch:
                break
            results.extend(batch)
            page += 1
        return results[:limit]
    
    