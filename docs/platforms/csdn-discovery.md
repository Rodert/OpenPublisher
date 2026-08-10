# CSDN Browser Discovery

Date: 2026-08-10

## Scope

Validated the CSDN Markdown editor with a clearly labelled, non-public test draft. The flow did not enter the publishing form or create a public article.

## Confirmed Draft Lifecycle

| Step | Observed state |
| --- | --- |
| Open editor | `https://editor.csdn.net/md/`; no article ID; history versions disabled |
| Enter title and Markdown | URL remains without an article ID |
| Save draft | URL changes to `https://editor.csdn.net/md?articleId=<id>` |
| After save | A numeric article ID exists and history versions become available |

The CSDN `articleId` is therefore created by the first successful draft save, not by opening the editor or typing article content.

## Adapter Implications

- Draft creation is a required, explicit step before final publishing.
- Persist `articleId` immediately after saving the draft.
- Retries must reopen the editor with the persisted `articleId`, rather than create a second draft.
- A missing `articleId` is not a valid state for any update or publish operation.
- Publishing must stay behind a separate approval boundary.

## Observed Editor Capabilities

- Markdown editor
- Title input with a visible 5-100 character requirement
- Draft save action
- Publish action
- History versions after draft creation
- Image/file insertion control

## Image Upload Validation

A local JPEG was uploaded through the CSDN editor's `图片` action and `Insert image` dialog. CSDN returned a hosted `i-blog.csdnimg.cn` URL and inserted it directly into the Markdown editor in this form:

```markdown
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/<asset-id>.jpeg#pic_center)
```

Uploading an image and saving the article are separate operations. The test deliberately left the updated draft unsaved after verifying the URL insertion; a production adapter must save the existing draft after every successful asset insertion.

## Publish Form Validation

The publish form requires article tags and supports a summary, cover image, category column, article type, creation statement, visibility, GitCode backup, multi-platform publishing, activity/topic selection, and scheduled publishing.

The first completed test used:

- Five tags: `科技`, `人工智能`, `云原生`, `AI Agent`, and `大模型应用`
- A manually provided summary
- Article type: original
- Visibility: public
- GitCode backup: enabled

The successful submission opened CSDN's success page with the status `发布成功！正在审核中` and a public article URL. CSDN did not show a GitCode repository URL or backup completion status on that page, so the backup must be recorded as requested rather than confirmed.

## Interface Capture Status

The current browser integration exposes DOM state and console logs but not complete browser network request bodies. The test confirmed the dynamic ID handoff using the editor URL. It did not record an endpoint, method, headers, or request payload, so those values must not be guessed in the CSDN adapter.

The next discovery pass should use a browser network tracing surface, when available, to capture and sanitize:

1. The initial draft-save request and response.
2. The subsequent update-save request using an existing `articleId`.
3. Image upload request and returned image URL.
4. Final publish request and returned public URL.
