from statsmodels.stats.power import FTestAnovaPower

# Initialisieren des Power-Analyse-Objekts
anova_power = FTestAnovaPower()

# Effektgröße (Cohen's f für kleine Effektgröße d=0.2)
effect_size = 0.2  

# Alpha-Wert
alpha = 0.05  

# Gruppengrößen
group_sizes = [5, 33, 20, 5, 6]  # Hier die Gruppengrößen anpassen
groups_total = 0

# Berechnung der Power für jede Gruppe
powers = []
for n in group_sizes:
    power = anova_power.power(effect_size=effect_size, nobs=n, k_groups=len(group_sizes), alpha=alpha)
    powers.append(power)

# Ausgabe der Power-Werte für jede Gruppe
for i, power in enumerate(powers):
    print(f"Power für Gruppe {i+1} (Größe {group_sizes[i]}): {power:.4f}")
