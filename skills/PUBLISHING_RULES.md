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
