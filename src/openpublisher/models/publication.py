from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class PublicationStatus(str, Enum):
    PUBLISHED = "published"
    SKIPPED = "skipped"
    FAILED = "failed"
    REQUIRES_LOGIN = "requires_login"


@dataclass
class PublicationResult:
    platform: str
    status: PublicationStatus
    url: Optional[str] = None
    external_id: Optional[str] = None
    error: Optional[str] = None
    details: Optional[Dict[str, str]] = None
