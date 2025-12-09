import sys

def solve():
    """
    Handles a single test case for the interactive problem.
    """
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
    except (IOError, ValueError):
        return

    # --- Helper Functions for Interaction ---
    def ask_query(start_node: int, node_set: list[int]) -> int:
        """
        Formats and sends a query to the judge, then reads the response.
        Exits if an error (-1) is received.
        """
        # Format: "? x k s1 s2 ... sk"
        query_parts = ["?", str(start_node), str(len(node_set))]
        query_parts.extend(map(str, node_set))
        query_str = " ".join(query_parts)
        
        print(query_str, flush=True)
        
        try:
            response = int(sys.stdin.readline())
        except (IOError, ValueError):
            sys.exit() # Exit on read error
            
        if response == -1:
            # Error case indicates an invalid query or other problem.
            sys.exit()
            
        return response

    def give_answer(path: list[int]):
        """
        Formats and sends the final answer to the judge.
        """
        # Format: "! k v1 v2 ... vk"
        answer_parts = ["!", str(len(path))]
        answer_parts.extend(map(str, path))
        answer_str = " ".join(answer_parts)
        
        print(answer_str, flush=True)

    #Your Code 
    l=[0]*(n+1)
    a=list(range(1,n+1))
    for i in range(1,n+1):
        l[i]=ask_query(i,a)

    s=sorted(a,key=lambda n:l[n],reverse=True)    
    p=[]

    for i in s:
        if len(p)==0:
            p.append(i)
        else:   
            st= p[0]
            cr= len(p)
            t = p+[i]
            r= ask_query(st,t)
            if r == cr + 1:
                p.append(i)

    give_answer(p)


def main():
    try:
        num_test_cases_str = sys.stdin.readline()
        if not num_test_cases_str:
            return
        num_test_cases = int(num_test_cases_str)
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        # Handles cases with empty input or malformed test case count.
        return

if __name__ == "__main__":
    main()