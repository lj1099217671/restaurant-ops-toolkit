# Security and data handling

## Never commit

- POS, delivery-platform, review-platform, or merchant credentials;
- cookies, session files, tokens, authorization headers, or `.env` files;
- real store sales, customer reviews, employee names, phone numbers, or IDs;
- proprietary endpoint documentation copied from a private system;
- screenshots or raw HTML captured from authenticated merchant pages.

Channel logic may be published when expressed as a generic data model. Do not
publish merchant-specific payment column names if they reveal a private system
schema, negotiated commercial arrangement, or internal accounting rule.

## Reporting a vulnerability

Do not open a public issue containing credentials, private data, or an exploitable endpoint. Contact the maintainer privately through the security contact published on the GitHub repository.

## Adapter boundary

Vendor-specific authentication and extraction belong in a separate private repository. Public adapters should operate only on files the user is authorized to export.
