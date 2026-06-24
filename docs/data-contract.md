# Public data contract

Each row represents one store and one date or reporting period.

Required fields:

| Field | Type | Meaning |
|---|---:|---|
| `date` | text | ISO date or period label |
| `store_id` | text | Stable anonymized store key |
| `store_name` | text | Display name; synthetic in examples |
| `revenue` | number | Net operating receipts for the row |

Recommended fields:

| Field | Type | Meaning |
|---|---:|---|
| `city` | text | City or operating region |
| `dine_in` | number | Dine-in receipts |
| `delivery` | number | Delivery receipts |
| `takeaway` | number | Takeaway receipts |
| `orders` | number | Paid order count |
| `guest_count` | number | Guest count where available |

Every field beginning with `channel_` is treated as a channel amount. The sum is checked against `revenue`.

Examples:

- `channel_group_buy`
- `channel_member`
- `channel_delivery`
- `channel_offline`

原始支付字段可以使用 `payment_` 前缀，再通过
`config/channel_rules.example.json` 归并。公开配置应仅使用通用或已获
授权公开的字段名；企业特定映射可以保持私有。

## Metric rules

- Store average revenue = total revenue / distinct stores.
- Average ticket = total revenue / total orders.
- Service-type closure = dine-in + delivery + takeaway - revenue.
- Channel closure = sum of all `channel_` values - revenue.
- A zero previous-period denominator returns `null` for growth rate rather than an invented percentage.
