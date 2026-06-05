from __future__ import annotations

from dataclasses import dataclass


GLOBAL_FORBIDDEN_TERMS = [
    "已发送",
    "发送成功",
    "已写入CRM",
    "已创建日历",
    "已创建任务",
    "已上传商品",
    "已退款",
    "马上退款",
    "赔偿方案已确认",
    "保证SEO排名",
    "保证销量",
    "调用DataForSEO",
    "调用Firecrawl",
    "生成图片链接",
    "image_url",
    "refund_commitment",
    "compensation_offer",
    "seo_ranking_guarantee",
    "sales_guarantee",
    "ecommerce_upload_payload",
]


@dataclass(frozen=True)
class GuardrailResult:
    passed: bool
    findings: list[str]


def check_text(text: str, forbidden_outputs: list[str] | None = None) -> GuardrailResult:
    findings: list[str] = []
    terms = list(GLOBAL_FORBIDDEN_TERMS)
    if forbidden_outputs:
        terms.extend(str(item) for item in forbidden_outputs)

    lowered = text.lower()
    for term in terms:
        if term and term.lower() in lowered:
            findings.append(f"forbidden term detected: {term}")

    return GuardrailResult(passed=not findings, findings=findings)
