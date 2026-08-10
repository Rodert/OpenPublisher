import unittest

from openpublisher.core.publication_policy import (
    PublicContentPolicyError,
    validate_reader_facing_content,
)
from openpublisher.adapters import PlatformAdapter
from openpublisher.models import Article, ArticleMetadata, ImageAsset
from openpublisher.models import PublicationResult, PublicationStatus


class ExampleAdapter(PlatformAdapter):
    name = "example"

    def validate_platform(self, article: Article) -> None:
        pass

    def publish(self, article: Article) -> PublicationResult:
        return PublicationResult(platform=self.name, status=PublicationStatus.PUBLISHED)


class PublicationPolicyTests(unittest.TestCase):
    def test_rejects_internal_system_name_in_body(self) -> None:
        article = Article(
            metadata=ArticleMetadata(title="每日科技简报"),
            body_markdown="This post was prepared by OpenPublisher.",
        )

        with self.assertRaises(PublicContentPolicyError):
            validate_reader_facing_content(article)

    def test_rejects_internal_label_in_image_alt_text(self) -> None:
        article = Article(
            metadata=ArticleMetadata(title="每日科技简报"),
            body_markdown="正文",
            images=[ImageAsset(source="image.jpg", alt="Temporary draft image")],
        )

        with self.assertRaises(PublicContentPolicyError):
            validate_reader_facing_content(article)

    def test_allows_reader_facing_content(self) -> None:
        article = Article(
            metadata=ArticleMetadata(
                title="每日科技简报",
                tags=["人工智能", "云原生"],
                seo_description="关注技术趋势与工程实践。",
            ),
            body_markdown="人工智能正在持续进入软件研发流程。",
        )

        validate_reader_facing_content(article)

    def test_adapter_validation_cannot_skip_public_content_policy(self) -> None:
        article = Article(
            metadata=ArticleMetadata(title="Daily report"),
            body_markdown="adapter discovery notes",
        )

        with self.assertRaises(PublicContentPolicyError):
            ExampleAdapter().validate(article)

    def test_adapter_appends_author_footer_once(self) -> None:
        article = Article(
            metadata=ArticleMetadata(title="Daily report"),
            body_markdown="A short technology update.",
        )

        adapter = ExampleAdapter()
        adapter.validate(article)
        adapter.validate(article)

        self.assertEqual(article.body_markdown.count("## 关于作者"), 1)
        self.assertIn("https://javapub.net.cn", article.body_markdown)
