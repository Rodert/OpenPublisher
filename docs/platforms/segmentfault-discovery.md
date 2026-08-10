# SegmentFault Browser Discovery

## Scope

Browser validation on 2026-08-10 using the authenticated `JavaPub` account. This record intentionally excludes credentials, cookies, request headers, CSRF values, raw request bodies, and browser-session data.

## Entry And Markdown Editor

- Home: `https://segmentfault.com/`.
- Login handoff: `https://segmentfault.com/user/login`.
- Click **撰写** then **写文章** to open `https://segmentfault.com/write`.
- The observed editor is CodeMirror Markdown, with `input[name="title"]` for the title and `.CodeMirror` for the Markdown body.
- The public article type defaulted to **原创**. The authenticated account exposed **个人文章** and **JavaPub** as destinations.

## Image Upload

The editor toolbar button `.icon-image` opens **添加图片**. Its **上传图片** flow accepts a local file and populates a platform-relative path before the final **确定** action.

The verified upload inserted this Markdown:

```markdown
![](/img/bVdp9r4)
```

The published reader page resolved and rendered it as `https://segmentfault.com/img/bVdp9r4`. Cover image selection is a separate optional control and does not meet the body-image requirement.

## Publish Configuration

- The selector allowed five tags; the validated article used `人工智能`, `机器学习`, `深度学习`, `llm`, and `prompt`.
- No independent summary or category field was observed.
- Cover image, timed publication, and copyright declaration were optional.

## Result

Article `今日科技观察：AI 智能体正在重塑研发协作节奏` was published successfully.

- Public article: `https://segmentfault.com/a/1190000048139523`
- Article ID: `1190000048139523`
- The public title, full mandatory author footer, selected tags, and hosted body image were verified.
