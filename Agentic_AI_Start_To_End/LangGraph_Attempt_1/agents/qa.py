from state.schema import CodeState
from utils.llm import get_llm

llm = get_llm()

def evaluate_code(state: CodeState) -> CodeState:
    """
    Evaluates the full code by generating and verifying test cases.

    Parameters:
    - state (CodeState): Current workflow state

    Returns:
    - Updated state with 'passed_tests' as True or False
    """
    prompt = f"""You are the QA agent.
Analyze the following code and generate test cases.
If the code works correctly, reply with "PASS".
If not, reply with "FAIL" and explanation.

Full code:
{state['full_code']}
"""
    result = llm.invoke(prompt).content
    print("🧪 QA verdict:\n", result)

    passed = "PASS" in result.upper()
    return {**state, "passed_tests": passed}
