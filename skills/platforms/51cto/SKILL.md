# 51CTO Publisher

This Skill is governed by [Mandatory Publishing Rules](../../PUBLISHING_RULES.md). It must not publish internal system names or operational details, including in drafts, images, metadata, or SEO fields.

## Required Daily Sign-in

Before every 51CTO publishing attempt, open `https://blog.51cto.com/user/sign` in the authenticated browser session.

- When the page says `今日已签到`, record `already_signed` and continue.
- When sign-in is available, perform it and record `signed` before opening the editor.
- If authentication, CAPTCHA, or secondary verification is required, stop with `requires_login`; the user must complete it in the browser.

Do not publish before this check. A sign-in result is operational metadata only and must never be inserted into the article.

## Article Lifecycle

1. Complete the daily sign-in check.
2. Open `https://blog.51cto.com/blogger/publish?old=1&newBloger=2`.
3. Validate the normalized article, including the mandatory author footer and reader-facing content boundary.
4. Fill the title and body. When 51CTO detects pasted Markdown, choose **确认** to convert it to rich text.
5. Wait for the editor to show an automatic-save timestamp. Treat this as a saved draft even when the URL and hidden fields do not expose a public article ID.
6. Upload at least one approved local image through the editor, wait for its hosted URL and rendered image, then wait for another automatic save. This is mandatory for every 51CTO test-publish run; automatic cover selection alone is insufficient.
7. Open **发布文章** and set all required publication fields.
8. Present the final reader-facing article and selected settings for explicit per-article approval.
9. In a newly created editor, click the final **发布** button only after approval; then capture the result URL and status. Do not treat a draft editor's **确认** button as successful publication.

## Confirmed Behavior

- A fresh editor does not expose `blog_id` or `work_id` in its URL or page fields.
- Entering content creates an automatic draft: the editor displays `已保存 <time>` and the draft count increases.
- Markdown pasted into the rich-text editor triggers a conversion dialog. Confirming the dialog creates headings, a separator, emphasis, and hyperlinks correctly.
- A successful new-article submission redirects to `https://blog.51cto.com/blogger/success/<article-id>` and displays `发布成功`.
- Verify the reader-facing URL by loading `https://blog.51cto.com/wangshiyu/<article-id>` and checking the returned page title. Do not infer publication from a draft count, title, or client-side hidden field.

## Publish Configuration

Observed fields and defaults:

- A required two-level platform category. Select both levels before final confirmation. For the validated article, `AI 智能体` and `编程 Agent` were selected.
- Up to five tags. The platform may prefill suggested tags; replace them with the normalized set rather than exceeding the limit.
- Article summary, maximum 500 characters.
- Optional topic and personal category.
- Cover mode: single image, three images, no image, or automatic extraction from article images. The observed default is automatic extraction.
- Article type. The observed default is original.
- Copyright statement. The observed default is `转载请注明出处`.
- Visibility: public or private. The observed default is public.
- Optional pinning under advanced options.

The validated submission used categories `AI 智能体` / `编程 Agent`; tags `人工智能`, `AI Agent`, `云原生`, `软件开发`, `大模型应用`; original; public; automatic cover; and a normalized summary.

## Images And Interface Trace

The editor exposes a single-file upload input and the publish panel exposes a cover-image uploader. The browser-control surface used in this discovery can inspect the controls but does not provide a file-selection operation or raw network interception. Therefore no upload endpoint, request schema, hosted image URL, or final publish endpoint is currently confirmed.

For a future observed upload, record only sanitized fields:

```json
{
  "event": "image_upload",
  "source_filename": "<filename>",
  "destination": "editor | cover",
  "endpoint": "<method and URL, if observed>",
  "response_schema": "<sanitized keys only>",
  "hosted_url": "<url>",
  "draft_save_observed": true
}
```

Never log or export cookies, CSRF values, authorization headers, passwords, CAPTCHA data, or full request bodies.

## Publication Result

Persist at least the following fields for every 51CTO attempt:

```json
{
  "platform": "51cto",
  "sign_in_status": "signed | already_signed | failed | requires_login",
  "draft_status": "not_created | autosaved | failed",
  "article_id": "<id, if observed>",
  "status": "draft | submitted | under_review | published | failed | requires_login",
  "article_url": "<url, if available>",
  "image_urls": ["<url>"],
  "error": null
}
```

## Safety

- Never click final **发布** without explicit per-article approval.
- Keep public-reader validation in force before draft save, image upload, and publish.
- Preserve the complete mandatory author footer after Markdown conversion and in the final rich-text article.
- Maintain a structured browser trace without secrets; raw interface capture is a separate capability and not a substitute for browser-visible confirmation.
