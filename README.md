
---

## ✨ README.md 

````markdown
# 📰 Korean News QA Fine-tuned LLaMA3

이 프로젝트는 **NAVER 뉴스 기사 본문**을 크롤링한 뒤,  
기사 내용을 기반으로 **QA 페어(QUESTION, ANSWER)** 를 자동 생성하여  
Meta LLaMA3-8B 모델을 파인튜닝한 결과물입니다.  

뉴스 기사의 **full text**를 받아와서 문맥 단위로 잘라낸 뒤,  
LLM을 이용해 핵심 정보를 묻고 답하는 형식의 QA 데이터셋을 구축했습니다.

---

## 📂 Dataset

- Hugging Face: [HaGPT/my-news-qa-dataset](https://huggingface.co/datasets/HaGPT/my-news-qa-dataset)  
- 로컬 JSONL: `qa_output.jsonl`  
- 예시:
```json
{"QUESTION": "ETF는 한국전력을 편입했나요?", "ANSWER": "아니요. 해외 원전 수출 모멘텀과의 연계를 강화하려는 구성입니다."}
{"QUESTION": "AI 페스타 2025는 언제 개막하나요?", "ANSWER": "행사는 30일에 개막합니다."}
````

> 데이터 준비:
>
> 1. 뉴스 기사 크롤링 (NAVER)
> 2. 기사 본문 추출 및 클린업
> 3. LLM 기반 QA 자동 생성 → JSONL 변환

---

## ⚙️ Training

* 프레임워크: [Unsloth](https://github.com/unslothai/unsloth) + Hugging Face Transformers
* 베이스 모델: `meta-llama/Meta-Llama-3-8B`
* 파인튜닝 방식: LoRA (QLoRA, 4bit)
* Epochs: 3 (소규모 실험)

모델은 로컬에 저장한 후 Hugging Face Hub로 업로드하여 재사용 가능하게 했습니다.

---

## 🚀 Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("HaGPT/my-news-qa-model")
tokenizer = AutoTokenizer.from_pretrained("HaGPT/my-news-qa-model")

inputs = tokenizer("AI 챌린지 2025 본선 참가팀들의 개발 기간은?", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 📊 Example Outputs

* **Q:** `"AI 페스타 2025는 언제 개막하나요?"`

* **A:** `"행사는 30일에 개막합니다."`

* **Q:** `"연구팀이 개발한 AI 모델은 무엇을 어떤 주기로 추정합니까?"`

* **A:** `"대기 중 암모니아(NH3) 농도를 하루 단위로 추정하는 모델입니다."`

---

## ⚠️ Limitations

* 실제 문장과 llm 답변 간의 의미적 유사도를 검증하는 단계는 아직 구현 X
* 데이터셋 규모가 작아 일반화 성능에 제약이 있음
* 긴 기사 요약 능력은 추가 연구 필요