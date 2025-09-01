# holbertonschool-chatgpt-introduction

## 📌 Description
Ce projet fait partie du curriculum **[C#27] Foundations v2.1 - Part 2** et a pour objectif d'apprendre à utiliser **ChatGPT** comme outil d'aide au développement.  
Il est centré sur deux axes principaux :
- **Debugging** : apprendre à diagnostiquer et corriger des erreurs dans du code existant.
- **Automation** : générer automatiquement du code, de la documentation et des tests basiques pour gagner en productivité.

---

## 🎯 Objectifs
- Identifier et corriger des erreurs de code grâce à l’IA.
- Automatiser des tâches répétitives de développement.
- Améliorer la qualité et l’efficacité du code.
- Développer des compétences de documentation et de gestion d’erreurs.

---

## ✅ Résultats attendus
- **Debugging** : être capable de repérer et corriger rapidement des bugs dans différents langages (Python, HTML/JS).
- **Automation** : savoir générer du code standard et de la documentation avec l’aide de l’IA.
- **Qualité de code** : produire du code plus robuste, lisible et maintenable.

---

## 📂 Structure du projet
Le projet est organisé dans le dossier `debugging/` :

- `factorial.py` → Correction du calcul de factorielle (itératif)  
- `print_arguments.py` → Correction pour afficher uniquement les arguments  
- `change_background.html` → Correction du bouton pour changer la couleur  
- `mines.py` → Jeu du démineur corrigé (détection de victoire ajoutée)  
- `factorial_recursive.py` → Factorielle récursive avec documentation  
- `checkbook.py` → Gestion de compte avec gestion d’erreurs utilisateurs  
- `tic.py` → Jeu de morpion corrigé et robuste  

---

## 📝 Tâches du projet
1. **Debugging - Python Factorial**  
   Corriger une implémentation de la factorielle qui bloquait en boucle infinie.

2. **Debugging - Python Arguments**  
   Afficher uniquement les arguments passés en ligne de commande, sans le nom du script.

3. **Debugging - HTML / Javascript**  
   Corriger un bouton qui ne changeait pas la couleur de fond (erreur d’ID).

4. **Debugging - Python Mines**  
   Ajouter la détection de victoire au jeu du démineur.

5. **Documentation - Python Factorial**  
   Ajouter une documentation claire sur la fonction de factorielle récursive.

6. **Error Handling - Python Checkbook**  
   Ajouter de la gestion d’erreurs pour éviter les crashs en cas de mauvaise saisie.

7. **Debugging - Tic Tac Toe Python**  
   Corriger le jeu de morpion afin qu’il gère correctement les entrées utilisateurs et la détection de victoire.

---

## 🚀 Utilisation
Exemples d’exécution :

```bash
$ ./factorial.py 5
120

$ ./print_arguments.py 1 2 3
1
2
3

$ ./checkbook.py
What would you like to do? (deposit, withdraw, balance, exit): deposit
Enter the amount to deposit: $100
Deposited $100.00
Current Balance: $100.00
