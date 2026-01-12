# Definition der Städte im Rheinland (Längengrad, Breitengrad)
# Koordinaten sind approximiert für bessere Visualisierung

cities = {
    'Köln':       (6.9578, 50.9367),
    'Bonn':       (7.0982, 50.7374),
    'Düsseldorf': (6.7763, 51.2254),
    'Aachen':     (6.0839, 50.7753),
    'Wuppertal':  (7.1833, 51.2562),
    'Leverkusen': (6.9847, 51.0459),
    'Düren':       (6.4816, 50.8032),
    'Euskirchen': (6.7886, 50.6606),
}



# Städtenamen und Koordinaten extrahieren
city_names = list(cities.keys())
city_coords = np.array(list(cities.values()))

def create_random_route(n_cities):
    """Erstellt eine zufällige Route (Permutation)."""
    route = list(range(n_cities))
    np.random.shuffle(route)
    return np.array(route)

print("Städte im Rheinland:")
print("-" * 40)
for i, (name, coords) in enumerate(cities.items()):
    print(f"{i}: {name:12} → ({coords[0]:.4f}°, {coords[1]:.4f}°)")
