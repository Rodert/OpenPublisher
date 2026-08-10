# 51CTO Browser Discovery

## Scope

First browser discovery on 2026-08-10, using the account's existing signed-in browser session. This record contains visible workflow behavior only; it deliberately excludes credentials, cookie values, CSRF values, and raw request bodies.

## Daily Sign-in

- Required entry URL: `https://blog.51cto.com/user/sign`
- Observed result: `今日已签到`
- Normalized sign-in result: `already_signed`
- The signed-in author profile shown by 51CTO: `JavaPub`

Every future 51CTO attempt must repeat this check before opening the editor.

## Editor And Draft

- Editor URL: `https://blog.51cto.com/blogger/publish?old=1&newBloger=2`
- The editor shows `草稿将自动保存` before content entry.
- Filling a title and body increased the visible draft count from 4 to 5.
- After waiting, the editor displayed `已保存 2026-08-10 12:03:00`.
- The fresh page and saved draft both had no visible `blog_id` or `work_id`; the editor URL did not change.

Conclusion: 51CTO creates an automatic draft without exposing a reusable article ID through the observed page state. A later test must inspect the draft inbox, final submission result, or a safe network trace before implementing idempotent retries around an ID.

## Markdown Conversion

Pasting Markdown into the rich-text editor raised this dialog:

`检测到粘贴内容符合 Markdown 语法，是否需要转换？`

Selecting **确认** converted headings, the horizontal separator, strong text, and the personal-homepage link into rich text. The required author footer was preserved at the end of the rendered article.

## Publish Form

Visible configuration included:

- required article category;
- personal category;
- a maximum of five tags;
- summary (up to 500 characters);
- topic;
- cover mode (single image, three images, no image, or automatic extraction);
- article type;
- copyright statement;
- public/private visibility;
- optional pinning.

The draft is currently left in the publication configuration view and has not been publicly submitted. Its selected settings are category `人工智能`, five relevant tags, original type, public visibility, automatic cover, and the configured summary.

## Images And Requests

Both editor and cover image upload controls are present. The current browser-control connection provides DOM inspection and console logs but not file selection or raw network request capture. No image was uploaded in this 51CTO discovery run, and no endpoint has been claimed.

The follow-up should use a browser flow that supports the visible file chooser, then capture a sanitized event record: destination, request method and URL if available, response key names, returned image URL, and the subsequent draft save. Credentials, request headers, CSRF values, and complete payloads must remain excluded.

## Final Publish Boundary

The final **发布** button is visible but was not clicked. Public submission requires the user's explicit per-article confirmation, even after every field is configured.
