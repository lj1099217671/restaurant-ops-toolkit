# 安全与数据边界 | Security and data boundaries

## 不要公开提交

- POS、外卖、评价平台或商户账号凭据；
- Cookie、Session、Token、Authorization Header 或 `.env`；
- 真实门店销售额、评价、员工姓名、手机号或内部 ID；
- 私有系统接口、认证流程或商户后台材料；
- 登录后页面的截图、HTML、网络响应或浏览器 Profile；
- 会暴露内部合作条款、核算结构或商业秘密的字段映射。

渠道方法可以公开，但应转换成通用数据模型。企业真实渠道配置应保存在：

- 单独的私有仓库；或
- 被 `.gitignore` 排除的本地私有配置。

## 如何报告安全问题

不要创建公开 Issue，也不要在 Discussion 中粘贴敏感信息。

请使用 GitHub 仓库 Security 页面中的 **Report a vulnerability** 私下报告。报告应包含最小复现信息，不要附带无关真实经营数据。

## 响应原则

维护者将：

1. 确认是否收到报告；
2. 判断影响范围；
3. 优先移除凭据或阻止继续泄露；
4. 修复后再公开披露必要信息；
5. 要求已泄露凭据立即轮换，而不是只删除文件。

## 适配器边界

厂商认证和私有数据提取应位于独立私有仓库。公开适配器只能处理使用者有权导出的文件。

---

Never publish credentials, sessions, private endpoints, merchant data, authenticated page captures, or commercially sensitive mappings. Report vulnerabilities privately through GitHub Security Advisories. Rotate exposed credentials immediately; deleting a committed secret is not sufficient.
