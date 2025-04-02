#include <stdlib.h>
#include <stdio.h>
#include "sandpiles.h"


void print_grid(int grid[3][3])
{
    int i, j;

    printf("=\n");

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

void add_grid(int grid1[3][3], int grid2[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            grid1[i][j] += grid2[i][j];
        }
    }
}

void sandpiles_sum(int grid1[3][3], int grid2[3][3]) 
{
    int i, j;

    add_grid(grid1, grid2);
    while (grid1[0][0] > 3 || grid1[0][1] > 3 || grid1[0][2] > 3 ||
           grid1[1][0] > 3 || grid1[1][1] > 3 || grid1[1][2] > 3 ||
           grid1[2][0] > 3 || grid1[2][1] > 3 || grid1[2][2] > 3)
    {
        int temp[3][3] = {0};
        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {
                if (grid1[i][j] > 3)
                {
                    temp[i][j] -= 4;
                    if (i > 0)
                        temp[i - 1][j]++;
                    if (i < 2)
                        temp[i + 1][j]++;
                    if (j > 0)
                        temp[i][j - 1]++;
                    if (j < 2)
                        temp[i][j + 1]++;

                }

            }
            
        }
        add_grid(grid1, temp);
        print_grid(grid1);

    }
}