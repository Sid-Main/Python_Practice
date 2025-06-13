from graph.workflow import build_graph
from state.schema import CodeState

if __name__ == "__main__":
    # Sample Python code to improve
    sample_code = """
import requests
from bs4 import BeautifulSoup

def scrape_product_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find("h1").text
    price = soup.find("span", class_="price").text
    return {"name": name, "price": price}

def get_multiple_products(urls):
    return [scrape_product_data(url) for url in urls]

def save_to_file(data, filename="products.json"):
    import json
    with open(filename, "w") as f:
        json.dump(data, f)
"""
    part_to_update= """
def scrape_product_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find("h1").text
    price = soup.find("span", class_="price").text
    return {"name": name, "price": price}
"""
    graph = build_graph()
    # graph.draw().render("langgraph_workflow", format="png", view=True)

    # Initial state dictionary for LangGraph
    # initial_state: CodeState = {
    #     "full_code": sample_code,
    #     "part_to_convert": None,
    #     "converted_code": None,
    #     "passed_tests": None,
    # }
    initial_state: CodeState = {
    "full_code": sample_code,
    "part_to_convert": part_to_update,
    "converted_code": None,
    "passed_tests": None,
}
    ascii_diagram = graph.get_graph().draw_ascii()
    print(ascii_diagram)



    # Run the LangGraph workflow
    result = graph.invoke(initial_state)

    print("\nFinal Full Code:\n", result["full_code"])
