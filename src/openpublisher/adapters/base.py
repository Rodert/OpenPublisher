from abc import ABC, abstractmethod

from openpublisher.models import Article, PublicationResult


class PlatformAdapter(ABC):
    """Stable execution boundary for one publishing destination."""

    name: str

    @abstractmethod
    def validate(self, article: Article) -> None:
        """Validate platform-specific fields before any side effect."""

    @abstractmethod
    def publish(self, article: Article) -> PublicationResult:
        """Publish an article and return a normalized result."""

