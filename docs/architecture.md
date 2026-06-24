# Architecture

```text
Authorized exports
      |
      v
Private/vendor adapters
      |
      v
Public normalized data contract
      |
      v
Deterministic metric kernel
      |
      +--> JSON / CSV
      +--> Excel or BI dashboards
      +--> Management reports
      +--> AI explanation layer
```

The public core must remain usable without access to a particular POS vendor.

## Repository boundaries

- `restaurant-ops-toolkit`: public schemas, metrics, validation, tests, synthetic examples.
- private adapters: authentication, proprietary endpoints, merchant-specific mappings.
- private operations workspace: real exports, reports, screenshots, reviews, and staff data.

AI may explain validated results, but primary calculations should remain deterministic and testable.
