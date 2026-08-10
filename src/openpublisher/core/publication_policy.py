from collections.abc import Iterable

from openpublisher.models import Article


FORBIDDEN_READER_FACING_TEXT = (
    "openpublisher",
    "adapter discovery",
    "test draft",
    "temporary draft",
)


class PublicContentPolicyError(ValueError):
    """Raised when internal implementation details would be published."""


def validate_reader_facing_content(article: Article) -> None:
    """Reject internal labels in every field that can reach a publishing platform."""
    fields = _reader_facing_fields(article)
    for field_name, value in fields:
        normalized = value.casefold()
        for forbidden in FORBIDDEN_READER_FACING_TEXT:
            if forbidden in normalized:
                raise PublicContentPolicyError(
                    f"Reader-facing {field_name} contains forbidden internal text: {forbidden!r}"
                )


def _reader_facing_fields(article: Article) -> Iterable[tuple[str, str]]:
    metadata = article.metadata
    yield "title", metadata.title
    yield "body", article.body_markdown

    optional_fields = {
        "summary": metadata.summary,
        "category": metadata.category,
        "seo_title": metadata.seo_title,
        "seo_description": metadata.seo_description,
    }
    for field_name, value in optional_fields.items():
        if value:
            yield field_name, value

    for tag in metadata.tags:
        yield "tag", tag
    for image in article.images:
        if image.alt:
            yield "image alt text", image.alt

