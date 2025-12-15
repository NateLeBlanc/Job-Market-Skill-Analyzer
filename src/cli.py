from ingestion.adzuna_client import AdzunaClient
from ingestion.adapters import adzuna_to_job_posting

def main():
    client = AdzunaClient(country="us")

    jobs = client.fetch_jobs(
        query="Software Engineer",
        location="Boston, MA",
        limit=25
    )

    normalized = [adzuna_to_job_posting(job) for job in jobs]

    print(f"Fetched {len(normalized)} jobs\n")

    for job in normalized[:3]:
        print(job.title)
        print(job.company)
        print(job.location)
        print("-" * 40)

if __name__ == "__main__":
    main()