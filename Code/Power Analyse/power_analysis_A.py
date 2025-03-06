from statsmodels.stats.power import FTestAnovaPower

# Initialisieren des Power-Analyse-Objekts
anova_power = FTestAnovaPower()

# Werte für die Berechnung 
effect_size = 0.2   # kleine Effektgröße für psychologische Untersuchung
alpha = 0.05  # Signifikanznivea, Standardwert von 0.05
group_sizes = [5, 33, 20, 5, 6] # Gruppengrößen
#group_toal = 69 #Gesamt

# Berechnung der Power für jede Gruppe
powers = []
for n in group_sizes:
    power = anova_power.power(effect_size=effect_size, nobs=n, k_groups=len(group_sizes), alpha=alpha)
    powers.append(power)

# Ausgabe der statistischen Kraft für jede Gruppe
for i, power in enumerate(powers):
    print(f"Statistische Kraft für Gruppe {i+1} (Größe {group_sizes[i]}): {power:.4f}")
