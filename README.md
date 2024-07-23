<h1>SCP Data Project</h1>

<h2>Setup Instructions</h2>

<h3>Create the Database</h3>

<p>Set up your database with the following table schema:</p>

```sql
CREATE TABLE scp_data (
  number INT NOT NULL PRIMARY KEY,
  class VARCHAR(255) DEFAULT NULL,
  clearance_level INT NOT NULL,
  description TEXT NOT NULL,
  image_url VARCHAR(255) DEFAULT NULL
);
```
<h3>Run the Data Scraping Script</h3>
<p>Run the <code>database_scrap</code> script to generate a CSV file with SCP data. The script is configured to scrape SCP entries from 1 to 1000. Verify that the CSV file is created properly.</p>
<h3>Install Required Libraries</h3>
<p>Install the necessary Python libraries listed in <code>requirements.txt</code>.</p>
<h3>Prepare the Image Folder</h3>
<p>Ensure an "Image" folder exists in the project directory. Create this folder manually if it’s not there. This folder will store downloaded images.</p>
<h3>Run the Main Script</h3>
<p>Execute the <code>main</code> script. It will import data from the CSV file into the database, enable search functionality, and download images if URLs are available in the database.</p>
<h2>Features</h2>
<ul>
  <li><strong>Search Functionality:</strong> Search SCP entries from the database.</li>
  <li><strong>Image Download:</strong> Downloads images to the "Image" folder if URLs are present.</li>
</ul>
<h2>Notes</h2>
<ul>
  <li>Make sure the database connection is properly configured in the scripts.</li>
  <li>Check that <code>requirements.txt</code> includes all required libraries.</li>
  <li>Ensure the "Image" folder is created before running the <code>main</code> script to avoid errors during image download.</li>
</ul>
