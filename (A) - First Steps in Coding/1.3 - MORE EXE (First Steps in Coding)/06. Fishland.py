price_per_kg_mackerel = float(input())
price_per_kg_sprat = float(input())
quantity_bonito_in_kg = float(input())
quantity_scad_in_kg = float(input())
quantity_mussels_in_kg = int(input())
price_per_kg_bonito = price_per_kg_mackerel * 1.60
price_per_kg_scad = price_per_kg_sprat * 1.80
price_per_kg_mussels = 7.50
full_price_per_bonito = quantity_bonito_in_kg * price_per_kg_bonito
full_price_per_scad = quantity_scad_in_kg * price_per_kg_scad
full_price_per_mussels = quantity_mussels_in_kg * price_per_kg_mussels
final_price = full_price_per_bonito + full_price_per_scad + full_price_per_mussels
print(f"{final_price:.2f}")
