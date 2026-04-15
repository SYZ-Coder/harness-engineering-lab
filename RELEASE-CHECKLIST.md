# Release Checklist

Use this checklist before publishing the repository to GitHub.

## Repository basics

- [ ] Repository name is confirmed
- [ ] `README.md` is suitable as the GitHub homepage
- [ ] `README.en.md` is present if bilingual presentation is desired
- [ ] `LICENSE` is present
- [ ] `.gitignore` is present
- [ ] `CONTRIBUTING.md` is present
- [ ] `AGENTS.md` is present

## Content review

- [ ] All links in `README.md`, `README.en.md`, and `INDEX.md` are valid
- [ ] The reading order still matches the current files
- [ ] The demos include verification steps
- [ ] No repo text still assumes access to the original repository
- [ ] Demo claims match the actual verification strength

## Cleanup

- [ ] Local IDE files are ignored and removed from the working tree
- [ ] No temporary build outputs or `__pycache__/` directories should be committed
- [ ] No private credentials or local absolute paths are present in publish-facing files

## Verification

- [ ] Python demos 02 / 05 / 06 / 07 / 08 / 09 have been run
- [ ] `practice/09-validation-review-demo/tools/validate_demo.py` has been run
- [ ] Java demo `mvn test` has been run

## Suggested first commit message

```text
Initialize standalone Harness repository with guides, templates, playbooks, and runnable demos
```

