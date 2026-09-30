# Alpha release publishing checklist

Status: publication pending. A version in CITATION.cff or a Markdown release note does not create a GitHub tag or release.

## Prepublication checks

- Verify the main-branch commit containing the complete alpha package.
- Confirm README, STATUS, roadmap, working paper, citation, and notes agree on scope.
- Verify saved text hashes and that the starter workbook remains unchanged from its checked version.
- Check relative links and the synthetic example totals.
- Check that no completed pilot, validated instrument, independent review, adoption, or journal publication is asserted.
- Check existing tags and releases to avoid duplicating or overwriting a version.

## Publish

1. In GitHub Releases, create `v0.1.0-alpha` at the verified package commit. If the tag already exists, inspect its target before proceeding.
2. Use the title and release body in [RELEASE_NOTES.md](../RELEASE_NOTES.md).
3. Mark the release as a prerelease. Publish only after the target commit and body are correct.
4. Read back the release URL, tag target, prerelease flag, and published status.
5. Record the actual publication date and URL in STATUS and CHANGELOG. Add `date-released` to CITATION.cff only after publication.

Reference: [GitHub release documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
