# OSCHINA Browser Discovery

## Scope

Browser validation on 2026-08-10 using the authenticated `JavaPub` account. This record intentionally excludes credentials, cookies, request headers, CSRF values, raw request bodies, and browser-session data.

## Entry And Markdown Editor

- Home: `https://www.oschina.net/`.
- Login handoff: `https://www.oschina.net/home/login`.
- Open the avatar menu and select **发布博客/智写** to enter `https://my.oschina.net/u/4006267/blog/ai-write`.
- The default editor is Markdown, identified by the visible action **切换到富文本编辑器**. The title input is `input.title-input`; the body is `.v-md-textarea-editor textarea`.
- The editor states that articles automatically save to the draft box. No draft ID behavior was independently verified.

## Image Upload

The Markdown toolbar image menu uses this two-step flow:

1. Click `.v-md-editor__toolbar-item-image`.
2. Click **上传本地图片** and select a local image through the file chooser.

The verified local upload inserted:

```markdown
![csdn-upload-test.jpg](https://oscimg.oschina.net//AiCreationDetail/up-0926634390679b4cfda0b414149619a2.jpg){{{width="auto" height="auto"}}}
```

The Markdown preview and public reader page both rendered that hosted image. Cover images are a separate concern and do not replace the required body-image upload.

## Publish Configuration

- Source: **原创**.
- Blog category: **AI**.
- Public visibility was enabled; comments were not disabled.
- Zone selection and scheduling were optional and not used.
- No independent manual tag or summary field was observed. The published page displayed terms derived by the platform from the article content.

## Result

Article `今日科技观察：让 AI 智能体进入工程化协作` was published successfully.

- Public article: `https://my.oschina.net/u/4006267/blog/19736245`
- Article ID: `19736245`
- The public title, original-source marker, full mandatory author footer, and hosted body image were verified.
