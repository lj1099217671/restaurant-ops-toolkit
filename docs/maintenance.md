# Maintenance policy

## Weekly

- Review open issues and pull requests.
- Run tests and the pre-publish scan.
- Confirm that examples remain synthetic.
- Check dependency and GitHub Actions update proposals.

## Before every release

- Review the full Git diff.
- Run `python scripts/prepublish_scan.py`.
- Run `python -m unittest discover -s tests -v`.
- Confirm that Git history has never included private merchant material.
- Update the changelog or release notes with metric-definition changes.

## Compatibility

Metric definitions are public API. A release must not silently change:

- units;
- denominators;
- exclusions;
- residual-channel behavior;
- missing-field behavior.

Breaking metric changes require a major version or an explicit migration note.

## Private boundary

Maintainers should test public logic against synthetic fixtures. Real merchant
exports may be used only in a separate private environment and must never be
copied into issues, pull requests, Actions artifacts, or repository history.
