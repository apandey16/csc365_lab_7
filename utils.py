def header():
    print("==============================================")
    print("Dijkstra Inn: The Best Inn in Town")
    print("==============================================\n")


def executeQuery(connector, query):
    connector.execute(query)
    return connector.fetchall()