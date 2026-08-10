# OSCHINA Publisher

This Skill is governed by [Mandatory Publishing Rules](../../PUBLISHING_RULES.md). Never publish internal system names, test labels, operational details, local paths, credentials, or browser-session data in reader-facing fields.

## Login And Entry

1. Open `https://www.oschina.net/` in the authenticated browser session.
2. If unauthenticated, hand off `https://www.oschina.net/home/login` to the user and retain the page until login is complete.
3. Open the avatar menu and click **发布博客/智写**. The Markdown editor URL is `https://my.oschina.net/u/<user-id>/blog/ai-write`.

## Markdown Article Lifecycle

1. Keep the default Markdown editor; its UI offers **切换到富文本编辑器**, which must not be selected when Markdown is requested.
2. Validate the title, Markdown body, mandatory author footer, and all reader-facing metadata before upload or publish.
3. Fill `input.title-input` and the Markdown textarea `.v-md-textarea-editor textarea`.
4. Insert all body assets before appending the author footer, so the footer remains the final article content.
5. Treat the editor's automatic draft save as a draft only; do not report success until the reader page is verified.

## Mandatory Body Image Upload

Do not use a cover image in place of the required body-image upload.

1. Place the Markdown cursor at the intended image position.
2. Click `.v-md-editor__toolbar-item-image` to open **插入图片**.
3. Select **上传本地图片**, wait for the file chooser, and upload the approved local image.
4. Confirm the editor inserts hosted Markdown in this form:

```markdown
![filename](https://oscimg.oschina.net//AiCreationDetail/up-<image-id>.jpg){{{width="auto" height="auto"}}}
```

5. Confirm the Markdown preview renders the image, then verify the same hosted image on the published reader page.

## Publish Configuration

1. Click **发布文章**, then complete the publish popover.
2. Choose **原创** unless the source is explicitly reposted.
3. Select an available blog category relevant to the article. The validated AI article used **AI**.
4. **选择专区** is optional. Do not select one unless the article specification requires it.
5. Keep **是否公开** enabled unless another visibility is requested. Keep **是否禁用评论** off unless requested.
6. Scheduled publishing is optional. Click **确定并发布** only after verifying the final settings.

The platform may derive public tag-like terms from article content. No independent manual tag field was observed in the publish popover.

## Publication Result

A successful publish redirects to:

```text
https://my.oschina.net/u/<user-id>/blog/<article-id>
```

Verify the title, original-source marker, mandatory author footer, and rendered hosted body image before reporting success. Persist only sanitized publication data:

```json
{
  "platform": "oschina",
  "article_id": "<id>",
  "status": "published | draft | failed | requires_login | requires_verification",
  "article_url": "<url>",
  "image_urls": ["<hosted-url>"],
  "error": null
}
```

Never log cookies, request headers, CSRF values, passwords, CAPTCHA data, raw request bodies, or browser session data.
