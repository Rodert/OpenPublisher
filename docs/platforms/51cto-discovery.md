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

- Current Markdown editor URL: `https://blog.51cto.com/blogger/publish`
- The editor shows `草稿将自动保存` before content entry.
- Filling a title and body increased the visible draft count from 4 to 5.
- After waiting, the editor displayed `已保存 2026-08-10 12:03:00`.
- The fresh page and saved draft both had no visible `blog_id` or `work_id`; the editor URL did not change.

Conclusion: 51CTO creates an automatic draft without exposing a reusable article ID through the observed page state. A later test must inspect the draft inbox, final submission result, or a safe network trace before implementing idempotent retries around an ID.

## Markdown Editor And Images

The visible `写文章` entry opens the Markdown editor. Its body-image toolbar button is `.editorphoto1`; the dropdown offers `上传图片` and `添加图片链接`.

- `上传图片` is the local-file path and is required for test publication.
- Selecting the approved test image inserted Markdown with a 51CTO-hosted `https://s2.51cto.com/...` URL.
- The same hosted image rendered in the editor before submission.
- The publish panel's cover controls are separate and do not satisfy the body-image requirement.

## Publish Form

Visible configuration included:

- required first-level and second-level article categories;
- personal category;
- a maximum of five tags;
- summary (up to 500 characters);
- topic;
- cover mode (single image, three images, no image, or automatic extraction);
- article type;
- copyright statement;
- public/private visibility;
- optional pinning.

The final confirmation requires both category levels. The verified Markdown-editor submission used `人工智能` / `深度学习`, five tags, original type, public visibility, automatic cover, and a configured summary.

## Images And Requests

The body-image upload was completed through the visible file chooser. Browser-visible confirmation is sufficient for this adapter discovery; no raw request endpoint, request body, cookie, CSRF value, or authorization value was collected. Preserve only a sanitized result record:

```json
{
  "event": "image_upload",
  "source_filename": "csdn-upload-test.jpg",
  "destination": "editor",
  "hosted_url": "https://s2.51cto.com/images/blog/front/202608/c58074a9176479542dd131517fb55ea39a9eec.jpg?...",
  "rendered_in_editor": true,
  "draft_save_observed": true
}
```

## Submission Result

An earlier attempt using draft `2071719` did not publish. The draft remains in the draft inbox; a draft-editor **确认** button is not sufficient evidence of submission.

The fresh article `今日科技观察：AI 智能体如何重塑软件研发协作` was successfully submitted from a new editor. 51CTO redirected to `https://blog.51cto.com/blogger/success/14838140`, displayed `发布成功`, and the reader-facing article URL was verified as `https://blog.51cto.com/wangshiyu/14838140`.

The Markdown-editor article `AI 智能体图文观察：研发团队如何构建可靠协作` was published with the required local body image. 51CTO redirected to `https://blog.51cto.com/blogger/success/14838168`, displayed `发布成功`, and the reader-facing URL was verified as `https://blog.51cto.com/wangshiyu/14838168`.
