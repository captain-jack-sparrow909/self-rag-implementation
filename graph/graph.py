from dotenv import load_dotenv
from graph.const import GENERATE, GRADE_DOCUMENTS, WEB_SEARCH, RETRIEVE
from langgraph.graph import END, StateGraph
from graph.nodes import generate, grade_documents, retrive, web_search
from graph.state import GraphState

load_dotenv()

def decide_to_generate(state: GraphState):
    print("---Assess the Documents--")
    if state['web_search']:
        return WEB_SEARCH
    else :
        return GENERATE


workflow = StateGraph(GraphState)
workflow.add_node(GENERATE, generate)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(WEB_SEARCH, web_search)
workflow.add_node(RETRIEVE, retrive)

workflow.set_entry_point(RETRIEVE)

workflow.add_conditional_edges(GRADE_DOCUMENTS, decide_to_generate, {
    WEB_SEARCH: WEB_SEARCH, 
    GENERATE: GENERATE
})

workflow.add_edge(RETRIEVE, GENERATE)
workflow.add_edge(WEB_SEARCH, GENERATE)

workflow.add_edge(GENERATE, END)

graph = workflow.compile()
