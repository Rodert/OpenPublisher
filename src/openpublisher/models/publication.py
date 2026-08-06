from dataclasses import dataclass
from enum import StrEnum


class PublicationStatus(StrEnum):
    PUBLISHED = "published"
    SKIPPED = "skipped"
    FAILED = "failed"
    REQUIRES_LOGIN = "requires_login"


@dataclass
class PublicationResult:
    platform: str
    status: PublicationStatus
    url: str | None = None
    external_id: str | None = None
    error: str | None = None
    details: dict[str, str] | None = None

