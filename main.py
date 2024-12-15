import sys
import queries.load_data as load_data
import queries.search_quotes as search_quotes


def main():
    if len(sys.argv) != 2:
        print("Incorrect number of arguments")
        print("Example: <python main.py load>")
        print("Example: <python main.py search>")
    
    action = sys.argv[1].lower().strip()
    if action == "search":
        search_quotes.search_quotes()
    elif action == "load":
        load_data.load_authors()
        load_data.load_quotes()
    else:
        print("Unknown action")
        print("Available actions: search, load")
    

if __name__ == "__main__":
    main()
