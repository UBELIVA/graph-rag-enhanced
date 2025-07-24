import json

sample = {
    "question": "什么是适航认证？eVTOL 如何通过适航认证？",
    "answer": """适航认证是指对民用航空器的设计、生产、使用和维修进行技术鉴定和监督，以确保飞行安全的过程。根据《中华人民共和国民用航空法》和《中华人民共和国适航管理条例》，适航认证由中国民航局负责，主要包括以下三大证书：

1. 型号合格证（Type Certificate, TC）：核查航空器的设计是否满足适航标准，包括型号设计、使用限制、数据单等内容。
2. 适航证（Airworthiness Certificate, AC）：证明每架飞机按照批准的设计和质量体系制造，能够安全运营。
3. 生产许可证（Production Certificate, PC）：证明企业具备在有效质量系统控制下，重复生产符合批准型号设计的航空器的能力。

对于eVTOL（电动垂直起降飞行器），通过适航认证的关键步骤包括：

- 设计阶段：确保eVTOL的设计符合适航标准，包括安全性、环境保护要求等。
- 生产阶段：建立符合质量体系要求的生产能力，并通过民航局的审核。
- 测试与验证：对每架eVTOL进行适航检查，确保其符合安全飞行的要求。
- 申请与审批：向中国民航局提交相关申请，包括型号合格证、适航证和生产许可证，经过审查后获得认证。

适航认证是eVTOL进入市场和商业化运营的核心环节，直接关系到其安全性和市场接受度。""",
    "retrieved_chunks": []
}

with open("/code/rag_eval_sample.json", "w", encoding="utf-8") as f:
    json.dump([sample], f, indent=2, ensure_ascii=False)

print("✅ rag_eval_sample.json 已成功生成！")
