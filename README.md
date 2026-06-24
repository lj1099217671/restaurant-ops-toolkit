# 餐饮经营工具箱 | Restaurant Ops Toolkit

[![CI](https://github.com/lj1099217671/restaurant-ops-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/lj1099217671/restaurant-ops-toolkit/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/lj1099217671/restaurant-ops-toolkit)](https://github.com/lj1099217671/restaurant-ops-toolkit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](pyproject.toml)
[![Project status: Alpha](https://img.shields.io/badge/status-alpha-orange.svg)](docs/roadmap.md)

**把分散的 POS、外卖、团购、会员数据，变成可复核、可比较的餐饮经营指标。**

**Turn fragmented POS, delivery, group-buying, and membership exports into auditable, comparable restaurant operating metrics.**

[中文说明](#中文说明) · [English](#english) · [快速开始](#快速开始--quick-start) · [路线图](docs/roadmap.md) · [参与贡献](CONTRIBUTING.md)

---

## 中文说明

### 它解决什么问题？

餐饮企业通常不是没有数据，而是数据散落在不同系统里，字段名称和统计口径也不一致。人工复制到 Excel 后，很容易出现渠道重复、漏算、店均口径不统一和同比结论无法复核的问题。

本项目先解决四件基础但高频的事：

1. 统一营业实收、订单、客单价、店均等指标；
2. 将不同支付字段归并为团购、短视频、会员、外卖、线下等渠道；
3. 自动检查堂食、外卖、外带和渠道金额是否与营业实收闭合；
4. 用稳定 JSON 输出结果，供 Excel、看板、管理报告或 AI 解释层继续使用。

### 谁适合使用？

- 连锁餐饮运营、财务和数据团队；
- 为餐饮企业提供 POS、BI 或咨询服务的团队；
- 希望建立可复核经营口径的餐饮从业者和开发者。

### 现在能做什么？

- 读取标准化 CSV；
- 计算营业实收、订单、客单价和店均；
- 对比本期与上期；
- 使用配置文件归并渠道；
- 记录缺失字段并执行渠道倒挤；
- 检查服务类型和渠道金额是否闭合；
- 在 Python 3.10–3.12 上运行自动测试。

### 它不是什么？

- 不是某个 POS 厂商的破解工具；
- 不包含商户账号、Cookie、私有接口或真实经营数据；
- 不替代财务审计、税务判断或企业最终经营决策；
- 当前为 **Alpha 阶段**，数据契约仍会在版本说明中迭代。

## English

Restaurant Ops Toolkit is a vendor-neutral, open-source metric kernel for multi-store restaurant operations.

It helps operators and analysts normalize authorized exports, calculate common KPIs, reconcile service-type and channel totals, compare periods, and produce machine-readable outputs. The public repository contains synthetic examples and deterministic calculations only. Proprietary connectors, credentials, and merchant data remain outside the project.

Current scope:

- standardized CSV input;
- revenue, store-average revenue, orders, and average ticket;
- configurable channel mapping and residual calculation;
- service-type and channel reconciliation;
- period-over-period comparison;
- reproducible tests and security checks.

Project status: **Alpha**. See the [roadmap](docs/roadmap.md), [methodology](docs/methodology.md), and [data contract](docs/data-contract.md).

## 快速开始 | Quick start

Requires Python 3.10+.

```powershell
git clone https://github.com/lj1099217671/restaurant-ops-toolkit.git
cd restaurant-ops-toolkit
python -m pip install -e .
```

汇总经营指标 / Summarize:

```powershell
python -m restaurant_ops_toolkit.cli summarize `
  --input examples/synthetic_sales.csv `
  --output out/summary.json
```

期间对比 / Compare periods:

```powershell
python -m restaurant_ops_toolkit.cli compare `
  --current examples/synthetic_sales.csv `
  --previous examples/synthetic_sales_previous.csv `
  --output out/comparison.json
```

渠道归并 / Map payment fields to channels:

```powershell
python -m restaurant_ops_toolkit.cli channels `
  --input examples/synthetic_payments.csv `
  --rules config/channel_rules.example.json `
  --output out/channels.json
```

验证 / Validate:

```powershell
python scripts/prepublish_scan.py
python -m unittest discover -s tests -v
```

## 为什么结果值得信任？ | Why trust the output?

- **明确口径**：指标的字段、单位、分母和零分母行为写入公开文档；
- **确定性计算**：核心数字由可测试代码计算，不由语言模型猜测；
- **闭合校验**：服务类型和渠道金额会与营业实收核对；
- **合成样例**：任何人都能复现示例结果；
- **自动测试**：每次提交都会在 GitHub Actions 中运行；
- **安全边界**：发布前扫描凭据、隐私和高风险文件。

详细说明见 [方法与有效性](docs/methodology.md)。

## 数据与商业安全 | Data and commercial safety

公开仓库允许存放通用渠道方法，但不允许存放：

- 账号、密码、Token、Cookie 或浏览器登录状态；
- 私有 POS 接口、认证流程或商户后台页面；
- 真实门店名称、ID、销售额、评价原文或员工信息；
- 会暴露私有系统结构、内部合作条款或核算规则的字段映射。

企业真实映射应保存在被 Git 忽略的私有配置中。详见 [SECURITY.md](SECURITY.md)。

## 公开不等于人人能直接修改

任何人都可以阅读、Fork、提出 Issue 或 Pull Request；只有仓库所有者和被明确邀请的协作者才能直接写入。外部贡献必须经过审核和自动测试后，才可能进入 `main`。

权限和审核流程见 [GOVERNANCE.md](GOVERNANCE.md)。

## 项目结构 | Project structure

```text
config/       通用渠道配置示例
docs/         数据口径、方法、路线图和维护说明
examples/     完全合成的示例数据
scripts/      发布前安全扫描
src/          指标和渠道计算核心
tests/        自动测试
```

## 参与与维护 | Contributing and maintenance

- 想提需求或报告问题：使用 [Issues](https://github.com/lj1099217671/restaurant-ops-toolkit/issues)；
- 想讨论方向：使用 [Discussions](https://github.com/lj1099217671/restaurant-ops-toolkit/discussions)；
- 想贡献代码：先读 [CONTRIBUTING.md](CONTRIBUTING.md)；
- 维护者日常操作：读 [中文维护手册](docs/maintainer-guide.zh-CN.md)；
- 安全问题：按 [SECURITY.md](SECURITY.md) 私下报告。

## 开源与商业边界 | Open-core direction

长期保留：

- 开源：数据契约、指标内核、校验规则、合成样例和基础报告；
- 私有或商业：专有系统连接器、托管调度、权限审计、企业模板和实施服务。

这样既让行业共同改进基础标准，也避免企业凭据和商业数据外泄。

## License

[MIT](LICENSE). Third-party exports and real merchant data remain subject to their own terms, authorization, and applicable law.
