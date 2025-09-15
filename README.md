
---

## 📰 Korean News QA with Fine-tuned LLaMA3

````markdown
# 📰 Korean News QA Fine-tuned LLaMA3

> **NAVER 뉴스 기사 기반 QA 데이터셋을 구축하고, Meta LLaMA3-8B를 파인튜닝한 프로젝트**  
> "뉴스 → QA → 파인튜닝 → 질의응답" 전체 파이프라인 구현 🚀  

---

## 🔎 프로젝트 개요
- **뉴스 기사 크롤링** → 본문 정제  
- **QA 자동 생성** (LLM 기반) → JSONL 변환  
- **LoRA 파인튜닝** → `Meta-Llama-3-8B`  
- **Hugging Face 모델 업로드** → 누구나 재사용 가능  

---

## 📂 데이터셋
- Hugging Face: [HaGPT/my-news-qa-dataset](https://huggingface.co/datasets/HaGPT/my-news-qa-dataset)  
- 로컬 JSONL: `qa_output.jsonl`

✅ 예시:
```json
{"QUESTION": "ETF는 한국전력을 편입했나요?", "ANSWER": "아니요. 해외 원전 수출 모멘텀과의 연계를 강화하려는 구성입니다."}
{"QUESTION": "AI 페스타 2025는 언제 개막하나요?", "ANSWER": "행사는 30일에 개막합니다."}
````

---

## ⚙️ 파인튜닝

* **프레임워크:** [Unsloth](https://github.com/unslothai/unsloth) + Hugging Face Transformers
* **베이스 모델:** `meta-llama/Meta-Llama-3-8B`
* **방법:** LoRA (QLoRA, 4bit)
* **Epochs:** 3

---

## 🚀 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("HaGPT/my-news-qa-model")
tokenizer = AutoTokenizer.from_pretrained("HaGPT/my-news-qa-model")

inputs = tokenizer("AI 챌린지 2025 본선 참가팀들의 개발 기간은?", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 📊 데모 결과

**Q:** `"AI 페스타 2025는 언제 개막하나요?"`
**A:** `"행사는 30일에 개막합니다."`

**Q:** `"연구팀이 개발한 AI 모델은 무엇을 어떤 주기로 추정합니까?"`
**A:** `"대기 중 암모니아(NH3) 농도를 하루 단위로 추정하는 모델입니다."`

---

## ⚠️ 한계점

* 문장-답변 **의미 일치 검증 단계 미구현**
* 데이터셋 규모가 작아 **일반화 성능 제한**
* 긴 기사 요약 능력은 추가 연구 필요

---

## ✅ 앞으로의 방향

* **검증 모듈 추가** (semantic similarity check)
* **대규모 데이터셋 확대**
* **요약 + QA 혼합 모델 연구**

