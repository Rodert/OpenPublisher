# CSDN Publisher

This Skill is governed by [Mandatory Publishing Rules](../../PUBLISHING_RULES.md). It must not publish internal system names or operational details, including in drafts, images, metadata, or SEO fields.

## Current mode

Browser mode only. The adapter must use a logged-in local browser session and must pause with `requires_login` when CSDN redirects to its login page.

## Article lifecycle

1. Open `https://editor.csdn.net/md/`.
2. Fill the title and Markdown editor.
3. Click **保存草稿** to create the initial CSDN draft.
4. Read `articleId` from the resulting editor URL.
5. Reuse that `articleId` for every subsequent save and for the final publish flow.
6. Complete the publish form only after the user has approved publishing.
7. Store the final public article URL and the CSDN article ID.

## Confirmed behavior

- Opening a fresh editor and entering content does not assign an article ID.
- The first successful draft save changes the URL to `https://editor.csdn.net/md?articleId=<id>`.
- After the first draft save, the editor enables history versions.
- An adapter must never infer an ID before the initial draft save.

## Image Upload

All CSDN test-publish runs must satisfy the global mandatory image-upload rule before final publication.

1. Open the editor toolbar action labelled `图片`.
2. In the `Insert image` dialog, select the `上传图片` tab and choose a local image.
3. CSDN uploads the asset and inserts Markdown in the editor using this form:
   `![在这里插入图片描述](<image-url>#pic_center)`.
4. Save the draft after insertion to persist the updated Markdown against the existing `articleId`.

Observed editor limits: `jpg`, `jpeg`, `png`, `gif`, `webp`, and similar image formats; one image up to 5 MB.

## Publish Configuration

The CSDN publish form requires at least one article tag. It also exposes these configurable fields:

- Summary (up to 256 characters)
- Cover image
- Category column
- Article type: original, repost, or translation
- Creation statement
- Visibility: public, private, follower-only, or VIP-only
- GitCode backup
- Multi-platform publishing
- Activity, topic, and scheduled publishing

The normalized CSDN configuration must persist the selected values before final publish. When GitCode backup is enabled, record it as `requested` until CSDN exposes a repository URL or a verifiable success state.

## End-to-End Checklist

1. Validate the normalized article, including the mandatory author footer and reader-facing content boundary.
2. Open the editor in a logged-in browser session; pause with `requires_login` if authentication is needed.
3. Create or reopen the draft and persist the CSDN `articleId`.
4. Upload every local image, wait for its hosted URL, replace the corresponding Markdown reference, and save the draft.
5. Open the publish form and apply the normalized title, tags, summary, cover, category, type, declaration, visibility, backup, activity, topic, and schedule settings.
6. Present the final reader-facing content and publish settings for explicit per-article approval.
7. Click the final publish action only after approval.
8. Read the success page, save the article URL, and distinguish `submitted`/`under_review` from a confirmed public result.
9. Record the GitCode backup as `requested` until its repository URL or success state is verifiable.

## Publication Result

Persist at least the following fields for every CSDN attempt:

```json
{
  "platform": "csdn",
  "article_id": "<id>",
  "status": "submitted | under_review | published | failed | requires_login",
  "article_url": "<url>",
  "image_urls": ["<url>"],
  "gitcode_backup_status": "disabled | requested | confirmed | failed",
  "error": null
}
```

## Safety

- Never click **发布文章** without an explicit per-article approval.
- Use a clearly labelled test title when validating the browser flow.
- Treat draft creation and public publishing as separate task states.
- Preserve the draft ID in the local publication record to make retries idempotent.
- Track asset upload and draft save separately. A returned CSDN image URL does not mean the article draft has been saved.
- Do not extract or log cookies, passwords, tokens, or CAPTCHA data.
- Run the mandatory reader-facing content validation before draft save, image upload, or publish. No CSDN-specific workflow can bypass it.
- Preserve the mandatory author footer at the end of the Markdown body through every CSDN conversion, save, and publish operation.
- Treat a CSDN success page that says `正在审核中` as `submitted`, not immediately as publicly available.

## Interface Discovery Notes

The observed browser-control surface exposes page state and console logs, but not full network request bodies. The implementation should keep a structured browser trace: editor URL before and after save, observed article ID, visible UI state, and non-sensitive console messages. A later browser-network capture can enrich this with method, endpoint, and sanitized request schema.
