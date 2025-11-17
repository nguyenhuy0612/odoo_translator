#!/usr/bin/env python3
"""Test clean fastText-only version"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from po_translator.utils.language_clean import detect_language_details

# Same 44 test cases from original test
test_cases = [
    ("Facture", "fr", "French invoice"),
    ("Factura", "es", "Spanish invoice"),
    ("Bon de commande", "fr", "French purchase order"),
    ("Orden de compra", "es", "Spanish purchase order"),
    ("Client", "fr", "French customer"),
    ("Cliente", "es", "Spanish customer"),
    ("Livraison", "fr", "French delivery"),
    ("Entrega", "es", "Spanish delivery"),
    ("Veuillez confirmer la commande", "fr", "French command sentence"),
    ("Please confirm the order", "en", "English command sentence"),
    ("Le montant total est calculé automatiquement", "fr", "French calculation"),
    ("The total amount is calculated automatically", "en", "English calculation"),
    ("Por favor confirme el pedido", "es", "Spanish please confirm"),
    ("Please confirm the order", "en", "English please confirm"),
    ("El importe total se calcula automáticamente", "es", "Spanish auto calculation"),
    ("The total amount is calculated automatically", "en", "English auto calculation"),
    ("Créer une nouvelle facture", "fr", "French create invoice"),
    ("Creare una nuova fattura", "it", "Italian create invoice"),
    ("Partenaire commercial", "fr", "French business partner"),
    ("Partner commerciale", "it", "Italian business partner"),
    ("Buenos días", "es", "Spanish good morning"),
    ("Bom dia", "pt", "Portuguese good morning"),
    ("Confirmar pedido", "es", "Spanish confirm order"),
    ("Confirmar pedido", "pt", "Portuguese confirm order - same spelling!"),
    ("Article", "fr", "French article (product)"),
    ("Article", "en", "English article"),
    ("Total", "en", "English total"),
    ("Total", "es", "Spanish total"),
    ("Date", "en", "English date"),
    ("Date", "fr", "French date"),
    ("Sale Order", "en", "English sale order"),
    ("Pedido de venta", "es", "Spanish sale order"),
    ("Commande de vente", "fr", "French sale order"),
    ("Stock Picking", "en", "English stock picking"),
    ("Albarán", "es", "Spanish delivery note"),
    ("Bon de livraison", "fr", "French delivery note"),
    ("Créer une Sale Order", "fr", "Mostly French with English term"),
    ("Create a nouvelle facture", "en", "Mostly English with French term"),
    ("Voulez-vous vraiment supprimer cet enregistrement?", "fr", "French delete confirmation"),
    ("¿Está seguro de que desea eliminar este registro?", "es", "Spanish delete confirmation"),
    ("Are you sure you want to delete this record?", "en", "English delete confirmation"),
    ("Facture N° %(number)s du %(date)s", "fr", "French with placeholders"),
    ("Invoice No. %(number)s from %(date)s", "en", "English with placeholders"),
    ("Factura Nº %(number)s del %(date)s", "es", "Spanish with placeholders"),
]

print("="*80)
print("CLEAN FASTTEXT-ONLY ACCURACY TEST")  
print("="*80)
print(f"\nTesting {len(test_cases)} cases...\n")

correct = 0
for text, expected, desc in test_cases:
    detected, conf = detect_language_details(text)
    if detected == expected:
        correct += 1
        print(f"✅ {text[:40]:40} → {detected} ({conf:.2f})")
    else:
        print(f"❌ {text[:40]:40} → {detected} ({conf:.2f}) [expected: {expected}]")

accuracy = correct / len(test_cases) * 100

print("\n" + "="*80)
print(f"FINAL RESULT: {correct}/{len(test_cases)} correct ({accuracy:.1f}%)")
print("="*80)

if accuracy >= 85:
    print("🌟 EXCELLENT - Production ready!")
elif accuracy >= 75:
    print("✅ VERY GOOD - Solid performance")
elif accuracy >= 65:
    print("👍 GOOD - Acceptable for most use cases")
else:
    print("⚠️  NEEDS IMPROVEMENT")

