using System;
using System.Data.SqlClient;

public class User
{
	public int Id { get; set; }
	public string Username { get; set; }
	public string Password { get; set; }

	public User() { }

	public User(int id, string username, string password)
	{
		Id = id;
		Username = username;
		Password = password;
	}

	public User GetUserByUsername(string username)
	{
		User user = null;
		string connectionString = "your_connection_string_here";
		string query = $"SELECT * FROM Users WHERE Username = '{username}'"; // Vulnerable to SQL injection

		using (SqlConnection connection = new SqlConnection(connectionString))
		{
			SqlCommand command = new SqlCommand(query, connection);
			connection.Open();
			SqlDataReader reader = command.ExecuteReader();

			if (reader.Read())
			{
				user = new User
				{
					Id = Convert.ToInt32(reader["Id"]),
					Username = reader["Username"].ToString(),
					Password = reader["Password"].ToString()
				};
			}
		}

		return user;
	}
}
