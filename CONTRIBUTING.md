# Contributing

Contributions should improve a vendor-neutral restaurant operations workflow.

## Requirements

- Use synthetic or explicitly public data in tests and examples.
- Keep calculations deterministic and independently testable.
- Document metric definitions, units, denominators, and exclusions.
- Do not add credentials, private endpoints, real merchant data, or platform-bypass code.
- Add or update tests for every calculation change.

## Development

```powershell
python -m pip install -e .
python -m unittest discover -s tests -v
```

Before opening a pull request, verify that sample outputs contain no real business identifiers.
