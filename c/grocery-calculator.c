#include<stdio.h>
void main()
{
    system("color f0");
    int sum = 0;
    printf("\n\n\n\t\tWELCOME IN OUR GROCERY SHOP\n\n");
    while(1)
    {
        char input[5];
        char operation = '+';
        int num;
        printf("\n\t\tEnter the price of item or any alphabet to see Total Bill\n\t\t-> ");
        if(scanf("%s", input))
        {
            fflush(stdin);
            num = atoi(input);    // typecaste string to int
            if(num == 0)
            {
                break;
            }
            else
            {
                //printf("%d\n",num);
                printf("\n\t\tEnter the operation ( '+'   '-'   '*'   '/' )\n\t\t-> ");
                scanf("%c", &operation);
                fflush(stdin);
                switch (operation)
                {
                case '+':
                    sum = sum + num;
                    break;
                case '-':
                    sum = sum - num;
                    break;
                case '*':
                    sum = sum * num;
                    break;
                case '/':
                    sum = sum / num;
                    break;
                default:
                    printf("\n\t\tPlease enter valid operation\n");
                }
                printf("\n\t\tCurrent Bill is: %d\n",sum);
            }
        }
        else
        {
            printf("\n\t\tSomething wrong");
        }
        system("cls");

    }
    printf("\n\t\tYou Total bill is: %d ",sum);
    printf("\n\n\n");
}






