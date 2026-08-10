from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class ArticleMetadata:
    title: str
    summary: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    category: Optional[str] = None
    cover_image: Optional[Path] = None
    seo_title: Optional[str] = None
    seo_description: Optional[str] = None


@dataclass
class ImageAsset:
    source: Path
    alt: Optional[str] = None
    published_url: Optional[str] = None


@dataclass
class Article:
    metadata: ArticleMetadata
    body_markdown: str
    source_path: Optional[Path] = None
    images: List[ImageAsset] = field(default_factory=list)
