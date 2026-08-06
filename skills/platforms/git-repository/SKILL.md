# Local Git Repository Publisher

## Purpose

Publish a normalized article into a local Git-backed content repository.

## Inputs

- Repository path
- Article output directory
- Markdown/front matter format
- Asset directory
- Commit message template
- Target branch and whether to push

## Workflow

1. Verify the repository exists and inspect its working tree.
2. Render the article and copy/resolve image assets.
3. Show the files and diff that would change.
4. Write the files, then optionally commit and push.
5. Return the commit, branch, repository and public URL when configured.

## Safety

- Never overwrite unrelated uncommitted changes.
- Never commit `.env`, tokens, cookies or passwords.
- Support write-only, commit-only and commit-and-push modes.
- Stop and report conflicts instead of force-pushing.

