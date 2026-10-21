from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

# class review(BaseModel):
#     key_themes: list[str] = Field(description="write down all the key themes discussed in the review")
#     summary: str = Field(description="a brief summary of the review")
#     sentiment: Literal["pos","neg"] = Field(description="return sentiment of review")
#     pros: Optional[list[str]] = Field(default=None, description="write down the all the pros inside the list")
#     cons: Optional[list[str]] = Field(default=None, description="write down the all the cons inside the list")

# here we can put the json schema rather then the basemodel

# schema
json_schema = {
  "title": "review",
  "type": "object",
  "properties": {
    "key_themes": {
      "items": {
        "type": "string"
      },
      "description": "write down all the key themes discussed in the review",
      "type": "array"
    },
    "summary": {
      "description": "a brief summary of the review",
      "type": "string"
    },
    "sentiment": {
      "description": "return sentiment of review",
      "enum": [
        "pos",
        "neg"
      ],
      "type": "string"
    },
    "pros": {
    #   "default": null,
      "description": "write down the all the pros inside the list",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "cons": {
    #   "default": null,
      "description": "write down the all the cons inside the list",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    }
  },
  "required": [
    "key_themes",
    "summary",
    "sentiment"
  ]
}

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    # max_tokens=500
)


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
- Insanely powerful processor (great for gaming and productivity)
- Stunning 200MP camera with incredible zoom capabilities
- Long battery life with fast charging
- S-Pen support is unique and useful
Cons:
- Bulky and heavy—not great for one-handed use
- Bloatware still exists in One UI
- Expensive compared to competitors""")

# print(result)
print(result['summary'])

