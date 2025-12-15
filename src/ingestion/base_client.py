from abc import ABC, abstractmethod

class BaseJobClient(ABC):
    @abstractmethod
    def fetch_jobs(self, query: str, location: str, limit: str):
        pass