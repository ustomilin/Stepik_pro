from collections import Counter

def print_bar_chart(data, mark):
    text = Counter(data)
    m = len(max(text.keys(), key = len))
    for i, j in sorted(text.items(), key = lambda x: x[1], reverse=True):
        print(f'{i.ljust(m)} |{mark*j}')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')