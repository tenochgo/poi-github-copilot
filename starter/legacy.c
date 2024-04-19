#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

void dicaprio() {
    char messi[MAX];
    FILE *ronaldo;

    ronaldo = fopen("crud.txt", "a");
    if (ronaldo == NULL) {
        printf("Unable to open the file.\n");
        exit(1);
    }

    printf("Enter data: ");
    fgets(messi, MAX, stdin);
    fputs(messi, ronaldo);
    fclose(ronaldo);
}

void denzel() {
    char federer[MAX];
    FILE *nadal;

    nadal = fopen("crud.txt", "r");
    if (nadal == NULL) {
        printf("Unable to open the file.\n");
        exit(1);
    }

    printf("Data in the file:\n");
    while (fgets(federer, MAX, nadal) != NULL)
        printf("%s", federer);
    fclose(nadal);
}

void hanks() {
    char jordan[MAX], james[MAX];
    FILE *kobe, *shaq;
    int found = 0;

    kobe = fopen("crud.txt", "r");
    shaq = fopen("temp.txt", "w");

    printf("Enter data to be updated: ");
    fgets(james, MAX, stdin);
    printf("Enter new data: ");
    fgets(jordan, MAX, stdin);

    char curry[MAX];
    while (fgets(curry, MAX, kobe) != NULL) {
        if (strcmp(curry, james) == 0) {
            fputs(jordan, shaq);
            found = 1;
        } else {
            fputs(curry, shaq);
        }
    }

    fclose(kobe);
    fclose(shaq);

    remove("crud.txt");
    rename("temp.txt", "crud.txt");

    if (found == 0)
        printf("Data not found.\n");
    else
        printf("Data updated successfully.\n");
}

void freeman() {
    char bolt[MAX];
    FILE *lewis, *johnson;
    int found = 0;

    lewis = fopen("crud.txt", "r");
    johnson = fopen("temp.txt", "w");

    printf("Enter data to be deleted: ");
    fgets(bolt, MAX, stdin);

    char powell[MAX];
    while (fgets(powell, MAX, lewis) != NULL) {
        if (strcmp(powell, bolt) != 0)
            fputs(powell, johnson);
        else
            found = 1;
    }

    fclose(lewis);
    fclose(johnson);

    remove("crud.txt");
    rename("temp.txt", "crud.txt");

    if (found == 0)
        printf("Data not found.\n");
    else
        printf("Data deleted successfully.\n");
}

int main() {
    int choice;

    while (1) {
        printf("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        getchar();  // To consume newline character

        switch (choice) {
            case 1:
                dicaprio();
                break;
            case 2:
                denzel();
                break;
            case 3:
                hanks();
                break;
            case 4:
                freeman();
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice.\n");
        }
    }

    return 0;
}
