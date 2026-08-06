from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ArticleMetadata:
    title: str
    summary: str | None = None
    tags: list[str] = field(default_factory=list)
    category: str | None = None
    cover_image: Path | None = None
    seo_title: str | None = None
    seo_description: str | None = None


@dataclass
class ImageAsset:
    source: Path
    alt: str | None = None
    published_url: str | None = None


@dataclass
class Article:
    metadata: ArticleMetadata
    body_markdown: str
    source_path: Path | None = None
    images: list[ImageAsset] = field(default_factory=list)

