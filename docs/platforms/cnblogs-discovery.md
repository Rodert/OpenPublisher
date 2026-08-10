# 博客园 Browser Discovery

## Scope

Browser validation on 2026-08-10 using the existing authenticated `JavaPub` session. This record intentionally excludes credentials, cookies, request headers, CSRF values, and raw request bodies.

## Entry And Editor

- Entry: `https://www.cnblogs.com/`
- Authenticated controls showed `写随笔` and `我的博客`.
- `写随笔` opened `https://i.cnblogs.com/posts/edit`.
- The observed editor default was Markdown, with title input `#post-title` and body input `#md-editor`.
- The platform displays a community-rule reminder and an explicit `内容由AI生成` declaration; it was enabled for generated content.

## Image Upload

The body image upload is a required two-step flow:

1. Click the toolbar item under `自动备份` with title `上传图片(Ctrl + I)`.
2. The resulting `插入图片` dialog offers a second `上传图片` button. Click it and use the file chooser.

The approved image was uploaded and appended to Markdown as a hosted `https://img2024.cnblogs.com/...` URL. The public reader page rendered that same image. URL input and image extraction are separate dialog actions and do not replace local-image upload.

## Publish Options

- Post type: 随笔.
- Summary field: `#summary`.
- AI declaration: `#post-is-aigc`.
- Public access, blog-home display, comments, and RSS were enabled by default.
- Homepage-candidate contribution remained disabled.
- The account's tag selector accepts available tags but does not automatically create arbitrary typed tags; clear unaccepted input before publish.
- Website category, personal category, and collection are optional for ordinary posts. Selection must be verified if used.

## Result

Article `今日科技观察：AI 智能体如何融入研发协作` was published successfully.

- Edit result: `https://i.cnblogs.com/posts/edit-done;postId=22367075;isPublished=true`
- Public article: `https://www.cnblogs.com/JavaPub/p/22367075`
- The reader-page title matched the submitted title and the uploaded hosted image rendered successfully.
