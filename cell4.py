# Visualisierung: Streudiagramm der Städte
fig, ax = plt.subplots(figsize=(10, 8))

# Städte als Punkte plotten
ax.scatter(city_coords[:, 0], city_coords[:, 1], 
           s=200, c='#2E86AB', edgecolors='white', linewidths=2, zorder=5)

# Städtenamen beschriften
for i, name in enumerate(city_names):
    ax.annotate(name, (city_coords[i, 0], city_coords[i, 1]),
                xytext=(10, 10), textcoords='offset points',
                fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.7))

ax.set_xlabel('Längengrad (°)', fontsize=12)
ax.set_ylabel('Breitengrad (°)', fontsize=12)
ax.set_title('6 Städte im Rheinland - Das TSP-Problem', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

# Achsenlimits anpassen
ax.set_xlim(5.8, 7.5)
ax.set_ylim(50.5, 51.5)

plt.tight_layout()
save_figure(fig, '01_staedte_streudiagramm.png')
plt.show()

print(f"\n→ Anzahl möglicher Rundreisen: {math.factorial(len(cities)-1)//2} (bei {len(cities)} Städten)")
