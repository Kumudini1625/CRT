def number_triangle(n: int) -> str:
    s=""
    for i in range(1,n+1):
        s+="".join(str(x) for x in range(1,i+1))+"\n"
    return s.strip()
if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))
