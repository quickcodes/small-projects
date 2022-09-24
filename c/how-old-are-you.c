#include<stdio.h>
void main()
{
    int bd=22;
    int bm=04;
    int by=2003;
    char choice;

    int day=0,month=0,year=0;



    do{
        system("cls");
        system("color f0");
        printf("\n\n\n\n");
        printf("\t\t\t\t\t Enter your birthday (DD/MM/YYYY)\n");

        printf("\t\t\t\t\t DD -> ");
        scanf("%d",&bd);

        printf("\t\t\t\t\t MM -> ");
        scanf("%d",&bm);

        printf("\t\t\t\t\t YYYY -> ");
        scanf("%d",&by);
        printf("\n");

        int cd=02;
        int cm=03;
        int cy=2021;

        printf("\n");
        printf("\t\t\t\t\t Enter current date (DD/MM/YYYY)\n");

        printf("\t\t\t\t\t DD -> ");
        scanf("%d",&cd);

        printf("\t\t\t\t\t MM -> ");
        scanf("%d",&cm);

        printf("\t\t\t\t\t YYYY -> ");
        scanf("%d",&cy);
        printf("\n");


        //calculate days
        if(cd>=bd){
            day=cd-bd;
        }
        else if(bd>cd)
        {
            day=(30+cd)-bd;
            cm = cm- 1;
        }
        else {
            printf("\t\t\t\t\t error found");
        }



        // calculate months
        if(cm>=bm)
        {
            month=cm-bm;
        }
        else if(bm>cm)
        {
            month=(12+cm)- bm;
            cy = cy- 1;
        }

        else{
            printf("\t\t\t\t\t error found");
        }


        // calculate year
        year=cy-by;


        printf("\t\t\t\t\t You live more than -->  %d Years %d Months and %d Days.\n",year,month,day);


        int Tday = day + (month*30) + (year * 365);
        int Tmonth = month + (year * 12);
        int weeks = Tday / 7;
        int hours = Tday * 24;

        printf("\n\n\n\t\t\t\t\t Your live more than -> %d+ <- years \n",year);
        printf("\t\t\t\t\t Your live more than -> %d+ <- month \n",Tmonth);
        printf("\t\t\t\t\t Your live more than -> %d+ <- weeks \n",weeks);
        printf("\t\t\t\t\t Your live more than -> %d+ <- days \n",Tday);
        printf("\t\t\t\t\t Your live more than -> %d+ <- hours \n\n\n",hours);
        printf("\n\t\t\t\t\t **********  BE THANK FULL  ********* ");
        printf("\n\t\t\t\t\t      **********  AND  *********      ");
        printf("\n\t\t\t\t\t  **********  SAY AWEOSME  *********  \n\n\n\n\t\t\t\t\t");
        system("pause");
        system("cls");
        printf("\n\n\n\n\n\n\n");
        printf("\t\t\t\t\t Press any key to play more \n\t\t\t\t\t     and 'x' for exit. ");

        choice=getch();

    }while(choice != 'x');




    getch();
}

















