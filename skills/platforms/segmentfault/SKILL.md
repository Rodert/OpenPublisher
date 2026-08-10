# SegmentFault Publisher

This Skill is governed by [Mandatory Publishing Rules](../../PUBLISHING_RULES.md). Never publish internal system names, test labels, operational details, local paths, credentials, or browser-session data in reader-facing fields.

## Login And Entry

1. Open `https://segmentfault.com/` in the authenticated browser session.
2. If unauthenticated, hand off `https://segmentfault.com/user/login` to the user. Preserve that page until login is complete.
3. Click **撰写**, then **写文章**. The editor URL is `https://segmentfault.com/write`.

## Markdown Article Lifecycle

1. Validate the title, Markdown body, mandatory author footer, and reader-facing metadata before upload or publish.
2. Fill `input[name="title"]`.
3. Use the CodeMirror Markdown editor at `.CodeMirror`; do not substitute HTML for Markdown. Its focus textarea is `.CodeMirror textarea`.
4. Ensure the author footer is the final article content after all body assets have been inserted.
5. Set the article type to **原创** unless the source is explicitly a translation or repost.
6. Select the destination blog requested by the user. The authenticated `JavaPub` account exposes **个人文章** and **JavaPub**.
7. Submit only after required image, metadata, and content checks are complete.

## Mandatory Body Image Upload

Do not use the optional cover upload as a substitute for the required article-body upload.

1. Place the Markdown cursor at the intended body-image position before opening the toolbar.
2. Click `.icon-image` to open **添加图片**.
3. Keep **上传图片** selected, choose the approved local image through its file input, and optionally enter alt text in **图片描述（选填）**.
4. Wait for the modal to populate the platform-relative image URL, then click **确定**.
5. Confirm the editor inserted Markdown in this form:

```markdown
![](/img/<image-id>)
```

6. After publishing, verify the reader page renders the resolved hosted URL `https://segmentfault.com/img/<image-id>`.

## Publish Configuration

- Tags: maximum five. Use only relevant, available tags and verify the UI reports no remaining required additions.
- Summary: no independent summary input was observed in this editor.
- Category: no independent article-category field was observed; tags carry the topic taxonomy.
- Cover: optional; use it only when the article specification requests a cover.
- Scheduling and copyright declaration are optional, and remain disabled unless requested.

## Publication Result

A successful publish redirects directly to:

```text
https://segmentfault.com/a/<article-id>
```

Verify the public page title, final author footer, selected tags, and rendered hosted body image before reporting success. Persist only sanitized publication data:

```json
{
  "platform": "segmentfault",
  "article_id": "<id>",
  "status": "published | draft | failed | requires_login | requires_verification",
  "article_url": "<url>",
  "image_urls": ["<hosted-url>"],
  "error": null
}
```

Never log cookies, request headers, CSRF values, passwords, CAPTCHA data, raw request bodies, or browser session data.
