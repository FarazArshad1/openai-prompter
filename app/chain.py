from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

with open('openai.txt', encoding='utf-8') as f:
    text = f.read()

template = """{text}
----------------------------------
Based on the above instructions, help me write a good prompt Template.

This Templates should be in python f-string. It can take in any number od variables delepending on my objective.

return your answer in the following format:

```
prompt
...
```
This is my objective

{objective}

"""


prompt = PromptTemplate.from_template(template)
prompt = prompt.partial(text = text)
chain = prompt | ChatOpenAI() | StrOutputParser()
