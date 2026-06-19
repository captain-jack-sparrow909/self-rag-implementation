from graph.graph import graph

def main():
    print("Hello from c-rag!")
    print(graph.invoke(input={"question": "what is agent memory?"}))


if __name__ == "__main__":
    main()
