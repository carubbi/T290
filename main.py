def main():
    import sys

    from graphs import Graph
    from stdlib import InStream
    from stdlib import writeln

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    writeln(G)

if __name__ == "__main__":
    main()