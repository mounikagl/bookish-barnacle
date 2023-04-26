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
    void OpenConnection(connection *db, char * filename)
    {
        db->SomeState = 1;

    }
    void ExecuteConnection(Connection * db, char * statement)
    {
    }

    void CloseConnection(connection * db)
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