#include "slide_line.h"

/**
 * slide_left - Fait glisser et fusionne les nombres vers la gauche
 * @line: Pointeur vers le tableau d'entiers
 * @size: Nombre d'éléments dans @line
 */
void slide_left(int *line, size_t size)
{
	size_t i, j = 0;

	/* Déplacer tous les éléments non nuls vers la gauche */
	for (i = 0; i < size; i++)
		if (line[i] != 0)
			line[j++] = line[i];

	/* Remplir le reste avec des zéros */
	while (j < size)
		line[j++] = 0;

	/* Fusionner les éléments identiques */
	for (i = 0; i < size - 1; i++)
	{
		if (line[i] != 0 && line[i] == line[i + 1])
		{
			line[i] *= 2;
			line[i + 1] = 0;
		}
	}

	/* Réorganiser à nouveau les éléments après fusion */
	j = 0;
	for (i = 0; i < size; i++)
		if (line[i] != 0)
			line[j++] = line[i];

	while (j < size)
		line[j++] = 0;
}

/**
 * slide_right - Fait glisser et fusionne les nombres vers la droite
 * @line: Pointeur vers le tableau d'entiers
 * @size: Nombre d'éléments dans @line
 */
void slide_right(int *line, size_t size)
{
	int i, j = size - 1;

	/* Déplacer tous les éléments non nuls vers la droite */
	for (i = size - 1; i >= 0; i--)
		if (line[i] != 0)
			line[j--] = line[i];

	/* Remplir le reste avec des zéros */
	while (j >= 0)
		line[j--] = 0;

	/* Fusionner les éléments identiques */
	for (i = size - 1; i > 0; i--)
	{
		if (line[i] != 0 && line[i] == line[i - 1])
		{
			line[i] *= 2;
			line[i - 1] = 0;
		}
	}

	/* Réorganiser à nouveau les éléments après fusion */
	j = size - 1;
	for (i = size - 1; i >= 0; i--)
		if (line[i] != 0)
			line[j--] = line[i];

	while (j >= 0)
		line[j--] = 0;
}

/**
 * slide_line - Gère le déplacement des nombres dans le tableau
 * @line: Pointeur vers le tableau d'entiers
 * @size: Nombre d'éléments dans @line
 * @direction: Direction du mouvement (SLIDE_LEFT ou SLIDE_RIGHT)
 *
 * Return: 1 en cas de succès, 0 en cas d'échec
 */
int slide_line(int *line, size_t size, int direction)
{
	if (direction == SLIDE_LEFT)
		slide_left(line, size);
	else if (direction == SLIDE_RIGHT)
		slide_right(line, size);
	else
		return (0);

	return (1);
}
