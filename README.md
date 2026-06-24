# Restaurant Ops Toolkit

面向中国连锁餐饮经营团队的开源数据处理核心：把不同 POS、外卖、团购和口碑平台导出的数据，统一成可复核、可比较、可持续迭代的经营指标。

This project provides a vendor-neutral analytics core for multi-store restaurant operations.

## Why this exists

餐饮企业通常不是“没有数据”，而是数据分散在 POS、外卖、团购、会员、点评和人工台账中。真正缺少的是：

- 稳定的数据口径；
- 门店、城市、品牌之间可比较的指标；
- 渠道合计与营业实收的自动核对；
- 可追溯的异常提示；
- 不绑定单一软件厂商的复用框架。

本仓库先解决最基础、最普遍的部分。具体 POS 登录、商户凭据和企业私有规则应放在独立的私有适配器中。

## Current capabilities

- 读取标准化 CSV；
- 汇总营业实收、订单、客单价和店均；
- 汇总任意 `channel_` 开头的渠道字段；
- 通过公开配置将支付字段归并为团购、短视频、会员、外卖和线下渠道；
- 对比本期与上期；
- 检查堂食、外卖、外带与营业实收是否闭合；
- 检查渠道合计与营业实收是否闭合；
- 输出稳定 JSON，便于接入 Excel、Dashboard、LLM 或管理报告。

## Quick start

Requires Python 3.10+.

```powershell
python -m pip install -e .
python -m restaurant_ops_toolkit.cli summarize `
  --input examples/synthetic_sales.csv `
  --output out/summary.json

python -m restaurant_ops_toolkit.cli compare `
  --current examples/synthetic_sales.csv `
  --previous examples/synthetic_sales_previous.csv `
  --output out/comparison.json

python -m restaurant_ops_toolkit.cli channels `
  --input examples/synthetic_payments.csv `
  --rules config/channel_rules.example.json `
  --output out/channels.json
```

Run tests:

```powershell
python -m unittest discover -s tests -v
```

## Data boundary

This repository intentionally contains:

- synthetic sample data;
- generic calculation logic;
- public schemas and validation rules.

It intentionally does not contain:

- merchant credentials or cookies;
- proprietary POS endpoints;
- real store names, IDs, sales, reviews, or employee information;
- platform bypass, CAPTCHA bypass, or high-frequency scraping logic;
- company-specific scoring rules.

See [docs/data-contract.md](docs/data-contract.md) and [SECURITY.md](SECURITY.md).

示例渠道配置只包含通用字段名。企业真实支付字段映射可以保存在
被 `.gitignore` 排除的私有配置中。

## Product direction

The long-term goal is an open-core restaurant operations platform:

1. Open-source metric kernel and data contracts.
2. Community-maintained import templates for common exports.
3. Private or commercial adapters for proprietary systems.
4. Reproducible management reports and anomaly detection.
5. Optional AI explanations built on deterministic calculations.

See [docs/roadmap.md](docs/roadmap.md).
Maintenance and release controls are documented in
[docs/maintenance.md](docs/maintenance.md).

## License

MIT. Real platform data and third-party exports remain subject to their own terms and applicable law.
