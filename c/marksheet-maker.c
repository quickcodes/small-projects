#include<stdio.h>
#include<dos.h>

// ****** Note *******
// if you are not using turbo c then uncomment code given below
//#include <windows.h>    //  header file for gotoxy
// Gotoxy function
//COORD coord= {0,0}; // this is global variable
//void gotoxy(int x,int y)
//{
//    coord.X=x;
//    coord.Y=y;
//    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),coord);
//}

// Main code
void main()
{

	char* name;
	int roll_no=0;
	int c=0, iis=0, maths=0, hindi=0, os=0;
	int at=0, per=0, div=0;
	clrscr();
	gotoxy(30, 2);
	printf("Softvision College");

	gotoxy(15, 4);
	printf("Enter the name: ");
	gets(name);
	gotoxy(45, 4);
	printf("Enter roll no: ");
	scanf("%d", &roll_no);
	gotoxy(22, 8);
	printf("------  Lets make Marksheet  ------");
	gotoxy(20, 10);
	printf(" Subject  |   Total marks  |   Obtained ");
	gotoxy(20, 12);
	printf(" ______________________________________\n ");
	gotoxy(20, 14);
	printf("#    C    |       100      |");
	gotoxy(54, 14);
	scanf("%d", &c);
	gotoxy(20, 16);
	printf("#   IIS   |       100      |");
	gotoxy(54, 16);
	scanf("%d", &iis);
	gotoxy(20, 18);
	printf("#  Maths  |       100      |");
	gotoxy(54, 18);
	scanf("%d", &maths);
	gotoxy(20, 20);
	printf("#  Hindi  |       100      |");
	gotoxy(54, 20);
	scanf("%d", &hindi);
	gotoxy(20, 22);
	printf("#    OS   |       100      |");
	gotoxy(54, 22);
	scanf("%d", &os);
	gotoxy(30, 24);
	printf("PRESS ENTER FOR RESULT");
	getch();
	clrscr();
	gotoxy(30, 2);
	printf("--< RESUT >--");
	gotoxy(15, 4);
	printf("Name: ");
	gotoxy(30, 4);
	puts(name);
	gotoxy(45, 4);
	printf("Roll No:  %d", roll_no);
	gotoxy(20, 6);
	printf("   Sub    |   Marks    |   Obtained");
	gotoxy(20, 8);
	printf("---------------------------------------");
	gotoxy(20, 10);
	printf("    C     |    100     |");
	gotoxy(54, 10);
	printf("%d", c);
	gotoxy(20, 12);
	printf("   IIS    |    100     |");
	gotoxy(54, 12);
	printf("%d", iis);
	gotoxy(20, 14);
	printf("  Maths   |    100     |");
	gotoxy(54, 14);
	printf("%d", maths);
	gotoxy(20, 16);
	printf("  Hindi   |    100     |");
	gotoxy(54, 16);
	printf("%d", hindi);
	gotoxy(20, 18);
	printf("    OS    |    100     |");
	gotoxy(54, 18);
	printf("%d", os);
	gotoxy(30, 20);

	per = (maths+os+iis+hindi+c)/5;
	gotoxy(10, 22);
	printf("Percentage: %d",per);

	if(per>60 && per<=100)
	{
		 gotoxy(32, 22);
		 printf(" 1st Div ");
	}
	else if(per>40 && per<=59)
	{
		gotoxy(32, 22);
		printf(" 2nd Div ");
	}
	else if(per>0 && per<=39)
	{
		gotoxy(32, 22);
		printf(" 3rd Div ");
	}




	if(maths<40){ at++; }
	if(c<40){ at++; }
	if(iis<40){ at++; }
	if(os<40){ at++; }
	if(hindi<40){ at++; }
	//printf("%d",at);
	if(at == 0 )
	{
		gotoxy(51, 22);
		printf(" Pass ");
	}
	else if(at==1)
	{
		gotoxy(51, 22);
		printf(" Pass atkt = 1 ");
	}
	else if(at<=2)
	{
		gotoxy(51, 22);
		printf(" Year Back ");
	}
	else
	{
		gotoxy(51, 60);
		printf("at: %d Something went wrong ", at);
	}



       //printf("marks Maths- %d C- %d IIS- %d Hindi- %d OS- %d",maths,c,iis,hindi,os
	printf("\n");
	getch();
}
