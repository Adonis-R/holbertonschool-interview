# Projet Sandpiles

Le projet *Sandpiles* consiste en la simulation de l'algorithme des piles de sable. L'objectif est de créer une série de fonctions permettant de manipuler des grilles de sable et de gérer des "chaos" dans ces piles.

## Contraintes

- Tous les programmes et fonctions seront compilés avec `gcc 4.8.4` en utilisant les options suivantes :
  - `-Wall -Werror -Wextra -pedantic`
  
- Tous les fichiers doivent se terminer par une nouvelle ligne.

- Le code doit respecter le style **Betty**. Le code sera vérifié avec les scripts `betty-style.pl` et `betty-doc.pl`.

## Règles du code

- **Pas de variables globales**.
- **Pas plus de 5 fonctions par fichier**.
- Les prototypes de toutes les fonctions doivent être inclus dans un fichier d'en-tête nommé `sandpiles.h`. Ce fichier doit être également poussé sur le dépôt.
- Tous les fichiers d'en-tête doivent être protégés par des *include guards*.
- Vous pouvez utiliser le fichier `main.c` fourni dans les exemples pour tester vos fonctions, mais ce fichier ne doit pas être envoyé dans votre dépôt. Les fichiers `main.c` fournis pour la compilation peuvent être différents de ceux montrés dans les exemples.

## Fichiers

- `sandpiles.h` : fichier d'en-tête contenant les prototypes des fonctions.
- `0-sandpiles.c` : fichier contenant les fonctions principales de l'algorithme.
- `0-main.c` : fichier pour tester vos fonctions. Ce fichier contient le point d'entrée du programme.

## Compilation

Pour compiler les fichiers sources, utilisez la commande suivante :

```bash
gcc -Wall -Wextra -Werror -pedantic 0-sandpiles.c 0-main.c -o sandpiles
```

Pour exécuter :
```bash
./sandpiles
```