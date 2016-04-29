
stable_amount = int(input().strip()) // 4
gene_str = input().strip()

def get_genes_to_remove(gene_str):
    freq = {"A":0, "T":0, "C":0, "G":0}
    for g in gene_str:
        freq[g] += 1

    return dict([(l,f-stable_amount) for l,f in freq.items() if f > stable_amount])

def is_valid(genes_to_remove):
    for l,f in genes_to_remove.items():
        if f > 0:
            return False
    return True

def add_gene(idx, gene_str, extra):
    if gene_str[idx] in extra:
        extra[gene_str[idx]] += 1
    return extra

def remove_gene(idx, gene_str, extra):
    if gene_str[idx] in extra:
        extra[gene_str[idx]] -= 1
    return extra

def increment_end(end_idx, gene_str, genes_to_remove):
    valid_sub = False
    while valid_sub != True and end_idx < len(gene_str)-1:
        end_idx += 1
        genes_to_remove = remove_gene(end_idx, gene_str, genes_to_remove)
        valid_sub = is_valid(genes_to_remove)
    return end_idx

def increment_start(start_idx, gene_str, genes_to_remove):
    valid_sub = True
    while valid_sub:
        genes_to_remove = add_gene(start_idx, gene_str, genes_to_remove)
        valid_sub = is_valid(genes_to_remove)
        start_idx += 1
    return start_idx

def update_solution(new_solution, curr_solution):
    if new_solution < curr_solution:
        return new_solution
    else:
        return curr_solution


def make_steady(gene_str):
    genes_to_remove = get_genes_to_remove(gene_str)
    start_idx = 0
    end_idx = 0
    
    valid_sub = is_valid(genes_to_remove)
    if valid_sub:
        return 0
    
    curr_solution = len(gene_str)
    genes_to_remove = remove_gene(start_idx, gene_str, genes_to_remove)
    valid_sub = is_valid(genes_to_remove)

    while end_idx < len(gene_str)-1:  
        end_idx = increment_end(end_idx, gene_str, genes_to_remove)
        curr_solution = update_solution(end_idx - start_idx + 1, curr_solution)

        start_idx = increment_start(start_idx, gene_str, genes_to_remove) 
        curr_solution = update_solution(end_idx - start_idx + 2, curr_solution)    
    
    valid_sub = is_valid(genes_to_remove)
    while valid_sub:
        start_idx = increment_start(start_idx, gene_str, genes_to_remove) 
        curr_solution = update_solution(end_idx - start_idx + 2, curr_solution) 

    return curr_solution
    
print(make_steady(gene_str))

