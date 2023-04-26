[17:07] Thambi, Amal



// Single-line comment




/* This program will do so and so implementations*/





/*




    Introduction

    Compilation in Windows & Linux

    Compilation Process in Linux

    Structure of a C Program

    Comments

    Datatypes

        - Primitive/Basic(int,char,float,double)

        - Derived (Arrays, Pointers)

        - User-Defined(Structure, Union, Typedef, Enum)  

    Print Output to Console - printf

    Take Input from User - scanf

    Control Statements

        if

        if-else

        else if

        switch => Heavily used in menu driven programs

    Loop

        do..while

        while

        for

    Operator & Precedence

    Functions

    Structures

    Pointers

    Memory Allocation




    DS




*/




#include<stdio.h>

#define PI 3.14





int tax(int ctc);

void table_dowhile();




void main()

{




// table_dowhile();

// table_while();

table_for();

}





void table_dowhile()

{

    int counter=1;

    do

    {

        printf("7 * %d => %d \n",counter,7*counter);

        counter=counter+1;

    } while (counter<=10);

   

}




void table_while()

{

    int counter=1;




    while (counter<=10)

    {

        printf("7 * %d => %d \n",counter,7*counter);

        counter=counter+1;

    }

   

}




void table_for()

{

    for (int i = 1; i <= 10; i++)

    {

        printf("7 * %d => %d \n",i,7*i);

    }

   

}




int tax(int ctc)

{

    return ctc*0.1;

}






