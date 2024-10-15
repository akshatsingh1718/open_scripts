from langchain_core.prompts import PromptTemplate
from .prompts import LK_CONTRIBUTION_PROMPT
from .llm import langchain_response


def contrib_response(
    heading: str, subheading: str = "<N/A>", reference_text: str = "<N/A>"
):
    prompt = PromptTemplate.from_template(LK_CONTRIBUTION_PROMPT)
    formatted_input = prompt.format(
        heading=heading, subheading=subheading, reference_text=reference_text
    )
    print("================= " + formatted_input)
    print(formatted_input)
    return dict(response=langchain_response(formatted_input), llm_input=formatted_input)
