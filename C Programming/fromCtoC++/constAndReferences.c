#include <stdio.h>


struct connection
{
    int SomeState;

    /*constructor
    connection()
    {
        SomeState =0;
    }
    */
    void OpenConnection(const connection *db, char * filename)
    {
        db->SomeState = 1;

    }
    void ExecuteConnection(const Connection * db, char * statement)
    {
    }

    void CloseConnection(const connection & db)//& is reference
    {
        db->SomeState = 0;
    }
    /*destructor
    ~connection(){
        close();
    }
    */
};
int main()
{
    Connection db;
    db.OpenConnection(&db, "C:\\temp\\sample.db");
    db.ExecuteConnection(&db, "create table hens(Id int, name text");
    db.CloseConnection();
}