# 博客园 Publisher

This Skill is governed by [Mandatory Publishing Rules](../../PUBLISHING_RULES.md). Never publish internal system names, test labels, operational details, local paths, or credentials in any reader-facing field.

## Article Lifecycle

1. Open `https://www.cnblogs.com/` in the authenticated browser session and verify the author controls are visible.
2. Click **写随笔** and use `https://i.cnblogs.com/posts/edit`. The observed default editor is Markdown.
3. Validate the title, body, mandatory author footer, and all reader-facing metadata before creating a draft or uploading any asset.
4. Fill `#post-title` and `#md-editor`.
5. When content is AI-generated, check **内容由AI生成** (`#post-is-aigc`).
6. Complete the mandatory body-image upload exactly as described below, then verify the returned hosted URL in `#md-editor`.
7. Fill a normalized summary (`#summary`). Select only categories, collections, and tags that are actually available in the account; do not create unrelated taxonomy merely to fill fields.
8. Retain public visibility unless the article specification requires another access level. Do not opt into homepage-candidate submission unless specifically requested.
9. Click final **发布**, then require `发布成功`, a published `postId`, and successful reader-page validation before reporting success.

## Mandatory Body Image Upload

This is a two-step control flow. Do not click only the toolbar item and assume an upload occurred.

1. In the Markdown toolbar under **自动备份**, click `li[title="上传图片(Ctrl + I)"]`. This opens the **插入图片** dialog.
2. In that dialog click the visible **上传图片** button, wait for the file chooser, and select the approved local image.
3. Wait for the editor to append Markdown in this form:

```markdown
![filename](https://img2024.cnblogs.com/...)
```

4. Confirm the URL is hosted by the platform, then publish and confirm the public page renders the same image.

The dialog also provides a URL-input path and extraction controls. They do not satisfy the local-image upload requirement.

## Publish Configuration

- Article mode: **随笔**.
- AI declaration: required for generated article content.
- Summary: `#summary`.
- Tags: the post editor's tag selector accepts account-available tags; it does not automatically create arbitrary typed tags. Do not leave unfinished text in its input.
- Website category, personal category, and collections are optional unless the article request mandates them. Some site-category controls may not persist selection for ordinary posts; verify the selected state rather than assuming a click succeeded.
- Default observed access: public. Homepage-candidate submission remains off.

## Publication Result

The successful edit URL has this form:

```text
https://i.cnblogs.com/posts/edit-done;postId=<post-id>;isPublished=true
```

Use the **立即查看** link, with public URL `https://www.cnblogs.com/JavaPub/p/<post-id>`, and verify the reader page title and rendered hosted image.

Persist a sanitized record:

```json
{
  "platform": "cnblogs",
  "post_id": "<id>",
  "status": "published | draft | failed | requires_login",
  "article_url": "<url>",
  "image_urls": ["<hosted-url>"],
  "aigc_declared": true,
  "error": null
}
```

Never log cookies, request headers, CSRF values, passwords, raw request bodies, or browser session data.
