from abc import abc, abstractmethod

class BaseJobClient(ABC):
    @abstractmethod
    def fetch_jobs(self, query: str, location: str, limit: str):
        pass