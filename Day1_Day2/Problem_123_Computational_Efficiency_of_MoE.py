# Calculate the computational cost savings of an MoE layer compared to a dense layer, 
# as discussed in the paper 'Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts 
# Layer.' Given the number of experts, sparsity (number of active experts), and input/output dimensions,
# compute the floating-point operations (FLOPs) for both and determine the savings percentage.

#concept :

# When all the layers are active, the computational cost of the dense layer FLOPs is given by:
# FLOPs_dense = n_experts * d_in * d_out
# When only a subset of the experts are active, then the computational cost of the MOE layer FLOPs is given by :
# FLOPs_MoE = k_active * d_in * d_out

def compute_efficiency(n_experts, k_active, d_in, d_out):
    """
    Calculate computational savings of MoE vs. dense layer.

    Args:
        n_experts: Total number of experts
        k_active: Number of active experts (sparsity)
        d_in: Input dimension
        d_out: Output dimension

    Returns:
        Percentage savings in FLOPs
    """
    FLOPs_dense = n_experts * d_in * d_out
    FLOPs_MoE = k_active * d_in * d_out

    savings_percentage = ((FLOPs_dense - FLOPs_MoE) / FLOPs_dense) * 100
    savings_percentage = round(savings_percentage, 4)  # Round to two decimal places
    
    return savings_percentage 