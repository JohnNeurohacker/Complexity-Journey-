def next_study_step(last_concept, github_activity):
    if "topology" in last_concept:
        return "Lectura: Persistent Homology in Biological Systems (arXiv:2210.135)"
    elif "phi" in github_activity[-3:]:
        return "Simulación: Criticality in Spiking Neural Nets (Nengo tutorial)"
    else:
        return "Base: Thermodynamics of Computation (S. Lloyd, 1989)"