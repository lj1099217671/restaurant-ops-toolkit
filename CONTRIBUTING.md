# 参与贡献 | Contributing

感谢你帮助改进餐饮经营工具箱。我们欢迎业务口径、文档、测试、示例和代码贡献。

Thank you for improving Restaurant Ops Toolkit. Contributions to metric definitions, documentation, tests, examples, and code are welcome.

## 最简单的参与方式

不需要会写代码：

1. 在 Issue 中描述一个真实的餐饮经营问题；
2. 说明输入数据、希望得到的指标及业务用途；
3. 使用虚构门店和合成数字，不粘贴真实经营数据；
4. 帮助检查中文或英文文档是否容易理解。

## 提交代码前

1. 先搜索现有 Issues，避免重复工作；
2. 较大的功能先开 Issue 讨论口径；
3. 从 `main` 创建自己的分支；
4. 使用合成或明确公开的数据；
5. 为计算变化增加测试；
6. 更新涉及的字段定义和版本说明。

## 本地验证

```powershell
python -m pip install -e .
python scripts/prepublish_scan.py
python -m unittest discover -s tests -v
```

## 指标变化必须写清楚

Pull Request 中必须说明：

- 指标解决什么业务问题；
- 输入字段和单位；
- 计算公式；
- 分母和排除项；
- 缺失值与零分母如何处理；
- 是否会改变历史结果；
- 使用了哪些合成测试数据。

## 禁止提交

- 账号、密码、Token、Cookie、`.env`；
- 私有接口、认证流程或商户后台内容；
- 真实销售额、评价、门店或员工信息；
- 验证码绕过、风控绕过或高频抓取逻辑；
- 未经授权复制的第三方代码、数据或文档。

## Pull Request 审核

外部 Pull Request 不会自动合并。维护者会检查：

1. 是否属于项目范围；
2. 业务口径是否清楚；
3. 测试和安全扫描是否通过；
4. 是否泄露私有或商业信息；
5. 文档是否能让非开发者理解。

English contributors may open issues and pull requests in English. Bilingual documentation improvements are especially welcome.
