def tax_simulator(scenarios):
    return [calculate_hifo(s) - calculate_fifo(s) for s in scenarios]
