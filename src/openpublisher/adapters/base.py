from abc import ABC, abstractmethod
from typing import final

from openpublisher.core.author_footer import append_author_footer
from openpublisher.core.publication_policy import validate_reader_facing_content
from openpublisher.models import Article, PublicationResult


class PlatformAdapter(ABC):
    """Stable execution boundary for one publishing destination."""

    name: str

    @final
    def validate(self, article: Article) -> None:
        """Apply mandatory footer and policy checks before platform-specific validation."""
        article.body_markdown = append_author_footer(article.body_markdown)
        validate_reader_facing_content(article)
        self.validate_platform(article)

    @abstractmethod
    def validate_platform(self, article: Article) -> None:
        """Validate platform-specific fields after mandatory policy checks."""

    @abstractmethod
    def publish(self, article: Article) -> PublicationResult:
        """Publish an article and return a normalized result."""
