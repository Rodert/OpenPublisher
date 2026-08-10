# Mandatory Publishing Rules

These rules apply to every publishing destination and cannot be bypassed by a platform-specific Skill or Adapter.

## Reader-Facing Content Boundary

Never publish internal system names, implementation details, test labels, adapter names, automation instructions, local paths, credentials, or operational notes in any reader-facing field.

At minimum, the following text is prohibited in titles, summaries, bodies, image alt text, captions, SEO fields, and publication metadata:

- `OpenPublisher`
- `adapter discovery`
- `test draft`
- `temporary draft`
- local filesystem paths
- authentication data and environment variable names

## Enforcement

1. Every Adapter must invoke the centralized public-content validation before any platform operation.
2. Validation failures must stop the task before draft save, asset upload, or publish.
3. The same validation applies to drafts and public articles. A non-public draft is not an exception.
4. Platform Skills may add stricter rules, but may not weaken or replace these rules.

## Mandatory Author Footer

Every published article must end with the configured author profile. The publishing pipeline appends it before centralized validation; platform-specific transformations must preserve it and must not duplicate it.

## Mandatory Image Upload In Test Runs

Every platform test-publish workflow must complete a real image upload before final publication. This is mandatory even when the platform supports automatic cover selection.

1. Upload at least one approved local image to the platform's article editor or media service.
2. Confirm the platform returned a hosted image URL and that the image is rendered in the editor or preview.
3. Save the draft after insertion, then verify the hosted image remains associated with the saved article.
4. Record the sanitized hosted URL in the publication result.

An automatic cover option does not satisfy this rule unless the uploaded image is already present in the article. A platform Skill may require additional image or cover checks, but may never omit this test-run requirement.
