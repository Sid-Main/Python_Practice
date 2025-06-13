from langgraph.graph import StateGraph, END
from state.schema import CodeState
from agents.main_controller import select_code_to_convert
from agents.converter import convert_code
from agents.qa import evaluate_code

def check_passed(state: CodeState) -> str:
    """
    Conditional function to decide next graph node based on QA result.

    Parameters:
    - state (CodeState)

    Returns:
    - 'end' if tests passed, else 'convert_again'
    """
    return "end" if state.get("passed_tests") else "convert_again"

def build_graph():
    """
    Constructs the LangGraph workflow graph.

    Workflow:
    main_controller -> converter -> qa
    QA success -> END
    QA failure -> converter (loop)

    Returns:
    - compiled StateGraph object
    """
    workflow = StateGraph(CodeState)

    # workflow.add_node("main_controller", select_code_to_convert)
    workflow.add_node("converter", convert_code)
    workflow.add_node("qa", evaluate_code)
    workflow.set_entry_point("converter")

    # workflow.set_entry_point("main_controller")

    # workflow.add_edge("main_controller", "converter")
    workflow.add_edge("converter", "qa")

    workflow.add_conditional_edges("qa", check_passed, {
        "end": END,
        "convert_again": "converter"
    })

 
    return workflow.compile()
