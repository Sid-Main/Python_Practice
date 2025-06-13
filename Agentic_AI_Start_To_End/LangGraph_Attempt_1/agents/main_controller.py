from state.schema import CodeState
from utils.llm import get_llm

llm = get_llm()

def select_code_to_convert(state: CodeState) -> CodeState:
    """
    Selects a part of the full code to convert.

    Parameters:
    - state (CodeState): Current workflow state

    Returns:
    - Updated state with 'part_to_convert' key
    """
    prompt = f"""You are the main controller agent.
Given this full code, select a part (e.g. a function) to be converted.
Return only the selected code segment.

Full code:
{state['full_code']}
"""
    response = llm.invoke(prompt).content
    print("MainController selected code segment:\n", response)
    return {**state, "part_to_convert": response}
