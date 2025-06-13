from state.schema import CodeState
from utils.llm import get_llm

llm = get_llm()

def convert_code(state: CodeState) -> CodeState:
    """
    Converts the selected code segment.

    Parameters:
    - state (CodeState): Current workflow state

    Returns:
    - Updated state with 'converted_code' and updated 'full_code'
    """
    prompt = f"""You are the converter agent.
Refactor or optimize this code segment.
Return only the updated code.

Code segment:
{state['part_to_convert']}
"""
    new_code = llm.invoke(prompt).content
    print("Converter output:\n", new_code)

    updated_full_code = state["full_code"].replace(state["part_to_convert"], new_code)
    return {**state, "converted_code": new_code, "full_code": updated_full_code}
