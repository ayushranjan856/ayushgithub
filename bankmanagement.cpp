# include <stdio.h>
 # include<conio>
#include<iostream>
using namespace std;
class bank
{
    char name[100],add[100],y;
    int balance;
    public:
    void open_account();
    void deposite_money();
    void withdraw_money();
    void Display_account();
};
void bank::open_account()
{
    cout<<"enter your full name";
    cin.ignore();
    cin.getline(name,100);
    cout<<"enter your address";
    cin.ignore();
    cin.getline(add,100);
    cout<<"what type of account you want";
    cin>>y;
    cout<<"enter amount for deposite";
    cin>>balance;
    cout<<"your account is created\n";

}
void bank::deposite_money()
{
    int a;
    cout<<"enter how much money you want to deposite";
    cin>>a;
    balance+=a;
    cout<<"total amunt you deposited"<<balance;

}
void bank::Display_account()
{
    cout<<"your full name:\t"<<name;
    cout<<"your address is:\t"<<add;
    cout<<"type of account you have opened\t"<<y;
    cout<<"amount you have deposited\t"<<balance;
}
void bank::withdraw_money()
{
    float  amount;
    cout<<"\n withdraw:";
    cout<<"enter amount to withdraw:";
    cin>>amount;
    balance=balance-amount;
    cout<<"now total amount is left:"<<balance;

}
int main()
{
    int ch;
    cout<<"enter your choice:1,2,3,4";
    cin>>ch;
    char x;
    bank obj;
    do{
        switch(ch)
        {
            case 1:cout<<"open account\n";
            obj.open_account();
            break;
            case 2:cout<<"deposite money:\n";
            obj.deposite_money();
            break;
            case 3:cout<<"WITHDRAW MONEY:\n";
            obj.withdraw_money();
            break;
            case 4:cout<<"display account:\n";
            obj.Display_account();
            break;
            case 5:
            if(ch==5)
            {
                exit(1);
            }
            default:
            cout<<"not valid input try again";

        }
        cout<<"\n do you want to select next option then press:y/n";
        cout<<"if you want to exit then press:n";
        cout<<"enter your choice";

        cin>>x;

        if(x=='n'||x=='N')
        exit(0);

    }while(x=='y'||x=='Y');

    return 0;

}