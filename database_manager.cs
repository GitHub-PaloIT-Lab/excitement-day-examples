using System;
using System.Collections.Generic;
using System.Data.SqlClient;

public class DatabaseManager
{
    private string _connectionString;

    public DatabaseManager(string connectionString)
    {
        _connectionString = connectionString;
    }

    public SqlConnection OpenConnection()
    {
        SqlConnection connection = new SqlConnection(_connectionString);
        try
        {
            connection.Open();
            Console.WriteLine("Connection opened successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error opening connection: " + ex.Message);
        }
        return connection;
    }

    public void CloseConnection(SqlConnection connection)
    {
        if (connection != null && connection.State == System.Data.ConnectionState.Open)
        {
            connection.Close();
            Console.WriteLine("Connection closed successfully.");
        }
    }

    public List<Dictionary<string, object>> ExecuteQuery(string query)
    {
        List<Dictionary<string, object>> results = new List<Dictionary<string, object>>();
        SqlConnection connection = OpenConnection();
        if (connection == null)
        {
            return results;
        }

        try
        {
            using (SqlCommand command = new SqlCommand(query, connection))
            {
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        Dictionary<string, object> row = new Dictionary<string, object>();
                        for (int i = 0; i < reader.FieldCount; i++)
                        {
                            row[reader.GetName(i)] = reader.GetValue(i);
                        }
                        results.Add(row);
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error executing query: " + ex.Message);
        }
        finally
        {
            CloseConnection(connection);
        }

        return results;
    }
}
