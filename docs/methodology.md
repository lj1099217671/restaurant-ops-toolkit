# 方法、信度与效度 | Methodology, reliability, and validity

本项目不以“看起来智能”为目标，而以“结果可复核”为目标。

## 1. 构念效度：指标是否代表真正想衡量的业务问题？

每个指标应明确：

- 业务名称和用途；
- 输入字段；
- 单位；
- 公式；
- 分母；
- 排除项；
- 缺失值和零分母行为。

例如，店均营业实收定义为：

```text
所选范围营业实收合计 / 所选范围去重门店数
```

它不自动等于同店店均，也不应混入闭店或无经营记录门店。不同业务问题必须使用不同门店范围。

## 2. 计算信度：相同输入是否稳定得到相同结果？

核心计算使用确定性 Python 代码，不依赖语言模型生成数字。相同输入、版本和配置应产生相同结果。

保障方式：

- 单元测试；
- GitHub Actions；
- 明确版本；
- 合成示例；
- 对指标变化记录 Changelog。

## 3. 内部效度：结果是否可能由口径错误造成？

项目使用闭合检查降低常见错误：

```text
堂食 + 外卖 + 外带 - 营业实收
渠道合计 - 营业实收
```

差额不为零时，输出应保留警告，而不是静默修正。

## 4. 外部效度：能否应用到其他餐饮企业？

公开内核不绑定某一 POS 厂商，通过标准数据契约和渠道配置适配不同来源。但不同企业的退款、优惠、佣金、税费和跨期规则可能不同，使用者必须核对本企业定义。

## 5. 当前限制

- 当前主要支持 CSV；
- 门店生命周期、同店和节假日逻辑仍在路线图中；
- 示例数据是合成数据，只用于验证计算，不代表真实行业基准；
- 渠道倒挤依赖输入口径完整；
- 输出不是审计意见、财务意见或经营保证。

## 6. AI 的边界

AI 可以用于解释、文档和候选分类，但不应替代：

- 核心金额计算；
- 数据闭合校验；
- 门店范围确认；
- 模糊记录的人工复核；
- 最终经营责任。

---

The project prioritizes reproducibility over apparent intelligence. Metric definitions, deterministic calculations, reconciliation checks, synthetic fixtures, tests, and documented limitations are used to improve reliability. Applicability to a specific business still depends on that business's accounting and operating definitions.
